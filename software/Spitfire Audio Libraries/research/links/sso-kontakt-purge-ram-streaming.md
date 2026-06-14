https://support.spitfireaudio.com/en/articles/11815574-spitfire-symphony-orchestra-faq
Spitfire Audio Help Centre · SSO FAQ + RAM-reduction article · accessed 2026-06-12
(also: https://support.spitfireaudio.com/en/articles/11815932-how-to-reduce-ram-in-bbc-symphony-orchestra-core-and-pro)

# SSO in Kontakt 8 — size, Player vs full, purge/RAM/streaming, external-drive gotchas

**Format / host:**
- Runs in **full Kontakt OR the free Kontakt Player**; **minimum Kontakt 7.5.2**. Owner has
  **Kontakt 8** → fully covered. (SSO is NOT a dedicated AU plugin like BBC SO/LABS — it is a
  Kontakt library, so in Logic you **open Kontakt 8 as an AU first, then load SSO inside it.**)
- **~368 GB** download (PCs may report lower). Up to **2 machines** per license.
- **4 GB RAM min, 6 GB recommended** per large Kontakt instrument (a baseline; multi-mic
  orchestral templates want far more).

**Cutting RAM / CPU (the levers that matter on the offline-drive rig):**
- **Purge unused techniques** via the **Technique Editor** — remove articulations (and their
  samples) you're not using. For a drone bed you typically need ONE long/sul-tasto technique,
  so purge everything else → massive RAM saving.
- **Remove unneeded mic signals** — each mic is a separately streamed layer. A single mic
  (Close OR Tree OR Outriggers) is a big saving vs loading all four. Ghost/wall work wants 1–2.
- Use the **economic/individual patches** where offered (lighter than full multi-mic patches).
- **DFD streaming**: Kontakt keeps only a small **pre-load buffer** of each sample in RAM;
  tune buffer size to your drive (Options → Engine). Smaller preload = less RAM, more disk hits.
- **Kontakt Options → Engine → CPU Overhead Protection** for dropout protection.

**External-drive reality (the `PlaySomeGodDamnMusic` drive):**
- SSO content lives on the offline drive. **Mount it before launching Logic**, or Kontakt
  shows the library "not found" / asks to locate. SSD strongly preferred — 368 GB streamed
  from an HDD over a slow bus is the classic dropout cause.
- **Best habit for this rig: bounce held beds to audio.** Once you've played the wall, render
  it → frees all the streaming/RAM and removes the drive as a live dependency (you can then
  PaulStretch / degrade the bounce). Same offline-wall habit as the Cells/LABS/BBC SO guides.
