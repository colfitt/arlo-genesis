https://www.youtube.com/watch?v=cxJh3Pk1RlU
CatSynth TV · Arturia Matrix 12 V: Demo & Tutorial · 2021-03-11

 hey everybody catsynth tv and today we are looking at the matrix 12v from arturia it is a 
recreation of the legendary oberheim matrix 12 as a software instrument we're going to demo all of 
its features along with some of the factory presets but before we begin please do subscribe to this 
channel for more synthesizer content coming out regularly and please do consider supporting our 
demos via patreon or kofi link's in the description below following on the success of the ob series 
oberheim released the expander in 1984. it was a powerful polyphonic analog synthesizer with an 
extremely flexible voice architecture it had two oscillators per voice a vcf with 15 different 
modes and a digitally controlled matrix system for mapping its myriad control sources to almost any 
other point in the signal path the matrix 12 introduced a year later was bigger and fatter with a 
keyboard 12 voice polyphony and more programming options both the matrix 12 and expander were 
prized by artists at the time and still command high prices today the matrix 12v recreates the 
architecture and sound of the original along with an interface inspired by the oberheim matrix 
series including the green led displays there are two oscillators a frequency modulation section 
the vcf several different kinds of modulation including envelopes trackers lfos ramps and more and 
of course the modulation matrix at the heart of the instrument we will go over each of these 
elements in more detail starting with the oscillators each oscillator has three waveforms sawtooth 
triangle and a pulse with width control we can stack all three waveforms together each oscillator 
also has its own volume control independent volume controls for each element is a theme throughout 
the matrix 12v let's bring in vco2 we can use the detune and a different pulse width to get an even 
fatter sound vco2 has an additional noise source there is also a hard sync function it works best 
with a single sawtooth or pulse waveform on vco2 okay let's turn off the sync and vco2 and jump 
right into the modulation any parameter with one of these buttons can be a modulation destination 
we'll click on vco1 pulse width it appears as the destination in the modulation page we can assign 
up to six sources let's add lfo1 if we go to the lfo section we can adjust the parameters including 
speed and waveform let's leave it on triangle for now and dial in the speed to get a good pulse 
width modulation effect as mentioned earlier every element has its own vca or volume control 
including each lfo moreover the vcas themselves can be modulation destinations let's bring up the 
vca for lfo1 in the modulation panel we're going to attach one of these ramps as a source a ramp is 
just a simple function that increases and stops at a maximum value a bit like having just the 
attack stage of an envelope by adding a ramp to the lfo the pulse width modulation comes in 
gradually let's add the sawtooth back in and open up vco1 frequency for modulation we'll add lfo2 
we can hear how the different waveforms affect the sound boom the most interesting is the sample 
option which uses period samples from any other modulation source let's use lfo3 if we set lfo3's 
waveform to randomer noise it's like a traditional sample in hole but we can also use different 
waveforms and frequencies to get different patterns now let's switch the source to envelope 3. 
these are classic adsr envelopes which also have delay parameters once again they each have their 
own vca this is a good opportunity to introduce the quantize option for modulation paths if you 
toggle a little q icon after the amount for the modulation source the values will be quantized 
we'll turn it on for this envelope source and we hear how we get a staircase effect envelopes work 
really well for modulating sync so let's remove envelope from vco1 and assign it to vco2 with sync 
on let's now introduce the track modulators these are functions that you can use to map and warp 
the values of other modulations let's take track 2 and use envelope 3 as its source and assign 
track 2 to vco2 frequency we can tweak the values of different track points to make each segment of 
the envelope non-linear so let's now turn our attention to the filter section as mentioned earlier 
the vcf has 15 modes including various low pass high pass band pass and some more exotic 
configurations for notch and phasing effects that were not found in most analog subtractive 
synthesizers of the time let's listen to each of them and how the frequency and resonance controls 
affect them wow  this three-phase filter is particularly unique though it portends emulator z-plane 
filters of course the filters can be modulated too if we click on the frequency parameter we see 
that it is modulated by envelope 1 which provides a contour to the sound we can use our lfo2 in 
sample mode as a second modulator and add lfo5 with a slow triangle sweep for even more variety 
that's pretty cool the filter section also includes two vcas you can use these to set overall level 
or for amplitude modulation in general i find it best to use vca2 for the overall amplitude 
envelope and reserve bca1 for amplitude we can set lfo4 to modulate vca1 ok let's turn off the lfos 
and look at the fm section this is a linear fm more like yamaha's fm instruments than the 
exponential fm found in the sequential profit 5 or roland jupiter 8. it can be set to modulate vco1 
or the vcf but not both let's try it with vco1 okay now with the vcf like other sections the fm has 
its own amplitude control that can be modulated let's use ramp 2. okay let's turn off fm and turn 
back on some of our filter modulations we now turn our attention to the advanced panels which can 
be accessed via these buttons above the keyboard we start with the effects panel there are two 
effects slots and a variety of common effects available for each let's put a flanger in slot 1. and 
an analog delay in slot 2. the mod panel provides a single view of all the modulation routes at 
once there are slots for up to 40 modulation routes arranged on two sub-panels on the first panel 
you can see the various modulation sources and destinations we have already programmed we can also 
add additional routes here with access to all the sources and destinations at once for example i 
can route from the mod wheel called lever 1 in the matrix 12 to filter resonance oh look there's 
that pesky vibrato that's always the default for the mod wheel why is that always the default for 
the mod wheel let's jump over to the page 2 panel to deal with that here we see some advanced 
parameters available for each of the elements in the voice the frequencies of vcos 1 and 2 and the 
vcf can be controlled from several sources including keyboard the lag modulator we'll come back to 
that one pitch bend or vibrato let's turn vibrato off as mentioned the frequency of vco1 and vco2 
can also be controlled by the lag modulator it basically slows down incoming values from its 
assigned source by default it is assigned to the keyboard and can be used as a portamento let's 
turn off the keyboard and turn on the lag for the vcos by increasing the rate of the lag parameter 
we get a slower portamento okay enough of that there are also some advanced parameters for the 
envelopes lfos and ramps that control their triggering behavior for example we can have ramp 2 
re-triggered by lfo1 let's turn the ramp modulation back up and set vco2 back to sync finally let's 
look at the voices page here we find the vibrato control essentially it's an extra global lfo with 
all of the waveforms except sample this page also lets us control the behavior of the 12 voices by 
default we rotate through all of them as we play notes on the keyboard we can set slight detunes to 
each of them which adds some variety we can also place them in different locations on the stereo 
field which you should be able to hear on headphones or speakers with good stereo separation we can 
also assign voices to different zones right now they are all assigned to zone one instead of 
rotating between voices we can stack them all on the same key using one of the unison modes we can 
also set up multiple zones either in different parts of the keyboard or stacked on top of one 
another let's assign voices 7 through 12 to zone 2 and set both zones to rotate we see the voices 
for both zones triggered for each key press we can also set each zone to be unison by transposing 
the voices in zone two we can get some really fat intervals as you can see this is quite a flexible 
and powerful instrument it can be a little daunting at first but once you get the hang of it you 
can get quite a variety of sounds for the remainder of this video we'll look at some of the factory 
presets um yes oh really do ah we hope you have enjoyed this detailed look at the matrix 12v to 
find out more please visit arturia.com and check out the description below this video thanks for 
watching check out more at www dot and please subscribe to cat synth tv spin a capita 