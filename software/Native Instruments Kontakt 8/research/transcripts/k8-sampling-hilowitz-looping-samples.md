https://www.youtube.com/watch?v=Vf5B90wOTTE
David Hilowitz · How to Make Decent Looping Samples (Kontakt loop modes, crossfades, WaveLab) · 2018

hi I'm Dave Hill awaits so first let me apologize my voice is kind of off because I have a cold so you'll just have to do your best to pretend like I sound totally normal okay so the past few weeks I've talked about different aspects of creating instruments recording editing chopping up samples and stuff like that and

we did a little bit of scripting this week I wanted to talk about looping specifically creating looping samples it's just one of the ongoing headaches of anybody who's had to do this for a while anytime you want to make a sample loop it's just it's always a manual process and it's prone to error and it's it's just

frustrating so I wanted to cover a few pieces of software that might make our lives a little bit easier but there's no magic bullet here you'll always have to do this a little bit manually okay let's go so what do we mean by looping of course what we mean is sounds that go on forever and there are

some cases where that really does make sense like synthesizers for example a synth lead probably is going to extend forever almost always but there are other instruments like a piano or a plucked harp where the natural decay where at one end of the waveform it's really loud and the other end the waveform it's really soft is exactly

what you want in fact that's kind of the whole point I'll give you an example here I've got a harp I actually built a harp Oh a little while ago and I'll probably do a whole other video about that at some point but here is a sample [Music] now let's imagine that I tried to isolate part of

that and make it loop [Music] kind of loses all of the character I mean it sounds like a synth you might as well have a sense there so if you're doing an acoustic instrument and it's a plucked instrument you're probably not going to want to have it loop so let's look at how we do looping in contact

I'm gonna get rid of this sample and I'm gonna pull in probably the easiest case for looping like by far the easiest kind of thing to loop is a synthesizer waveform that's a very basic synthesizer waveform so like a sawtooth wave or a sine wave or something because what you're looking for when you're trying to create loop

points is you're looking for periodicity you're looking for repeated patterns because what you're trying to do is you're trying to isolate a pattern and you're trying to find the start point of the pattern the end point of the pattern so that the pattern can just be like repeat it over and over and over again by the sampler

so I'm gonna pull in c4 we know that the note number it's very convenient and I can actually spread it for the entire length of the keyboard and there's what it sounds like okay so two ends after a second so what we need to do is we need to set a loop point which is extremely easy because

this is a synthesizer waveform and a very basic one so I double click on it it brings up the wave editor and in order to get a sample loop activated I just click this little one here and you can have up to eight looping segments which you know allows you to loop different parts of your waveform and

generally with a sound what you want to do is you want to find something that's after the initial attack you can see here even though this is a synthesizer waveform and in theory every single oscillation it's going to be pretty much the same this is an analog synth and when it first triggers the the oscillator it's a

little bit different it's actually you can see the waveform actually takes a little while to settle into a groove so what we want to do so we want to just kind of choose an arbitrary chunk of this in the middle and if we play it now it's going to make a clipping noise [Music] so obviously we don't

want that clipping noise we want it to be completely smooth as though there's no looping going on so what we wouldn't need to do is we need to zoom in which we can do using this little button and we can see essentially the start point a microscopic version of the start point and a microscopic version of the

end point and the goal is to have those waves mesh so on the left side we have the end point and what we're just gonna drag it so it matches up and now if I hit the same note no clipping of course that's an artificially easy scenario setting waveforms for a very very basic synth patch is just

always gonna be very very easy it's a pain to do it manually it's also something that like there are algorithms out there that will do this for you and they're pretty good at figuring that one out so basically what's easy for a human is also easy for the computer okay so while we're here we should talk about

the loop modes so there are a bunch of different loop modes until end is the default one and basically it means that anything after the loop is ignore so you hit the key and now I'm gonna let up so as the sample is decaying it's continuing to loop what this means effectively is that this chunk of audio

after your loop is never used and you could actually in theory just truncate your waveform and save some disk space it seems trivial but when you have like 8000 samples getting rid of those tails is actually pretty useful so then if we go to until release this actually does use this end chunk so we're gonna do the

same thing I'm gonna hold down the key I'm gonna let up so you saw it half there instead of looping forever and letting the entire release phase play out it actually just went into this tail portion and played that and it actually ran out of waveform to play so in a sense the until end is a better

default and that's why they've probably picked it as a default okay and then we've got these sub modes until end forwards and backwards and until release forwards and backwards now look what happens so it's playing the live portion forwards and then it gets to the end of it and instead of cycling back to that nice perfect loop

point it's actually playing the sample backwards so forwards backwards forwards backwards not that many sample sound good that way so you're probably not going to use it that much but there are occasional uses for that okay then you've got this interesting parameter count you'll see here that contact offers the possibility of having eight different loop points so

you could in theory have a little chunk here and then you could go here and be like I want to make another chunk here and then here and then make another chunk here and then you could say I want you to play this one three times and play this one twice and then this one play this zero

means forever so okay now I'm going to play it it's going to sound terrible because I didn't actually fine-tune those loop points but watch what it does okay I personally never found a use for having multiple dew points in a sample but I'm sure that there's a use for them somewhere then there's some pretty sophisticated a grid

here and this is actually more useful for if you've sampled a drum loop and you want to chop it up and kind of manipulate some of the sounds it also works for since that have like a gated trance or an arpeggiator or something rhythmic you can use it to kind of chop up the sample and then sync

it with MIDI which is pretty cool okay so we've looked at this very basic synth waveform and that's probably kind of an artificial example because it's just so easy to work with what if we have a real world sample like a violin I'm going to get my violin and we're gonna record just one note and we're going

to try to manipulate it in contact and see how difficult that is [Music] okay there we go okay so we have our violin note here and I'm going to rename it okay now I'm going to pull in the violin note it's one note up from it's probably about an a I don't know worry about the tuning in

a little bit okay so we've put it here [Music] okay so we've got our violin and we don't have any loop point set so what first thing I'm going to do think I set the start point here the end point looks good and as you can see this waveform is a mess and the reason it's a mess

is because when you play the violin obviously you bow down then you put up then you bow down and every single time you do that you completely change the dynamics you completely change the actual waveform that you're generating and the violin is a complicated instrument that's kind of what makes it sound so nice by the way I

should get rid of this filter it's wondering why it sounded so muffled so I'm gonna set a loop point and I'm going to drag this and I know I don't want it to be at the very start because we don't want the very start to repeat over and over again but see what happens if I choose a

very short chunk of this wave maybe we say okay we're past our attack phase here and that's probably as close as we're gonna get so now I'm gonna play that note again [Music] so the problem here is that we have a very short chunk of audio and the loop sounds one way at the beginning sounds a different

way at the end and that repetition that repetition of a short chunk of audio over and over and over again is very very noticeable so what we want really is to have a much much longer loop so that the ear kind of can't remember what it sounded like at the end when it gets to the beginning again

so let's say we were able to take this whole chunk and the loop with that that's probably as good as it will be now we're going to zoom back out I'm gonna hear how that sounds [Music] so that is kind of brutal with violin you actually have an option there's some string libraries that just try to extend

notes as long as possible and basically what they do is they have these string players play like a single note for as long as they can possibly hold it and then they try to find a loop point in the longest part of the sound that works not completely natural sounding the other option with a violin because you

have these multiple rebounds is you can include the rebounds as part of the sound spitfires British drama toolkit actually did that recently they recorded all these string players doing what I just did bowing and then rebo and then rebo and they looped it after two or three bones your ear kind of can't tell because the samples are

so long that's not what we've come to expect from a string library it's a pretty clever technique though and it sounds pretty great okay so let's let's play with this some more I think the rebo in happened here and then I think the other one happened here so let's let's try that [Music] okay so that sounds bad

but there's another option that we have and that is cross fading and it's a pretty clever thing that a lot of samplers have built-in which is basically what it does is it takes a little bit of audio from the beginning of the loop and pastes it at the end of the loop and vice versa so that the

sample points are much better meshed and here's what that sounds like I'm going to just enter in an arbitrary value [Music] okay so you can see it got rid of the click it still doesn't sound natural but it sounds a lot better okay so let's say that you don't want to use contact to set your loop points

they're a bunch of reasons why you wouldn't for one thing if you set the loop points in contact those loop points and that all of that work that you're putting into each sample finding the loop point and all of this fine tuning that's stuck in contact there's no way to export that data out of contact so if

you ever want to use another sampler like Ableton Live or SFZ or something you'll have to redo all of that work so I would almost always rather set loop points in an external audio editor I just I don't like the idea of being stuck in a specific piece of software even free audio editors like Oh see an

audio allow you to set loop points so if we wanted to set a loop in a scene audio what we do is we'd select a chunk of audio and we would right-click it to create region and loop and we can call it whatever we want doesn't matter then we're just going to convert region to loop okay so

we've saved it and now all we need to do is go back into contact and re-import the sample and there you can see the loop points been set of course osya audio is actually really really hard to work with for sending a loop points it doesn't have anything like this loop editor it's just it's not really set

up for that you can edit the points it can delete them it can change them very slightly but it's just not a tool that's very well suited to this so let's take a look at some other pieces of software that we could use so they're a bunch of freeware options there's something called loop audition here which is

a piece of Windows software which I've managed to get to work kind of using something called wine-bottle err which is a thing that lets you run pretty simple windows apps on your Mac and trying to run it now as you can see it takes forever to launch and the user interface is pretty kludgy but it does work

in after a fashion okay so let's check out loop audition here and what you do is you point it to a directory you don't point it to a specific file it's out there we've got a violin note and we've got violin too so you double click on some sample and it shows you the waveform and it also

shows you any loop points that might be defined in it and then you have options up here like auto loop auto loop tries to find the right loop point for a specific sample so what happens if we click this said searching for loops yeah sorry I didn't find any loops okay so it wasn't able to automatically find

any loop points one cool thing that this does have that Oh seen audio doesn't have is it has a loop Tweaker if you do view loop points yeah this is basically just the same view that contact was showing us before that loop edit button this is the way that loop audition ear does that same thing it's basically

just showing us the waveform at the start and the waveform at the end and we can try to make them match up as much as we want so and we can of course here the sample if we want to in this case we're hearing how awful of a looping job I did a no scene audio then you

can do crossfading and let's this is the duration of the crossfade let's say we did okay here how's that sound [Music] okay so that fixes the clipping point so this is already a pretty useful tool you can use it to burn that auto fading right into your sample you can use it to tweak your loop points even

if it can't automatically find the loop point for you it's still pretty useful there's also a pitch detection algorithm which in this case seems to have come up with wildly different estimates as to what note I was playing MIDI note 60 maybe know- 558 million no zero not very useful I have found it to be pretty useful

with more consistent samples but with something like a violin where you've got vibrato that's actually changing the pitch slightly throughout the entire length of the sample it's pretty much useless okay so that's a loop audition here definitely worth having on your hard drive but it's not going to fix everything probably the best piece of software that I've

found for doing this is actually steinberg's Wavelab and it works even in Wavelab elements which is I think $99 right now so let's check that out so here we are this is Wavelab Elements 9.5 the latest version so let's take a chunk of audio here and what we're going to do is going to right click on it

we're going to do create loop from selection and then we can listen to the loop okay so it sounds terrible now we're going to go into loop Tweaker which is and you're probably pretty familiar with these windows by now this is exactly what we had in contact but the difference with what we had in contact is it's

actually looking for loop points based on its own algorithm and it's looking for them automatically these blue buttons allow you to kind of move the loop start and loop end but instead of moving it by individual samples it's actually looking for waves that actually match up a little bit so there we go that's a pretty close match

now let's listen to that okay so it's not perfect it's never going to be perfect because this is not a sample that's really meant to loop but if we go here and we do crossfade it's got these crossfade points that are automatically set up for us so if we were to hit apply but actually modify our audio

and here's what it sounds like that's probably too short of a loop but it gives you an example of what you can do then there's this funny other tool tone uniform Iser what it does is it chops up your wave into little slices and then it overlays it over the entire length of loop to make it smoother

sounding here's what that sounds like so it's pretty artificial sounding one of the things that it does is when it's doing that process of kind of chopping things up and overlaying them it also does a pre crossfade meaning that you get a little bit of that before your loop point and the reason for that is they know

that their weird sliced up audio is going to sound a little odd especially right next to audio that has not been screwed with so they have this delicate fade that kind of deals with that problem I don't use the tone uniform eyes are very much it's kind of useful for like synth patches but for like natural instruments

like a violin it's you know it's got to make it sound much more artificial that being said the loop Tweaker is just an amazing feature and totally worth it in my opinion okay so another cool thing that Wavelab can do is it can actually detect the pitch of your wave so if you go into sample attributes here

and you hit create because what that does is it creates a metadata header for your WAV file you select a little bit of audio and then you do detect from audio selection and it uses some algorithm to determine the pitch of your sound if you pull this into contact it's going to set the root key to a2

which is super useful okay so I kind of wanted a better real-world example other than this one violin note so I'm going to sample these wine glasses and see if I can't make contact library out of it okay so I just spent about half an hour recording wine glass samples and I've got a bunch of samples that

sound like this so pretty much all I did is I selected chunks of audio pretty much arbitrarily and I created loop points by right-clicking and then doing create loop from selection once I'd done that I went into the Tweaker went into crossfade and just hit apply that does the automatic crossfading I didn't manipulate any of the settings

and then I saved it and now I'm ready to go into contact see you there okay so now I'm back in contact I dragged all of my samples in I actually made four groups so that I could have some round robins and yeah so when I opened up any of the waves basically all of the loop points

that were set in wave lab are already in contact and it's a beautiful thing not to have to futz with the wave editor at all yeah let's see how it sounds [Music] so yeah that was an interesting experiment it's kind of pretty but it's also a little bit eerie maybe better suited for horror movies or something so

yeah anyway that's looping I hope this video was helpful I'm gonna put a link to the instrument in the description to the YouTube video and yeah if you've been enjoying these videos make sure to hit the subscribe button take care
