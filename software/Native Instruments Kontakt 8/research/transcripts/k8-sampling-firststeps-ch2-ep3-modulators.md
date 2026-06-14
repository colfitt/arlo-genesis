https://www.youtube.com/watch?v=ssD_wd20Onk
NI / Steve (FIRST STEPS) · Adding Modulators, ADSR Envelopes, LFOs, Velocity and MIDI CC — KONTAKT: FIRST STEPS (Ch.2 Ep.3) · 2023

hey my name is steve composer engineer and lecturer welcome back to the channel and your first steps into the contact sampler [Music] in the last video we checked out additional groups and we've made use of the velocity layers that we'd recorded now though it's time to take it a little bit further and have a look at modulators

and how they can be used to shape and control our sound let's check it out [Music] all right so what are modulators this might be a very new concept to you if you haven't done anything like synthesis before but if you have done synthesis before this is going to be old hat to you but it's worth a

little bit of a recap so modulators are basically something that can adjust the shape or the tone or adjust an effect or parameter on an effect automatically or triggered when something happens a few examples might be an envelope that shapes the sound so attack decay sustain release that's a form of a modulator another thing could be the

modulation dial on your keyboard there's a reason it's called the modulation dial or the modulation wheel and it's because it controls midi cc which can be used and tied to a modulator in contact as well basically you can think of modulators as changing something like a parameter or a shape of a note over time automatically or triggered

by something this can actually be really powerful and they get more powerful as you experiment with them more and become more familiar with them modulators are what's creating the shape of the note and the release of the note particularly modulators also play a role with pitch like vibrato or pitch bending up and down they change volume they

change dynamic layers they can use lfos like different sort of wavelengths from cyan to rectangle or square or to triangle or something like that or there could be envelopes or external controllers they could be things like midi cc or even velocity modulation is the root of a lot of different libraries it's how the samples play together while

they are in a few places in contact they are mostly concentrated on the group layer so they're mostly used here and that's what we're going to take a look at mostly today let's take a look at a few examples okay so we've got our sounds here we've got our bells and our plugs and what i'm going to

do is i'm just going to focus on the pluck's sound so i'm going to turn my group solo on and my selected groups only so i can see just the plug samples and here only the plucked samples where modulators come in is usually at the group level if we dive down here we can actually already see mod

appearing in a few places let's take a look at this amplifier for example we're going to add an envelope or an attack hole decay sustain release envelope what this does is shapes the sound if you're familiar with subtractive synthesis you know that you can use this to change the transient of the note with the attack and decay

so it comes in slower swells in or hits really hard at the beginning you can also change the release so as you let go of the key how long does it take to die away if i click on mod here we can actually see that one has already been applied and on the first group that you create

inside contact you'll usually get an envelope added there automatically the way that this works is it's attached the type of modifier this envelope to the volume and it is impacting the whole volume range this is just where it's set up though if you actually want to see the modifier it is much further down as we scroll down

to the bottom here is the actual modifier now there's a bit of a quick shortcut if you're never too sure which modifier you're looking at you can press this little button and it will direct you and that yellow box to where the modifier is so you know with confidence that that's definitely the modifier that you're using and

you can see there it's attached to volume so if you're ever unsure just click on that one click that little button and it will point you to the modifier now you can hear at the moment the attack is very hard if i press those hits again those plugs they start straight away but if i increase the attack

let's say to something like a good sort of hundred or so milliseconds you can really start to hear the sound that that's changing you know the attack is slowly coming in or a little bit slower at least let's make that really dramatic let's bring it up quite high let's see about four or five hundred milliseconds quite an

interesting change there now we've got this kind of swelling type sound very different so you can really change the way that this works on all of them now let's put that back to zero and let's jump up to our second group i'm going to select bells now because i've got group solo on and selected groups only i

can only see the selected group zones so that's what these are here and i can only hear the bells [Music] now here there is no modifier added and that is why as soon as i let go of the key you can hear that note sort of snapping off it'd be really nice if there was a bit of

a release to it like it died away so as i let go it took a moment to fade out that's what the envelope could definitely add if we go add modifier i'm going to select envelopes and i'm going to go select my ahdsr that stands for attack hold decay sustain release and i'm going to make sure that

it's set to volume which it is and then jump down to the modifier there it is now that i've got that on there there's a little bit of delay to it now which is great these samples aren't very long they're over pretty quickly so i don't need a huge release time but it not cutting off abruptly is

definitely an improvement the way that this all works is the attack is how fast it goes from zero to a hundred percent volume decay is then how it decays down to the sustain volume and the sustained volume is out of 100 or out of the total volume here so i might want to put that sustain back to

the top so i don't lose any volume i'm just looking for attack and release particularly on simple instruments i really want to just to change the way that it swells in and change the way that it dies away so putting the sustain up to the top will definitely make that happen so then i can roll off the

attack on this one if i want let's have a listen it takes away some of that bite that was there so that could be quite useful now if i just make a dramatic change here to this attack so it's very obvious and now i flick back to plugs and i jump down to this one's modifier you'll notice

the attack is different so if i wanted to hear both of these at the same time let's turn group solo off we're really just hearing the plucks because the plucks are coming immediately in and that attack on the bells is so slow that really not a lot is being heard from the bells at all that's the challenge

of these envelopes is that they are group specific so if i put them on one group i have to put them on all the other groups and i have to change each control individually if i want them to all be the same now in chapter three we're going to definitely take a look at how to tie all

of them together under one knob to make it much easier to control all of them so definitely subscribe for that video because you're going to definitely want to know how to do that okay so that's envelopes they are very very useful but there are other ways that you can modulate your source as well let's take a look

at some of the other common examples if i take a look at this plux group here we actually could see velocity is on one of these already so velocity is attached to volume and this is quite common so that if i actually let's put it up to all the way to zero here if i hit the key

softer so therefore with less velocity it's going to produce a softer quieter note [Music] as i hit it harder it's going to increase the volume let's have a listen i'm going to hit from soft to loud [Music] you can hear the volume increase there so we can build a little bit of a volume change into the way

that we play now this could be quite useful because if you're a piano player you know that hitting the key softer makes a softer sound hitting the key harder makes a louder sound so you want to replicate that with a keyboard this could be the best way to do it the thing is though you'll often see things

like velocity curves on software instruments and that's because the way that it responds is not necessarily linear as in you can't just steadily increase it perfectly if i play something it's taking quite a lot of pressure to get to that very loud sound so i might want to make that easier to get to that loud sound so

it gets louder faster that's where we can use this little shaper box here if i tap on this shaper box and i activate it i've got a linear progression and as i play my notes [Music] you can see that it's going from low velocity to high velocity there along this graph and it's changing the overall volume based

on that if i want to i can bend this a little bit so that as the velocity increases it gets louder faster before it flattens out later let's try that i quite like that that's not too bad i think it's it could definitely use with some fine tuning we'll have to see how it goes but that's actually

created something really useful let me just grab that i'm just going to select it there with the yellow box and hit the delete key or the backspace key that's taken that one away because what i'm going to do now is add a different type of modulator i'm going to choose from external sources which is where our velocity

would have come from but i'm going to choose midi cc this time now midi cc is a wonderful thing that can be used to control different parameters basically all the knobs and dials that you can see and sliders the stuff that's on your keyboards or midi controllers are using midi c to control something basically each one is

set to a particular midi cc channel and then that channel has you know 0 to 127 or 1 to 127 on it it's just like velocity where it's measured in 1 to 127 each cc channel it also has that same range but this time you're saying that the top range might be the top volume and the bottom

range is the bottom volume or you can attach it to pitch or you could attach it to a parameter there's a lot of great features for this midi cc is very useful and if you've done anything with software instruments before you've probably come across it at least from the mod wheel perspective and that's what i'm going to

attach to here the mod wheel on your keyboard is actually usually always attached to midi cc channel one so we can see their midi cc has been selected and this is where i would change my channel one it's already set to one so we're all good to go and it's attached to volume by default which is great

so now if i change my mod wheel have a look at the volume here [Music] now you are seeing the volume dance around a little bit and that's because there are two active modifiers here or modulators here one is the envelope that's shaping it so that's going up to sustain value then releasing as i let go so

that's being shown on the volume control but also the volume change so we got our midi cc there i'm just going to take a way out envelope for a moment so now we'll only be able to control the volume through our midi cc so it's that top volume at the moment [Music] but as i move the mod

wheel [Music] a very different change there so that could be quite useful midi cc just a quick note it can be scripted later and you know most of the time i do prefer to do it later on in scripting i prefer to use my modulators a little bit differently but you can build it into your library if

you want to right now so you're you're basically saying to the library always use mod wheel one for volume now another common little modifier would be pitch bending so pitch bend is not going to be a controlling anything within this amplifier section we can only control the volume or the pan here and you can see that if

we try and add external source pitch bend here i can't select tuning there's nothing there so let's take that out because what we're going to need to do is come up to the modifier up here and add it to the tuner now you can actually see pitch bender's already been added in there which makes it perfectly easy

to use and this part is attached to pitch which is great so if i bend my pitch wheel now we've got something happening there and that could be an exciting little feature if you want to increase the amount let's jump it up let's do the full 12 semitones so really cool feature with that sort of synthy sound

maybe that massive pitch bend might be more useful or more cool otherwise that subtle sort of two semitone bend that you know guitar strings will often do or synthesizers will often do that's in a lot of libraries so that might be just a standard feature to throw into all the groups anyway now this is where you may

want to use the edit all groups feature because let's take a look here at the two groups we've got our bells group here and there's no modifier for pitch bend on our plugs group there is so let's just take that pitch bend away and i'm going to turn on edit all groups by doing that i'm now editing

everything you can see both groups are selected there let's jump down here add in our external sources pitch bend again we're going to turn it up to the full 12 semitones and let's take a look at bells well there it is and that is why the edit all groups button exists it's very important if you want to

make major changes to all groups it saves you some time now normally as i said in a previous episode you want to make sure that that is turned off whenever you're not needing it so straight away now i'm going to turn that one off once i'm finished with it but that button can definitely save you some time

now one last little thing i want to show you the lfos or low frequency oscillators they are waveforms that slowly oscillate below human hearing so we can't hear them as sounds but we can use them as controllers one great example would be tremolo if i wanted to add a little bit of tremolo to my plucks i could

do so using a square wave now if i select plucks and i jump down here and i go into my lfos i'm going to choose rectangle which is just contact's way of calling it a square wave i'm not too sure why they say rectangle wave instead of square wave but there you go i'm going to select that

one there it's going to be attached to volume which is what we want for a tremolo and if i click down here we can see our modulator being added there i can adjust the rate at which this is going and a number of other different things but let's just play some notes and see what happens [Music] you

could hear a little bit of a pulse then it cut out then it came back but these samples again are very very short so we probably want to speed that rate up a little bit so let's jump in here and increase the rate [Music] really cool tremolo effect up here back in the group settings we can actually

change the depth of this so if we don't want it to be as severe if i pull this back a little bit now we've got that's starting to sound quite nice it's quite subtle i think i quite like it might be something i want to do in the final thing who knows now another little note about these

modulators is you can actually modulate the modulator crazy i know if we jump down here and hit mod i can use a modulator to modify one of these controls if i wanted to modify the frequency for example buy another lfo we could let's jump in i'm going to modulate it by the sine wave and here's our modulating

sine wave down here so every second it's going to adjust an amount here so if i play you can see it kind of moving backwards and forwards there increasing the rate decreasing the rate that's quite cool because it had a sort of like type sound to it which is quite nice probably would be more effectual on the

sustained held pad sounds that we sampled but maybe that's something worth investigating later for now that's a detailed look at modulators so now we can begin to shape our sound further with modulators and control more things and they become more powerful as you think of more ways to use them in the next video though we're going to

take a look at how to loop those samples so that we can play them indefinitely it's time to get some sustain to our library on your way out don't forget to subscribe and ding that bell so you get notified when that one drops but until then i'll catch you in the next one [Music] you
