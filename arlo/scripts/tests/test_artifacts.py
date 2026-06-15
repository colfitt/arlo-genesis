"""Tests for the Patches/ + Chains/ artifact converter in export_chunks.py.

Artifacts (patches, chains) use YAML frontmatter and become ONE atomic chunk
per file, tagged via provenance.content_type so retrieval can distinguish a
real patch/chain from prose-corpus technique writeups.

Run from anywhere:
    python3 -m pytest arlo/scripts/tests/test_artifacts.py
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPT_DIR))

from export_chunks import (  # noqa: E402
    artifact_id,
    build_artifact_chunk,
    convert_artifact_file,
    split_frontmatter,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def collect_warnings():
    warnings: list[str] = []

    def log(msg: str) -> None:
        warnings.append(msg)

    return log, warnings


class TestSplitFrontmatter(unittest.TestCase):
    def test_patch_frontmatter_parsed(self) -> None:
        meta, body = split_frontmatter((FIXTURES / "patch.md").read_text())
        self.assertEqual(meta["type"], "patch")
        self.assertEqual(meta["device"], "Test Device")
        self.assertEqual(meta["tags"], ["drone", "ambient", "freeze"])
        self.assertEqual(len(meta["controls"]), 2)
        self.assertEqual(meta["controls"][0]["name"], "Mix")
        self.assertEqual(meta["controls"][0]["value"], "8 (of 10)")
        self.assertTrue(body.lstrip().startswith("# Test Freeze Pad"))

    def test_no_frontmatter_returns_none(self) -> None:
        text = (FIXTURES / "artifact-no-frontmatter.md").read_text()
        meta, body = split_frontmatter(text)
        self.assertIsNone(meta)
        self.assertEqual(body, text)


class TestArtifactId(unittest.TestCase):
    def test_patch_id_slugifies_device_folder(self) -> None:
        root = Path("/r")
        fp = root / "Patches" / "Eventide H90" / "foo-bar.md"
        self.assertEqual(artifact_id(fp, root), "arlo-patches-eventide-h90-foo-bar")

    def test_chain_id_top_level(self) -> None:
        root = Path("/r")
        fp = root / "Chains" / "bar-baz.md"
        self.assertEqual(artifact_id(fp, root), "arlo-chains-bar-baz")


class TestBuildArtifactChunkPatch(unittest.TestCase):
    def setUp(self) -> None:
        self.fp = FIXTURES / "patch.md"
        meta, body = split_frontmatter(self.fp.read_text())
        self.chunk = build_artifact_chunk(self.fp, FIXTURES.parent, meta, body)

    def test_schema_fields(self) -> None:
        self.assertEqual(self.chunk["type"], "text")
        self.assertEqual(self.chunk["source"], "arlo")
        self.assertEqual(self.chunk["tier_used"], 0)
        for required in ("id", "content", "tags", "provenance"):
            self.assertIn(required, self.chunk)

    def test_discriminator_and_provenance(self) -> None:
        prov = self.chunk["provenance"]
        self.assertEqual(prov["content_type"], "patch")
        self.assertEqual(prov["device"], "Test Device")
        self.assertEqual(prov["title"], "Test Freeze Pad")
        self.assertEqual(prov["arlo_file"], "fixtures/patch.md")

    def test_tags_from_frontmatter(self) -> None:
        self.assertEqual(self.chunk["tags"], ["drone", "ambient", "freeze"])

    def test_content_includes_settings_and_prose(self) -> None:
        content = self.chunk["content"]
        self.assertIn("Mix: 8 (of 10)", content)
        self.assertIn("Feedback: 10", content)
        self.assertIn("Freeze the tail into a pad.", content)

    def test_content_strips_sources_section(self) -> None:
        content = self.chunk["content"]
        self.assertNotIn("Transformed from Pedalxly", content)
        self.assertNotIn("research/links/example.md", content)


class TestBuildArtifactChunkChain(unittest.TestCase):
    def setUp(self) -> None:
        self.fp = FIXTURES / "chain.md"
        meta, body = split_frontmatter(self.fp.read_text())
        self.chunk = build_artifact_chunk(self.fp, FIXTURES.parent, meta, body)

    def test_discriminator_and_provenance(self) -> None:
        prov = self.chunk["provenance"]
        self.assertEqual(prov["content_type"], "chain")
        self.assertEqual(prov["gear"], ["Test Device A", "Test Device B"])
        self.assertEqual(prov["artists"], ["Test Artist"])
        self.assertNotIn("device", prov)

    def test_no_tags_field_is_empty_list(self) -> None:
        self.assertEqual(self.chunk["tags"], [])

    def test_content_keeps_preamble_and_path_no_settings(self) -> None:
        content = self.chunk["content"]
        self.assertIn("An intro paragraph describing the chain arc.", content)
        self.assertIn("A → B → out.", content)
        self.assertNotIn("Settings:", content)
        self.assertNotIn("Source file: Research/Chains/example.md", content)


class TestConvertArtifactFile(unittest.TestCase):
    def test_patch_emits_one_chunk(self) -> None:
        log, warnings = collect_warnings()
        chunks = convert_artifact_file(FIXTURES / "patch.md", FIXTURES.parent, log)
        self.assertEqual(len(chunks), 1)
        self.assertEqual(warnings, [])
        self.assertEqual(chunks[0]["provenance"]["content_type"], "patch")

    def test_no_frontmatter_warns_and_skips(self) -> None:
        log, warnings = collect_warnings()
        chunks = convert_artifact_file(FIXTURES / "artifact-no-frontmatter.md", FIXTURES.parent, log)
        self.assertEqual(chunks, [])
        self.assertTrue(any("no YAML frontmatter" in w for w in warnings))

    def test_malformed_yaml_warns_distinctly_and_skips(self) -> None:
        """A file that HAS frontmatter but fails to parse must report 'malformed',
        not the misleading 'no frontmatter'."""
        log, warnings = collect_warnings()
        chunks = convert_artifact_file(FIXTURES / "artifact-bad-yaml.md", FIXTURES.parent, log)
        self.assertEqual(chunks, [])
        self.assertTrue(any("malformed" in w.lower() for w in warnings))


if __name__ == "__main__":
    unittest.main()
