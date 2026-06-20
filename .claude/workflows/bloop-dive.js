/**
 * bloop-dive — run ONE research bloop against ONE target.
 * ---------------------------------------------------------------------------
 * This is a Workflow: a script that orchestrates many sub-agents deterministically.
 * Read it as your worked example of how sub-agents + fan-out + verify + synthesize fit
 * together. The TEACHING NOTES inline call out the moving parts.
 *
 * Four phases (see research/playbook.md §3):
 *   1. RECON      — 1 sub-agent reads what the corpus ALREADY holds → returns gaps.
 *   2. FAN-OUT    — ~5 sub-agents in PARALLEL, one research lens each.
 *   3. VERIFY     — skeptic sub-agents adversarially refute the load-bearing claims.
 *   4. SYNTHESIZE — 1 sub-agent writes the digest file + returns a COMPACT summary.
 *
 * The Workflow writes ONLY to research/bloops/. The corpus, the index, and v2 are
 * never touched here — promotion is a human step (playbook §7).
 *
 * Invoked by /bloop (or by hand) with args:
 *   {
 *     target:     "Chase Bliss MOOD MkII",        // required: what to research
 *     slug:       "chase-bliss-mood-mkii",        // required: filename slug
 *     date:       "2026-06-19",                    // required (script can't call Date.now)
 *     category:   "gear" | "software" | "technique",
 *     corpusPath: "gear/Chase Bliss MOOD MkII",   // existing corpus dir, or null if new
 *     focus:      "looping + MIDI control",        // optional emphasis
 *     musicGoal:  "Cold-wire track B",             // optional active music goal
 *     freshSignal: false,                          // optional: add a last30days lens
 *     lenses:     [ ...override default lenses ]    // optional
 *   }
 */

export const meta = {
  name: 'bloop-dive',
  description: 'Run one research bloop: recon the corpus, fan out research lenses, adversarially verify, synthesize a staged digest in research/bloops/.',
  phases: [
    { title: 'Recon',      detail: 'read what the corpus already holds; return the gaps' },
    { title: 'Fan-out',    detail: '~5 parallel research lenses, each sourced' },
    { title: 'Verify',     detail: 'adversarially refute the load-bearing claims' },
    { title: 'Synthesize', detail: 'write the digest + return a compact summary' },
  ],
}

// --- read + validate inputs -------------------------------------------------
// args can arrive as a live object OR a JSON string depending on the caller —
// normalise so a.field works either way.
let a = args || {}
if (typeof a === 'string') { try { a = JSON.parse(a) } catch (_) { a = {} } }
const target     = a.target
const slug       = a.slug
const date       = a.date
const category   = a.category || 'gear'
const corpusPath = a.corpusPath || null
const focus      = a.focus || ''
const musicGoal  = a.musicGoal || ''
const freshSignal = a.freshSignal === true

if (!target || !slug || !date) {
  throw new Error('bloop-dive requires args.target, args.slug, and args.date')
}

const digestPath = `research/bloops/${date}-${slug}.md`

// The "technical" lens means different things for gear vs software.
const technicalBrief = category === 'software'
  ? 'Parameters that matter, automation / MIDI-learn, plugin formats (VST3/AU/AAX), CPU cost, preset management, routing & sidechain.'
  : 'MIDI implementation + full CC map, expression/CV, I/O & routing, preset recall, and the exact control surface ARLO would drive.'

// Default research lenses. Each becomes one parallel sub-agent in the fan-out.
// Override per-run via args.lenses.
const DEFAULT_LENSES = [
  { key: 'official',   brief: 'Official manual, spec sheet, firmware/changelog, manufacturer docs. Ground truth on what it does.' },
  { key: 'community',  brief: 'Forums & Reddit (Gearspace, r/<gear>, manufacturer forum): real-world tips, gotchas, favourite settings, bugs.' },
  { key: 'video',      brief: 'YouTube demos/tutorials: dialed-in settings, signal chains, what experienced users actually do with it.' },
  { key: 'technical',  brief: technicalBrief },
  { key: 'comparison', brief: "How it compares to alternatives and where it earns its place in the user's rig and genres (ambient / lo-fi / post-rock / electronic)." },
]
const lenses = a.lenses || DEFAULT_LENSES
if (freshSignal) {
  lenses.push({ key: 'fresh', brief: 'Use the last30days research tool to surface what is NEW in the last 30 days: firmware, techniques, deals, releases, notable discussion.' })
}

// --- schemas: force sub-agents to return validated structured data ----------
// TEACHING NOTE: passing `schema` to agent() makes the sub-agent call a
// StructuredOutput tool. agent() then returns the validated OBJECT (not text),
// and the model auto-retries until it matches. No parsing, no regex.

const RECON_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['known', 'existingArtifacts', 'gaps'],
  properties: {
    known: { type: 'string', description: '2-4 sentences: what the corpus already establishes about this target.' },
    existingArtifacts: { type: 'array', items: { type: 'string' }, description: 'Relative paths of corpus files that already cover this target.' },
    gaps: {
      type: 'array',
      description: 'Specific, concrete gaps the existing material is missing. Drives the fan-out.',
      items: {
        type: 'object', additionalProperties: false,
        required: ['gap', 'priority'],
        properties: {
          gap: { type: 'string' },
          priority: { type: 'string', enum: ['high', 'medium', 'low'] },
        },
      },
    },
  },
}

const LENS_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['lens', 'findings'],
  properties: {
    lens: { type: 'string' },
    findings: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        required: ['claim', 'detail', 'sources', 'confidence', 'notable'],
        properties: {
          claim: { type: 'string', description: 'One-sentence factual claim.' },
          detail: { type: 'string', description: 'Supporting specifics / how-to / exact settings.' },
          sources: { type: 'array', items: { type: 'string' }, description: 'URLs or named sources. Empty array if none — never invent.' },
          confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
          notable: { type: 'boolean', description: 'True if load-bearing enough to deserve adversarial verification.' },
        },
      },
    },
  },
}

const VERDICT_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['claim', 'verdict', 'reason'],
  properties: {
    claim: { type: 'string' },
    verdict: { type: 'string', enum: ['confirmed', 'refuted', 'uncertain'] },
    reason: { type: 'string' },
    correctedDetail: { type: 'string', description: 'If refuted/uncertain, the corrected or caveated version. Empty if confirmed.' },
  },
}

const SYNTH_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['target', 'digestPath', 'summary', 'verifiedFindings', 'suggestedCorpusEdits', 'candidateChunks', 'followUpQuestions'],
  properties: {
    target: { type: 'string' },
    digestPath: { type: 'string' },
    summary: { type: 'string', description: '3-6 sentences: what this bloop actually learned.' },
    verifiedFindings: { type: 'array', items: { type: 'string' }, description: 'The confirmed, promotion-worthy findings as short statements.' },
    suggestedCorpusEdits: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        required: ['file', 'change'],
        properties: { file: { type: 'string' }, change: { type: 'string' } },
      },
      description: 'Concrete edits to the per-item corpus to propose to the human.',
    },
    candidateChunks: { type: 'array', items: { type: 'string' }, description: 'Short, standalone facts suitable for the suggestion index.' },
    followUpQuestions: { type: 'array', items: { type: 'string' }, description: 'New questions this bloop surfaced — to append to queue.md.' },
  },
}

// === PHASE 1 · RECON ========================================================
// One sub-agent reads the corpus so the bloop LAYERS on prior passes (playbook §1).
phase('Recon')
const reconCorpus = corpusPath
  ? `Read the existing corpus for this target under "${corpusPath}" (and its research/ subfolder): GearProfile, *-DeepResearch.md, *-UsageGuide.md, links/, transcripts/, manuals/, presets/. List what already exists and summarise what is already known.`
  : `There is no existing corpus folder for this target. Treat it as net-new and frame the gaps from scratch.`

const recon = await agent(
  [
    `You are the RECON pass of a research bloop on: "${target}" (category: ${category}).`,
    reconCorpus,
    focus ? `The human asked to emphasise: ${focus}.` : '',
    musicGoal ? `Active music goal to serve: ${musicGoal}.` : '',
    `Return: a tight summary of what is ALREADY known, the existing artifact paths, and a prioritised list of the CONCRETE GAPS the next research pass should fill. Be specific — "no MIDI CC map" beats "needs more detail".`,
  ].filter(Boolean).join('\n\n'),
  { label: `recon:${slug}`, phase: 'Recon', schema: RECON_SCHEMA },
)

const gapsText = (recon && recon.gaps || []).map(g => `- [${g.priority}] ${g.gap}`).join('\n') || '- (recon returned no explicit gaps; research broadly)'
log(`Recon done — ${(recon && recon.gaps || []).length} gaps identified for "${target}".`)

// === PHASE 2 · FAN-OUT ======================================================
// Each lens is an independent sub-agent with its OWN clean context. parallel()
// runs them at once and BARRIERS (waits for all) — we need every lens before we
// can decide what to verify. A thunk that throws resolves to null, so filter.
phase('Fan-out')
const buildLensPrompt = (lens) => [
  `You are the "${lens.key}" research lens of a bloop on: "${target}" (category: ${category}).`,
  `Your angle: ${lens.brief}`,
  `Known so far (do not just repeat it — go BEYOND it):\n${(recon && recon.known) || '(nothing on file)'}`,
  `Gaps to prioritise:\n${gapsText}`,
  focus ? `Emphasis: ${focus}.` : '',
  musicGoal ? `Serve this music goal where relevant: ${musicGoal}.` : '',
  lens.key === 'fresh'
    ? `Use the last30days research tool (find it via ToolSearch) for recent signal.`
    : `Use WebSearch + WebFetch. Prefer primary sources. NEVER invent a source or a setting — if you cannot source it, leave sources empty and mark confidence low.`,
  `Return your findings as structured data. Mark the load-bearing ones notable:true so they get verified.`,
].filter(Boolean).join('\n\n')

const lensResults = await parallel(
  lenses.map(lens => () =>
    agent(buildLensPrompt(lens), { label: `lens:${lens.key}`, phase: 'Fan-out', schema: LENS_SCHEMA })
  )
)
const findings = lensResults.filter(Boolean)
const allFindings = findings.flatMap(r => (r.findings || []).map(f => ({ lens: r.lens, ...f })))
log(`Fan-out done — ${findings.length}/${lenses.length} lenses returned, ${allFindings.length} findings total.`)

// === PHASE 3 · VERIFY =======================================================
// Adversarial check of the load-bearing claims. Each skeptic is told to REFUTE,
// defaulting to "uncertain" if it cannot confirm — this is what keeps plausible-
// but-wrong findings out of the digest. Cap the count to stay bounded.
phase('Verify')
const notable = allFindings.filter(f => f.notable).slice(0, 12)
const verdicts = notable.length
  ? (await parallel(
      notable.map(f => () =>
        agent(
          [
            `Adversarially verify this claim about "${target}". Try to REFUTE it.`,
            `Claim: ${f.claim}`,
            `Detail: ${f.detail}`,
            `Cited sources: ${JSON.stringify(f.sources)}`,
            `Use WebSearch/WebFetch to check it against independent sources. If you cannot confirm it from a credible independent source, return "uncertain" — do not give it the benefit of the doubt. If it is wrong, return "refuted" with the corrected detail.`,
          ].join('\n\n'),
          { label: `verify:${f.lens}`, phase: 'Verify', schema: VERDICT_SCHEMA },
        )
      )
    )).filter(Boolean)
  : []
const confirmed = verdicts.filter(v => v.verdict === 'confirmed').length
log(`Verify done — ${confirmed}/${verdicts.length} confirmed, ${verdicts.filter(v => v.verdict === 'refuted').length} refuted.`)

// === PHASE 4 · SYNTHESIZE ===================================================
// One sub-agent WRITES the digest file (it has the Write tool) and RETURNS the
// compact summary the steering session uses. The big text stays on disk; only the
// summary comes back — that is the context-rot defense in action (playbook §1).
phase('Synthesize')
const digest = await agent(
  [
    `You are the SYNTHESIS pass of a research bloop on "${target}" (category: ${category}).`,
    `Write a digest to EXACTLY this path using the Write tool: ${digestPath}`,
    ``,
    `Use this structure (mirror the house DeepResearch/UsageGuide tone — practical, sourced, no fluff):`,
    `# Bloop — ${target}`,
    `Date: ${date} · Category: ${category}${corpusPath ? ` · Corpus: ${corpusPath}` : ''}`,
    `## What we already knew  (from recon)`,
    `## New findings  (verified)   — group by lens; cite sources inline`,
    `## Flagged / uncertain        — refuted or unconfirmed claims, with corrections`,
    `## Suggested corpus edits     — exact files + what to add`,
    `## Candidate index chunks     — short standalone facts for the suggestion index`,
    `## Follow-up questions        — what to bloop next`,
    `## Sources`,
    ``,
    `INPUT DATA:`,
    `Recon: ${JSON.stringify(recon)}`,
    `Findings: ${JSON.stringify(allFindings)}`,
    `Verdicts: ${JSON.stringify(verdicts)}`,
    ``,
    `Rules: prefer verified/confirmed findings in "New findings"; move refuted/uncertain to "Flagged". Never invent sources. Then return the compact summary as structured data (digestPath = ${digestPath}).`,
  ].join('\n'),
  { label: `synthesize:${slug}`, phase: 'Synthesize', schema: SYNTH_SCHEMA },
)

log(`Bloop complete — digest at ${digestPath}.`)
return digest
