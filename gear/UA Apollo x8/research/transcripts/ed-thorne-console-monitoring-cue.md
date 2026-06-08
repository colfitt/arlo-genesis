https://www.youtube.com/watch?v=0DZM9y6tmBQ
Ed Thorne | Mixing & Mastering · How To Set Up Monitoring, Virtual Channels, Inserts, and Cue Mixes in Universal Audio's Console! · 2020-11-09

(Auto-captions, cleaned to prose. Demoed in Console with Logic, but the process applies to other DAWs.)

Console is a highly functional digital mixer for routing your input and headphone monitoring. Before a basic setup, establish whether you're monitoring a MIX or a CUE MIX.

The easy way (basic): Assuming your DAW master bus output is set to channels 1 and 2, the Apollo feeds that through your monitor output by default, and also to your headphones if you have MIX selected in the Cue Outputs menu. You can monitor your inputs too if you have the channel open, gain up, and the channel fader up. Balancing the DAW output and the live input signal this way is the most basic way to record and monitor in Console.

The better way (cue mix): For maximum flexibility, set up a Cue Mix. A Cue Mix is UA's name for a monitor send — much like an aux/bus send in a live scenario. (There are also Aux sends, which are the traditional auxiliary processing send channels.) To set one up:

1. Go to Settings → I/O Matrix and create two virtual channels in the OUTPUTS column. These new channels appear in Console.
2. Link them as a stereo pair (click the left channel, link), and rename the pair to something like "DAW Output."
3. In your DAW, assign your main left/right outputs to that new virtual channel.
4. Back in Console, assign your headphone mixes: go to Cue Outputs and swap the source from MIX to CUE 1, CUE 2 (a maximum of four cues if you have two or more Apollo devices). Assign where each cue mix is going — to whichever headphone output you need.

All connected Apollo devices appear in Cue Outputs. A Solo shows a single headphone output; a Twin gives the additional option of line outs 3 and 4 (so you can send the mix to a headphone amp or speakers in another room). Plug into the corresponding headphone output, then balance/mix your monitor levels by adjusting the send levels on the channels you want to hear.

Monitoring with effects: To monitor with reverb or delay, assign these into an Aux insert. To send reverb to a vocal on input 1, send the desired amount to Aux 1 in input 1's send section; then to hear it in your monitor cue, go to the Aux 1 channel's sends and raise the fader going to Cue 1 (or whichever cue your performer is on). If one performer wants reverb and another wants delay, set up Aux 2 with delay, send that input to the delay aux, and on the aux strips route reverb to one performer's cue and delay to the other's.

Routing the click: You can send your DAW's click track to a separate virtual channel for per-musician control. Go back into Settings, set up two more virtual channels, stereo-link and label them "Click." In the DAW mixer, find the click channel and assign its output to those virtual channels (3 and 4). Back in Console you'll see the click channel and your DAW output next to it. To assign the click into your cue mixes, click the Sends box on the click channel and assign as needed.
