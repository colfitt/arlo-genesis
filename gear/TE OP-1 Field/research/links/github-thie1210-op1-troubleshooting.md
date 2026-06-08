https://gist.github.com/thie1210/74f3774a83cb36169a9154eb827910b9
github gist (thie1210) · community troubleshooting guide (references r/OP1users) · OP-1 / OP-1 Field

The community's go-to "my OP-1 won't charge / won't boot / how do I reset" guide. Combos apply to the Field too (TE-Boot is the same).

## TE-Boot (firmware / reset / diagnostics)
- Power off, disconnect USB, wait a few seconds.
- **Hold the COM key while turning power on** → TE-Boot screen (a speaker click = normal operation). From here: upload firmware or factory reset.
- (Diagnostic tests: hold SHIFT + COM on power-on; Shift-2 = motherboard test, Shift-3 = colour-bar/loopback tests.)

## Won't start / won't charge — battery recovery
1. Power off completely; disconnect USB; wait a few seconds.
2. **Connect to a computer/charger via USB and leave it OFF for a few hours.**
3. Disconnect USB, wait ~3 s, reconnect, check for charging. Repeat as needed.

## Battery-gauge recalibration (starts but charge reading is wrong)
1. Disconnect USB, turn ON, and **leave it on until it powers itself off** — do NOT manually power down (can take up to ~18 h).
2. Once the screen is black, fully charge over USB (2.5–6 h). Battery is ~1800 mAh.

## When it charges
- Charges when OFF + on USB power; when ON + USB connected (unless disabled in OPT menu: SHIFT+COM, then 4); and in TE-Boot with USB connected.

## Rig takeaway
TE advises charging the cell at least every 6 months (dossier §8). If the OP-1f sits unused between sketch sessions, top it up periodically — a fully drained Li cell is what triggers the "won't turn on" panic, and the leave-it-on-USB-off-for-hours recovery above is the fix.
