https://help.uaudio.com/hc/en-us/articles/115004340706-Troubleshooting-No-Devices-Found-and-Other-Connection-Issues
Universal Audio Support · "Troubleshooting No Devices Found and Other Connection Issues"
(supporting: UA "How to Allow Universal Audio Software on macOS"; Sweetwater "Enabling Kernel Extensions on Mac with Apple silicon"; audiosupport.co.uk case #5219, Jun 2025)

(Distilled from search + a fetchable third-party walkthrough; help.uaudio.com blocks direct fetch. This is the Apollo's #1 real-world pain point — Thunderbolt/driver fragility, especially after macOS updates.)

THE COMMON FIX — ALLOW THE UA SYSTEM EXTENSION (after install or a macOS update):
1. Apple menu → System Settings (System Preferences on older macOS).
2. Privacy & Security.
3. Scroll down to the message: "System software from developer 'Universal Audio' has been updated" / blocked.
4. Click "Allow" next to it.
5. RESTART the Mac when prompted — critical for the driver change to take effect.
6. Verify: open UAD Console and the UAD Meter & Control Panel; the Apollo should show as connected and active.

APPLE SILICON (M1/M2/M3) — ENABLE KERNEL EXTENSIONS (one-time, BEFORE installing UAD software):
1. Shut down. Press and hold the power button until "Loading startup options" appears → Options → Continue (Recovery mode).
2. Set the Security Policy to "Reduced Security."
3. Check "Allow user management of kernel extensions from identified developers." OK.
4. Restart. THEN install UAD software and "Allow" it in Privacy & Security.
- Keep these Security Policy settings — UAD needs them to function. UAD software must be on an INTERNAL system drive (external boot drives are not supported).

CONNECTION TROUBLESHOOTING:
- Connect the interface DIRECTLY to the computer. Hubs and docking stations "can cause complications and are not supported."
- Every UA Thunderbolt device must be daisy-chained from a SINGLE Thunderbolt port (Apollos share clocking over Thunderbolt).
- Swap the Thunderbolt data cable — bad/defective cables are common, even relatively new ones. Confirm it's a true Thunderbolt cable (USB-C ≠ TB3).
- Last resort: full uninstall of UAD software (removes apps, drivers, prefs) then reinstall the latest version like new.

PRACTICAL RULE FOR THE RIG: don't update macOS the day before a session; check UA's compatibility page first; after any macOS update expect to re-grant the Privacy & Security permission and restart.
