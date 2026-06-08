https://www.elektronauts.com/t/banks-and-parts/12461
elektronauts.com · Octatrack subforum (+ "Banks & patterns" /15570, "Slotlist/parts/patterns/banks/scenes" /16722, "structure project-bank-pattern" /220271, manual p.72)

# Parts vs Banks vs Patterns vs Scenes — the mental model that ends the confusion

The single biggest newcomer trap on the OT. The clean hierarchy:

```
SET            (one per CF card's work; holds the shared Audio Pool)
 └ PROJECT     (16 banks, 128 Flex + 128 Static sample slots, BPM, arrangements)
    └ BANK     (16 of them per project)   →  4 PARTS  +  16 PATTERNS
       ├ PART     = "a preset/patch for your 8 tracks": machine assignments,
       │           sample assignments, FX, track params, LFO setups, + 16 SCENES
       └ PATTERN  = sequencer data only (trigs, p-locks, length, tempo) — POINTS at a Part
```

## Why "I changed one knob and other patterns changed"
- **A Part is shared by multiple patterns.** Each bank has only **4 Parts but 16 Patterns** — so several patterns reference the same Part. Tweaking a machine/FX/scene edits the PART, which propagates to every pattern linked to it. That's a feature (variations) once you expect it.
- Community framing: "parts are simply a preset/patch for the setup of my 8 tracks." Patterns are just the notes/trigs played through that patch.

## The deeper gotcha: sample slots are PROJECT-WIDE
- "The sample lists for static and flex machines are shared by ALL banks. Change the sample in slot 4 and it changes for all banks/patterns" — until you switch projects.
- So a Flex/Static slot is a project-global pointer. Reassigning a slot ripples everywhere it's used. Workaround some use: keep empty machines pointed at a silent short "NULL" audio file as safe templates across banks.

## Saving / retention (critical)
- **If you are NOT working "within a project," only the ACTIVE bank is retained at power-off.** Changes to OTHER banks are lost unless you **SAVE PROJECT.** Always Save Project before powering down or pulling the card.
- **PART must be saved separately** too — and **PART RELOAD** lets you tweak a Part destructively live, then snap back to the last saved state. Save the Part when you like it; reload to undo a jam.

## The takeaway for surviving the learning curve
Internalize "**Part = sound, Pattern = sequence, slots = project-global, SAVE everything**" and 80% of the OT's "why did that happen?" mysteries disappear.
