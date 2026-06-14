https://www.youtube.com/watch?v=po-xMQSA3c4
Rishabh Rajan · Massive X Tutorials: Lush Pads (Advanced) · 2019-06-28 · 7:40

The single most useful copyable evolving-pad recipe in the captured set. Builds a "lush evolving pad" from the init patch using two wavetables, noise, a filter modulated by THREE simultaneous modulators (LFO + mod-envelope + Performer), a third oscillator added via the insert-effect slot, and reverb→chorus. Cleaned from auto-subs.

---

Starting with the Init Massive X preset (found under the QuickStart category) — a basic sawtooth. The sawtooth is the basis of the pad sound, so keep it as is. Bring in the second wavetable and set that also to a sawtooth (on the right). It sounds a bit boring, so add detune: right-click the first and transpose it down a bit, right-click the second and transpose it up a bit. That's already sounding richer.

Jump to the amp envelope and tweak the ADSR: attack at about the halfway mark, release at about the halfway mark, sustain down a little.

Now bring in some noise as well — use the white noise. The noise sounds significant and seems to overpower the two oscillators, so bring in a filter — the blue Monarch filter. Play the filter frequency down. Use an LFO to modulate it: click-and-drag to set a very subtle amount, use a sine wave shape and a very slow-moving LFO.

Also use the modulation envelope to modulate the same frequency down, very similar to the amp envelope: long attack, long decay, long release (probably extra-long release), sustain at about the halfway mark. Make sure the LFO has a slightly wider range compared to the envelope.

Bring in more movement with the Performer: drop the Performer on that third modulator slot, so now THREE different modulators affect the same parameter (the filter frequency). Pick a shape and draw a random pattern; set the Performer's range/length to just two bars. Very subtle movement there.

Bring in a THIRD oscillator over in the insert effects — Massive X lets you add an oscillator there. Route it in the Routing tab: right now the oscillators and the noise are going into this oscillator, which is unwanted, so double-click to disconnect that, disconnect the other connection, and route everything to the [output bus]. Set this added oscillator to a bell shape and tune it up an octave. Modulate the pitch of this pulse oscillator with a V LFO / V modulator set to a range of 12 semitones, modulator shape = square wave, significantly fast modulation rate. Bring its mix down so it's not too loud. Also gradually change the pulse width — use L4 (another LFO) with a nice wide range. Set the sustain on that modulation envelope a bit higher so the sound stays brighter.

Next, probably the most important element: the reverb. Use the Wunderlust algorithm. Add a chorus right after — adding chorus after the reverb is preferred. Up the noise a bit more and pitch it up a bit higher.

The dull moments come from the LFO bringing the cutoff down too far, so change that LFO to unipolar so it doesn't go any lower than its set position.

Final touch: add voice randomization on the pitch for the first wavetable and the second wavetable, and add it to the resonance as well. Now every time you play a new note, those three parameters are slightly different.

That's how to create a complex evolving pad sound in Massive X.
