https://www.youtube.com/watch?v=e02KQkN4ZuY
One Man And His Songs · Arturia Buchla Easel V Tutorial Ep#4 - The Modulation Oscillator · 2021-01-18

hello welcome back to the buckle easel tutorial series today we're dealing with the modulation 
oscillator which is the second sound source in the buckle easel and it does a lot of different 
things we've got quite a lot to talk about today the first thing that we need to discuss is i 
reluctantly have to talk a little bit more about how we get sound to the outside world i'm trying 
to deal with it component by component but sometimes we've got no choice other than to just bring a 
few more bits and pieces in everything that we've dealt with up until now with the complex 
oscillator has been on gate one output one i'm going to turn that off for the moment and we're 
going to switch over to channel b instead channel b is connected to gate number two in this module 
that i'm historically refusing to talk about modulation oscillator is hardwired to gate 2 in 
exactly the same way that the complex oscillator is hardwired to gate 1. so now if i turn level 2 
up with channel b at a non-zero volume we hear a different sound what you're hearing now is the 
modulation oscillator at the moment you're hearing the square wave but you could be hearing a 
triangle or you could be hearing a sawtooth just turn this volume off it's a 9. that's the first 
thing that we need to understand about the modulation oscillator it's a it's an oscillator in just 
the same way that the complex oscillator is it's capable of generating audio tone and we have three 
different wave shapes to choose from they're not the same as the three wave shapes in the tambour 
control over here they do have different characteristics these oscillators now the basic keyboard 
oriented functionality of the two oscillators is the same so if i take an envelope output and plug 
it into gate 2 instead we're now hearing the modulation oscillator being triggered by the envelope 
in exactly the same way that we did for oscillator one let's get back to our static wave one thing 
that i'll mention really quickly because i regretted not talking about it in the last video is the 
purpose of the fine tune knob if you're in quantized mode and you're stepping up in semitone 
offsets it's the fine-tuned knob that gives you the ability to reach the values in between those 
two offsets i didn't mention that when we were talking about the complex oscillator and just 
thought i'd throw it in okay so got an oscillator capable of generating three three different waves 
and by default it's hardwired to gate b great stuff well we can vary its frequency just in the same 
way that we can with the complex oscillator it's a little bit weird see on the modulation 
oscillator the slider is called frequency and over here it's called pitch but fundamentally got the 
same functionality take it out of quantized mode smooth curve so why are these two sliders being 
called different things well because with the complex oscillator it's always and only pitch that 
that is controlled with this slider the modulation oscillator is also capable of acting as a low 
frequency oscillator if we click this high low switch here to low now the frequency range of the 
oscillator is from almost nothing up to 50 odd hertz but depends on what key you're pressing on the 
keyboard and all the various factors but if i turn the level up i'm just getting that kind of 
pulsing click thing going on and eventually it's going to become audible as a very low bass sound 
where i'm zoomed out as far as i possibly can now the lfo it whilst it's kind of cool to make 
sounds as low as that that's not really its purpose in lfo mode it's designed to be used as a 
modulator somewhere else and this is where things can potentially get a little bit tricky to track 
because we're back into the territory of having to understand internal wiring there are hardwired 
connections between these two oscillators you see this switch up here at the moment it's toggled to 
i think it stands for balance external i'm not going to talk about the external mode for reasons 
we'll come into much later on it's a little bit complicated but basically that's just the 
oscillator acting as an oscillator if i flick the switch to am oscillator it's now hardwired into 
the complex oscillator it's basically going to act as an am modulator on the complex oscillator 
it's a bit of a tricky sentence so let's just kind of slow down and try and figure some stuff out 
let's start off with a really simple default position of our good old oscillator the complex 
oscillator generating a nice simple basic tone now i'm going to start increasing the modulation 
slider of the modulation oscillator here what happens we're in a square wave configuration here see 
on or on off on off the modulation oscillator the square wave of modulation oscillator is 
modulating the complex oscillator's volume the amplitude turn it up a little bit so we just zoomed 
in on the oscilloscope there so we can see it a little bit more clearly now we're increasing the 
amount of modulation on the amplitude now i'll increase the speed at which those modulations occur 
okay so there's amplitude modulation at lfo rate bring the modulation slider back down and the 
effect disappears so why are we hearing all that what's going on there well it's because the 
modulation oscillator as i say is hardwired behind the scenes into the complex oscillator in two 
different configurations we've just seen the first one of them so by increasing the modulation 
slider when we're in one of these two modes we have an implicit effect on the complex oscillator we 
modulate its amplitude if i switch to fm oscillator and we bring the complex oscillator back in now 
we're going to modulate the pitch of the complex oscillator let's do that slow it down a bit let's 
switch the shape of the modulation oscillator let's turn it into a triangle instead it'll make 
those frequency changes smooth slow it down even more and increase the depth of the modulation make 
that pitch change bigger you can see the tuner is getting more excited now so these two settings 
here amosk and fmask are hardwired pre-configured selection options that connect these two 
modulation these two oscillators together the third switch disconnects those internal connections 
so when you're in the the upper mode let's call it balanced mode there's no internal modulation 
being applied to the complex oscillator and so now if i bring complex oscillator back in it doesn't 
matter what i do with any of these sliders you're not going to hear it okay so that was all on 
channel a that's complex oscillators channel but as we can see the modulation oscillator can kind 
of get in on the act say can i join in and do a little bit of modulation to the complex oscillator 
turn channel a back off channel b is there all the time it took me by surprise momentarily then 
until i realized i was in low frequency mode that oscillator is actually outputting signal it's 
just that we can't hear it because it's so low if i flick to high mode there's the tone i bring 
this tone back in and also bring channel a back into the equation you're now hearing both of those 
effects at the same time hearing complex oscillator in channel a modulation oscillator in channel b 
and you can see that they're slightly out of step their frequencies are slightly out of step and 
that's why you get this kind of strobing effect on the oscilloscope i have actually tried in one of 
my more bored moments to sync them up perfectly it's about one and a half steps out so somewhere 
between 501 and 502 gets you as close as you can to those two waves being perfectly synchronized 
but you can't actually hard sync them let's put oscillator a back to sleep again the complex 
oscillator and just refocus our attention on the modulation oscillator role on its own so we're 
back to having a nice simple tone this could be modulated in exactly the same way complex 
oscillator could so let's throw an envelope into pitch so we did all this kind of stuff with the 
complex oscillator but as things stand if i plug something into this modulation input we're 
actually going to have no effect on anything we're not going to hear anything if the modulation 
oscillator isn't hardwired to the complex oscillators amplitude or frequency modulation inputs 
modulation slider seems to have nothing to do there's it's not having any effect on the sound on 
either oscillator i can bring the original oscillator back in and these sliders are still dead but 
that's not the end of the story if i turn both oscillators on i put them both in all double 
frequency range pretty unpleasant but the point i want to demonstrate is that these sliders are 
both dead well that one is definitely because it's not plugged into anything but this one is not 
doing anything but if i take a jack out of this socket up here that says mod cv out the modulation 
oscillators control voltage out if i take something from there and plug it into the complex 
oscillators tomba modulation now i've got modulation capability over anything i want it's basically 
let's just sent it into low frequency mode there this modulation output is directly accessible from 
your mod cv out socket so this is in addition to the hardwired connections here so once things 
stand at the moment this complex oscillator is operating basically consistent volume or amplitude 
if i switch to am oscillator mode now in addition to having the tombrol effect i'm also modulating 
the amplitude it's doing two separate jobs one of them from the hardwired connection and one of 
them from the explicit and socratic connection over here and just a quick word about am and fm 
modulation most of the examples that i've shown you today have been in low frequency mode so if i 
get the complex oscillator up and running again and we switch instead to having a look at insight 
i'll take that modulation away i've got a nice simple wave there we go so this is currently 
oscillating at 260 hertz it's a c what i want to find out is what's the frequency of the tone 
currently being generated by the modulation oscillator well let's set it to something fairly 
sensible what's that children let's bring it down a bit i want to make it lower than that perfect 
okay so modulation oscillator b is now cycling at 100 hertz and oscillator complex oscillator a at 
260 hertz when we apply am modulation to those two waves in other words add them together we're 
going to get what's called a sum and difference effect and the best way to demonstrate that is to 
bring the modulation so i've turned it into am oscillator mode now so the modulation oscillator is 
hardwired into the complex oscillator now i'm going to increase the modulation and have a look what 
happens around the 2 to 400 hertz range these two side towers called side bands they're the sum and 
difference of the two difference the of those two combined waves so we have 260 plus 100 so this is 
going to be 360 over here there we go brilliant and we have 260 minus 100 this is going to be 160 
over there that's the fundamental concept behind amplitude modulation as we increase modulation the 
sidebars just get bigger and that's tonal coloring the only difference between am modulation and fm 
modulation is that you get the same effect you're going to get those two towers again but you also 
get um an infinite series of additional harmonics so you get the base frequency plus 2n plus 3m 
plus 4n so you get 360 460 560 and they get smaller and smaller as they tail away so it's a 
slightly different algorithm but both really easy to understand and see so that's our introduction 
to the modulation oscillator finish it there's a bit of a heavy one today i'm sorry about that i 
hope you enjoyed the video and found it useful if you did please consider subscribing hit 
notifications you'll be sure not to miss the next episode in the series hope to see you then thanks 
a lot for watching you 