https://gregkocis.com/how-to-create-multiple-outputs-for-kontakt-8-in-logic-pro/
gregkocis.com · Greg Kocis · current (Kontakt 8 era)

# Multiple outputs: Kontakt 8 → Logic Pro (separate Kontakt instruments to their own Logic channels)

## 1. Enable multiple outputs IN Kontakt 8
1. Launch the **Kontakt 8** AU inside Logic.
2. Find the **Output Section** at the bottom of Kontakt; if hidden, go to **View → Outputs**.
3. Click the **"+"** to add new output channels; choose how many stereo outputs you want (e.g. 8 for a drum kit, or one per instrument).
4. Click Apply; optionally **save as default** so future sessions start multi-out.
5. **Pro tip:** name the outputs ("Strings," "Drone," "Pad") so they read clearly in Logic.

## 2. Route each instrument to its own output
- For each loaded instrument, click the **gear/output icon** in the instrument header and pick its output channel.
- Default is that everything sums to output 1/2 (st.1) — you must reassign manually.

## 3. Set up Logic's mixer
1. Open the **Mixer** (press **X**).
2. Find the Kontakt instance and click the small **"+"** at the bottom of its channel strip — each click adds an **Aux** track whose input is auto-assigned to the next Kontakt output in ascending order (Aux 1 = Out 3/4, etc.).
3. Rename the aux tracks to match.

**Result:** each Kontakt instrument has independent volume, EQ, and FX in Logic — e.g. a wet shimmer reverb on the drone aux only, dry on the string aux.

**Gotcha (Logic-specific):** you must instantiate Kontakt as the **Multi-Output** variant from Logic's plugin menu (e.g. "Kontakt 8 ▸ Multi-Output (16xStereo)") for the "+" aux trick to expose channels. The plain stereo instance won't.
