/**
 * bloop-gapscan — sweep the corpus and seed a ranked research queue.
 * ---------------------------------------------------------------------------
 * This is the AGENDA half of blooping (playbook §6). It is a Workflow so the
 * judgment fans out across the corpus instead of rotting one context.
 *
 * Pipeline:
 *   1. INVENTORY — 1 loader agent reads the deterministic inventory file.
 *   2. ASSESS    — batches of devices judged IN PARALLEL (doc-model aware).
 *   3. RANK      — 1 agent merges into a single ranked queue + open questions.
 *
 * The deterministic inventory (research/.gapscan-inventory.ndjson) is built by
 * Bash first, so byte counts / file presence are facts, and the agents spend
 * their judgment on what MATTERS, not on re-scanning.
 *
 * args: { date: "2026-06-19", inventoryPath?: "research/.gapscan-inventory.ndjson" }
 */

export const meta = {
  name: 'bloop-gapscan',
  description: 'Sweep gear/ and software/ for missing or thin artifacts and return a ranked research queue with rationale and open questions.',
  phases: [
    { title: 'Inventory', detail: 'load the deterministic corpus inventory' },
    { title: 'Assess',    detail: 'judge completeness + gaps in parallel batches' },
    { title: 'Rank',      detail: 'merge into one ranked queue' },
  ],
}

// args can arrive as a live object OR a JSON string depending on the caller —
// normalise so a.date works either way.
let a = args || {}
if (typeof a === 'string') { try { a = JSON.parse(a) } catch (_) { a = {} } }
const date = a.date
const inventoryPath = a.inventoryPath || 'research/.gapscan-inventory.ndjson'
if (!date) throw new Error('bloop-gapscan requires args.date')

// Shared context every assessor + the ranker must reason with. This is the
// judgment that a pure-Bash gap list cannot encode.
const CONTEXT = [
  `PROJECT CONTEXT — ARLO is a music-rig assistant: a MIDI control + patch/chain`,
  `suggestion layer over this owned-gear corpus. The owner's genres are ambient,`,
  `lo-fi, post-rock, and electronic. Anchor devices skew toward texture/looping`,
  `(Chase Bliss MOOD MkII & Blooper, Hologram Microcosm & Chroma Console, etc.).`,
  ``,
  `DOC MODEL — judge gaps against how THIS corpus actually documents things:`,
  `  • Gear: GearProfile.md + research/<name>-DeepResearch.md + <name>-UsageGuide.md,`,
  `    plus links/ and transcripts/. A MIDI-capable device (midi:true) with NO captured`,
  `    CC chart (ccChart:0) is a HIGH-value gap because ARLO needs the control surface.`,
  `  • Software: research/<name>-UsageGuide.md (and a <vendor>-Navigator.md for`,
  `    multi-product vendors). Software has NO DeepResearch by design — deepResearch:0`,
  `    is NORMAL for software, NOT a gap. The real software gap is a multi-product`,
  `    vendor covered by a single thin UsageGuide (e.g. one guide for all of iZotope).`,
  ``,
  `WHAT COUNTS AS A GAP worth a bloop:`,
  `  • midi:true but ccChart:0  → capture the CC map (high, ARLO-relevant).`,
  `  • Thin coverage for scope (few KB / few links for a deep or multi-product device).`,
  `  • GearProfile template sections left unfilled (role-in-rig, signature uses) that`,
  `    research could populate with concrete signature uses.`,
  `  • Stale or shallow DeepResearch/UsageGuide relative to the device's importance.`,
  `NOT a gap: a well-documented device (full docs + CC chart + many links/transcripts).`,
].join('\n')

// --- schemas ----------------------------------------------------------------
const INVENTORY_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['devices'],
  properties: {
    devices: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        required: ['category', 'name', 'path', 'deepResearch', 'usageGuide', 'researchBytes', 'links', 'transcripts', 'midi', 'ccChart'],
        properties: {
          category: { type: 'string' },
          name: { type: 'string' },
          path: { type: 'string' },
          deepResearch: { type: 'integer' },
          usageGuide: { type: 'integer' },
          researchBytes: { type: 'integer' },
          links: { type: 'integer' },
          transcripts: { type: 'integer' },
          midi: { type: 'string' },
          ccChart: { type: 'integer' },
        },
      },
    },
  },
}

const ASSESS_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['devices'],
  properties: {
    devices: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        required: ['name', 'category', 'path', 'completeness', 'gaps', 'recommendBloop', 'priority', 'rationale', 'suggestedFocus'],
        properties: {
          name: { type: 'string' },
          category: { type: 'string' },
          path: { type: 'string' },
          completeness: { type: 'string', enum: ['strong', 'moderate', 'thin'] },
          gaps: { type: 'array', items: { type: 'string' } },
          recommendBloop: { type: 'boolean' },
          priority: { type: 'string', enum: ['high', 'medium', 'low'] },
          rationale: { type: 'string' },
          suggestedFocus: { type: 'string', description: 'What the first bloop on this target should emphasise.' },
        },
      },
    },
  },
}

const QUEUE_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['generatedFor', 'targets', 'notes'],
  properties: {
    generatedFor: { type: 'string' },
    targets: {
      type: 'array',
      description: 'Ranked, highest value first. Include the ~15-20 most worthwhile, not all devices.',
      items: {
        type: 'object', additionalProperties: false,
        required: ['rank', 'target', 'category', 'path', 'priority', 'why', 'suggestedFocus', 'openQuestions'],
        properties: {
          rank: { type: 'integer' },
          target: { type: 'string' },
          category: { type: 'string' },
          path: { type: 'string' },
          priority: { type: 'string', enum: ['high', 'medium', 'low'] },
          why: { type: 'string' },
          suggestedFocus: { type: 'string' },
          openQuestions: { type: 'array', items: { type: 'string' } },
        },
      },
    },
    notes: { type: 'string', description: 'Any cross-cutting observations about the corpus state.' },
  },
}

// === PHASE 1 · INVENTORY ====================================================
phase('Inventory')
const inv = await agent(
  `Read the file "${inventoryPath}". It is NDJSON — one device record per line. Return ALL records as the devices array, faithfully (do not drop or invent any).`,
  { label: 'load-inventory', phase: 'Inventory', schema: INVENTORY_SCHEMA },
)
const devices = (inv && inv.devices) || []
log(`Loaded ${devices.length} device records.`)

// === PHASE 2 · ASSESS =======================================================
// Partition into batches and judge each batch in its own clean context, in
// parallel. parallel() barriers here because RANK needs every assessment.
phase('Assess')
const BATCH = 10
const batches = []
for (let i = 0; i < devices.length; i += BATCH) batches.push(devices.slice(i, i + BATCH))

const assessPrompt = (batch, idx) => [
  `You assess corpus completeness for batch ${idx + 1}/${batches.length} of the ARLO gear/software corpus.`,
  CONTEXT,
  `Devices in your batch (deterministic inventory facts):`,
  JSON.stringify(batch, null, 0),
  `For EACH device: judge completeness (strong/moderate/thin), list the concrete gaps,`,
  `decide whether it deserves a research bloop, set a priority, give a one-line rationale,`,
  `and a suggestedFocus for the first bloop. For borderline calls, you MAY Read the actual`,
  `research file(s) under the device's path to judge depth — do not judge a 40KB doc as`,
  `thin without looking. Apply the DOC MODEL rules above (software deepResearch:0 is normal).`,
].join('\n\n')

const assessments = (await parallel(
  batches.map((b, idx) => () =>
    agent(assessPrompt(b, idx), { label: `assess:batch${idx + 1}`, phase: 'Assess', schema: ASSESS_SCHEMA })
  )
)).filter(Boolean)
const assessed = assessments.flatMap(x => x.devices || [])
const recommended = assessed.filter(d => d.recommendBloop)
log(`Assessed ${assessed.length} devices — ${recommended.length} recommended for a bloop.`)

// === PHASE 3 · RANK =========================================================
phase('Rank')
const ranked = await agent(
  [
    `Merge these per-device assessments into ONE ranked research queue for ${date}.`,
    CONTEXT,
    `Assessments:`,
    JSON.stringify(assessed, null, 0),
    `Rank highest-value first. Lead with ARLO-relevant high-value gaps (MIDI CC maps for`,
    `midi:true devices that lack one, anchor texture/looping devices, thin multi-product`,
    `software vendors). Include the ~15-20 best targets with concrete open questions each.`,
    `Set generatedFor = "${date}".`,
  ].join('\n\n'),
  { label: 'rank-queue', phase: 'Rank', schema: QUEUE_SCHEMA },
)

log(`Queue ranked — ${(ranked && ranked.targets || []).length} targets.`)
return ranked
