# Loudness Normalization on Spotify

**Source:** Spotify for Artists official documentation
**URL:** https://support.spotify.com/us/artists/article/loudness-normalization/
**Captured:** 2026-05-24
**Tags:** `mastering`, `LUFS`, `streaming`, `reference-fact`, `delivery`

---

## Overview

Spotify applies loudness normalization to balance audio levels across its platform. The service adjusts tracks to **-14 dB LUFS**, according to the ITU 1770 standard. This normalization occurs during playback only; original audio files remain unmodified.

## How Normalization Works

The system treats albums and playlists differently:

- **Albums**: All tracks normalize together to maintain relative volume differences
- **Playlists/Shuffled**: Individual tracks adjust independently

## Gain Compensation

**Negative gain** reduces louder tracks, while **positive gain** amplifies softer ones. For positive gain applications, Spotify leaves **1 dB headroom for lossy encodings** to preserve audio quality, with a specified example showing tracks limited to -16 dB LUFS when True Peak maxes at -5 dB FS.

## Premium User Options

Premium subscribers can select alternative normalization levels:

- **Loud**: -11 dB LUFS (with limiter at -1 dB)
- **Normal**: -14 dB LUFS
- **Quiet**: -19 dB LUFS

## Mastering Guidelines (per Spotify)

- Target masters at **-14 dB integrated LUFS**
- Maintain **True Peak below -2 dB** for louder tracks to avoid distortion during compression encoding

---

## Cross-platform reference (for ARLO retrieval)

| Platform | Integrated LUFS target | True Peak ceiling |
|----------|------------------------|-------------------|
| Spotify (Normal) | -14 LUFS | -1 dBTP (Spotify says -2 dB for safety) |
| Spotify (Loud, premium) | -11 LUFS | limited to -1 dB |
| Spotify (Quiet, premium) | -19 LUFS | n/a |
| Apple Music | -16 LUFS | -1 dBTP |
| YouTube Music | -14 LUFS | -1 dBTP |
| Tidal | -14 LUFS | -1 dBTP |
| Amazon Music | -14 LUFS | -2 dBTP |
