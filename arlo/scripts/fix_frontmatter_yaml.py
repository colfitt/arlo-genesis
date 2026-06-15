#!/usr/bin/env python3
"""One-shot repair: quote Patches/ + Chains/ frontmatter scalars that break YAML.

The Pedalxly→Genesis transform emitted some `description:`/`title:` values with
unquoted colons or partial quotes, which fail yaml.safe_load. This re-quotes the
exact offending scalar line as a YAML double-quoted string (escaping \\ and "),
preserving the value verbatim. Body bytes are never touched.

Dry-run by default; pass --apply to write.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

# indent, key (anything up to the FIRST ': '), value. Keys may be nested and
# contain slashes/spaces (e.g. 'Treble/Presence trim').
KEYVAL_RE = re.compile(r"^(\s*)(\S.*?): (.+)$")


def _all_strings(obj):
    """Yield every string leaf in a parsed YAML structure (recurses dict/list)."""
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from _all_strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _all_strings(v)


def _split_fm(text: str):
    """Return (opening, fm_text, rest) or None if no parseable frontmatter block."""
    if not text.startswith("---"):
        return None
    close = re.search(r"\n---[ \t]*\n", text)
    if not close:
        return None
    return text[:3], text[3 : close.start()], text[close.start() :]


def _yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def repair_fm(fm_text: str) -> tuple[str, list[tuple[str, str]]]:
    """Re-quote offending scalar lines until the block parses. Returns (new_fm, changes)."""
    lines = fm_text.split("\n")
    changes: list[tuple[str, str]] = []
    for _ in range(20):
        try:
            yaml.safe_load("\n".join(lines))
            return "\n".join(lines), changes
        except yaml.YAMLError as e:
            mark = getattr(e, "problem_mark", None)
            if mark is None:
                raise
            ln = mark.line
            old = lines[ln]
            if old.lstrip().startswith("- "):
                raise RuntimeError(f"offending line is a flow list item: {old!r}")
            m = KEYVAL_RE.match(old)
            if not m:
                raise RuntimeError(f"offending line is not a simple scalar: {old!r}")
            indent, key, val = m.groups()
            if val[:1] in "[{":
                # Bail only if it's a genuine flow collection; a value that merely
                # starts with '[' but doesn't parse (e.g. '[▲]+[CTL 1] ...') is a
                # string the author wrote and is exactly what needs quoting.
                try:
                    parsed = yaml.safe_load(val)
                except yaml.YAMLError:
                    parsed = None
                if isinstance(parsed, (list, dict)):
                    raise RuntimeError(f"offending value is a real flow collection: {old!r}")
            new = f"{indent}{key}: {_yaml_quote(val)}"
            lines[ln] = new
            changes.append((old, new))
    raise RuntimeError("did not converge after 20 passes")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry-run)")
    ap.add_argument("--root", type=Path, default=Path.cwd())
    args = ap.parse_args()

    targets = []
    for sub in ("Patches", "Chains"):
        d = args.root / sub
        if d.is_dir():
            targets += [p for p in sorted(d.rglob("*.md")) if p.name.lower() != "readme.md"]

    fixed = 0
    for p in targets:
        text = p.read_text(encoding="utf-8")
        split = _split_fm(text)
        if not split:
            continue
        opening, fm_text, rest = split
        try:
            yaml.safe_load(fm_text)
            continue  # already valid
        except yaml.YAMLError:
            pass

        new_fm, changes = repair_fm(fm_text)
        new_text = opening + new_fm + rest

        # Verify: parses now, body byte-identical, every re-quoted value round-trips
        # into the parsed structure verbatim (handles nested keys).
        meta = yaml.safe_load(new_fm)
        assert isinstance(meta, dict), f"{p}: still not a mapping"
        assert new_text[len(opening) + len(new_fm) :] == rest, f"{p}: body changed!"
        leaves = set(_all_strings(meta))
        for old, _new in changes:
            raw_val = KEYVAL_RE.match(old).group(3)
            assert raw_val in leaves, f"{p}: round-trip mismatch for {raw_val!r}"

        fixed += 1
        print(f"\n{'FIX' if args.apply else 'DRY'} {p}")
        for old, new in changes:
            print(f"   - {old}")
            print(f"   + {new}")
        if args.apply:
            p.write_text(new_text, encoding="utf-8")

    print(f"\n{'Applied' if args.apply else 'Would fix'}: {fixed} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
