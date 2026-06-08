"""Tests for export_chunks.py.

Run from anywhere:
    python3 -m unittest discover -s ~/Dev/arlo/scripts/tests
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

# Make scripts/ importable when running from anywhere
SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

from export_chunks import (  # noqa: E402
    build_chunk,
    convert_file,
    extract_inline_citations,
    extract_scraped_at,
    filepath_slug,
    parse_h2_sections,
    parse_metadata_header,
    parse_tags,
    slugify,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def collect_warnings():
    """Returns (log_fn, warnings_list) — log_fn appends messages to warnings_list."""
    warnings: list[str] = []

    def log(msg: str) -> None:
        warnings.append(msg)

    return log, warnings


class TestSlugify(unittest.TestCase):
    def test_basic(self) -> None:
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_lowercase(self) -> None:
        self.assertEqual(slugify("ALL CAPS"), "all-caps")

    def test_strip_punctuation(self) -> None:
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_em_dash_dropped(self) -> None:
        # Em-dash is non-word; collapses to a single dash
        self.assertEqual(slugify("First — Second"), "first-second")

    def test_collapse_multiple_dashes(self) -> None:
        self.assertEqual(slugify("a---b"), "a-b")

    def test_numbers_preserved(self) -> None:
        self.assertEqual(slugify("3M M23"), "3m-m23")

    def test_underscores_to_dash(self) -> None:
        self.assertEqual(slugify("foo_bar_baz"), "foo-bar-baz")

    def test_empty_string(self) -> None:
        self.assertEqual(slugify(""), "")


class TestFilepathSlug(unittest.TestCase):
    def test_nested_path(self) -> None:
        corpus = Path("/tmp/arlo/corpus")
        file = corpus / "albums" / "beatles-abbey-road.md"
        self.assertEqual(filepath_slug(file, corpus), "albums-beatles-abbey-road")

    def test_top_level_file(self) -> None:
        corpus = Path("/tmp/arlo/corpus")
        file = corpus / "stub.md"
        self.assertEqual(filepath_slug(file, corpus), "stub")


class TestParseMetadataHeader(unittest.TestCase):
    def test_canonical(self) -> None:
        text = (FIXTURES / "canonical-album.md").read_text()
        meta = parse_metadata_header(text)
        self.assertEqual(meta["scope"], "album-anchored — the production identity of *Test Album*")
        self.assertEqual(
            meta["source"],
            "Deep-research synthesis (2026-05) — verify before treating as authoritative",
        )
        self.assertEqual(meta["aesthetic-stack-relevance"], "late-90s, indie-rock, lo-fi")
        self.assertEqual(meta["tags"], "`test-artist`, `test-album`, `lo-fi`, `indie-rock`")

    def test_no_header(self) -> None:
        text = (FIXTURES / "no-metadata.md").read_text()
        meta = parse_metadata_header(text)
        self.assertEqual(meta, {})

    def test_lyrics_style_extra_fields(self) -> None:
        """arlo's lyrics files have **Canonical references:** which the parser must capture."""
        text = """# Test\n\n**Scope:** lyrics\n**Source:** synth (2026-05)\n**Canonical references:** Book A; Book B\n**Tags:** `a`\n\n---\n\n## Foo\n\nbody"""
        meta = parse_metadata_header(text)
        self.assertEqual(meta["canonical-references"], "Book A; Book B")


class TestParseTags(unittest.TestCase):
    def test_canonical(self) -> None:
        self.assertEqual(
            parse_tags("`test-artist`, `test-album`, `lo-fi`"),
            ["test-artist", "test-album", "lo-fi"],
        )

    def test_empty(self) -> None:
        self.assertEqual(parse_tags(""), [])

    def test_no_backticks(self) -> None:
        self.assertEqual(parse_tags("plain text no backticks"), [])

    def test_single(self) -> None:
        self.assertEqual(parse_tags("`solo`"), ["solo"])


class TestExtractScrapedAt(unittest.TestCase):
    def test_year_month(self) -> None:
        self.assertEqual(extract_scraped_at("Deep-research synthesis (2026-05) — verify"), "2026-05")

    def test_year_month_day(self) -> None:
        self.assertEqual(extract_scraped_at("Note (2026-05-24) — added"), "2026-05-24")

    def test_no_date(self) -> None:
        self.assertIsNone(extract_scraped_at("Just text with no date"))

    def test_empty(self) -> None:
        self.assertIsNone(extract_scraped_at(""))


class TestParseH2Sections(unittest.TestCase):
    def test_canonical_skips_meta_sections(self) -> None:
        text = (FIXTURES / "canonical-album.md").read_text()
        sections = parse_h2_sections(text)
        titles = [s["title"] for s in sections]
        # The two real H2s should be kept
        self.assertIn("First Section Title", titles)
        self.assertIn("Second Section — With An Em-Dash", titles)
        # All meta sections should be skipped
        self.assertNotIn("Sources", titles)
        self.assertNotIn("Cited Retrieval Topics", titles)
        self.assertNotIn("See Also", titles)
        # Em-dash-suffix anti-hallucination should also be skipped (simple-title match)
        for t in titles:
            self.assertNotIn("Anti-Hallucination", t)

    def test_no_h2s(self) -> None:
        text = (FIXTURES / "no-h2s.md").read_text()
        sections = parse_h2_sections(text)
        self.assertEqual(sections, [])

    def test_body_content_preserved(self) -> None:
        text = "# Title\n\n## First\n\nFirst body content.\n\n## Second\n\nSecond body content."
        sections = parse_h2_sections(text)
        self.assertEqual(len(sections), 2)
        self.assertEqual(sections[0]["title"], "First")
        self.assertEqual(sections[0]["body"], "First body content.")
        self.assertEqual(sections[1]["title"], "Second")
        self.assertEqual(sections[1]["body"], "Second body content.")

    def test_h3_inside_h2_not_split(self) -> None:
        """An H3 within an H2 body should NOT cause an H2 split."""
        text = "## Outer\n\nbefore\n\n### Inner H3\n\nafter"
        sections = parse_h2_sections(text)
        self.assertEqual(len(sections), 1)
        self.assertEqual(sections[0]["title"], "Outer")
        self.assertIn("Inner H3", sections[0]["body"])


class TestExtractInlineCitations(unittest.TestCase):
    def test_external_links_captured(self) -> None:
        body = "Cites [Wikipedia](https://wikipedia.org/foo) and [Site](http://example.com)."
        citations = extract_inline_citations(body)
        self.assertEqual(len(citations), 2)
        self.assertEqual(citations[0]["url"], "https://wikipedia.org/foo")
        self.assertEqual(citations[0]["title"], "Wikipedia")
        self.assertEqual(citations[0]["type"], "external-url")
        self.assertEqual(citations[1]["url"], "http://example.com")

    def test_relative_paths_skipped(self) -> None:
        body = "Links to [other file](./other.md) and [external](https://example.com)."
        citations = extract_inline_citations(body)
        self.assertEqual(len(citations), 1)
        self.assertEqual(citations[0]["url"], "https://example.com")

    def test_no_links(self) -> None:
        self.assertEqual(extract_inline_citations("Plain text with no links."), [])

    def test_malformed_link_ignored(self) -> None:
        """A link with an unclosed paren shouldn't crash; it just isn't captured."""
        body = "Bad: [text](unclosed and then normal text."
        # Should not raise. Whether the link is captured is implementation detail;
        # what matters is no crash.
        citations = extract_inline_citations(body)
        self.assertIsInstance(citations, list)


class TestBuildChunk(unittest.TestCase):
    def test_canonical_shape(self) -> None:
        corpus = FIXTURES.parent  # use the fixtures' parent as a stand-in corpus
        filepath = FIXTURES / "canonical-album.md"
        text = filepath.read_text()
        meta = parse_metadata_header(text)
        sections = parse_h2_sections(text)
        chunk = build_chunk(filepath, corpus, meta, sections[0]["title"], sections[0]["body"], set())

        # Required v2.0 fields
        for required in ("id", "type", "source", "content", "provenance"):
            self.assertIn(required, chunk)

        self.assertEqual(chunk["type"], "text")
        self.assertEqual(chunk["source"], "arlo")
        self.assertEqual(chunk["tier_used"], 0)
        self.assertIn("test-album", chunk["tags"])

        prov = chunk["provenance"]
        self.assertEqual(prov["section"], "First Section Title")
        self.assertEqual(prov["section_slug"], "first-section-title")
        self.assertEqual(prov["source_kind"], "deep-research-synthesis")
        self.assertEqual(prov["scraped_at"], "2026-05")
        self.assertIn("aesthetic-stack-relevance", prov)

        # Citation targets pulled from inline links
        self.assertIn("citation_targets", chunk)
        urls = [c["url"] for c in chunk["citation_targets"]]
        self.assertIn("https://example.com/page1", urls)
        self.assertIn("https://example.com/page2", urls)

    def test_id_format(self) -> None:
        corpus = FIXTURES.parent
        filepath = FIXTURES / "canonical-album.md"
        meta = {"source": "synth (2026-05)", "tags": ""}
        chunk = build_chunk(filepath, corpus, meta, "Hello World", "body", set())
        # arlo-<filepath-slug>-<h2-slug>
        # filepath relative to corpus parent = fixtures/canonical-album.md → slug fixtures-canonical-album
        self.assertEqual(chunk["id"], "arlo-fixtures-canonical-album-hello-world")


class TestConvertFile(unittest.TestCase):
    def test_canonical_emits_expected_chunks(self) -> None:
        log, warnings = collect_warnings()
        chunks = convert_file(FIXTURES / "canonical-album.md", FIXTURES.parent, log)
        # Two real H2s; four meta sections skipped
        self.assertEqual(len(chunks), 2)
        self.assertEqual(warnings, [])
        # First chunk has citation_targets
        self.assertIn("citation_targets", chunks[0])
        # Second chunk title preserved with em-dash
        self.assertEqual(chunks[1]["provenance"]["section"], "Second Section — With An Em-Dash")

    def test_no_metadata_warns_but_continues(self) -> None:
        log, warnings = collect_warnings()
        chunks = convert_file(FIXTURES / "no-metadata.md", FIXTURES.parent, log)
        self.assertEqual(len(chunks), 2)
        self.assertTrue(any("no bold-prefix metadata" in w for w in warnings))
        # Tags should be empty when no metadata
        self.assertEqual(chunks[0]["tags"], [])

    def test_no_h2s_skips_file(self) -> None:
        log, warnings = collect_warnings()
        chunks = convert_file(FIXTURES / "no-h2s.md", FIXTURES.parent, log)
        self.assertEqual(chunks, [])
        self.assertTrue(any("no H2 sections" in w for w in warnings))

    def test_malformed_link_no_crash(self) -> None:
        log, _ = collect_warnings()
        chunks = convert_file(FIXTURES / "malformed-link.md", FIXTURES.parent, log)
        self.assertEqual(len(chunks), 1)
        # Content preserved verbatim
        self.assertIn("malformed link", chunks[0]["content"])

    def test_duplicate_h2_disambiguates(self) -> None:
        log, _ = collect_warnings()
        chunks = convert_file(FIXTURES / "duplicate-h2.md", FIXTURES.parent, log)
        self.assertEqual(len(chunks), 3)
        slugs = [c["provenance"]["section_slug"] for c in chunks]
        # Three sections: Notes, Other Section, Notes (-2)
        self.assertEqual(slugs[0], "notes")
        self.assertEqual(slugs[1], "other-section")
        self.assertEqual(slugs[2], "notes-2")
        # Unique chunk IDs
        ids = [c["id"] for c in chunks]
        self.assertEqual(len(ids), len(set(ids)))


if __name__ == "__main__":
    unittest.main()
