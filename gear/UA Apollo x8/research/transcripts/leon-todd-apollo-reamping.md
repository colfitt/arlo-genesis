https://www.youtube.com/watch?v=LM_KV4tQqpU
Leon Todd · AX8 & UAD Apollo Reamping · 2018-08-14

(Auto-captions, cleaned to prose. Note: this clip reamps using a Fractal AX8's own outputs into the Apollo's front instrument input — it does NOT use a dedicated Radial reamp box. It's included because it demonstrates the core Apollo-side reamp routing logic — print a dry DI, then feed it back out a line output and into the front of a rig — which is identical in principle to the X-Amp loop, minus the dedicated reamp box that handles level/impedance.)

This is something I've been asked about a few times — how to use a Fractal AX8 and the Universal Audio Apollo Twin to reamp guitars. The nice thing about the Apollo Twin is it has a high-impedance guitar (instrument) input, which basically means you can cut a clean DI and send that straight back out to the front input of your amp/modeler without the need for a reamp box. (For this rig: the X-Amp does that level/impedance conversion job when you're reamping into real pedals/amps instead of a modeler with its own front input.) I'll go over all the ins and outs and the Pro Tools settings — it'll vary between DAWs, but I'm a Pro Tools user.

Recording the dry DI: To record the dry track at the same time as the wet, go into the AX8's global menu → In/Out, and scroll across to the audio section. By default you're using the two main outputs to record in stereo. The important thing is to set output 2 to mirror NOT output 1 but INPUT 1 — this echoes input 1, meaning output 2 carries the clean DI of whatever you're playing. Take output 2 from the AX8 and send it to a DI track in your DAW. That's the track you'll reamp later.

Connections: The main guitar track is input 1, instrument — plug your guitar in there. You'll have a preset loaded in the AX8, and you want its main output (output 1) to go into mic/line 2 of the Apollo Twin. Output 2 is mirroring input 1 (the clean DI) and that goes into the instrument input of the Apollo. So you've created two signals: output 1 = the AX8 preset with amp/cab sims; output 2 = the dry DI mirror.

Recording: Set lines 3 and 4 as a bus send in the bus menu. Then in assignments set DI to input 1, reamp to input 2, and the AX8 input also to input 2. In the DAW, set the DI track output to lines 3 and 4. The nice thing about the UAD is you can monitor on the input. Arm the DI track and the normal recording track, mute both record tracks, and record a quick DI take. You now have a dry DI recorded.

Reamping: Change your I/O. Physically move the guitar cable so you're now hitting the front of the AX8 (you can switch to a different patch — e.g. a Recto patch). The DI track is set to output to line 3/4 on the back of the Apollo, which feeds the front of the AX8. Now play back the dry DI track and you hear the reamped signal coming back through the new amp. You can mute the DI, A/B the original wet track against the reamped track, and you've successfully reamped.

It's not quite as easy as with the Axe-FX II or III (which have dedicated reamp outputs), but it does the job.
