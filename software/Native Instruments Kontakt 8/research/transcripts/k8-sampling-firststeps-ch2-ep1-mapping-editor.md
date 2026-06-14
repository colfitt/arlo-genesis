https://www.youtube.com/watch?v=Gj-ZLEmn15I
NI / Steve (FIRST STEPS) · Adding Your First Samples To Kontakt Via the Mapping Editor — KONTAKT: FIRST STEPS (Ch.2 Ep.1) · 2023

if you've been following along with our contact tutorial series you have already seen some amazing ways to create some samples now it's time to get acquainted with the contact sampler and start getting our samples into an instrument that you can play [Music] hey my name is steve composer engineer and lecturer welcome back to the channel and your

first steps into the contact sampler we are launching into chapter two of this series now chapter one of course took you through many different ways to create samples both acoustic recordings and hardware synthesizers and even manipulating them with further effects and sampling methods now though we're going to dive in and build an instrument inside contact we're going

to learn about how to get the samples into zones those zones into groups how to control those with modulators and effects and get an instrument that you can actually play there's already been some amazing feedback on that first chapter so do keep it coming why not let us know in the comments how you've been using this series

i'd love to see what you're doing you can of course at any time go back and have a look at those videos revisit and remind yourself on some of the content but for now let's dive in and get going okay so what is contact contact is a sample which means it's playing back pre-recorded sounds that are mapped

to specific keys and sometimes specific velocities and hits now these sounds can be percussive or they can be pitched like the ones that i created in chapter one that we'll be using in this chapter really though anything can be sampled and anything can be played back which makes it really flexible at creating something brand new and really

exciting or recreating your favorite instruments contact is one of the more complex samplers with a lot of creative options and a lot of amazing tools to help speed things up and get really creative with the sample libraries you're creating however to get a basic library up and running it's actually fairly straightforward so that's what we're going to

take a look at through this chapter however the first thing you need to know is how contact is structured it is structured in a particular way this will begin to make a lot more sense as we dive into the library and start building it contact is essentially accepting samples and putting them into what's called zones those zones

can be mapped across one or more keys and across any particular velocity range this is how we can be a little bit economical with our sampling as we saw in the first episode of chapter one you could sample in major thirds or minor thirds or something larger like fifths or octaves and you can stretch those samples down

or up to other keys so you can be a little more economic you don't have to record every single note just a few so you can stretch them over the other notes that are around them now those zones need to be collected together into groups and you could have multiple groups depending on multiple different collections of sounds

or whether they're short or long articulations whether you intend them to be sustained or just one shot samples there could be a lot of deciding factors as to what one belongs in what group it's it's really up to you but those groups are then all contained in an instrument so to recap you have samples and they live

inside zones those zones can be spread across multiple keys and any range in velocity all of those zones are then collected together into groups and those groups are collected into an instrument hope you're with me so far this will make more sense as we progress through the instrument creation you'll actually see the groups that play you'll see

the zones belonging into them and see why i'm making decisions to put some zones together in a group and others into different groups in this particular case with my instrument i've got four different sample layers and i'm going to put them each into their own group so i'll have four groups this is so i can control things

like volume or pitch or envelope later on to specific groups rather than all of them together gives me a little more flexibility okay so let's take a look at the contact sampler so i've loaded up contact sampler here and you'll notice that it's got a few main components first of all i've loaded this standard instrument or library

that i've got so we have this alicia keys piano it's quite a nice piano sound and it's one of the ones that came in a collection with complete at some stage one of the benefits of buying contact in a complete bundle is that you get some of those instruments along with it now those extra instruments are all

seen down the side here you can see i've got a lot of drummers that are often appeared at the top because i've put my library preference into a to z so it's going through each one of these is an instrument or a library as i scroll through i do have other products in here from spitfire some from

output down here lots of different ones as i scroll through here's some evolution series lots of different things now our library unfortunately won't appear in there we'll never get it to appear directly in that library panel the reason for that is native instruments has a particular licensing agreement that you have to sign and hand over a lot

of money to do unless you're looking to become a developer and a software company that sells your sample libraries there's not really much of a benefit to this however if you come across to files you can actually go through any kind of hard drive or library and load up any single one so for instance here is a

library that is not connected to my libraries panel and if i double click it it ends in nki so it loads up here underneath so that way once you've got your library you can easily do that you can load it up in the file browser the other option of course is once you have your library built and

designed you can actually just drag and drop any nki file in there that's a native instrument's contact instrument drag and drop that there and you can see it appears nicely there and i can play that one so there's actually a library that i've created for piano book you can actually download that for free if you want to

but we're going to take a look now at diving in and creating our own instrument really quickly though before we do you'll notice that i'm actually using this in standalone if you take a look here i haven't got a door or anything open up behind it it is literally just the contact sampler there's nothing open up behind

here you can develop your library in contact as a standalone app or you can load contact into a software instrument in logic and do it in there or in ableton or pro tools or whatever your door of choices you're not limited and i really love that they do have a standalone app because sometimes you just don't need

the door behind it there's no reason for that however in the later stages as you start to test your library it can be really cool to load up your instrument into a door and double check some features are working things like maybe automation to see if that's working or midi cc control see if they're being recorded in

the door to be able to be played back as well as well as of course if you open it up in a door you can program in your own midi into that region cycle it and just have it play back so if you're really testing something and you wanted to change controls and not worry about playing anything

on a keyboard that could be a great example to have a door open for you instead for now though we'll just continue in the standalone mode there's absolutely no difference to how this is going to develop our library okay so to create a brand new instrument you need to jump up into the little save icon on here

the floppy disk and jump down and go new instrument it's as easy as that at the moment it's just showing you the header but if we open up the spanner this goes behind the instrument into the back end of the instrument in here you have a number of different things you have some instrument options which you can

easily load up if you ever need to we'll be getting into that in chapter three but across here are some other areas that open up and they can be quite important earlier we spoke about samples and zones we'll be loading our first samples into contact sampler in a moment and we'll be doing that in the mapping editor

the mapping editor is where we would load a zone with a sample in and decide where it's going to appear and what keys are going to be playing it and what velocity is going to be playing it the other option of course that we can see up here is group editor so these zones that i put into

this mapping editor will be only in group one and we can create groups two three and so on we can rename the groups do whatever we like with them so we'll be looking at that in more detail next video as well episode 4 we take a look at the wave editor this is where you would see the

sample inside the zone so that's going to become a bit more important in episode 4 when we take a look at looping a sample now we can toggle on and off these as we need so that's really really easy to do now underneath in this section down here this is outside of our group layer and we spoke

before about how there are zones which have the samples in them those zones belong in groups and those groups belong in an instrument this is the instrument layer that we were talking about earlier so these instrument functions and effects and everything affect all of the groups rather than just one group specifically whereas when we're inside the group

editor and doing anything in these boxes for one of the selected groups that is going to be just for the one group that's not going to be for the whole thing and again if we're in the mapping editor and we're editing something there that's just the sample or zone within the group within the larger instrument so some

of these windows are specifically inside certain layers okay so let's drag in our first samples now really quickly i've got a new library that's up here called follow on and that's what the instrument name is going to eventually be and i've got a folder that i've set up with everything that i need inside here documents to plan

different things all the recording sessions we did in chapter one and now the samples are all located in here in here we've got our four sample groups that we're going to be using and i'm going to load this last one first these plugs so i'll double click in here and here are all of my samples my 10

samples from my plugs and what i'm going to do is i'm going to make sure i've got my editor in view behind me i'm going to highlight all of these and i'm going to drag them in now watch as i drag them in because the closer i drag them to the bottom here the less space the zone

will be taking up is in the less keys that they will be taking up as i drag and move my mouse up to here all of this done while holding the drag from my finder they're going to be taking up and spreading out more space now i like to make sure that i've only got them on single

keys and i'll show you why in a moment but let's just drag them in now so i'm going to highlight all of these and let's drag them in so you can see that as i hold at the top you can see the zones starting to form and they're spreading out and then contracting as i bring them down

so i'm going to bring them down right down i don't want to go so far to the bottom because then the bottom is going to just stack them all up but i'll just leave them about there so taking up one instrument each let go and here they are each one of these is an individual zone and if

i open up the wave editor you'll see the sample within each one of those it's slightly different you can see the sample name at the top here changing every time i click on something different and the same up here as well you can see the waveform it's referencing is a little bit different now in chapter one you

would have remembered that we named our samples a very specific way in episode two remember to check back to episode 2 if you weren't sure on how to name your samples all of these being labeled though as the instrument underscore the group that they're going to belong in underscore the key that they were sampled on the note

that was sampled on so when we dive into here and select all of these all of these will be labeled something along those lines this makes it really easy to do the next part and this is why you'll be thanking yourself that you took that extra step earlier on if we jump into edit and jump down to

auto map setup this is going to pick apart the different parts of the name that are separated by the underscores so you can see that like follow on there and then normally there'll be an underscore plus underscore c2 so it's brought it all out now you can use that data to do certain functions so if i wanted

the plux to be the name of the group i could jump in here and go make group name for c2 i can say make root key now this is very important we need to tell contact the sampler what the original note of that sample was if we don't it means that when we play a different key it's

not going to transpose it correctly if i record a c2 but i say that the root note is d2 for example when i actually play d2 it won't be the pitch of d2 because it will be transposing it so you need to say to every one of these zones what the sample root note really was so that's

why it's very easy to do when you've got the name already built into it because you can just say make that the root key now i'm going to take away this i'm going to just ignore it for now i'll rename our group manually what i'm going to do here though is leave it as make root key and

hit apply now when i select a particular note you'll see that the root key has been picked out on the keyboard and that one there c2 should match the name c2 let's check another one just to make sure so this one here is being put onto what's up there g sharp two yep g sharp 2 is there

all done this is another reason why we use sharps and not flats because contact is ready for sharps it knows what sharps are and it can do these sorts of automatic things when you label them as sharps so if you have a g sharp don't label it a flat even if that is chromatically correct or melodically correct

label everything as sharps now right now all of these samples are just grouped together at the bottom we actually now need to spread them out based on their root key so what i'm going to do is another little shortcut i'm going to highlight all of these i'm going to jump into edit i'm going to jump to auto

map functions and there's one in here for auto spread key ranges via root keys what this is going to do is spread out the zones but centering them around your root keys so that way it's going to move that zone to the root key and then just spread out based on what's around it before it runs into

another zone let's take a look at that if i click that now there we go we can see that all of these regions have been spread out now this top one and this bottom one have spread out a long way and i'm actually going to be reducing that because i only want the instrument to go from c2

to c5 now before we could click on some empty space but there's no empty space so i can't deselect any of these so just a little shortcut or a little help if you jump into the edit menu and go deselect all zones now you can click on one okay so let's bring this back to c2 there's two

ways of doing this the first way is to actually just drag on the region itself as i hover on any of these sides we get some arrow markers and i can just drag this one back to c2 nice and easy if i want to do the same thing to this top one i'll show you the other way

is that you can drag it of course which i find a little bit easier but if you know exactly what value you want you can come in here and you can drag this one up and down or you can even double click and go c5 bang there we go really easy okay so now we have some samples

in there let's actually play the keyboard and see if it responds [Music] wonderful we have a sound we have something being played back which is really really cool last thing of course is how do we save this now that we've got our samples and our libraries starting off we now need to save it we need to do

something to make sure that we can come back to this later it's a very straightforward and simple process but there are a few steps involved on a few different options okay if i jump up to the save icon here and i jump in and go save edited instrument it brings it up with a pretty standard save box

and it's gone to my last one ambido library that i created a while back now what i've done here is i've gone into my follow-on instrument i've clicked on the instrument folder and this is where i want to store my instrument now the way that i like to do it is i like to store inside a folder

called contact because then at the end of the day you should be able to just grab the whole contact folder and away you go but i also pop in here instrument development the reason i put it inside instrument development is that i actually save a few different versions as i go as i make significant changes i might

save it as v1 v2 v3 and so on at the very end then i would create my alpha or beta testing or gold master testing and get it ready for sharing or ready for distribution or saving to my hard drive to reuse later and we'll definitely be taking a look at that of course in chapter three where

we go test the library and see what to look out for so now though what i want to do is give it a name and probably score it as a underscore v1 so i jump in here into instrument development and i'm going to go follow on unscore v1 now how i save it is very important thinking again

about how we're traveling at the moment and what we're doing at the moment we're wanting to develop the instrument we're wanting to save it we're wanting to be able to reopen it on this computer theoretically nothing should be changing or moving on this computer and no files should be going anywhere while you're working on this project that's

just a golden rule of thumb of anything everything created to be honest any project that you're working on don't move your files until you're done so in that case when i'm going through the development stages and i'm maybe saving different versions what i might do is save the patch only that will leave all the samples based somewhere

else on my computer which they already are and it won't duplicate the samples therefore taking up more space that way as well as i add more samples i'm not going to have conflicting samples or having to go find and copy more samples in it just keeps a single instrument file and that's all we need for now the

samples as long as i leave them in the same spot will always be found later on though you do want to use patch and samples when you start sharing your instrument you're going to need patch and samples what patch and samples does is it saves the file the instrument file the dot nki but it also saves a

patches file this is really handy because then what you're doing is you're saving all the samples together with an nki and they're not absolute file paths so they can be found no matter where you copy them to as long as the sample folder and the nki file are together in the same folder your computer or any computer

will be able to find the samples for it so really handy when you start sharing your library with others or testing it on other computers for now though as i said i'm just going to pick patch only and hit save on that one so i can come back at any time that's now saved at the top there

we can see that and we're all ready to go the only other one there was monolith monolith saves all the samples and the instrument into one file it's kind of like a zip file but you can still access it this can be handy particularly for testing purposes but when you start scripting and you're getting into custom graphics

it has some major drawbacks so i wouldn't get in a process or a habit of following a monolith file for saving i would save patch only while development leave all your files in place and then the final one when you're starting to test save patch and samples and there we have it so we've become acquainted now with

contact the sampler its structure and what it looks like and some of the features within it you've loaded your first samples created your first instrument and saved it ready for the next lesson so in the next video we're going to dive into additional groups and velocity layers and see how we can make those a part of our

library this is part of a full series with three chapters so do remember to hit that subscribe button so you don't miss out and ding the bell so you get notified on the next one of course if you're looking at this in the future don't forget to head down to the description for the full playlist so don't

forget to subscribe on your way out but otherwise i'll catch you in the next one [Music] you
