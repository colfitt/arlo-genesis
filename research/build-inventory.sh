#!/usr/bin/env bash
# build-inventory.sh — deterministic corpus inventory for the bloop-gapscan workflow.
# Scans gear/ and software/ and writes one NDJSON record per device to
# research/.gapscan-inventory.ndjson (gitignored — it is a regenerable cache).
# Run from anywhere in the repo (it cd's to the repo root): `bash research/build-inventory.sh`
#
# NOTE: intentionally NOT `set -o pipefail`. The find|wc, find|head and grep|head
# pipelines below rely on a non-zero find/grep exit being masked by the trailing
# wc/head/sed, so a missing or empty directory yields 0 instead of aborting the run.
set -eu
shopt -s nullglob 2>/dev/null || true

root=$(git rev-parse --show-toplevel) || { echo 'build-inventory.sh: not inside a git repo' >&2; exit 1; }
cd "$root"

OUT=research/.gapscan-inventory.ndjson
: > "$OUT"

# Count files directly under a dir; 0 if the dir is missing.
count_files () { [ -d "$1" ] || { echo 0; return; }; find "$1" -maxdepth 1 -type f 2>/dev/null | wc -l | tr -d ' '; }

# Escape a string for safe embedding inside a JSON double-quoted value (backslash, then quote).
esc () { local s=${1//\\/\\\\}; s=${s//\"/\\\"}; printf '%s' "$s"; }

for cat in gear software; do
  for dir in "$cat"/*/; do
    dir="${dir%/}"
    [ -d "$dir" ] || continue
    name=$(basename "$dir")
    research="$dir/research"
    dr=$(find "$research" -maxdepth 1 -type f -iname '*deepresearch*' 2>/dev/null | wc -l | tr -d ' ')
    ug=$(find "$research" -maxdepth 1 -type f \( -iname '*usageguide*' -o -iname '*navigator*' \) 2>/dev/null | wc -l | tr -d ' ')
    mdcount=$(find "$research" -maxdepth 1 -type f -name '*.md' 2>/dev/null | wc -l | tr -d ' ')
    bytes=$(find "$research" -maxdepth 1 -type f -name '*.md' -exec cat {} + 2>/dev/null | wc -c | tr -d ' ')
    links=$(count_files "$research/links")
    transcripts=$(count_files "$research/transcripts")
    gp=$([ -f "$dir/GearProfile.md" ] && echo 1 || echo 0)
    midi=$(grep -i '^midi:' "$dir/GearProfile.md" 2>/dev/null | head -1 | sed 's/.*: *//' | tr -d ' \r')
    [ -z "$midi" ] && midi="unknown"
    cc=$(find "$dir" \( -iname '*cc-chart*' -o -iname '*midi*cc*' -o -iname '*midi*manual*' -o -iname '*midi*implementation*' \) -type f 2>/dev/null | head -1)
    hascc=$([ -n "$cc" ] && echo 1 || echo 0)
    manuals=$(count_files "$dir/manuals")
    presets=$(count_files "$dir/presets")
    # Field list MUST stay in lockstep with INVENTORY_SCHEMA in .claude/workflows/bloop-gapscan.js.
    # Free-text fields (cat/name/dir/midi) are JSON-escaped via esc(); the rest are integers.
    printf '{"category":"%s","name":"%s","path":"%s","deepResearch":%s,"usageGuide":%s,"researchMd":%s,"researchBytes":%s,"links":%s,"transcripts":%s,"gearProfile":%s,"midi":"%s","ccChart":%s,"manuals":%s,"presets":%s}\n' \
      "$(esc "$cat")" "$(esc "$name")" "$(esc "$dir")" "$dr" "$ug" "$mdcount" "$bytes" "$links" "$transcripts" "$gp" "$(esc "$midi")" "$hascc" "$manuals" "$presets" >> "$OUT"
  done
done

echo "Wrote $(wc -l < "$OUT" | tr -d ' ') device records to $OUT"
