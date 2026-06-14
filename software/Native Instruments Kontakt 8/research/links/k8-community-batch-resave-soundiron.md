https://soundiron.com/pages/pro-tip-1-run-a-kontakt-batch-resave-on-your-libraries-to-speed-up-instrument-load-times
soundiron.com (sample-library developer) · "Pro Tip #1: Run a Kontakt Batch Resave" · undated (current)

# Kontakt batch re-save — the single most important post-install step

**Why it matters.** Batch re-save stores the *sample path information for a library specifically for your machine and hard-drive layout*. This dramatically speeds up loading times — especially for big/RAM-heavy libraries — because Kontakt no longer has to search for samples each load. Soundiron calls it "the most important thing you can do after installing any Kontakt library."

**Steps:**
1. Open Kontakt → click the **Files** button (top toolbar) → choose **Batch Re-Save** from the dropdown.
2. Confirm the warning prompt → **Yes**.
3. A browser window opens — navigate to and select your **library folder** → **OK**.
4. Kontakt resaves every preset (.nki/.nkm) with localized sample-path data.

**Missing-samples protocol:** if a "Samples Missing" window appears during the resave, click **Browse For Folder**, point it at the folder that actually contains the library's samples, and confirm. This relinks broken paths *as part of* the resave.

**Rig note (external sample drive):** because the resave bakes in the path for *this machine and this drive*, anyone running Spitfire/Komplete libraries from an external drive should batch re-save after the first install from that drive. If the drive's mount path/letter changes you can re-run it to relink.
