#!/usr/bin/env bash
# build-inventory.sh — deterministic corpus inventory for the bloop-gapscan workflow.
# Scans gear/ and software/ and writes one NDJSON record per device to
# research/.gapscan-inventory.ndjson (gitignored — it is a regenerable cache).
# Run from the repo root: `bash research/build-inventory.sh`
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

OUT=research/.gapscan-inventory.ndjson
: > "$OUT"

count_files () { find "$1" -maxdepth 1 -type f 2>/dev/null | wc -l | tr -d ' '; }

for cat in gear software; do
  for dir in "$cat"/*/; do
    dir="${dir%/}"
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
    printf '{"category":"%s","name":"%s","path":"%s","deepResearch":%s,"usageGuide":%s,"researchMd":%s,"researchBytes":%s,"links":%s,"transcripts":%s,"gearProfile":%s,"midi":"%s","ccChart":%s,"manuals":%s,"presets":%s}\n' \
      "$cat" "$name" "$dir" "$dr" "$ug" "$mdcount" "$bytes" "$links" "$transcripts" "$gp" "$midi" "$hascc" "$manuals" "$presets" >> "$OUT"
  done
done

echo "Wrote $(wc -l < "$OUT" | tr -d ' ') device records to $OUT"
