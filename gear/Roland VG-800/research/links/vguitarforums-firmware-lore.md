https://www.vguitarforums.com/smf/index.php?topic=38330.0
vguitarforums.com · "Firmware update" thread (stevereel + Elantric) · started Feb 25, 2025 · cross-checked vs official BOSS support page

## Verified firmware reality (as of June 2026)
- **Latest official version is still v1.02 (Jan 16, 2025).** Official BOSS VG-800 Updates & Drivers changelog lists exactly ONE history entry:
  - **Additional functions:** *"Support for BOSS TONE STUDIO for VG-800."*
  - **Bug fixes:** *"Improved system stability."*
- **No version later than 1.02 exists on the official support page.** No v1.03/1.04/1.05.
- Shipping units came on **v1.01**; v1.02 is the update.

## The "low E/A latency fix" claim — VERDICT: UNVERIFIED / likely false
- Several secondary web snippets assert the low E/A-string latency was *"fixed a year later"* in a firmware update. **This cannot be substantiated.** The official changelog shows nothing of the kind, and the forum firmware thread contains **no user report** of a latency/tracking fix — its actual content is a macOS unzip problem (extracting `VG-800_UPA_up.bin` from the zip after Apple changed the Archive Utility).
- **Most likely confusion:** the *GM-800* (sister Serial-GK unit) DID get a substantive **v1.10** update with tracking-related changes. The "fixed a year later" lore appears to be GM-800 firmware being misattributed to the VG-800. Treat the VG-800 latency-fix claim as **unconfirmed and probably a cross-product mixup** until BOSS publishes a v1.03+.
- Practical implication: do NOT expect a firmware to fix low-string wobble. **Calibration (SENS/DISTANCE) is the fix**, not a download.

## Firmware update gotcha (real, documented)
- **stevereel (Feb 25, 2025):** on macOS the downloaded zip must yield the file **`VG-800_UPA_up.bin`** — Apple's updated unarchiver can leave you with a folder structure instead of the raw `.bin`, breaking the USB-C update. Extract the `.bin` explicitly.

## Mode note tied to firmware
- **FW 1.02** is what enables **USB GENERIC class-compliant audio mode** (for iOS/Android), at the cost of disabling the highest-CPU "Re-Guitar" multichannel USB mode (Elantric).
