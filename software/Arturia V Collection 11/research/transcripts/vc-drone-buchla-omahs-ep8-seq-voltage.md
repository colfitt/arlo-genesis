https://www.youtube.com/watch?v=lsj28DfvgAw
One Man And His Songs · Arturia Buchla Easel V Tutorial Ep#8 - The Sequential Voltage Source · 2021-01-25

hello welcome back to the buckle easel tutorial series today we're talking about the sequential 
voltage source i'm going to call it the sequence for the rest of the video because i think that's a 
bit overly fancy the point that they're making or the point that don buchler was making when he 
named this module is that it's more just it's more than just a fancy way of making different tones 
it's used as a voltage a control voltage generator and those control voltages can do much more than 
simply generating fancy notes in an arpeggio first things first let's just hear it plug the 
sequential voltage source one of the sequencer outputs into the pitch of the oscillator that we're 
currently hearing give it some modulation amount and start messing with our sliders we've got five 
distinct tones notes being played by the oscillator the pitch of those notes is being modulated by 
the sequencer so the sequencer isn't making sound itself it's not making those notes it's sending 
control voltages into the oscillator and modulating the oscillator's pitch it's really important to 
bear in mind to remember what the sequence is doing it's not a tone generator it's a modulation 
source i don't want that happening all the time in runaway train mode i want to impose some kind of 
control over it and the easiest way to do that is with an envelope so let's get an envelope 
involved in the equation so my envelope generator is set to sequencer if i turn the envelope 
generator to something else now i've got some kind of weird kind of hybrid thing shouldn't have 
done that let's get back to sequencer mode the envelope generator is taking a trigger off the 
sequencer the sequencer is taking its timing from the easel's clock so we set the speed of the 
sequencer down here and the relative level of the control voltage outputs on our five sliders and 
now that we have an envelope we have much more control a little bit of decay on the set on the 
tones it's nice okay great stuff so we're up and running with the basic sequencer in the classic 
mode modulating the pitch of the oscillator let's change that to modulate tomb instead steve 
hillage will be proud of me now let's do both at the same time let's trigger both oscillators 
simultaneously yet another output i'll come out of here as well because we can have three 
connections why not come in here get the envelope firing both gates and i saw this example in the 
in the user manual so it's pretty cool i'll show you send modulation oscillator through the 
inverter instead and now we've got basically inverted controls when oscillator 1 is playing high 
modulation oscillators playing low so it's actually quite an impressive job that the sequence is 
doing at the moment it's doing two quite distinct things the first thing is firing the envelope 
generator that's we have a semi-modular synth here you know this stuff is wired in the background 
invisible to us when we click the sequencer switch we send the sequential voltage source triggers 
these five blue lights that are coming on or triggers firing the envelope generator so that's one 
thing the envelope generator is in turn opening the two gates but it's also directing its control 
voltage outputs via its blue output socket into multiple different destinations and this is the 
point that i'm trying to make you can send these signals wherever you want just so happens we're 
sending to two pitch based oscillator modulations and one tone based modulator oscillator 
modulation so that's all very exciting now those five independent triggers that we're hearing we 
can turn each one of those on or off with our toggle switches now an important point to note about 
these switches they control the firing of the sequences that the sequences triggers they don't 
attenuate the control voltage coming out of the output these control voltages are still being 
output from the the sequences output sockets at each stage of these blue lights these blue lights 
are not kind of disappearing on steps three and four it's just that steps three and four aren't 
generating triggers anymore and we can prove that very easily by taking it back out of envelope 
mode don't need them anymore um and we'll we'll just ignore modulation oscillator 2 that was a bit 
fancy we're just going back to a nice simple example when i give the complex oscillator direct 
access to the outside world again and we're not firing off an envelope you'll hear all the distinct 
tones so these control voltages are still coming out of this output we're just not using the 
triggers now at the moment as things stand with it being like basically hardwired directly into the 
output the sequencer isn't triggering isn't having any effect anymore the fact that the envelope 
generator is firing these um triggers is irrelevant because the envelope generator isn't attached 
to anything so two completely distinct features of operation don't get carried away thinking these 
switches silence this part of the circuit they don't they only stop it from triggering whatever it 
happens to be connected to at the moment it's connected to the envelope generator okay instead of 
taking our timing from the clock let's switch to keyboard mode and now the blue light is stuck 
every time i press a key on the keyboard we're going to step forward by one step so i'm pressing 
the same key as you can see on the interface and every time i press the key i'm triggering the 
sequencer which is then generating the new control voltage output which is having the effect on the 
pitch and tone in the complex oscillator if i press a different key on the keyboard i'm now 
generating a new set of five tones so the keyboard input is a control voltage in its own right and 
that is having modulation effect on the sequencer itself we can decouple that dual nature of the 
keyboard instruction from the oscillator by turning keyboard mode off and now it wouldn't matter 
which key on the keyboard i play we're going to get the complex oscillator's base tone modulated by 
whatever control voltage settings are set on the sequencer so there's the low rumbling whatever it 
is b flat of the natural oscillator well it's actually a b flat modulated by whatever this gate is 
currently set to so i'll just start hitting a random key on the keyboard a new random key on the 
keyboard doesn't matter now the keyboard is acting purely as a delivery mechanism for the trigger 
and it's having no tonal impact on the sound because we've disengaged that feature from the complex 
oscillator so all of these different modules interacting you have to be aware of all of the 
features of each of them at each time obviously in this video series we've dealt with one module at 
a time and kind of get that plate spinning but when we then use that module in conjunction with 
another you have to remember all of the features of that oscillator where's that tone coming from 
you may think well the complex oscillator has a keyboard setting that determines that different 
keys that you play on the keyboard generate different control voltage outputs from that module 
let's have a look how we can interact with the pulsar so now here we are in uh free mode so the 
pulsar is basically in control of its own destiny and then everything that we've learned about the 
pulsar now applies so because we've switched to sync this is now quantized and is all based on the 
host tempo switch to clock mode this then becomes the means by which we control the sequencer now 
i've loaded a new patch up to talk about the um particular quirk of the way that the keyboard 
pulsar uh trigger fires into the sequence so what i've done here is i've got a really really simple 
patch the sequence is just plugged into the oscillator's pitch and not doing anything else so we've 
got this kind of static tone and i'm going to press a key on the keyboard she's going to fire the 
pulsar the pulsar is going to trigger the sequencer and we'll hear these five different tones 
straightforward enough now it turns out that if the pulse's gate is still open when you send the 
next keyboard instruction in uh the sequencer doesn't step on so if i mash this keyboard fast 
enough the sequential voltage source will stick on gate one if i slow down and allow the pulsar to 
finish its envelope steps on perfectly happily if i increase the period of the pulsar which means 
the gate is open for longer on each note then the effect happens at even slower keyboard rates so 
now i'm able to play the keyboard consistently quickly you can see and here how often i'm pressing 
the key and the sequence and never steps on because the pulsar gate is never fully closing and once 
it does fully close then the sequencer steps on so just be aware that that's how it's wired that 
the gate needs to be fully closed before it will accept the next trigger see uh trigger instruction 
i can only generate that effect in keyboard mode all of the others seem to be absolutely fine so 
there you go it's just one of those things beware of it i've come across it in um in presets where 
there are sequences set up we'll deal with this stuff later it's in the advanced pages where if if 
it's generating the sequence and playing lots of notes then the pulsar can't effectively fire and 
the sequencer because the gate is basically open all the time finally we have this stages toggle 
switch set to three four or five set yourself up a nice simple little envelope based um sequence 
here and you can hear it's playing all five steps i switch to three it will just cycle around the 
first three so this is how you permanently disengage one or two of the of the steps of the 
sequencer and now it's just going to play those four notes because we're in pulsar mode here i 
increase the rate of the pulsar to make it play faster that's the sequential voltage source covered 
hope you enjoyed the video found it useful if you did please consider subscribing hit notifications 
you'll make sure not to miss the next episode hope to see you then thanks a lot you 