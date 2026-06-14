https://www.youtube.com/watch?v=N6wprMToxSg
David Hilowitz · How I make sample libraries — 2020 Edition (Kontakt, SFZ, Decent Sampler, REAPER) · 2020

[Music] hi i'm dave hilowitz so last week i attached a slinky to my violin and i thought it sounded really cool a bunch of people reached out and asked me to turn that sound into a sample library so yeah that's what we're doing here we're going to do that today i'm going to document the entire process from

recording to chopping to making a contact instrument i'm also going to chop this video up into like little bite-sized quick tip videos so if you see the same content reappearing on the channel in like a week or two don't get angry i'm really just trying to make it easier for people to find the information that they need

without having to sift through like a longer video okay let's get started before i get started with any recording project i like to do what i call sample math um you know try to figure out how long the project is gonna take generally that helps me uh stay sane as i'm like working through a bunch of boring

recording um so let's say i'm gonna record 36 notes and i'm gonna record three velocity layers and five round robins that's a total of 540 samples not so bad if i then figure that each sample is going to take maybe 10 seconds but you know let's be conservative and there'll probably be some flubs i'll probably mess up

a few and have to redo them so let's say on average it's going to be 20 seconds per sample that results in 10 800 seconds 10 800 seconds is exactly 180 minutes which is exactly three hours chopping up 540 samples is not a trivial task you know there ways of making it a little bit quicker for yourself

but um it can be quite a headache so before you commit to a large number of samples i would look at what aspects of this you can prune down so today the sample that i'm making is just going to be like a free thing that i release on the website uh and i don't really care about velocity

layers i don't care about round robins i don't even really care about sampling every single violin note i can do every other note and be fine so if we reduce down everything suddenly this 540 samples has now become 24 samples which should take me like six minutes or something to record um not bad at all okay i

think we're ready to get started so there's several different philosophies about how to structure um sample recording there are people who plan a session out meticulously in advance i am at the other end of the spectrum i don't plan at all and the reason for that is especially when i'm recording weird oddball instruments as i often do

i often make mistakes and having to go back and reset the counter and fix where i am is very very frustrating especially if you're holding a violin and you've got the bow and you've got the headphones and you're in the right position for me it makes much more sense to just kind of keep the recorder running and

record everything when i mess up sometimes i'll make a loud noise or i'll clap or do something like that so i can see a spike in the audio and i know okay that was a flub also generally if i see the same note appear twice i know that the second one is the good one i generally try

to record everything into one wav file the reason for that is i do noise reduction um like destructively at the beginning of the editing process and it's just way easier to bring one wav file into rx or whatever um if i do have to stop and i have multiple wave files i'll generally glue them together before i

do the noise reduction the other thing that's worth mentioning is you know right now i only have one velocity layer but if i had multiple velocity layers i would always record the notes from each velocity layer separately like i find it way easier to run through the entire scale doing piano then run through the entire scale during

mezzo forte and so on and so forth rather than having to switch velocities [Music] okay so i have recorded uh the violin one velocity layer and i've recorded a little snippet of silence at the end of the session our next order of business is to do some basic noise reduction in izotope rx so what i'm going to

do is i'm actually going to drop down to the finder and i'm going to find these big files the full run through files as i've called them and i'm just going to duplicate them in the finder and i'm going to append rx to the end of both of them and in this way i run no risk of

accidentally overwriting my data i always keep the original data because i tend to be pretty aggressive when it comes to noise reduction and sometimes when i listen back to the results i end up wanting to dial it back a little bit okay so let's open this up and i'm also going to open up this which is the

silence for this particular mic you'll notice that i am applying rx destructively so to speak although i am keeping a backup and i'm applying it separately for each of the mics pull this in and here's our silence and there is our session uh it's important uh when you're doing this never to actually delete chunks of audio uh

you know that temptation is huge to just like get started with editing but since we have multiple mics we need both of these files to have exactly the same timing so don't do any um you know edits here other than applying rx okay let's open up spectral denoise and yeah teach it what silence sounds like and here

i'm gonna do say 24 and i'm going to leave everything pretty much as is sometimes i mess with a curve to either bring down the hiss a ton or to do a little bit less towards the top end i think we're just going to go with the default settings for today as you can see i've chosen the

best algorithm and as a result this is going to take a while it's going to take three minutes so i'm going to turn off the camera and when i come back we can continue it's always a beautiful thing when you can see the spectral readout update itself from left to right and you can just see all the

silence disappearing okay now i'm going to do the exact same thing for the piezo mic generally piezo mics have very very little noise i'm going to do a little bit less noise reduction but yeah the process is identical okay so we've just saved the piezo rx version can close out of izotope of course reaper is still referring

back to the old non-rx version so what i'm going to do is i'm going to go into item settings and i'm going to do choose new file for each of these another thing that's worth noting is that i hit g and group these tracks um basically what that does is it means that any edit that i apply

to this one will get applied to this one and vice versa okay time to split everything up this is usually pretty easy i'm actually going to just hit d and see what it recommends um that actually looks pretty good i'm basically just trying to do like rough splits at this point to just kind of um isolate what

is notes and what is me just screwing around with a violin uh because there was there was a fair amount of that uh okay uh i'm going to yeah let's do it let's just see what it's like and one of the wonderful things about grouped tracks i'll say that right off the bat is that it does all

of the edits to both tracks even though i actually only selected the piezo mic it did all of the determinations about what was silence and what was notes based on the piezo track which i think is going to be a little bit more reliable than the room mic but it split both tracks which is really nice okay

let's save a new version of the project okay so we've got our basic splits done now what we need to do is we need to label them uh with regions and we need to figure out what notes these are so first i'm going to show you what the manual process would look like if i were going to

do this entirely by hand then i'm going to show you this script that i used that i actually paid money for that will do it for me so the first thing i want to do is i want to select all my samples and hit f2 and make sure preserve pitch when changing rate is not checked hit okay

i always change the pitch using the rate rather than the algorithm just because that's my habit okay so if i were going to do this manually what i would do is i would put a tuner up on the screen and you can use riatune which is the tuner that comes with reaper it's pretty good actually [Music] okay

so this is g3 so we're going to do two things here we want to label these so in theory i would go like this and i would create a label and this said that it was g3 i would label it g3 and then uh i'm going to do some tuning on it and i do that by using

um shift shift three and shift four which uh i have um actually i'll show you the action for it i have these custom scripts which increase or decrease the item rate by 1 cent and basically those allow me to do the sample tuning manually when i'm doing it manually so this one is sharp by about 13 cents

so i need to press shift f3 about 13 times you can see up here it shows you the actual pitch change that it's going to perform on this yeah dead on so that's how you manually tune this another thing that's worth noting about doing that is when you change the rate it actually changes the length of your

sample because it's playing it slowly you want to turn on snap and make sure that you sync the end point to actually be the exact endpoint of your samples um and yeah there's key combinations for that like i just press um option slash or something um i'll save all of these uh extra scripts that i use um

so that you can download them and make use of them yourselves okay so we've seen what the manual process is for determining the pitch and tuning samples let's look at some automated scripts um there's this guy named x-ray or x-ray if you're french who's developed this massive suite of reaper scripts that are very very helpful for samples

there's one for um you know naming regions in a sort of programmatic fashion which is really helpful if you have like round robins there's some for doing pitch detection which is what we're going to look at here there's just like a bunch of useful things some of them are free some of them cost money this one actually

costs like 75 or 150 euros depending whether or not you're an individual or a company yeah check this out so i've zoomed out what i'm going to do is i'm actually going to select all of the items on this track the piezo track and i'm going to go down here and i'm going to run this script and

it pops up a window with yeah a bunch of settings and i'm going to keep everything at its defaults the way this script works is it exports out each of these items and then runs it through command line utility called aubio aubio is a kind of audio library that does pitch detection among other things and it's much

much more accurate than anything that you'll find in a daw so if you look down here it says done and i close this and we can actually go here and you can see that it not only determined that this was midi note 55 note g4 but it actually fixed the pitch for us of course uh it didn't

fix the pitch on both i've only done pitch detection on one of the two so the next thing i'm going to do is i'm going to use another x-ray script to kind of sync up the tracks and it syncs things using columns so i select everything i'm going to zoom back out here and i'm going to pull

up another xrayme script so the script that i want is called set selected items length and rate by column according to track under mouse or first track with selected items catchy i know i'm going to select everything i'm going to make sure that that first track is selected i'm going to hit run and as you can see

it synced everything up the next thing i'm going to do is i'm actually going to go through and select all of these especially the ones that only have one item and you can actually just do insert separate regions for each selected item and as you can see it not only creates regions around these items but it actually

names them according to the name of the item and as it happens the x-ray script has named all of the items correctly so once i'm done with this process i can basically just export right out to contact and just like that with just a few scripts that i ran uh i have tuned my samples and i'm ready

to start working on loop points when you're recording a bowed stringed instrument like a violin one of the common tasks that you need to worry about is removing uh boeings some people do like to leave boeing's in because obviously it results in a more natural sounding sample uh at the same time uh it can be jarring for

composers and some people just expect to have like smooth almost synth-like sounding strings okay so we have here a bunch of violin samples and as you can see each of these little points here are re-bowings there's another one and um on their own they sound fine but uh they can be quite jarring for people who are composing

and we need to see if we can't remove them or at least lessen them so that they're a little bit less noticeable the way we're going to do that is actually just using a cross fade we're going to create a split and we're going to move this here and as you can see because we're using reaper it

creates a nice cross fade between the two the danger of that because this is a solo instrument is we are of course doubling up on violins during that crossfade period so here we've got one violin here we've got two violins and then here we've got one violin again the longer the crossfade region the more noticeable that transition

is going to be if you've got a long region like this in the middle of that it actually sounds like there are two violins and it's very very noticeable at the same time if i go and make this crossfade super short [Music] you immediately can hear the bowing and in fact it actually sounds more artificial than if

i just left the bowing intact so really that's all it is it's just finding the perfect length of crossfade uh and we're going to go to the next one going to do the same thing and if i uh press shift up on reaper it actually boosts the display it's not actually changing the audio it's just changing the

way the audio gets displayed so i can see these re-bowings much more clearly and once i've gotten all the way to the end i'm just going to listen back to the whole thing and make sure it sounds natural to me that's a whole deal basically just tweaking crossfades until you find something that just sounds natural to your

ear it's a completely subjective process and it's a little bit time consuming but you know it's not so bad i'm going to turn the camera off so you don't have to watch me do this for the remaining 24 samples or whatever this is when i come back we can talk about how to add loop points and export

them out of reaper and import them into contact so when i'm putting together a sampling library i like to do all of my looping stuff in the daw where i record my samples i don't like to use the loop editor in context or in another sampling tool to do it at that point the reason for that is

i often like to release my samples as sfzs and sfz does not have any uh facility for doing crossfading you have to do the crossfade destructively right when you're rendering out your samples so here's how i do it in reaper we'll start here we've got this violin sample what i like to do generally is i like to

position my samples at the start of a bar line it just makes it easier to kind of work with it and do any math that i might have to do hopefully won't have to do any math but maybe we will we'll see okay so we've got a nice sample to work with i'm actually going to close this

so it's not in the way and here's what it sounds like on time okay so nice long sample pretty easy to work with uh what i'm going to do now that i've got on the bar line is i'm going to pick an arbitrary point maybe about a second in and that will be the beginning of my cross

fade so what i'll do is i'll put a split point here and i'll just grab this chunk that comes after and i'm going to undo so it heals that that split there but i'm going to remember i did it at this point we're going to need to know that because we're going to need to create a loop

region in just a second okay so i've healed it now i'm going to shrink this here so that we can start our crossfading here and i'm going to paste this in and you'll remember this is the bit of audio that starts right here right after that second tick mark and i'm going to drag it forward so that

the entire first part of it extends into the end and this is the end of our loop so our loop extends from that split that i put there and we're gonna make a little region and we're gonna try it out i'm just gonna turn on looping and let's see if it loops seamlessly that's it that's all you

need to do and if you position everything on the bar line like i did uh it's actually very easy to just go through and like almost like programmatically um copy little bits of audio from the beginning to the end of your samples and then pull back we can actually shrink the parent region the one that's uh encompassing

everything so that its end is the end of the loop point because there's no point in rendering out more audio than you're ever going to use so also now what we're going to do is we're going to open up our region list and you'll remember we created a new region for that loop point next thing i'm going

to do is i'm going to call it hashtag loop and that's going to come into play later when i export out my samples reaper actually will export out any region that starts with a number sign and it will export that out and embed it in your wave and contact and other samplers can actually read that as like

the wave cue point so you don't need to actually do any work in contact or in sports ondo or decent sampler or anything like that it'll just read the loop directly out of the wav file so that's pretty pretty handy uh okay let's go to the next one uh we'll repeat okay let's uh let's listen to it

sounds great okay now i'm going to hit shift r and that's going to create our loop and i'm just going to label it okay that's it i'm going to turn the camera off and when i come back i will have set loops for all of these samples see you in a bit okay so i'm back i've set

loop points for all of these regions it only took about 15 minutes wasn't so bad obviously if you have a large number of samples you probably want to look into some sort of automated solution okay so the next step is to figure out how to export these in such a way that contact can read the loop points

um that's actually really really easy so the first thing we're going to do is we're going to go to the region render matrix which is probably the most useful feature in reaper as far as i'm concerned just the ability to specify exactly which regions and exactly which tracks get exported since i have two mics here i'm going

to export out all tracks separately and i'm going to do it for each of these groups you'll notice that i'm not clicking on any of these loop regions because those actually get exported out automatically you'll see that in a second okay next we go to render and by default this is what the window looks like so we're

going to go up here we're going to make sure that we're actually exporting out our region render matrix so basically all of these decisions that we made down here will now uh be used in order to figure out what files to generate and immediately you can see which files are being generated here basically it's just going to

generate this massive number of unlabeled wav files so we need to fix that we want each of these regions to be labeled according to the region name so there are a bunch of wild card tokens you can see them all here the region name is just called dollar sign region so if we look here everything is labeled

according to the midi note number although we've still got two files for each midi note number those two files correspond to these two tracks so we also want to include the track which uh in sampling world we're going to turn into the group name so let's look back at what it's going to generate you can see here

it's going to generate midi note number group name which is it's perfect if we had different dynamics different velocity layers we would also have labeled that as part of either the track or as part of the region depending on how we set up our session and that would also make its way into the file name next thing

we need to do is just double check the sample rate does not always match the project sample rate for some reason okay so what about these loops how do we export those go down here and click right bwf chunk that's the thing that's actually going to embed um metadata in the wav files that it exports and then

click this drop down and go to markers and regions starting with number sign all of our loop points start with the number sign so all of them are going to be embedded in our wav files the final thing i'm going to do is just specify directory otherwise it's just going to output it right into your daw session

directory and you do not want that okay looks pretty good i'm going to hit render and sit back and watch i'm going to open up a new project and we're actually just going to work on a contact instance right here in reaper since we've got it open i'm going to click effects and load up contact start a

new instrument always a fun moment okay now i'm just going to drag all of these samples into contact in random positions and then we're going to get started on auto mapping so i right click all the samples and i do auto map setup and the first thing we're going to do set to single key we're actually going

to ignore the midi note name because i don't like using midi node names and then finally this thing is going to be the group name and it's going to create two groups piezo and room there's this weird thing with contact where for some reason when it has to create a new group it stops the auto mapping process

you can see there it stopped both times when it had to create two new groups so now we're free to select all of these and hit auto and it's finally done it for us okay and i'm going to click this which will do selected groups only so we can actually see what's in each of these groups we

can see there's nothing left in group one so we can actually delete this one so we've got piezo and we've got room so the thing about this of course is that it has not set the root note so what we're going to do is we're actually going to unselect selected groups only i'm going to right click here

and do select all zones then i'm going to right click on this and do batch tools move root keys to center and what that does is it sets the root key to the note that each of these zones is actually occupying uh it actually sets it to the center if you had it uh occupying a whole range

but since we've got each one of these to only occupy a single um half step then it basically just sets it to the same value uh okay so uh now that we have uh the root note set i should be able to just play a chord okay so it sounds pretty good already uh i'm going to actually

um select all of these and just fill in all of these gaps by clicking here you'll notice that i didn't select the ones on the end because i don't want contact to stretch things all the way down to the the beginning of time although we could probably go down to the lower c and then grab this one

and go up a little bit to get ourselves a little bit more of a range okay so right now one thing that i need to change immediately is i need to lengthen the release time here and i'm going to add the attack a little bit more it's already got attack built into the samples obviously but just on

the off chance that there's like a clicking noise at the start of one of the takes it's always a good idea to put a few milliseconds of attack at least okay let's give it another [Music] i spin it sounds really good actually uh and this is without any kind of reverb or anything uh if i wanted to

um add reverb i would do that here and uh grab one of these [Music] so this sounds great it's a nice sounding violin patch so if i go in here and we look at one of these samples you immediately can see that contact has actually pulled in the loop let me play this note that's like the longest

eight seconds of my life by the way but yeah it's pretty good it pulls in the loops i don't have to do any tweaking with the wave editor even better i can now turn around and make an sfz sample and because uh those loops are embedded in the file i don't have to do any extra work to

kind of translate it to many different formats uh so that's a huge win so of course what we've been listening to has been a mix of both the piezo and the room let's check out what the just the piezo would sound like so i'm going to go to room here i'm going to turn off edit all groups

of course and i'm going to turn down the mic on the room [Music] it sounds great i'm pretty happy with the sample okay so we've made our contact instrument at least a basic one now why don't we make a decent sampler version and an sfz version i'm going to save the contact one as slinky violin i'm going

to come back to this later and add more bells and whistles but the core work is done already okay so we've got our contact instrument and we've got our track called contact i'm going to actually add a new decent sampler instance i guess i'll do vst3 and i'm going to add a sportszondo instance i'm actually going to

close these now and i have two options since i'm converting over a contact instrument i can either use the um lua creator tools export scripts to uh export out decent sampler instruments um or i can do it by hand since i've got the lua export script i might as well use it so i'm going to open up

creator tools and right here we can see that it has established a link between creator tools in between that contact instance that's inside of reaper it's found two groups called piezo in room and as you can see i've got like a trusty script here that can export ds presets so i'm going to throw that down here hit

play and then hit command option c and that should copy the entire console and then i'm just going to paste it out and you'll notice down here that uh it has an extra console message that actually we don't want to have part of our xml definition this ready so just delete that and beyond that we should have

a workable instrument here there are some things that we can get rid of for example the path we actually want the path to be relative so we don't want this entire absolute path so i'm just going to do find and replace and i'm going to find this the long file name path and just replace it with nothing

okay i'm going to hit save and let's load it in decent sampler [Music] [Applause] very very good i'm actually going to go back to the decent sampler documentation and i'm going to grab the definitions for the two knobs filter frequency and the reverb level and i'm just going to plop those at the top and i'm going to

go down here and i'm going to copy this effects block which will add a low pass filter and reverb to the preset uh also because i uh want there to be a longer release time i'm going to go to each of these groups and set release time to well at least two seconds i would say now we

can do reload and we've got tone and reverb knobs first step towards actually having a skin for this thing [Music] okay and just like that we have a decent sampler instrument the only thing left to do at this point is to add a skin okay so we've done a contact instrument we've done a decent sampler instrument uh

time now to make an sfc and i'm going to use the exact same technique that i did for decent sampler i'm gonna just uh run a script against creator tools and uh only this time it's going to be the sfz export script that i use just super super basic i'm just going to paste it in here once

again i'm going to get rid of this from the bottom and don't really need the thing from the top make sure that all these values look good i'm going to remove the absolute urls because uh we want all of our url paths to actually be relative and basically just find and replace this and replace it with nothing

and i think everything else we can pretty much trust i'm gonna hit save and uh yeah let's load it up in sportszondo and uh see what happens no error messages that never happens on the first try there's always something that's great [Music] i'm really happy with this so i'm going to do at this point is i'm going

to set a release time for the envelope uh it's actually this uh ampeg release uh and yeah i'm just going to grab that because i'm being super lazy uh and i'm just gonna put that for each of the groups and i'm gonna set it to one because that's what i set it in the contact and the decent

sampler versions okay and we'll have reloaded i don't even have to click anything swarzon does really good like that so that's it just like that we have an sfz a decent sampler and a contact instrument uh hope this was a helpful video obviously it was kind of like a deep dive the only thing left for me to

do at this point is to create a nice ui for the contact version create a nice skin for the decent sampler version so the instrument that i made in this video is going to be available in a few days basically i just want to play with it a little bit more and yeah just figure out what works

what doesn't work um once it's been refined i will uh put a link to it in the description to this youtube video i would love to hear about your tips and tricks for sampling uh even with um great uh lua scripts for reaper and great lua scripts for uh creator tools i still feel like there's so many

ways that this process can be sped up i still learn tips and tricks every day that speed up my workflow so yeah keep them coming uh okay um i think that's it this was a long one if you enjoyed this video it'd be great if you could hit like and um if you've not already subscribed um now

would be great time got a lot more contact videos coming and a lot more like audio experiments that i have underway that i can't share yet but we'll share soon okay see you soon
