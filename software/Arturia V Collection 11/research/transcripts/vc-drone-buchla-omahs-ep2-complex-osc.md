https://www.youtube.com/watch?v=d9ov8xwOYdQ
One Man And His Songs · Arturia Buchla Easel V Tutorial Ep#2 - The Complex Oscillator · 2021-01-16

hello welcome to the arturia bucula easel tutorial series it's a bit of a mouthful that one today 
we're dealing with the complex oscillator this is the heart of the synthesizer it's the most 
important sound making source the synth has now what i've done is cleared the synthesizer down as 
much as i possibly can so it's completely empty in fact if i press a key on the keyboard now the 
keyboard isn't even attached to the synthesizer it's completely bare for the purposes of today 
we're only going to worry about the complex oscillator but in order to hear it i need to turn some 
volume up so i'm going to move this slider and we're not going to worry about what the dual 
low-pass gate is we'll deal with it in a different video but for today just treat it like a volume 
control this is the oscillator in action it's generating tone all the time it's just a question of 
whether or not we activate a sound source to be able to hear it and you can see that by default 
it's kind of a sine wave triangle kind of hybrid thing it's not really anything it certainly isn't 
the sine wave that's its harmonic distribution you know it's quite quite complex it's obviously not 
a very interesting sound we want to add additional harmonic content to it to make it more 
interesting how can we do that well there are two fundamental processes that we can use we can 
apply wave mixing by bringing a second brand new wave into the equation and we have a tombow 
control oh down here we'll deal with each of those separately first things first wave mixing let's 
get our sound up and running again and now i'm going to introduce a second wave and the shape of 
the wave that's going to be introduced is determined by this timbre switch currently set to 
triangle it'll get louder as i turn this dial up so i'll just turn it down a little bit there's the 
triangle and then as we pull back again we go back to our original sound the top setting is called 
an impulse train let's see what that looks like this is the most complex of the waves so this 
impulse chain is being mixed with our original wave and we get the composite wave and finally we 
have a square wave which when added to our original wave ends up not looking very much like a 
square wave at all and there we have it so an awful lot of flexibility just from that knob and the 
three different switches on offer to us in addition to all of that we have a timber slider and what 
this introduces is a concept called wave folding wave folding is a really interesting form of 
synthesis it's basically like an additive form of synthesis rather than subtract it where you use 
filters to pull things away with wave folding we basically introduce new harmonics into the sound 
and the way we do it is you set an arbitrary ceiling a control voltage ceiling beyond which the 
signal's not allowed to go if it would go through the ceiling instead of doing so it folds back on 
itself and basically makes an increasingly complex wave that in turn is additional harmonics and we 
hear that as interesting tone let's see it in action there's our simple wave now as i start to 
increase this slider just make it a little bit louder you'll see the wave temporarily get loud and 
then begin to fold on itself so i'll just pause that momentarily so this is as if i'd carried on 
making the wave bigger and bigger louder and louder introducing additional harmonic content but 
when it gets to the stage where it reaches the ceiling it basically kind of buckles on itself and 
folds back in if we get this back up and running again and carry on increasing the timbre you can 
see the wave gets folded more and more and more ever increasingly complex more and more little 
wiggles in the wave across that entire spectrum we can also apply the second wave at different tom 
at different wave shapes so there's an awful lot of tonal complexity to be had with those two 
combinations of the dual wave philosophy with the wave folding applied to the composite wave so 
that's our that's the basis of our sound that's why the buccal easel is capable of making such rich 
and interesting tones because right at its heart it's got this interesting unusual form of 
synthesis let's have a look at some of the other features of the oscillator what is this tone that 
we're hearing well it's a c why is it a c because i pressed a c on the keyboard if i press a g it's 
going to start playing a g and it will carry on doing so until it receives a new instruction here's 
an a and so on and so on where's that coming from well the reason why we're hearing chromatic tones 
is because the oscillator is currently in keyboard mode which means that every key on the keyboard 
is being translated into a control voltage that control voltage is being fed into the oscillator 
the oscillator is interpreting that instruction that size of voltage as an instruction to generate 
a signal of a particular frequency we can decouple the keyboard from the oscillator and now when we 
turn the volume slider up we're going to get a very different sound and it now doesn't matter what 
key i play on my keyboard all the way down they're all going to generate the same tone that just 
happens to be the lowest key i hit on the keyboard there's a c again so this enables us to use it 
really easily as a keyboard put it in keyboard mode and we're going to get something that's pretty 
familiar to us but of course an oscillator is just a sound generation module and so we can decouple 
it from the keyboard completely and take manual control of the frequency i bring the sound back in 
again so the last note i played was a c but now i can start varying the pitch manually using the 
pitch slider you can see it starts out it says c0 now as i turn this move this pitch slider up can 
you hear that it's stepping up in semitones if i kind of let it come to rest at any given time the 
tuner is always going to tell us that it's playing a note of a particular pitch that's because of 
the quantized switch quantize basically means that when i increase the pitch manually using the 
pitch slider do so in chromatic jumps if i turn quantizing off and do the same thing with the pitch 
slider now we're going to get a completely smooth increase and decrease we have a fine tune knob 
which gives us pretty much what it says on the label i just uh moved that knob with a left click 
and drag if i right click with my mouse i can move it up in tiny increments this is true for all 
controls on arturia products left click and if i double click it resets it back to the default 
position whatever that may be now there are a few controls in the complex oscillator i've not dealt 
with yet we've got these two with the arrows pointing into them and we've got the polarity switch 
we need a modulation source in order to be able to talk about those three things and in the next 
video we'll introduce the envelope generator which is guess what the modulation source hope to see 
you then thanks very much for watching see you next time you 