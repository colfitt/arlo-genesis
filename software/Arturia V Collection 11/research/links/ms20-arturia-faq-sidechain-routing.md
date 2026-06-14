https://support.arturia.com/hc/en-us/articles/4807961569436-KORG-MS-20-V-Sidechain
Arturia (official FAQ) · "KORG MS-20 V - Sidechain" · n.d. — ⚠️ page 403s automated fetch (Arturia support blocks bots); content below triangulated from search-engine excerpts of this exact FAQ + the manual.

The official answer to "how do I feed external audio into MS-20 V in a DAW":
- "The KORG MS-20 V can be triggered by an external audio source, and **you must first define this audio source as the sidechain input of your plugin.**"
- "Once the sidechain is properly set, the audio signal is **patchable inside the KORG MS-20 V plugin in the patch panel, from 'Ext Out'.**"
- "**Your DAW needs to support sidechaining on virtual instruments** in order to route an audio signal into the KORG MS-20 V. The process varies depending on the DAW you are using." (Arturia explicitly punts to the DAW manual for per-DAW steps.)
- The ESP then lets you "process external audio … run your own audio through KORG MS-20 V's filters and crunchy output, create wild feedback routing, and use incoming sound to generate envelope follower signals."

⚠️ The phrase "support sidechaining **on virtual instruments**" is the catch — see ms20-sidechain-daw-au-vst3-gotcha.md. Not every host exposes a sidechain input on an *instrument* plugin, and the AU build of MS-20 V specifically has been reported as not showing one in Logic.
