#!/usr/bin/env python3
"""
arlo → JSONL chunk converter.

Walks arlo's markdown corpus and emits one JSONL record per H2 section,
conforming to patchbay v2.0 chunk schema. Bridge to ARLO while v3.1
markdown-canonical milestone is paused.

Usage:
    python3 export_chunks.py
    python3 export_chunks.py --corpus PATH --output PATH --verbose

Design contract:
    See ~/Dev/patchbay-plugin/docs/specs/2026-05-27-arlo-jsonl-converter-design.md
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# H2 titles to skip — bibliographies, meta sections, cross-refs.
# Matched against the title's "simple part" (text before any em-dash).
SKIPPED_H2_TITLES = {
    "sources",
    "cited retrieval topics",
    "see also",
    "anti-hallucination notes",
}

# [text](url) — matches markdown inline links
INLINE_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def slugify(text: str) -> str:
    """URL-safe slug: lowercase, non-alphanumerics to dashes, collapsed."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def filepath_slug(filepath: Path, corpus_dir: Path) -> str:
    """corpus/albums/beatles-abbey-road.md → albums-beatles-abbey-road"""
    rel = filepath.relative_to(corpus_dir)
    parts = list(rel.parts[:-1]) + [rel.stem]
    return "-".join(parts)


def parse_metadata_header(text: str) -> dict[str, str]:
    """Extract **Field:** value pairs from the header (before first H2 or ---).

    Returns dict keyed by slugified field name (e.g., 'tags', 'source',
    'aesthetic-stack-relevance').
    """
    lines = text.split("\n")
    header_lines: list[str] = []
    seen_h1 = False
    for line in lines:
        if line.startswith("# ") and not line.startswith("## "):
            seen_h1 = True
            continue
        if line.strip() == "---" or line.startswith("## "):
            break
        if seen_h1:
            header_lines.append(line)
    header_text = "\n".join(header_lines)

    meta: dict[str, str] = {}
    # Single-line bold-prefix metadata: **Key:** value
    for match in re.finditer(r"^\*\*([^:*]+):\*\*\s*(.+?)$", header_text, re.MULTILINE):
        key = slugify(match.group(1))
        value = match.group(2).strip()
        meta[key] = value
    return meta


def parse_tags(tags_value: str) -> list[str]:
    """Parse `a`, `b`, `c` from a Tags-line value. Returns [] if empty."""
    if not tags_value:
        return []
    return [m.group(1) for m in re.finditer(r"`([^`]+)`", tags_value)]


def extract_scraped_at(source_value: str) -> str | None:
    """Extract YYYY-MM or YYYY-MM-DD from the **Source:** value (e.g., '... (2026-05) ...')."""
    if not source_value:
        return None
    m = re.search(r"\((\d{4}-\d{2}(?:-\d{2})?)\)", source_value)
    return m.group(1) if m else None


def parse_h2_sections(body: str) -> list[dict[str, str]]:
    """Split body into [{title, body}, ...] for each H2, skipping meta sections.

    'Meta' = sections whose simple-title (before any em-dash) is in
    SKIPPED_H2_TITLES.
    """
    parts = re.split(r"^## (.+?)$", body, flags=re.MULTILINE)
    # parts: [pre, title1, content1, title2, content2, ...]
    sections: list[dict[str, str]] = []
    i = 1
    while i < len(parts):
        title = parts[i].strip()
        content = parts[i + 1].strip() if i + 1 < len(parts) else ""
        simple = title.lower().split("—")[0].strip()
        if simple not in SKIPPED_H2_TITLES:
            sections.append({"title": title, "body": content})
        i += 2
    return sections


def extract_inline_citations(body: str) -> list[dict[str, str]]:
    """Return [{type, url, title}, ...] for every [text](http(s)...) in body.

    Internal (relative-path) links are skipped — they're cross-refs, not
    external citations.
    """
    citations: list[dict[str, str]] = []
    for match in INLINE_LINK_RE.finditer(body):
        title = match.group(1)
        url = match.group(2)
        if url.startswith("http://") or url.startswith("https://"):
            citations.append(
                {
                    "type": "external-url",
                    "url": url,
                    "title": title,
                }
            )
    return citations


def build_chunk(
    filepath: Path,
    corpus_dir: Path,
    meta: dict[str, str],
    h2_title: str,
    h2_body: str,
    used_slugs: set[str],
) -> dict:
    """Assemble one chunk dict conforming to v2.0 schema."""
    fp_slug = filepath_slug(filepath, corpus_dir)
    base_slug = slugify(h2_title)

    # Disambiguate duplicate H2 titles within the same file
    h2_slug = base_slug
    n = 2
    while h2_slug in used_slugs:
        h2_slug = f"{base_slug}-{n}"
        n += 1
    used_slugs.add(h2_slug)

    chunk_id = f"arlo-{fp_slug}-{h2_slug}"

    # Build provenance — file path relative to corpus_dir.parent so it reads as 'corpus/...'
    rel_path = filepath.relative_to(corpus_dir.parent)
    provenance: dict = {
        "arlo_file": str(rel_path),
        "section": h2_title,
        "section_slug": h2_slug,
    }

    # Map metadata fields into provenance
    for k, v in meta.items():
        if k == "tags":
            continue  # tags is top-level on the chunk
        if k == "source":
            # Split into source_kind + scraped_at. Strip any (YYYY-MM[-DD]) parenthetical
            # from the source_kind since the date is already captured in scraped_at.
            simple = v.split("—")[0].strip()
            simple = re.sub(r"\s*\([^)]*\)", "", simple).strip()
            provenance["source_kind"] = slugify(simple)
            scraped = extract_scraped_at(v)
            if scraped:
                provenance["scraped_at"] = scraped
            continue
        # Preserve any other bold-prefix metadata field as-is
        provenance[k] = v

    chunk: dict = {
        "id": chunk_id,
        "type": "text",
        "source": "arlo",
        "tier_used": 0,
        "content": h2_body,
        "tags": parse_tags(meta.get("tags", "")),
        "provenance": provenance,
    }

    citations = extract_inline_citations(h2_body)
    if citations:
        chunk["citation_targets"] = citations

    return chunk


def convert_file(filepath: Path, corpus_dir: Path, log) -> list[dict]:
    """Process one markdown file. Returns list of chunk dicts."""
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        log(f"WARN: failed to read {filepath}: {e}")
        return []

    meta = parse_metadata_header(text)
    if not meta:
        rel = filepath.relative_to(corpus_dir.parent)
        log(f"WARN: no bold-prefix metadata header in {rel}")

    sections = parse_h2_sections(text)
    if not sections:
        rel = filepath.relative_to(corpus_dir.parent)
        log(f"WARN: no H2 sections in {rel} — skipping file")
        return []

    used_slugs: set[str] = set()
    chunks = [
        build_chunk(filepath, corpus_dir, meta, s["title"], s["body"], used_slugs)
        for s in sections
    ]
    return chunks


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert arlo markdown corpus to JSONL chunks (patchbay v2.0 schema)."
    )
    parser.add_argument(
        "--corpus",
        type=Path,
        default=Path.home() / "Dev/arlo/corpus",
        help="Input directory (default: ~/Dev/arlo/corpus)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path.home() / "Dev/arlo/chunks.jsonl",
        help="Output JSONL file (default: ~/Dev/arlo/chunks.jsonl)",
    )
    parser.add_argument("--verbose", action="store_true", help="Per-file chunk counts to stderr")
    args = parser.parse_args()

    if not args.corpus.is_dir():
        print(f"Error: corpus directory not found: {args.corpus}", file=sys.stderr)
        return 1

    warn_count = 0

    def log(msg: str) -> None:
        nonlocal warn_count
        print(msg, file=sys.stderr)
        warn_count += 1

    # Walk all .md files in corpus, skip READMEs (documentation, not content)
    files = sorted(p for p in args.corpus.rglob("*.md") if p.name.lower() != "readme.md")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    total_chunks = 0
    with args.output.open("w", encoding="utf-8") as out:
        for filepath in files:
            chunks = convert_file(filepath, args.corpus, log)
            if args.verbose:
                rel = filepath.relative_to(args.corpus.parent)
                print(f"  {rel}: {len(chunks)} chunks", file=sys.stderr)
            for chunk in chunks:
                out.write(json.dumps(chunk, ensure_ascii=False) + "\n")
            total_chunks += len(chunks)

    print(
        f"\nProcessed {len(files)} files, emitted {total_chunks} chunks, {warn_count} warnings",
        file=sys.stderr,
    )
    print(f"Output: {args.output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
