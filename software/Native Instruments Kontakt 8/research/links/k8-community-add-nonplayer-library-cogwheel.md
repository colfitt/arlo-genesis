https://support.native-instruments.com/hc/en-us/articles/6677339715741-How-to-Add-Non-Player-Libraries-to-Kontakt-7-8-s-Browser
Native Instruments support (distilled via community + Triumph Audio mirror: https://www.triumphaudio.com/blog/loading-our-libraries-into-kontakt-for-quick-loading) · current

# Adding a NON-Player (full-Kontakt) library to Kontakt 7/8's browser — the NEW way

**What changed.** The old standalone **"Add Library"** button (and the older wrench/cog "Manage Libraries" panel) is gone. Non-Player libraries are no longer activated in Native Access — you import them manually into Kontakt's own browser.

**Steps (Kontakt 7/8):**
1. Open Kontakt → go to the **Library** tab (left side panel).
2. Click the **cogwheel ("Import Content") icon** in the **lower-left** of the Library tab.
3. In the Import Content window, click **Add**, navigate to the folder containing the non-Player library, select it → confirm.
4. The library now appears in Kontakt's Library Browser. (Non-Player libraries require **full Kontakt**, not Player — and do NOT need Native Access activation.)

**Bulk import:** check **"import subfolders as individual libraries"**, point it at a parent folder holding several libraries, and each subfolder imports as its own library entry. (Handy for an external drive full of third-party Kontakt libs.)

**Remove a library:** cogwheel → select the library → **Remove** (removes the browser entry, not the files).

**If a library won't appear:** it was likely built with **Kontakt < 5.0** — run **Batch Re-Save** on it first to make it K7/8-browser-compatible.

**Player vs full recap:** Player libraries (serial in Native Access) browse in both Player and full Kontakt. Libraries with NO serial = full-Kontakt only, imported via the cogwheel; in Player they'd only run in 15-min demo mode.
