https://www.youtube.com/watch?v=JUTHsAtt650
David Hilowitz · How I sampled my modular synth (Logic Auto Sampler → EXS → Decent Sampler) · 2021

this is my modular synth [Music] over the past year i've been slowly adding to it and a bunch of people have asked me for an update video so that's what this is at least in part i'm going to talk about the two new modules that i've added distinct and maths then in part two of this video i'm

going to record the modular and i'm going to use those recordings to make decent sampler libraries so that should be a lot of fun i'm also going to show how to take exs instruments and convert them for use in decent sampler uh some new stuff got added so uh if you work with those formats you'll definitely want

to check this out okay let's get started since my last modular video i've added only three modules make noise maths expert sleepers distinct and the listen for mixer module by 4ms not much to say about that last module it's basically just a mixer with a headphone out oh yeah and i also added this drawing by my five-year-old

son in case you're wondering those round things are meant to be musical notes okay first let's talk about the distinct mk4 it's made by expert sleepers which is based in edinburgh scotland it's actually a completely unique module within the world of eurorack it's a little computer instead of performing one function it has dozens and dozens and dozens

of different modes all of which do wildly different things here it is being used as an oscillator and now i'm using it as a reverb effect [Music] and here it is again now being used as a quantizer [Music] because the distant can become almost any type of module it's actually kind of great for somebody like me if

i'm thinking i might need a specific kind of module for my setup i can often use distinct to kind of try it out before i invest in a dedicated module what's even cooler about testing is that new algorithms are being added all the time it has an sd card slot which you can use to upgrade your device

with new firmware you can also use that sd card slot to play back samples there's even a version of spitfire lab's soft piano that's been designed for it i've had this module for over a year now and i feel like i'm still only barely scratching the surface of what it can do okay now let's talk about maths

maths is an extremely popular multifunction module broadly speaking in the world of modular you've got things that make and process sound then you've got things that make and process control voltages and control voltages are signals that are used for changing parameters now maths can work with both types of signals but by and large it's the second one

of those two it's a module for making and changing control voltages and those control voltages are then fed into other modules to change their parameters here's a super basic example i'm going to hook up my keyboard to plats plaits is a multi-function oscillator which means it's one of the things in this rig that's actually generating sound flats

has these four knobs that let us control different aspects of the sound pretty cool sounding already let's say that i want this knob to be moving constantly obviously i can use my hands but that gets a little tiresome instead i'm going to hook up maths and have it move the knob for me maths has 4 channels on

the left side we have channel 1 and on the right side we have channel 4. channels 1 and 4 are for generating values that change over time and they have way more controls than channels two or three these middle two channels can be used to generate constant value signals so obviously since we want this knob to actually

move we're gonna use either channel one or four for convenience sake i'm going to use channel 4 since it's on the right side so by default this isn't actually doing anything and the reason it's not doing anything is we haven't inputted anything into that little trig input up at the top when maths receive something through that little

jack it triggers its waveform generation engine i don't want to be bothered with any of this right now so i'm just going to press this cycle button now that i've pressed that the waveform is just going to trigger over and over again in a loop you see how that led is glowing it's sort of pulsating that tells

us the frequency of the waveform that we're generating the next thing we're going to do is we're going to turn up the attenuverter on plats [Music] that controls how much that input signal is actually changing that knob's value so as you can see there are three controls for channel four rise which controls the first part of the

curve fall which controls the second part of the curve and then this shape knob which allows you to go from concave to convex [Music] okay so we've got the beginnings of a patch here let's take it one step further let's add an effect so as that happens one of the many many things that distant can do is

it can be a reverb i'm going to switch to algorithm l2 which is the mono to stereo reverb next i'm going to unplug the audio output from plats which was previously just going directly into the mixer and i'm going to plug it into the input on distinct then i'm going to hook up distance outputs to one of

the stereo channels on the mixer okay so now that i've got a patch that i actually like i'm gonna try to record it and make a decent sampler instrument now the traditional way of doing this is you hit record in your audio software then you go over to your keyboard and you press every single key on the

keyboard or all the keys that you want to sample and in that way you get a recording of your synth that's pretty tedious so instead i'm going to use the auto sampler that's built into logic pro on the mac as you can see here i've specified some specs for my external instrument the output is arturia keystep and

the input is inputs one and two on my audio interface the autosampler can be found here in the menu and when you click on that it pops up a box that looks like this where you can specify the range of notes that you actually want to sample and it's going to just work its way through the piano

keyboard sending midi signals to the modular rig and recording the audio output then once it's done it'll have created an exs instrument that's compatible with logic's own sampler plugin so these default settings look pretty good i'm going to hit sample and i'm going to call this modular patch 8. now i'm not actually going to sample every single

note which is why i have it set to six semitones so basically it samples c0 then it skips up six semitones samples f-sharp skips up six semitones and in that way it gets two notes per octave i won't make you sit through this in real time so our sampling is complete where's our instrument okay so what autosampler

does out of the box is it creates an exs instrument excess is the legacy file format that logic has used for at least 20 years at this point there used to be a plugin called exs24 and now that plugin is just called sampler and it looks a little bit different but underneath it's the same exs24 that everybody

knows and loves and yeah this is it this is the built-in logic pro sampler if you go up here you'll see that there's a folder called auto sampled here we've got modular patch 8 which is the one i just created now if i play some notes now that sound that we're hearing right now that's not coming out

of my modular that's coming out of this sample and if we go over here to mapping we can see that it has created these nice neat samples you can see here are the individual notes so the first thing i'm going to do is i'm going to go here and i'm going to do save as and i'm going

to make a new folder let's say on the desktop and i'm going to call it modular patch 8 and here i'm going to save the xs to this new location and this is super important i'm going to check this box save with audio data okay so we're in a really great position here we've got an exs file

that was just created by logic and in this directory we've also got a folder that contains all of the audio files that go along with that exs is kind of structured a lot like decent sampler in that there's a main file that contains all the mappings and then there's a folder that contains all the actual samples over

on the right hand side i've got pretty much a blank directory this is where we're actually going to be building our decent sampler preset in this directory i've got another directory called samples the only thing in this directory is this background image which uh is what i'm going to be using for my instrument the other thing that's

in here is a template and as you can see it's a little bit of xml that i'm going to be copying pasting into my instrument so i don't have to start completely from scratch you'll find with decent sampler that you can actually reuse your code a lot from old instruments or from other people's instruments i mean there's

no better way to learn about the format than to see how somebody else built their instrument okay so let's do the conversion i'm going to be using the standalone version of decent sampler just because it looks cleaner when you're making a video to use the standalone version in theory you can use any version i think except ios

at this point every version of decent sampler from 1410 onward has an import exs functionality built in basically all you have to do is go to the developer tools menu and do import excess file and what i'm going to do is i'm going to pull in this file [Music] and just like that we've converted our exs file

now you may know exs is a proprietary file format that apple developed they do not publish a spec in order to create this translator i had to find a lot of old forum posts where people had divulged a little bit about the format i did a lot of guesswork and reverse engineering so they're definitely going to be

many extended features of exs that are not imported but you should get your basic sample mapping and that's you know 90 of the work okay so at this point we've done the conversion we've got a ds preset but it hasn't actually generated a file so if we want this to actually be a preset that we can attach

a ui to we want to save it so i'm going to go into the file menu again into developer tools and then just do save preset and i'm going to save it to this blank directory and i'm going to call it modular patch eight i'm gonna hit save and you can see here it's created a preset so

let's look at this in sublime text and as you can see here it's converted all the mappings over and it's even created empty groups uh like a ui element an effects element this is because under the hood even if you don't have those elements decent sampler creates them in memory so when you save it out it's going

to save out those blank elements these things up here you can delete them they're really just for internal use there's no harm in leaving them in but you might as well delete them just because it makes it look a little bit cleaner okay so we've saved this ds preset over to this new directory but the samples haven't

been copied you have to copy the samples yourself so i'm going to go into this directory i'm going to copy these and i'm just going to put them in this samples directory now if i try to load this it's not actually going to be able to find the samples and the reason for that is over here in

the exs patch the samples were all in a directory that had the same name as the patch modular patch 08 with reverb obviously you're free to keep that structure i prefer to put all my samples in a folder called samples so i'm going to go back into the ds preset file and i'm just going to change these

paths with find and replace and do replace all now is a good time to go back to decent sampler and reload the patch just to make sure it still works [Music] uh so as i said before i've also got a template with a couple knob definitions uh so what we're gonna do is we're gonna grab that template

and i'm just gonna grab the ui and the effects and i'm going to paste it in here i'm going to copy over these ui and effects now we go back here we do reload and just like that in a matter of minutes we've gone from patch that existed only on my modular synth to something that you can

redistribute to people um using decent sampler oh one other thing if you're on mac and you do get a dreaded like apple sandboxing message saying that uh it can't access the samples because of uh sandboxing limitations here is a nice workaround um basically you go up a level in the finder and then you drag the entire folder

onto decent sampler if you do that then the entire folder gets blessed by the operating system and it kind of defeats apple's sandboxing limitations if you've only got one ds preset in a folder like we do here it'll just load that preset but for example if you were to like let's say we had another patch that was

called if we drag this here it'll pop up a choose preset dialog box so yeah worth knowing about okay i think that's it i hope you enjoyed this combined modular and decent sampler video all the patches i made in the video are available for free download link in the description to this video if you enjoyed this it'd

be great if you could hit like and if you haven't done so already now is a great time to subscribe i've got a ton of videos on the way um yeah bunch of stuff about decent sampler a bunch of stuff about hardware uh some experiments i'm doing so a lot going on in the pipeline if you decide

to subscribe make sure you also ding that bell so you can actually be notified when i make one of these videos and um yeah i guess that's it see you next time [Music] you
