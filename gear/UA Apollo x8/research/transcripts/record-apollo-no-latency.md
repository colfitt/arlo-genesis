https://www.youtube.com/watch?v=5WLX7fwCqK4
Ricardo Tolbert · HOW TO RECORD WITH UAD APOLLO WITH NO LATENCY (THE RIGHT WAY) · 2020-08-28

(Auto-captions, cleaned to prose.)

This shows how to get no latency with a high buffer size — useful if you have a slow computer, and it keeps your computer from crashing as often while recording. This is the proper way to use the UAD interfaces: it's what they were intended for.

First, make sure you have signal coming through the Console app and through your DAW. Use the main output the Apollo comes with — outputs 1 and 2, i.e. monitor left/right.

Set your playback engine (buffer size) to 1024. Rule of thumb: 1024 is the highest most Macs go (some Windows machines go to 2048). Normally you use a high buffer for MIXING because it frees up more CPU for plugins. When recording you'd normally go as LOW as possible (64/128 samples) for low latency — but a low buffer risks crackling, clicks, and crashes on a slower machine.

The trick: with the high buffer (1024), the DAW monitor path is "super late" — about 1000 samples of latency, clearly audible doubling. To fix that without lowering the buffer, turn ON Low Latency Monitoring in the DAW. Now you're monitoring through the UAD Console app (the direct hardware signal straight to your headphones) and NOT through the DAW at the same time. If you monitored through the DAW you'd hear that high-buffer latency, because you'd be hearing the DAW's processed return instead of the Apollo's direct signal.

So the combination is: record at a high buffer (so the computer doesn't crash) AND keep latency-free monitoring (via Console / low-latency monitoring). Critically — do NOT monitor through both the Console app AND the DAW at once, or you'll hear the direct signal plus the delayed DAW signal doubled. Make sure the record track's output is set to monitor left/right, playback engine at the highest setting, and low-latency monitoring checked.

Important caveat on plugins: Low-latency monitoring bypasses the plugins on the armed record track (so any plugin on the track you're recording to won't be heard while monitoring). Plugins elsewhere in the template that you're NOT recording to won't be bypassed. So if you want the performer to hear effects (compressor, EQ) while tracking, put them in the Console app inserts, not on the DAW track. For reverb/delay while monitoring, set up a send to a Console aux (auxiliary 1, etc.) just like you would in the DAW, and now the performer has reverb in their cue.

Bottom line: this is the smartest way to work, especially on a slower machine or recording on your own system — use the UAD/Console direct monitoring, record at a high buffer, and you won't get crashes, clicks, or the client/you hearing doubled latency. A lot of people complain about the UA platform when it's just user error in the I/O routing.
