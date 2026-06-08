Manual: SL MkIII User Guide V2, p.6, p.13–14, p.25
Novation manual

# The Sessions / Parts / Patterns model — the data hierarchy

## The hierarchy (top down)
- **Session** = the whole save unit. Contains all **8 Parts** (each = its own sequencer + Template + destination + MIDI channel + colour), and all **8 patterns per Part**, plus the Scales settings, Arp settings, and Zones. There are **64 Sessions** total.
- **Part** = one of 8 sequencer "tracks." Each Part has its own Template (control map), MIDI channel (1–16, no global channel), destination (USB/DIN1/DIN2/CV-Gate, any combination), and colour.
- **Pattern** = one 16-step sequence. Each Part holds **8 patterns**. Each pattern has its own Steps view (per-step data) and Patterns view (start/end/direction/sync/shift) settings.
- **Step** = one of 16 steps in a pattern. Each step carries: notes (poly), velocity, gate (1–32 steps long), chance/probability, and **6 micro-steps**.

So one Session = 8 Parts × 8 patterns × 16 steps × 6 micro-steps, plus templates/scales/arp/zones.

## Sequencer on/off and entering Sequencer view
- **Turn sequencer On/Off:** hold **Shift + Sequencer**. Sequencer button = white (on), orange (off).
- **Enter Sequencer view:** press **Sequencer**. Two subviews: **Steps view** (Steps button) and **Patterns view** (Patterns button).
- When the Sequencer button is orange (off) you can still press it to *view/edit* the sequence, but the **Transport buttons are unusable until the sequencer is re-enabled.**
- The **Grid** button toggles the 8×2 pads between the last Sequencer subview and Template mode.

## Part Settings (Templates view) — Shift + Sessions
Press **Shift + Sessions** to enter Templates view. Select a Part with the soft buttons under the screens, then:
- **Template** (left-most rotary): choose which control-map template the Part uses. Rectangle goes grey while loading, white when loaded. Unnamed = "Template X"; rename only in Components.
- **Destination:** set rotaries above USB / DIN1 / DIN2 / CV-Gate1 / CV-Gate2:
  - USB: Off / On
  - DIN: Off / 1 / 2 / Both
  - CV/Gate: Off / 1 / 2 / Both
  - A Part can go to **multiple destinations at once**. Destinations are stored in the Session.
- **Channel** (rotary 6, third screen): MIDI channel **1–16** per Part. There is **no global MIDI channel.**
  - **Gotcha:** Channel **16** is the global channel for Program Change & Song Select. A Part set to ch.16 can have an external device's PC accidentally change the *Session on the SL itself* and lose unsaved work.
- **Input Monitoring** (off by default): when On, MIDI notes received on the Part's channel forward to the Part's destinations. The internal sequencer **always records external MIDI notes regardless** of this setting.
- **Edit Part Colour:** with a Part selected, press one of the 8 coloured pads.

## Session management (Sessions button)
- **Sessions layout:** 64 sessions across **4 pages of 16** (the 8×2 pads). Up/down arrows left of the pads change page.
- **Load:** enter Sessions view, press a pad.
- **Save:** press **Save** (it flashes), press **Save** again to confirm. To save to a *new slot*, after Save flashes pick a different pad (overwrites that slot). While Save flashes you can use the two left-most soft buttons to scroll session colours.
- **Clear a session:** select it, hold **Clear** + press its pad (resets all data to default).
- **Cued session switch** (while playing): press a pad in Session view → pad turns white, session loads at the **end of the currently playing pattern on Part/track 1**.
- **Instant session switch** (while playing): **hold Shift + press a pad** → new session picks up from the current position in the playing pattern.
- **Program Change load:** send PC on **ch.16** → session loads instantly. **Add 64 to the program ID** → the sequencer *cues* the session load instead of instant.
- **Song Select load:** send Song Select while the sequencer is **stopped**; the Song ID = the session to load.
- **Save Lock:** **hold Shift + Save** to toggle. When on, the SL cannot save sessions (Save LED off) — protects work from accidental PC-ch.16 overwrites. State persists through power-off. Repeat to turn off.
