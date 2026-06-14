https://support.spitfireaudio.com/en/articles/11815319-can-i-download-my-library-to-an-external-hard-drive
Spitfire Audio Help Centre · support article · accessed 2026-06-10
(+ https://www.spitfireaudio.com/info/library-manager · library manager overview)
(+ https://support.spitfireaudio.com/en/articles/11815356-moving-libraries · Moving Libraries)

# Spitfire Audio app — external-drive install + move workflow

## The app
The **Spitfire Audio app** (macOS/Windows) is the library manager: install/update all Spitfire products, "view all your libraries at a glance," smart filtering by name/size/install status, and a clear install process letting you choose between a direct download or a specific HDD/SSD install location.

## Installing to an external drive (e.g. `PlaySomeGodDamnMusic`)
1. Find the **Install** button next to the library.
2. Click the **folder icon** to browse to the external drive's location.
3. Click **Install** to download there.
- To make it permanent: app **Settings → Default Content Path** → point at the external drive.

## Drive format requirements (important for the rig's external drive)
- **Mac: must be `Mac OS Extended (Journaled)`.** Windows: NTFS.
- **ExFAT** will prompt a reformat; **FAT32 is incompatible** ("doesn't support data unpacking").
- Running libraries from external storage: **SSD preferred**; if HDD, **7200 rpm minimum**.
- Need enough free space during install (compressed downloads unpack — budget ~2× the listed size while installing).

## Moving an already-installed library (the offline-drive reality)
The app relocates only the *registration*, **not** the actual content. To move content: drag the library folder to the new location (or use a transfer app), THEN tell the app where it went:
- Each product's tile has a **cog menu** with two key options:
  - **Locate** — relink a library that's been moved on the **same** machine (point it at the new path).
  - **Repair** — resolve plugin errors / re-authorize a library on a **new machine or drive**.

## Rig note
Because the user's Spitfire content lives on the external drive **`/Volumes/PlaySomeGodDamnMusic/Sample Libraries/Spitfire`**, that drive must be **mounted before launching Logic** or the plugins will show "library not found" / need a **Locate**. The *plugins* (AU/VST3 in `~/Library/Audio/Plug-Ins/...`) live on the system drive and always load; it's the multi-GB **sample content** that requires the drive online. Kontakt-based Spitfire libs (Loegria, Swarm, Evolutions, Symphony Orchestra) behave the same — Kontakt needs the sample path mounted.
