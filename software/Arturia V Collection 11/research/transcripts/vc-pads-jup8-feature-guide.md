https://www.youtube.com/watch?v=tRRPh32RdA8
Digiphex Electronics · Arturia Jupiter 8 V4 - Tutorial, Guide to Every Feature · 2020-12-11

  that's my patch open the light for the new arturia jupiter eight this is version four we're going 
to take a look at this patch and in doing so we're going to look at every feature on the jupiter 8 
v version 4. and i might flip back and forth between a few different patches to explain different 
features and what they're doing on my channel you'll find an analysis of several different artists 
where i go through and show the sense sounds that they used how they put it together and even the 
music theory behind it so be sure and check out my other videos and subscribe so let's just go from 
left to right here starting with the lfo section my patch is using an lfo and you can see it's in 
sync with this light here and so the first button here is your choice between hertz and sync so you 
can have it sync to the tempo of your doll or you can have it run based on the hertz value click on 
it you can see that that's 2.25 hertz and hertz means cycles per second then there's the delay time 
slider and that is after you hit the key how long does it take for the lfo to take effect 7.5 
seconds is the maximum on that and then you have the choice free running or re-trig so will it 
start over every time you press a key or does the lfo ignore you pressing keys then you can choose 
the waveform that your lfo will be all right i've turned the lfo depth up a bit to emphasize it and 
i'll let you hear what it does that's the sine wave saw wave square wave they're calling it noise 
but it's kind of a random wave then we come to the vco modulator section and so that's where you 
can choose the depth of the lfo to the vco so this only affects the oscillator pitch and then you 
can have the envelope affect the pitch you can choose which oscillators because there's two of them 
you can choose which one is affected by your lfo and your envelope or are they both affected then 
the pulse width modulation what they're calling the rectangle wave so it's the pulse wave there and 
you can have the lfo affect that you can manually do it now you can have the envelope do it and the 
extent to which that won't happen and then you have cross modulation let me switch over to my bell 
patch that i did and that's due to cross modulation the cross modulation takes vco2 and effect uses 
it to affect vco1 and makes bell sounds and stuff like quite a var variety of bell sounds you can 
get with that and you have a choice of the range in marked in feet like the conventional organs had 
and you could choose the type of wave the vco1 will be triangle saw rectangle square square being 
thought of as being clarinet sounding saw thought of as kind of a string sound and you can actually 
see why a saw is a string and square wave sounds like a clarinet and the reason it does is because 
the reed inside the clarinet makes an on off oscillation many times a second if you're playing a i 
guess 440 times a second it's flipping back and forth and letting air in in an on off fashion so 
when you duplicate that with electronics it sounds like a clarinet and then the ramp shape of the 
saw wave is like the mechanical operation of a violin or something playing on string because many 
many times per second the bow grabs a hold of the string lifts it up and immediately drops it picks 
it up again very slowly and drops it again so if you're pulling the bow across the string it's 
doing that action 440 times a second electronics it sounds like a string the saw can also be used 
for brass sounds and for that you use the envelope to shape it more the way your mouth would 
operate on the brass to instead of abruptly start the sound you'll start to sound slowly like 
someone pushing air into a brass instrument next button is normal and low for the vco2 range so you 
can use vco2 as an lfo if you put that on low and we're going to cross modulate vco1 let me turn 
this lfo off so this is vco2's sine wave by means of cross modulation here is feeding into vco1 
with a low setting so more of an lfo speed setting and it's modulating the pitch of it typically 
though you would use it for a bell type of sound or cross modulation you have the fine tune for 
vco2 vco1 doesn't have that so you could have two saw waves and detune one for kind of a chorusy 
sound and then you have sync where the sp rectangle wave or this pulse wave of vco2 is being forced 
to reset according to the cycles of vco1 you can see that vco1 is staying steady in its pitch but 
its cycle length is forcing vco2 to reset even when it hasn't finished a cycle and vco2 is falling 
in pitch due to this envelope and because it's falling in pitch it's wave lengths and cycles are 
changing as it is reset by the cycle length of vco1 and it makes a strange sound when it is 
abruptly reset many times a second and then we get to the mixer the source mix you can mix between 
vco1 and 2 or you can have both in my patch my patch open the light uses the noise just a little 
bit though it's primarily made up of the saw wave but it does add noise to it and this is a high 
pass filter and then the low pass filter in resonance and 12 db or 24 db slope of the filter and 
then the modulation where you can choose whether it's envelope one modulating the filter or 
envelope two typically you'll use envelope one you can turn the cut off all the way down then 
because the envelope is opening and closing the filter now you don't have to have it physically 
open like that then you can choose for the lfo to modulate your filter so let me turn this off and 
you'll hear the lfo modulating the filter then there's key follow with key follow all the way up 
the low note sounds dull and as i turn it down all the way down the low note is bright all the way 
up the high note is brighter so you can adjust the balance of brightness between high and low notes 
so that your patch sounds consistent up and down the keyboard then the vca level which is just 
generally the volume level it can be controlled by envelope 2 or lfo for kind of a tremolo effect 
okay now we get to the envelopes envelope 1 was typically used to control the vcf envelope 2 is 
typically used to control the vca or volume so you have one for the tone of it one for the volume 
okay what's this what this is indicating is that envelope one will now modulate the filter we can 
turn the cutoff all the way down initially and use the envelope to shape the filter as we want to 
so we start turning up the decay and we hear some sound now here you could use this for bass sounds 
because you have a quick opening closing of the filter put a little resonance with that and go a 
little lower you see how you could get a bass sound out of that now what's happening is if i were 
to open and close this real fast the cutoff manually that's what's happening over here the envelope 
is doing that for me it's opening and closing real fast every time i hit the key now let's say i 
wanted to open up the cutoff really slowly and then bring it down that's what the attack is for it 
says how slowly it's going to open up so if i put it up here now it'll open slowly and close make 
it even slower now typically with a brass instrument it opens slow and somewhere right in this 
range here would be ideal for brass well the sustain is what volume level will it remain at when 
i'm holding down the key after the decay cycle the release is once i let go of the key that's what 
that's all about how long will it continue to ring out i like to let turn these both up high and 
let the notes smear over one another and we're just using envelope 2 to control the volume if we 
turn these down and then slowly turn the decay up again we get the quick opening and closing of the 
vca this time because it's controlling this so it's equivalent of me manually raising and lowering 
this level raised slowly and i can have it come down to the sustained level while i hold the key 
and i can decide when i let off the key how long is it going to ring out with the release that's 
what the typically what envelope and envelope 2 do then you have your overall volume and your 
overall master tuning you have your unison detune which if it's in over here in the voice assign 
section if it is set to unison which means all the oscillators play on one note you can make a 
super saw type of sound by detuning all of those saws that are playing together back into the poly 
mode pan spread is uh going to send the oscillators to the left or right or center as you play them 
if you're listening to this in stereo then you've got portamento which is glide you have dispersion 
which is a new function if you click this little panel here you can see what's going on the voices 
can be slightly different in pitch like an analog synthesizer would be pulse width can hit a 
different spots envelope cut off and give it a little more analog feel as you play each oscillator 
will vary a little bit there's three different levels of that and a custom level where you can set 
them like you want them then the voices sign solo you'll be playing bass or mono unison where you 
play one note and it has all the oscillators and you can use the detune two different poly modes 
this is for if you have a long release over here in the envelope section if we had used that long 
release where the notes are smearing over one another we can get that with this poly mode but with 
this poly mode the second one it will not allow that to happen because the new notes will cut off 
the old notes then hold is used if you want an arpeggio to turn the arpeggiator on and i'm not 
holding the keys right now i don't have to hold them down because i hit the hold button hit that it 
turns it off and i have to hold the keys down to get my arpeggiation and you have a range that's 
the octave range so that's covering one octave two three four and the pattern of the arpeggio does 
it just go up down only reverse random and does the arpeggiator go according to hertz so certain 
number of cycles a second or is it synced to the tempo of your daw and you have your bender 
functions here for your mod and wheel and bender and down here at the bottom you see various things 
where you have undo show the history of undo and redo and this is something new compared to version 
three is that now we have macro knobs here at the bottom so to access those you hit this settings 
button well you see the the general settings the midi macro pertains to these four dials down here 
and you can set it up custom right now brightness handles vcf cutoff timber is doing the resonance 
time is doing four different envelope functions movement deals with these lfos but this is custom 
you could go down here to add destination and make those customized then there are some tutorials 
in there now for the advanced functions so down here i had talked about this new function 
dispersion where you can have the pitch of various oscillators be a little bit out of tune compared 
to the others and typically what i would do is come up here to the modulation choose sample and 
hold and with these settings here that i'm exaggerating it here this is the depth over here on the 
right so let me exaggerate it just to show you what it does so every time i play the same note it 
sounds different and so i would prefer to use something like that that varies as opposed to 
something down like down here with the voice dispersion which is going to be static and then 
there's a second lfo or actually the third for the entire synthesizer here you have one right here 
and then you have these two then you have a modulation mixer where you can actually mix the two 
lfos you can choose to sum them and other math functions of the two together and then choose that 
destination of where that goes to it has a sequencer and it has a keyboard functions that can be 
sent to various destinations so those are the destinations possible for the velocity to control so 
the harder you play you could have a reverb function change or any of your you know delay function 
changes you could have no delay and then when you hit the key hard you get a delay that type of 
thing but you can also control typical things that you would use velocity control like filter 
settings things like that after touch can control things mod wheel can control keyboard tracking 
then you have your effects so you can have a parametric eq if you double click these settings they 
will return to their defaults so obviously the in the song open the light the keyboard sound pans 
all over the place and so there is stereo panning here as one of the effects and overdrive and here 
are the various ones that are available for these you can choose to run these in a series so that 
one effect runs into the next and you can also have them run independently and that is all the 
functions on the new jupiter 8. now i will mention that they've taken away the the most important 
thing about the jupiter 8v and in version 3 it had split and layer so you could layer up sounds 
together you could have the bass on the left hand and have the strings on the right hand and for 
whatever reason they took that function away and that's that's the most important function to me on 
this synth and i have hundreds of patches for version three that are not compatible with this new 
version and so i can't use any of those patches and i can't do many of them are intended to use as 
splits and layers and so i can't use any of those so i won't be using this synth but i guess for 
the future this will show you how to use this synth and everything here pretty much applies to 
version three if you have that as well just pointing that out glad you could join me for this see 
you in the next video 