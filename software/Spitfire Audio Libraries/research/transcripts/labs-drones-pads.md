https://www.youtube.com/watch?v=SVf3k-a0aZs
DaveMarks · Create Better drones and pads with Spitfire LABS · 2025-04-15 (9:39)

[The single most on-aesthetic LABS tutorial found: a working composer builds a long, evolving, playable G-drone for a live show entirely from three layered Spitfire LABS instruments, then EQs/reverbs/delays them into a "sound bed for an entire scene." This is the exact drone-wall, layering-and-trails workflow this rig wants.]

## The brief

For a recent live show in Bremen, Germany (Limitless Orchestra), the opening was six minutes of sustained G with a "mother earth" quality and a voiceover over the top. The keyboard player had to hold G for six minutes — painful to listen to and to play if it's just a boring sine wave. The goal: design an instrument that's really dynamically responsive and has an interesting mixture of sounds, so a single held drone stays alive.

## The build — three LABS instruments blended

Three Spitfire LABS plugin sounds layered: a pad on the LEFT, a bass in the MIDDLE, a pad on the RIGHT.

### Left pad — LABS "Arctic Swells," Decay preset
Only two presets in that sound: Decay and Swells. On the left he used Decay. Settings:
- Release cranked up pretty high (so you get a nice long trail when you let go).
- Sustain all the way up.
- Decay almost halfway.
- Variation halfway.
- A little reverb.
- A nice long (gradual) ATTACK so it doesn't just blast in when you hit a key — "so it doesn't just go *whenever I hit it*." It breathes in.

Why the long attack + long release: it lets the player let go occasionally and play again, so the sound feels like it's breathing — and the player's hands don't get tired holding one position for the whole show.

Then a LOT of EQ to get rid of all the top end — muffle it right down. Reason: with three sounds combined, if every layer sends lots of high-end, then with a voiceover and live instruments on top it'll either get turned down or EQ'd out in the PA. He also tunes/voices each sound for exactly the job it has to do.

### Right pad — LABS "Arctic Swells," Swells preset
Same plugin, this time the Swells preset — a lot more breathy (a combination of violin and some flute material that was captured).
- Release right up (long trail at the end).
- Sustain way up.
- Decay almost all the way up.
- Variation halfway.
- A LOT more reverb.
- Same gradual attack so it breathes in.
- EQ off a lot of the top end so it sounds grainier and more mid-rangey.

**Special move:** Valhalla Supermassive on this pad, on a PLATE setting, 100% WET mix — "the whole of that sound is happening inside the reverb."

### Why two near-identical pads with different settings — the "orbit" trick
The two pads oscillate and move in different ways. Mental model: two objects orbiting a planet. They start moving the same way (east–west), then one starts moving north–south, so they only occasionally coincide. They orbit the *same musical information* but the points where they line up are few and far between. That's how you create interest and modulation in a static drone — set similar sounds with something fundamentally different in them (different ADSR settings + one running 100% wet through a plate).

### Middle — LABS "Black Hole," PlusBad preset (the bass/dirt)
Very dirty sound.
- Release cranked right up.
- Reverb up.
- Attack up.
Even with release up he wanted more, so he added the Yak delay (Safari Pedals) to get a darker repeat with less top end as it decays. Then Channel EQ to kill the fizzy top end. Again EQing to make space for the other layers.

## Final layer tricks

- **EQ overall:** much less top end across the board; less bottom end in the pads (sub-bass lives in the middle layer only).
- **Delay/reverb tails:** add delay + reverb so each of the three has a *different trail* coming off the end.
- **Keyrange / octave splits (in MainStage layer editor):** assign a different range/octave to each instrument. The sub-bass (Black Hole) only sounds in the lowest octave — play the next G up and nothing happens — because that foggy, dirty sound clouds and gunges up the higher, fluty sounds if allowed up there. The Arctic Swells on the right has its lowest C as its lowest available register. The Arctic Swells Decay on the left plays everywhere across the keyboard, so different things happen in different places — makes the instrument feel "different, not unpredictable."
- **Dynamics as performance:** even just playing three octaves of G, how gently or hard you hit the higher notes gives very different effects, and you can let go at certain times. Result = a really interesting evolving sound.

## Takeaway
This gives a sound bed for an entire scene — "you could do that and just have one instrument play over the top and your cue's done." For the live show it was a fantastically playable, very dynamic six-minute drone that sounded wonderful in a stereo PA, and wasn't painfully boring to play. Things to keep in mind when designing drone instruments: dynamic responsiveness, long attack/release for breathing, aggressive EQ to carve space between layers, keyrange splits to keep dirt out of the highs, and one layer drowned 100% wet in a plate for movement.
