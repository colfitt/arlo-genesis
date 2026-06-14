https://www.youtube.com/watch?v=HtLUrMopqPE
The Audio Programmer × Native Instruments · How to build a Kontakt instrument from start to finish · 2024

Hey, what's up, everybody? This is Josh from\h The Audio Programmer, and we're thrilled to\h\h announce this new video series we're doing in\h partnership with Native Instruments on building\h\h your own creative audio tools using Kontakt. If\h you don't know anything about what Kontakt is or\h\h how to get started, this is the perfect video\h for you. In this first

video, we're going to\h\h build our first Kontakt instrument together. I'll\h also provide an overview of the Kontakt platform,\h\h along with a first-look walkthrough of the core\h concepts. And if you don't have any experience\h\h with Kontakt or audio programming in general,\h don't worry. Just follow along with me, and I'll\h\h explain all the important parts along the way. Kontakt

is an industry-leading platform for\h\h creating, playing, and customizing software\h instruments, synths, audio effects, and MIDI\h\h tools used globally by thousands. It's become\h an essential tool for composers, producers,\h\h and sound designers. It's widely used in\h music-making, film scoring, game audio,\h\h and more. It's deep, but it's also accessible, so\h you can start simple and explore more features as\h\h you

progress. Here's a little about the benefits\h of using Kontakt. One: it's easy for beginners and\h\h powerful for experts. One of the biggest benefits\h is that you can get a playable instrument within\h\h minutes, coupled with the flexibility to\h customize deeper as needed. It can be as\h\h easy as dragging and dropping some samples\h into Kontakt, then using Kontakt's extensive,\h\h

high-quality signal processing library as powerful\h building blocks to customize your instrument. This\h\h library includes top-tier effects from throughout\h the NI collection, including RAM, Replika, Reaktor\h\h filters, tape saturation, convolution reverb,\h and much more, all built directly into Kontakt,\h\h eliminating the need for third-party plugins.\h Once you have customized your instrument to your\h\h liking, you can use Kontakt's built-in graphic\h

widgets to design your user interface. As you\h\h look to customize your instrument further, you\h can go deeper with the Kontakt Script Processor\h\h and Komplete UI to give you the flexibility\h you need to bring your vision to life. We'll\h\h be talking more about those later in this video. Two: maintenance-free. Another huge benefit is\h\h that NI handles all the

maintenance for\h Kontakt, so you don't have to worry about\h\h updates and breaking changes. This means that\h you can rest assured knowing that anything you\h\h build will be compatible with all the current\h operating systems, major plug-in standards,\h\h and DAW hosts both now and in the future. Three: release via the Kontakt ecosystem.\h\h Once you've finished building your instrument,\h the

Kontakt ecosystem offers a powerful path\h\h to discovery. Kontakt is used by thousands of\h creators looking for new inspiration. And when you\h\h build with Kontakt, your instrument becomes part\h of this vibrant, creative network. You can release\h\h your product independently, or, if you want to\h reach an even wider audience, apply for Kontakt\h\h Player licensing. More on this later in

the video. Four: extensive support. And if you get stuck,\h\h there are many resources available to help\h you. Along with extensive documentation,\h\h you also have access to the NI forum, NI Slack\h workspace, and community Discord servers as well.\h\h You can easily connect with other Kontakt\h builders and learn from one another.\h Five: hardware integration via the Native\h Kontrol Standard,

or NKS. What if I told you\h\h that you can configure your Kontakt instrument\h to work seamlessly with hardware devices? NKS\h\h allows you to integrate Kontakt instruments with\h NKS-compatible hardware, making it easier for\h\h musicians to interact with your instrument using\h physical controls. This not only enhances the user\h\h experience, but also makes your instrument more\h attractive to a larger

audience. I'll be showing\h\h you how to do this in a separate tutorial. Now, let's dive in and build our first\h\h Kontakt instrument together, explaining\h the key fundamentals along the way.\h Before we dive straight in, I wanted to give you\h a brief overview of a Kontakt instrument. Kontakt\h\h instruments consist of three layers. The first is\h called the Instrument

Editor. This is where we'll\h\h start building our instrument by adding samples\h and creating the playback behavior. This is the\h\h core of what we want our instrument to do. The\h second layer is called Komplete UI. This is Native\h\h Instruments' new visual framework that we'll use\h to create the graphical user interface that people\h\h will see when they're using your

instrument.\h The third layer is called the Kontakt Scripting\h\h Processor, or KSP for short. This is where we'll\h connect controls from our Instrument Editor with\h\h the visual elements that we've created with\h Komplete UI and bring our instrument together.\h Okay, so now we're in Kontakt, and the first thing\h we need to do is create a new Kontakt instrument\h\h by

clicking on File in the menu. The first option\h should be "New Instrument." If that option isn't\h\h available, then Kontakt is in Default View, and\h we need to switch to Classic View. The way you do\h\h this is by clicking on the View menu. The first\h option here allows you to switch between Default\h\h and Classic View. Switch to the

Classic View\h here. Now, when you click on File, you should\h\h see the option for New Instrument. Go ahead\h and click on that. Now you'll be taken to this\h\h new view with your brand-new Kontakt instrument. [Music] Now that we have an overview, we're going\h\h to start off with the Instrument Editor, which\h is the core of our instrument. You

can access\h\h the Instrument Editor by clicking on the wrench\h button here in the top left. In this tutorial,\h\h we're going to create a simple sampler\h instrument from some samples I recorded\h\h from a toy xylophone. If you'd like to follow\h along with me, you can find a link to everything\h\h you need in the video description below. The view

that you see first when you open the\h\h Instrument Editor is the Effects and Modulation\h section. We'll come back to these a little bit\h\h later. Along the top of the Instrument Editor, you\h have five tabs: Instrument Options, Group Editor,\h\h Mapping Editor, Wave Editor, and Script Editor. [Music] Now it's time to dive in and put some\h\h samples into our

instrument. We can do this\h by opening the Mapping Editor section. The\h\h Mapping Editor is where we assign, or map,\h samples to specific keys and velocities on\h\h our keyboard. And before we go forward, let's\h discuss some terminology around key mapping\h\h so we're all speaking the same language.\h A "zone" refers to a sample placement and\h\h what keys and velocities

they apply to. A\h "key map" is a collection of all the zones.\h Now, with that being said, let's talk about\h how to get some samples into Kontakt. First,\h\h let's open the folder with our samples. Here are\h eight samples I've recorded from a toy xylophone.\h\h You can see more on how I recorded the xylophone\h in a separate video

in the video description\h\h below. This is a simple instrument with only\h eight notes that I've recorded at one velocity.\h\h The first note is at a low C and goes up to a\h C one octave higher, without the black notes.\h\h One quick note: notice that all the samples are\h being named using the same naming convention,\h\h which in this

case is number_ name of\h instrument_ note letter and number. You\h\h can use whatever convention you like,\h but the key here is to keep your naming\h\h consistent. This is especially important\h as you start recording larger sample sets.\h Here are the notes: [Laughter]\h\h Now, one thing that I love about the\h flexibility of Kontakt is how you can map\h\h samples

in different ways. I'll show you a few\h different methods that you can use to do this.\h [Music] The first method to key mapping\h is mapping one sample to multiple keys.\h\h Let's take the first sample and drag it from\h the window and hover it over the Mapping Editor,\h\h without dropping it. The highlighted area\h indicates the number of keys

that the sample\h\h will map. As you move the sample up or down\h inside the Mapping Editor window, as you move\h\h it towards the top, Kontakt will map your sample\h across multiple keys and, by default, pitch the\h\h sample up chromatically from the root note of\h the sample. As you hover the sample towards the\h\h bottom of the editor, this

mapping will happen\h for a decreasing number of keys. Let's drop the\h\h sample on note C1 towards the top, where Kontakt\h will map this single sample over about one octave.\h Now that I've dropped the sample, you can\h see the active keys for the instrument\h\h highlighted in blue at the bottom of\h Kontakt. Let's play the active notes.\h As I

mentioned before, Kontakt, by default,\h pitches the sample up chromatically from the\h\h root note of the sample. The yellow box in the\h Mapping Editor is the sample zone. I can change\h\h the number of keys this sample zone applies to\h by moving the edges of the zone left or right.\h\h As I drag the zone to the right, you'll notice\h

that if I play the keys, the pitch gets higher,\h\h but the sound also gets shorter. If I drag the zone out to the left to\h\h cover the lower keys, the sample will get longer. This is because Kontakt needs to play the sample\h\h faster or slower to accurately replicate\h the pitch. The further you are away from\h\h the root

note of the original sample, the less\h quality that you'll hear from the sample itself.\h\h This is something to take into consideration\h when you're creating sample sets. However,\h\h there is a solution for this. In the Source\h section below, we have an option to change\h\h back the playback mode. Currently, the mode is\h DFD, which stands for Direct From Disk.

There are\h\h several playback modes that allow us to retain\h the timing of the sample while pitch-shifting.\h\h I'll talk more about these a little bit later, but\h for now, we'll keep the mode on DFD. By the way,\h\h if I wanted to turn off Kontakt's key tracking, I\h can do it here by turning Tracking off. Now you'll\h\h hear the

same pitch across all keys. Now, let's delete this sample from\h\h Kontakt by clicking on it and pressing Delete. [Music] In the first example, we put one sample\h\h on multiple keys. In this example, we'll assign\h multiple samples to one key. Before we start,\h\h let's go ahead and zoom in a little bit\h on this Mapping Editor for more precise\h\h

editing. You can do that by going to the bottom\h right and pressing the plus arrow. Let's take\h\h sample C1 and drag it onto note C1. Now let's take sample E1 and drop\h\h it onto the same key. If we play this key,\h\h we now have a harmony of C1 and E1. I mentioned\h earlier that changing the zone of

the sample left\h\h or right decreases or increases the active keys\h the zone applies to. But did you know that you\h\h can also change the active velocity mapping of a\h zone by dragging the top and bottom of the zone\h\h up or down? The velocity is how hard you press\h on the key. The heavier the press, the higher\h\h the

velocity, and you can see the velocity from\h the red line that appears when you press a key.\h Let's set sample C1 to trigger for lighter\h velocities and sample E1 for higher velocities.\h Now, when I press the key at a lower velocity,\h you'll hear note C1, and when I press the key\h\h at a higher velocity, you'll hear sample

E1. This\h is handy when you're recording an instrument where\h\h you may need different samples to demonstrate\h different velocities, such as a piano. When you\h\h hit a key softer or harder, the difference in\h the piano is more than the volume. The actual\h\h timbre and sonic characteristic of the piano key\h changes. Kontakt's flexibility to play different\h\h samples based on

velocity gives you the ability to\h create a more expressive and realistic instrument.\h In our first example, we demonstrated one\h sample to multiple keys. In our second example,\h\h we demonstrated multiple samples to one key. And\h in this third example, we're going to demonstrate\h\h multiple samples on multiple keys. What we're\h going to do is drag each sample individually onto\h\h

its corresponding note. Now, one thing that you'll\h notice is that if you look at the note numbers,\h\h we don't have any sharps or flats. So, this is\h only the white notes—none of the black notes\h\h in this scale. So, let's go ahead and drag\h these samples onto the corresponding notes.\h Now, as I mentioned before, we don't have any\h

active notes for these black notes—that is,\h\h the sharps or flats. But one thing that we can\h do here is use Kontakt’s key tracking to help us\h\h fill in those black notes. So, I'll drag out the\h zones of the preceding key so that this entire\h\h octave is filled in with active notes. Now we have our first playable Kontakt\h\h

instrument. [Music]\h\h Now feels like a good time to save our instrument\h to keep our progress safe. Go up to the top menu\h\h to File. Go to “Save Edited Instrument.” Be\h sure not to go down to “Save Multi,” as that's\h\h something different. “Save Edited Instrument.”\h As you can see, there are some options on how\h\h we can save our

instrument. First, there is the\h “Patch Only” option, which will create an .nki\h\h file. This is the file that holds the settings\h and configuration for the Kontakt instrument on\h\h its own. The second option, “Patch + Samples,” is\h the same as the first but also copies the samples\h\h themselves into the same directory as the .nki\h file. The third option,

“Monolith,” embeds the\h\h samples into the .nki file as a monolith file. I personally recommend creating a new folder for\h\h your instrument and choosing “Patch + Samples.”\h So, let's do that now. We'll create a new folder.\h\h Let's call this “Toy Xylo Kontakt.” Now we will save the instrument.\h\h We will call this “Toy Xylo.” What this will do is

create an\h\h .nki file and a separate folder in the same\h directory for your samples, keeping things\h\h organized. The first option of saving the .nki\h file means that you need to relocate the samples\h\h if you move them later, which can be a hassle.\h A monolith packs everything into one .nki file,\h\h which is convenient but limits you from adding

or\h editing samples later. So, I would avoid it unless\h\h you were packaging this as a final product. Now, let's open the folder quickly, and you\h\h can see that we now have the .nki file and a\h new folder where our samples are stored. So,\h\h we can take these original samples and move them\h elsewhere if we wanted to, and

it would not affect\h\h the instrument. [Music]\h\h Before we finish with the Mapping Editor, I\h wanted to talk a little bit about the Source\h\h section. As I mentioned before, this is an area\h where you can Kompletely change the sound of\h\h your instrument just by experimenting with\h this section. This is not exhaustive and is\h\h beyond the scope of this

tutorial, but here are\h just a few of the cool things that you can do.\h As I mentioned before, Kontakt has\h several types of sampling algorithms\h\h that can help you shape and add character to\h your instrument. I'll describe these briefly.\h The first playback mode is the Sampler\h mode. This mode is best for traditional\h\h sampling and probably the best

option\h for our instrument. In our instrument,\h\h we don't have many samples, so these can be loaded\h directly into our RAM for immediate playback.\h The second mode is DFD, which stands for Direct\h From Disk. This refers to streaming directly from\h\h the hard disk drive rather than attempting\h to load your samples into RAM. This is best\h\h for very large

sample sets, such as if you were\h creating a richly sampled 32-gig piano library.\h\h Kontakt is one of the only samplers on the\h market that allows direct-from-disk streaming,\h\h and that's one of the things that has\h made it so powerful over the years.\h The third mode is Wavetable mode. Did you\h know that Kontakt can be used as a wavetable\h\h

synth? Yes, you can load your own wavetables\h into Kontakt and use the wavetable mode to\h\h create your own synthesizer. Some examples of\h libraries that have been made this way include\h\h Conflux, Leap, Analog Dreams, and more. The next four playback modes—Tone Machine,\h\h Time Machines 1, 2, and Pro—all use\h time-stretching algorithms to help keep\h\h the duration of the sample

constant, regardless\h of the pitch of the original sample. So, if you\h\h have an original sample and you're trying to pitch\h it far up or down the key range, then one of these\h\h modes is probably ideal for you. Tone Machine uses\h granular synthesis to accomplish this, while the\h\h Time Machines use other methods. Experiment\h with these to find the

best results for you.\h Beat Machine is ideal for dividing rhythmic loops\h into slices that are mapped to keys, while the\h\h S1200 and MP60 algorithms are designed to keep the\h character and sound of classic vintage samplers.\h You can also use the Tune parameter to tune your\h entire instrument up or down and use the Reverse\h\h button to reverse your

sample sets. As I'm sure you can see, you can go\h\h much deeper with the Mapping Editor, but\h this is designed to help you get started.\h Now, let's make this instrument even\h more amazing using the Group Editor.\h Let's open the Group Editor by clicking on the\h Group Editor tab here at the top. We can also now\h\h close our

Mapping Editor by clicking off of it. Groups are a way that we can batch organize our\h\h samples and customize them. This is how we can\h use Kontakt to build extensive libraries that\h\h use sample groups for different articulations,\h mic positions, velocity layers, and more. As you\h\h can see, we already have Group 1 created for\h us. Let's duplicate Group

1 by right-clicking\h\h on the group and selecting “Duplicate.” When naming your groups, you may want\h\h to consider names that are more intuitive.\h But since we're going to be changing effects\h\h throughout this tutorial, I'm going to keep\h the name simple as Group 1 and Group 2 for now.\h Now, keep in mind that I created\h this group by duplicating

Group 1.\h\h This means that all the samples I had in Group 1\h are now in Group 2. If we had wanted to create a\h\h new group with no samples, we can select “Create\h Empty Group” at the top right of the Group Editor.\h By default, the “Edit All Groups”\h button is currently enabled. This\h\h means everything that I do

for one group\h will apply to all groups. For example,\h\h let's reverse the samples using the\h “Reverse” button in the Source section.\h Now, let's enable “Group Solo” in the Group\h Editor. This allows us to select and audition\h\h one group at a time. We can solo between the\h groups by clicking on the groups themselves.\h Now you'll see that when

I flip back and forth\h between the two groups, they still sound the\h\h same. So here's Group 1, and here's Group\h 2. Now, let's select Group 1, disable the\h\h “Edit All Groups” button, then turn off reverse\h playback. Now we'll play Group 1 and play Group 2,\h\h and we can hear that Group 1 is playing\h forward, and Group 2

is now playing backwards.\h The question is, how can we flip back and\h forth between these groups without the need\h\h to group solo? I'll show you two ways in this\h next section called “Group Start Options.”\h To start, let's unselect “Group\h Solo.” Now, when I play a key,\h\h you'll hear both Group 1 and Group 2—one sample\h will be playing

forward, and the other backward.\h There are a few ways that we can give the\h user the ability to switch between groups.\h\h Let's click on “Group Start Options.” Here are\h the options that we can select from. “Always” is\h\h the option that's currently enabled, where the\h group will always trigger when we press a key.\h “Start on Key.” Here we

can create what is\h called a key switch. This is where we can\h\h press one key to enable Group 1 and a different\h key to enable Group 2. Let's give this a try.\h First, we'll make sure that Group 1 is selected\h and that we have the “Group Start Option” set to\h\h “On Key” selected. Now, key C0 is our

key switch.\h This means that when the user presses key C0,\h\h this will switch to Group 1. We can tell that this\h key switch is active if we look down at the very\h\h bottom of Kontakt, because we see the red key on\h key zero. The red key indicates the key switch.\h Let's do the same for Group 2 with

a different\h key. We will select “Group Start Options,”\h\h “Group Starts on Key.” Now we will change\h this to a different key. Let's make it D0.\h Now this means that when I press C0, that\h this activates Group 1—playing the samples\h\h forward. Now when I press D0, this will\h deactivate Group 1 and enable Group 2,\h\h so the samples should

be playing backwards. [Music] The next option is “Start on Controller.”\h\h This is where we can use a MIDI controller value,\h such as a button press on a MIDI controller,\h\h to achieve the same effect. But we won't\h worry about that for this tutorial.\h “Cycle Round Robins” is the next option.\h Round robin is the name for a technique\h\h that

is normally used to play sounds that have a\h slight variance to give our instrument some life.\h\h There are a number of reasons we may want to do\h this, but one of the most common is to record\h\h multiple samples of an instrument at the same\h key and velocity to prevent a machine-gun type\h\h of effect that comes with playing

the\h same exact sample at rapid succession.\h In our sampler, I only have one sample I\h can trigger when I hit the note C1. But\h\h I could cycle between groups to create some\h variance. To show this, let's have some fun.\h First, let's select Group 1. Then we will change\h “Group Starts” to “Cycle Round Robin.” Let's\h\h keep the “Position

in Round Robin Chain” to\h one—this will become apparent why later on.\h Now, let's switch to Group 2 and switch the\h “Group Starts” option also to “Round Robin.”\h Let's change the “Position in\h Round Robin Chain” to Group 2.\h Now, let's go to the Source section. Bear in\h mind, this is the Source section for Group 2,\h\h because Group 2

is currently selected. Let's\h turn off Reverse. Now, let's turn up the Tuning.\h\h If I press Shift and click, then this will\h do fine tuning. Let's turn it up so we can\h\h hear this effect—we'll turn it up to about 0.4. Now let's press the C1 key. You will hear the\h\h sample play first from Group 1 because that is

in\h Round Robin Chain 1. Now if I press it again, it\h\h will cycle to the other sample from Group 2 with\h the different tuning. Each time you press it, it\h\h will change to the sample from the next group. Now\h you have round robins. This is a predictable way\h\h that we know what sample is going to play next.

For this type of use case, we may want a little\h\h bit more unpredictability. We can do this\h using a variant option called “Cycle Random.”\h\h Let's enable “Cycle Random” for both groups now. This creates the impression of an instrument that\h\h slides in and out of tune. You could take this\h even further by creating more groups with slightly\h\h varying

tunings, cycling randomly between them. The final option, “Slice Trigger,” applies more\h\h to loops and is beyond the scope of this tutorial. Before we move to our next section, let's change\h\h our Group Start Options back to key\h switches. The way that we do this is:\h\h select one of our groups—we'll select Group\h 1—switch it from “Random” to “Start on

Key.”\h\h Make sure that Group 1 is set to switch on\h key C0. Now we'll select Group 2, we'll change\h\h “Group Start Options” from “Random” to “Start on\h Key,” and let's make sure that this is set to D0.\h\h You'll know if you are set up correctly\h if you look at the keyboard at the bottom,\h\h and you have key

switches in red for C0 and D0. Next, we're going to cover the Effects section.\h\h Kontakt has a massive library of\h audio effects that allow us to shape,\h\h enhance, and polish our instruments from within\h Kontakt, without the need for external plugins.\h There are four types of effects. The first is\h the Group Insert Effect. This is an effect that\h\h

we can apply to one or a set of groups. Some\h examples of ways this is typically used include\h\h different articulations, mic positions, or round\h robins. When you apply a group insert effect,\h\h this would not affect other groups. Let's take a look at a quick example\h\h by applying a group effect to Group 2. First,\h I will make sure

that I have Group 2 selected.\h\h Then, I will go to the Group Insert Effect\h section and click “Add Effect.” Let's go\h\h down to LoFi. Now, I will select LoFi. Now we can use our key switches to\h\h change between the unaffected clean sound and a\h bit-crushed LoFi sound. Here is the clean sound...\h And here is Group 2, which

is the LoFi sound. [Music] While I'm here, there are a few other\h\h things to keep in mind in your design. The first\h is that group effects are polyphonic, which means\h\h that the effect is applied per voice, not per\h group output. So, if I press two keys at once,\h\h that means that the LoFi effect is being applied\h per

key, not per group output—just something\h\h to keep in mind. Also, modulators, which we'll\h talk about later, can only be applied to group\h\h effects and not to any other type of effect. Next, let's talk about Instrument Insert\h\h Effects. We can find the Instrument Insert\h Effects section by scrolling down. These\h\h effects apply to the entire instrument.\h Think of them

like a global effects rack.\h\h Some examples of typical usage may be a master\h compressor to unify the sound or a reverb to\h\h apply some space to the entire instrument. Let's apply an instrument effect now.\h\h Scroll down to Reverb and select Raum. While I'm here, one thing that you'll\h\h notice is that options between different types\h of effect groups

may be slightly different.\h\h For example, you'll see if I go back to the\h group effects, that we don't have any options\h\h for reverbs. As we scroll down to look at the\h parameters for Raum, we'll see that we also have\h\h parameters that we can tweak to our liking. Let's go ahead and give it a test. This is\h\h a

little bit too much reverb for me, so I'm\h just going to turn this down to about 30%.\h And now we can hear that this effect\h applies to both Groups 1 and 2.\h The third level of effects in Kontakt\h is the Instrument Send Effects section.\h\h This is an effects chain that is shared across\h all groups, where we can

apply differing amounts\h\h of effects to the groups, or alternatively,\h we can add the send to the instrument level.\h For example, let's say we were making a\h string library. We may want the staccato\h\h strings—that are short—to have less\h reverb than our longer legato strings,\h\h to simulate how our room space might behave. Let's take a look. I'm going to

add a Psyche Delay\h\h effect to the Instrument Send Effects section. One way that we can add this send effect is on\h\h the instrument level via the Instrument\h Effects section. This would affect both\h\h groups. Let's go to “Add Effects,” scroll\h down to “Utilities,” and then “Send Levels.”\h\h Now we have the Psyche Delay as a send\h on the Instrument

Insert Effects section.\h If I wanted to apply this to the group level,\h I can take this off of the Instrument Insert\h\h Effects section and go up to the group level.\h Let's apply more of a Psyche Delay to Group 2,\h\h which is the LoFi group. So once again, on the\h Group Insert Effects section, I scroll down to\h\h “Utilities,”

down to “Send Levels.” And\h now let's test what that sounds like.\h Let's give it a little bit of\h feedback, and let's pitch it up\h\h a little bit. [Music]\h Now, let's apply the same effect to Group\h 1, but we don't want as much of an effect\h\h on this one. So once again, we go down\h to the Group Insert

Effects section,\h\h make sure that Group 1 is selected, and\h now we'll add the effect. Scroll down to\h\h “Utilities,” to “Send Levels.” And what I can\h do is I can turn this effect down so that we\h\h barely hear it. [Music]\h And now we can switch between Group 1 and Group\h 2 to hear the difference—hear how we have a

lot\h\h more delay on Group 2, then back to Group 1, it's\h just very slightly. So, this is a way that we can\h\h take an effect and send it in differing amounts\h to each group to adjust to our tastes and needs.\h Finally, we have the Instrument Main Effect\h section. This is very similar to the Instrument\h\h Insert Effect section,

but think of this more\h like your master bus, where you can apply any\h\h type of final limiting, compression, or EQ. For this example, let's add some Wow and Flutter\h\h to give the instrument a little bit of character. Let's turn up the Wow a little bit.\h This is off. [Music]\h This is on. I'm going to turn\h down the

mix just a little bit.\h Group 2...\h That sounds pretty good to\h me. Let's add a limiter.\h As you can see, we've just touched the surface\h of what we can do with effects within Kontakt.\h\h I invite you to experiment even further with\h these effects to make this instrument your own.\h Now, let's talk about modulators. Modulators\h are a way

that we can control and shape\h\h a parameter over time, making our\h sound more expressive and dynamic.\h Looking at the bottom of our Instrument Editor,\h we can see that we already have one modulator—an\h\h envelope that shapes how our volume fades in and\h out when we press a key. If I change the attack,\h\h it changes the shape of the

sound. [Music]\h Another way that we can apply modulators is\h to group effects. Let's take a look. Let's\h\h scroll up here to our Group Effects section.\h Currently, we're on Group 1. What we can do is\h\h we can add an effect. Let's add a filter. I will\h go to Lowpass, and let's add the Pro 53 filter.\h [Music] So now

we have a filter cutoff,\h\h and let's go ahead and modulate this. What we can\h do is we can right-click, let's select an LFO,\h\h and assign LFO. This means that we can shape the\h filter cutoff over time with the sine wave LFO.\h [Music] Now,\h\h what I can do is I can go down to the bottom. The\h way that

I go down to the bottom is by clicking\h\h this arrow here. This will take me down to the\h bottom, and here I can adjust the sine wave.\h\h Let's make the frequency a little bit faster. [Music]\h That feels better. We can go back up\h to the group by clicking on this arrow,\h\h and here we can change the amount

that we want\h this LFO to affect the filter cutoff as well.\h\h So currently it's at 100. If we switch it down\h to zero, then it doesn't modulate it at all.\h\h So, let's go ahead and put that at 100.\h Let's add a little bit of resonance.\h [Music] That feels pretty good to\h\h me. As you can see, this vastly

changes the shape\h of the sound, and you can get some very creative\h\h effects, especially if I start playing with the\h resonance. Let's do the same to the resonance\h\h but with an enveloperather than an LFO. First, let's right-click on resonance.\h\h Let's select AHDSR envelope. And now... If we turn the resonance down a little bit...\h Now, that's a little

bit too fast for my\h liking. Let's make this a little bit slower.\h So, as you can hear, now I changed the\h attack of that envelope, and now it's\h\h adding resonance that's going over time. These two examples should help give you a\h\h starting point, and there are many others.\h One other note is that the modulation\h\h options will depend

on the effect that you\h select. Experiment and shape your sounds.\h Now we're finished building the core of our\h instrument, and we're ready to move on to building\h\h our own custom user interface using Komplete UI. If you've built instruments in Kontakt before,\h\h you'll know that the user interface\h was traditionally created using KSP,\h\h which stands for Kontakt Script Processor.

This\h meant slicing up bitmap images, managing film\h\h strips, and hard-coding control positions. This approach to UI building still works,\h\h but the evolution of user interfaces and\h high-definition displays has created a need for a\h\h new solution. This solution has now arrived with\h Komplete UI, available in Kontakt 8 and above.\h Komplete UI is a modern UI framework built from\h

the ground up for modern Kontakt instruments.\h\h This replaces the older KSP-based interface\h workflow, which is now considered a legacy\h\h method—still supported, but not\h recommended for new development.\h Komplete UI is designed to make building user\h interfaces faster and easier, while keeping\h\h your instruments looking sharp on modern displays.\h Here are two of the many benefits of Komplete UI:\h One:

Modern, scalable UI design. Komplete UI\h marks a big shift from static graphics to a\h\h fully programmable, dynamic visual system. Now\h you can create responsive, customizable controls\h\h directly in code. No more prepping film strips or\h individual image assets. Whether you're building\h\h a UI programmatically or incorporating custom\h visuals, Komplete UI gives you the flexibility\h\h to work the way that

you want. It supports modern\h vector graphics, including SVG, so your interface\h\h looks crisp on any screen—from standard displays\h to 4K and Retina. And if you still prefer using\h\h traditional assets, Komplete UI supports a\h range of image formats like PNG, JPEG, WEBP,\h\h and TIFF. You're in full control of how your UI\h is built, and it'll look great on

any resolution.\h Two: Clean, modular workflow. Komplete UI\h introduces a clean separation between your\h\h visual interface and the logic that powers your\h instrument. You can use Komplete UI to lay out\h\h your user interface—defining the controls, layout,\h labels, and visual hierarchy. Then, you use KSP to\h\h wire those controls to the underlying instrument\h behavior—controlling filters, envelopes,\h\h playback modes, and more.

This separation makes\h your development process faster, more modular,\h\h and easier to maintain—especially when working as\h part of a team or scaling up to larger projects.\h Now let's dive in, and I'll help\h you get set up with Komplete UI.\h [Music] Before we start, we're going to need\h to do some downloading and setup. This may\h\h look a little daunting

if you're just starting\h out, but don't worry. I'll be taking things\h\h slowly. Just follow along with these easy\h steps, and everything will work out fine.\h The first step is to download Microsoft's\h Visual Studio Code. This is where we'll\h\h be writing our Komplete scripts. It's a free\h download, available for both Windows and Mac,\h\h and I've created some separate

videos on how\h to download and install this, so please see\h\h the video description for more information. Next, download the Komplete UI extension from\h\h the Native Instruments website. The link is\h in the description as well. Think of this\h\h extension as a plugin that will allow us to get\h helpful tools for writing our Komplete scripts,\h\h such as syntax highlighting

and documentation\h when we hover over Komplete UI keywords.\h The third step is to install the Komplete UI\h extension in Visual Studio Code. First, we'll open\h\h up Visual Studio Code, and on the left sidebar, we\h will go to the Extensions tab on the bottom left.\h\h Now we will go to the three dots\h in the top right-hand corner,\h\h and

we will select Install from VSIX. Locate the VSIX extension that you just\h\h downloaded, and click Install. Once this is\h done, you should see a dialog in the bottom\h\h right-hand corner that says "Kompleted installing\h extension." To make sure that this installed\h\h correctly, just search for Komplete in your\h extensions, and you should see Komplete Script.\h The next step is

to return to Kontakt, and\h let's go to the Kontakt Settings by going up\h\h to the top left, clicking on Settings. Now,\h let's go down to the Developer tab. We want\h\h to enable Developer Mode. This option will allow\h for additional logging and making sure that our\h\h images are being updated on the fly and refresh\h automatically as we change

the Komplete script.\h Next, let's set up a resource container for\h our instrument's resources. The resources\h\h are where we'll store any images, scripts, and\h other assets that we create for our instrument\h\h in Kontakt. First, open the Instrument\h Editor, then click Instrument Options.\h\h Then, under Instrument, we want to create a\h Resource Container. Let's set this folder in\h\h our project

folder, “Toy Xylo Kontakt,”\h and we will call this folder Resources.\h Select Save. Now we'll get a dialog that\h says, "Resource folder was not found. Do\h\h you want to create one?" Click Yes. Now\h we should get another dialog that says,\h\h "A resource container was created." Click OK. Now, let's take a look at what happened in our\h\h project folder.

There have been a bunch of new\h files that have been created, but we don't need\h\h to worry about these other files for now. The most\h important thing is in the Resources folder—we have\h\h a folder called Komplete Scripts. This is where\h we will write and store all of our Komplete\h\h scripts that we write with Visual Studio Code. We're

nearly ready to start coding. Let's go to\h\h the Explorer, that's on the top tab on the\h left. Now let's go to File and click Open\h\h Folder. Now we want to navigate to the folder\h where our Komplete scripts will be stored.\h\h So go to our project folder, to Resources,\h then to Komplete Scripts, and select Open.\h In Komplete Scripts,

let's create a new\h file. Click on New File. It's important\h\h that this first file is called main.kScript. This file is called a module. All kScript files\h\h need to be within the Komplete Scripts\h folder within the Resource Container.\h Only one more step and we'll be\h ready to code. Let's go to Kontakt,\h\h to the Instrument Options. In here, you'll

see a\h Komplete UI section where we need to point Kontakt\h\h towards our main module. Go to the folder within\h the main module, and that will open up our Finder,\h\h and we just need to locate the main.k file. Click\h Open, and we're finally ready to start coding.\h Komplete UI is already installed as a\h library that came bundled within

Kontakt.\h\h So now we just need to make some commands\h to interact with it. Let's take a look at\h\h the Komplete UI documentation to find out how. As we can see, there are several libraries that\h\h have come with Komplete UI, and one of those is\h the UI module. Let's go ahead and click in here,\h\h and then click in

Components, and we can see\h different types of components that we can draw\h\h for our user interface. Let's go to the Text\h Component. This displays text on our screen.\h Let's copy this code, and let's paste it into\h our kScript and see if we get some text that says\h\h “Hello World” on our screen. By the way, don't\h forget to

hit Save on your kScript, or else you\h\h may not see any changes on your user interface. Let's close out the Instrument Editor, and now we\h\h can see that we have created our Komplete\h UI user interface that says Hello World.\h Let's take a look at how quickly this refreshes.\h We'll shorten this down to “Hello,” and wow—that\h\h refreshed within

a second or two. So, we can\h see that as we're drawing more components on\h\h our user interface, that we'll get some\h real-time feedback to be able to make\h\h our user interface pixel perfect. Before we move to the next section,\h\h we have one more thing that we should do.\h On the Native Instruments developer website,\h\h they have a set

of Kontakt Controls. These are\h visual components that we would commonly use for a\h\h user interface, like buttons, sliders, and knobs. Let's go ahead and download those. I'll put the\h\h link in the description below. Next, let's\h unzip the folder. Open the folder, and here\h\h we can see that we have some more kScripts.\h These are for visual components such

as knobs,\h\h switches, toggle buttons, sliders, and so on. Since these are kScripts, we need to put them\h\h in the kScript folder that we have in\h our project. Let's open up our project,\h\h go to Resources, Komplete Scripts, and let's take\h Kontakt Controls and put them in with our main.k.\h We'll come back to these a little\h bit later, but

for now, we're done.\h Now that we have Komplete UI set up, we will\h briefly move over to the Kontakt Script Processor,\h\h or KSP for short, to create some parameters\h for our instrument. These parameters—such as\h\h volume or filter cutoff—are the controls\h we want our users to interact with.\h After creating these parameters in KSP, we'll\h return to Komplete UI

to build corresponding\h\h interface elements, such as sliders or\h knobs, and finally connect them to our\h\h parameters for a seamless user experience. [Music] Kontakt Script Processor, or KSP for\h\h short, is Kontakt’s built-in scripting language\h that defines how your instrument responds,\h\h behaves, and performs. Here are just a few\h of the many things you can do with KSP:\h 1. Connect

UI elements to parameters. Use\h KSP to link sliders, knobs, and buttons\h\h to engine parameters like volume,\h filter cutoff, envelope settings,\h\h or anything else your instrument needs to control. 2. MIDI event processing. You can use KSP to\h\h intercept and transform MIDI data on the\h fly—from remapping notes and velocities\h\h to creating custom articulations or\h scripting intelligent note behavior.\h 3.

Customize playback behavior. Create unique\h performance responses—legato transitions, phrase\h\h playback, round robins, randomization, and dynamic\h sample switching—all made possible through KSP.\h 4. Create user interfaces. This may be a\h surprise for new users, but in the past,\h\h KSP was used to build the visual interface\h of Kontakt instruments—placing controls,\h\h assigning images, and laying out panels.\h However, with the introduction of

Komplete UI,\h\h this part of the workflow has moved\h to a more modern and visual design\h\h environment with Komplete UI, leaving\h KSP to focus on behavior and logic.\h Now, let's jump into KSP, and\h I'll show you how to get started.\h The first step to scripting with KSP is\h opening the Script Editor in Kontakt.\h\h The Script Editor is the

last tab in the\h Instrument Editor. Let's open that up.\h Press the Edit button to open up the text editor\h within the Script Editor. As with Komplete UI,\h\h you can use an external text editor to write your\h scripts, but I want to keep this tutorial simple,\h\h so we'll just be writing our script\h right here in Kontakt and referencing\h\h

the KSP manual from the NI website. If we close out the Script Editor and\h\h go back to our instrument, we can see that we have\h a Pro 53 filter that we have assigned to Group 1.\h\h Let's see if we can make the Pro 53 filter cutoff\h a parameter that's controlled by a slider in our\h\h Komplete UI. [Music]\h

I'm going to make this even easier for\h us later on by switching the Pro 53 to\h\h the first effect in our Group Signal Chain.\h Now, let's return back to our Script Editor.\h Here's an overview of what we're going to do.\h First, we'll use KSP and Komplete UI together\h\h to create a slider. Then, we'll figure out how\h to

access the filter cutoff parameter from our\h\h instrument. Finally, we'll use KSP to connect\h the cutoff parameter from the instrument to\h\h the slider, so when we move the slider, it\h changes the filter cutoff in the instrument.\h Before we start writing any code, let's write\h down what we want to do in plain language. This\h\h is a great habit for

any programmer,\h and I use this method all the time.\h Let's think of coding as an event-based recipe.\h It often starts with: “When something happens,\h\h I want something else to happen.” So, based off of this simple logic,\h\h we could start with something like: “When the\h program starts, create a slider called ‘Filter\h\h Cutoff’ between the values of 20 and

20,000.” I\h picked those values because those are the typical\h\h frequency values for a filter cutoff. Then we can say something like: “When\h\h the Filter Cutoff changes, I want to update\h the filter cutoff from the slider value.”\h Now let's do the same process again, but make\h our pseudocode a little bit more codelike. It\h\h may look something like this:

When we start the instrument,\h Create a slider called Filter Cutoff. Use a function like\h\h createSlider("filter_cutoff", 20, 20000) When filter_cutoff changes,\h Update the Pro 53 cutoff parameter\h to match the slider value.\h Now, I will say that I've had the privilege\h of having already worked this out in advance,\h\h so the way this will play out will be\h quite close

to what I put here. However,\h\h I find that this type of thinking out loud\h and writing it down helps me convert my intent\h\h into the code that I'm going to write. With that being said, let's go over to\h\h the KSP documentation and see if we\h can change our intent to actual code.\h As with what I described earlier,

everything\h in KSP is event-based. This means that we need\h\h to describe what we want to happen based on some\h type of change that we see in the instrument. The\h\h way this is done in code is called a callback. Let's take a look at the callback section in\h\h KSP. One thing that I'll say is that it's very\h important

to read the documentation. Many times\h\h there are nuances to be aware of. In this case, we\h can see that any callback needs to start with an\h\h on <callback_name> and end with an end on command. One of the most common callbacks that you'll see\h\h anywhere in coding is when your application\h or your instrument starts. Typically,\h\h this will involve

initializing some\h type of resources and setting values.\h If we take a look at our callback\h list, we can see that we have a\h\h command called on init. Let's take a look at that. As you can see, this is an initialization callback\h\h that is called when an instrument is first loaded.\h What's really nice about this documentation is\h\h that

we have a coding example that we can look to. We have this on init command. Then we have a whole\h\h bunch of code. This can look very daunting,\h but don't worry about any of this. The most\h\h important thing is that we see this end on down\h at the bottom to close out our on init command.\h Let's go

ahead and put that into our code now. All right, here we are back in our script editor.\h\h Let's go ahead and take this pseudocode\h that we made. I'm just going to cut it\h\h out of here and paste it over in this\h text editor here, just so we don't lose\h\h it. And now we're ready to start our code.

So the first thing that we need is on init,\h\h and then right below that, we will put end on.\h Then we will hit apply, and we don't have any\h\h errors, so the script has been updated. So we've\h just written our first KSP code. Congratulations.\h Okay, let's make this do something else now.\h Going back to our pseudocode, we've

now figured\h\h out the "when start" part of this. Let's see if\h we can figure out the "create slider called filter\h\h cutff between 20 and 20,000." Let's go back to our\h documentation. Let's go and search for "slider."\h And we will go to this first result\h called "UI slider." This creates a slider,\h\h and it takes two arguments: the minimum\h

value of the slider and the max value.\h\h What's nice about this example is that we can see\h that there is an on initexample. Let's go ahead\h\h and just take this and copy this into our KSP. The convention here is that everything between\h\h the start of the callback, which is on\h init, and the end of the callback, end

on,\h\h is indented. So let's go ahead, paste that\h there. We're going to change "test" to "filter\h\h cutff slider." It has to have the dollar\h sign before it, so make sure that you keep\h\h that there. I'll just call this "cutoff slider."\h I'm going to change the values to 20 to 20,000.\h So now we have a cutoff slider.\h Let's

go to the next step.\h Now, I know what you may be asking yourself.\h You may be asking yourself why I'm declaring a\h\h UI slider in KSP when I said that Komplete UI was\h responsible for the sliders. And you're partially\h\h right. The only part that I would add is that\h Komplete UI is only responsible for drawing the\h\h slider.

KSP is for describing what the slider\h will actually do—what the minimum and maximum\h\h values are, what parameter it controls, what\h happens when you change the parameter, and so on.\h So think of KSP like the brain of the\h slider. That is what it actually does.\h\h Komplete UI is like the face. That\h is only what you see. In other

words,\h\h you need to declare the slider in both KSP-land\h and in Komplete UI for the slider to fully work.\h Now, the question you may be asking is:\h how does KSP talk to Komplete UI? Well,\h\h there's a special command that we need\h to add here called expose_controls.\h\h Let's go ahead and open the documentation. Expose_controls is a special command

that\h\h makes the UI widgets that I've created in KSP\h accessible as parameters in Komplete UI. This\h\h is the connection point between KSP and Komplete\h UI. You'll see what I mean shortly, but the most\h\h important thing to know for now is just that we\h need this expose_controls command that we can copy\h\h here, and we can paste in our

on init callback. Let's press apply to make sure there are no\h\h errors. And there are no errors,\h so we're good to go for now.\h So let's switch over to the Komplete UI\h documentation to see how to draw a slider. We can\h\h see that slider is part of the Komplete Controls\h package. Let's go ahead and click on that.\h

In the example code for slider, we can see that\h the first command is import slider from Kontakt\h\h controls. If we take a look at the Kontakt\h controls folder that we downloaded earlier,\h\h we can see that we have a slider.kscript.\h This is what this command is referring to.\h The next part, export var main, is just a variable\h that

serves as our insertion point into the\h\h drawing code itself. Then we declare a slider. The\h constructor here in the documentation shows us all\h\h the parameters we can use to customize our slider.\h We can see here that only two are required:\h\h the control ID, which needs to be the same as the\h corresponding KSP control that we created earlier,\h\h

and the label, which is the text that will\h display under the slider that identifies it.\h Let's just copy all of this\h into our KScript for now.\h Taking a look back at our KSP, we see that the\h name of the slider we declared was called cutoff\h\h slider. Let's change my slider to cutoff slider. Let's change the label to

something\h\h more intuitive, like filter cutff. Let's go back to our Kontakt instrument,\h\h and let's close our instrument\h editor. And now we see a slider.\h We notice a few things though. First of all,\h the slider label isn't showing. This is because\h\h the label text is white, but the background\h is also white. Also, the user interface area\h\h is very

small. Let's fix those first. Let's open up the instrument editor,\h\h then go to instrument options. Here we can\h change the canvas size of our instrument.\h\h Let's change the height to 300. We close this. Now\h we close our instrument editor, and now we can see\h\h that our user interface area is much bigger. Now, let's get this label showing.

For this,\h\h I'm going to use a component from our UI module\h called ZStack. ZStack is a component container,\h\h which means that it's able to hold child\h components and stack them on top of each\h\h other. So here we see that we have three\h rectangles. One is stacked on top of the other,\h\h and this is the result down here

at the bottom. So what we want to do is draw a rectangle,\h\h then draw the slider on top of the\h rectangle. Let's go ahead and do that now.\h First, we will import ZStack and Rectangle\h from UI. Next, let's take the slider code\h\h that we created earlier and move it down\h a few lines to make room for our

ZStack.\h\h ZStack is a container, so eventually we're\h going to have the ZStackhold our rectangle,\h\h which is going to draw our background, and\h then the slider on top of the rectangle.\h Next, I've created a ZStack with an open\h bracket and a closed bracket. Everything\h\h we want inside the ZStack is going to be within\h these two brackets. Also notice,

I didn't create\h\h a second export var main. That's because we\h already have one. We only need one export var.\h If we take a look at our user interface,\h we'll see that we don't actually see anything,\h\h including our slider. This is because\h something is wrong. What we need to do\h\h is take the slider and put it inside the

ZStack. Let's copy this code. Let's place it inside the\h\h ZStack, and now we see our slider again.\h Let's go ahead and indent the slider to\h\h make it easy for other people to read. Now we see that we have the ZStack with\h\h the slider inside the ZStack. We need one more\h thing, which is our background. Let's go back

to\h\h the documentation. Let's take this rectangle\h and just copy this for now, paste it inside.\h And now we can see that our background is red,\h and we can see the label filter cutff once again.\h Let's go back into our code. Let's indent\h this and add a space so this is easy to\h\h read. And now we have our

ZStack,\h which draws the rectangle, then draws\h\h the slider directly over top of the rectangle. Let's test out our instrument. As we can hear, the\h\h slider isn't doing anything yet. That is because\h we haven't done the second part of our pseudocode,\h\h which is: when the filter cutff changes, we want\h to update the filter cutoff from the slider value.\h

Let's go ahead and do that now. Let's\h open up our instrument editor. Now,\h\h let's open up our KSP documentation and look for\h another callback that corresponds with what we're\h\h looking for. Let's go to callbacks. If we take a look at our callbacks,\h\h we have one that's called on ui_control. Let's\h take a look at this. The documentation says:

"UI\h\h callback executed whenever the user interacts with\h a particular UI widget." So in this case, we want\h\h that particular UI widget to be our filter cutoff. If we take a look at the documentation a little\h\h bit further down, we see that we have an example\h where it says we use on ui_control. Then we need\h\h to put inside

of the parentheses the\h parameter that we're listening for.\h\h Then we need to end with an end on message. Let's go ahead and do that in our KSP script\h\h now. Here is the command that I've created that\h will listen for changes from the cutoff slider.\h\h We start off with the on ui_control command. Then,\h in parentheses, we put the

UI widget that we're\h\h listening for changes from, which in this case is\h the cutoff slider. Remember to put the dollar sign\h\h in front as well, or else your script won't work\h properly. Then we finish with an end on command.\h Now, we just need to find a way to update\h the filter cutoff parameter with the value\h\h of the

slider. For this part, we need to go to\h the section marked Engine Parameter Commands.\h\h Let's go ahead and open that section now. Now we need a way that we can set the engine\h\h parameter for filter cutff. Let's\h go to the set_engine_parcommand.\h\h As we can see from the documentation, it says that\h set_engine_par will control various Kontakt engine\h\h parameters.

This takes five arguments: 1 The first is the parameter\h\h that we're looking for. 2 The second is the value.\h 3 The third is the group. 4 The fourth is the slot.\h 5 And the fifth is a generic parameter. Let's go through these one at a time.\h\h The first part specifies the parameter by using\h one of the built-in

engine parameter constants.\h\h Let's go ahead and open that up in a separate tab. The engine parameters section contains a list\h\h of all the potential parameters that we\h can access in Kontakt, including all the\h\h parameters for effects and modulators. In the\h drop-down menu here on the left, we can see\h\h that this is divided into sections, including\h filters and

EQs, insert effects, send effects,\h\h modulators, module types, and subtypes. Let's go into filters and EQs, since we're\h\h looking for the filter cutoff. As you can\h see, the first variable, ENGINE_PAR_CUTOFF,\h\h controls the cutoff frequency for all the filters. In my KSP script, I've started the command\h\h set_engine_par and set the first parameter as\h ENGINE_PAR_CUTOFF, that I've found from the

list\h\h of our engine parameters. The second parameter\h is the value to which the parameter needs to\h\h be set. Notice that it says that the range of\h values should be from 0 to 1,000,000. So we\h\h want to get the value from our cutoff slider.\h But the values here go between 20 and 20,000.\h What this means is that we

either need to\h switch the value of the cutoff slider to\h\h go between 0 and 1,000,000, or that we need\h to do some type of math to take the 20 to\h\h 20,000 and scale it up to 0 to 1,000,000. To keep things simple for this tutorial,\h\h I've decided to change the minimum and maximum\h of the cutoff slider to

0 to 1,000,000, rather\h\h than 20 to 20,000. Here, I've set cutoff slider\h as the second parameter within set_engine_par.\h The next parameter is the group. It says the index\h of the group in which the specified parameter\h\h resides. Here, we can see the Pro-53 filter cutoff\h is in group one. The other thing that it says in\h\h the documentation is

that the index needs to be\h zero-based. That means that we start off with\h\h the number zero rather than one. So even though\h this is group one, the index of group one is zero,\h\h and the index of group two is one. It's a little\h confusing to get the hang of at first, but this\h\h is a convention that is

very common within coding. The next parameter is the slot parameter. This is,\h\h once again, a zero-based index of the specified\h parameter. So if we go back to our instrument,\h\h we see that the Pro-53 effect is the first in\h the group insert effects chain. That means that\h\h the index of this effect will, once again, be\h zero, since it

is the first effect in the chain.\h The last parameter is a generic parameter. It says\h that the parameter applies to instrument effects\h\h and internal modulators. Since we're working on a\h group effect, we don't need to worry about this.\h\h Go down to the bottom, and it says: for all\h other applications, set this parameter to -1.\h Now we should

be ready to test out our cutoff\h parameter. Let's go ahead and hit apply, see if\h\h we have any errors. And we have no errors. Let's\h go to our instrument view and test our instrument.\h So now we hear that this filter cutff is working. Let's do one more parameter together, and we'll\h\h go a little bit more quickly this

time.\h We're going to adjust one of the modulators,\h\h which is going to be the LFO that we have attached\h to the filter cutff. Let's see if we can figure\h\h out how to adjust the frequency and make that\h a parameter that's accessible to the user.\h First, we'll declare a UI slider\h in our KSP. We'll call this one LFO\h\h

slider. To keep things simple, I will set the\h minimum and maximum between 0 and 1,000,000.\h Next, I've created another ZStack, where I've\h created a rectangle which is the color red,\h\h and above that, a slider that now has\h the control ID LFO slider to match with\h\h the UI slider that I've declared in\h KSP. I will call this LFO

frequency.\h One problem though—we need something that will\h hold both of our ZStacks. If we go over to our\h\h instrument view, we'll see that we have\h nothing showing in our user interface.\h\h We need some type of UI component where we can put\h the ZStacks together, putting the cutoff slider\h\h at the top and the LFO slider beneath it. Fortunately,

Komplete UI has a solution,\h\h which is VStack. It's a component that arranges\h its children in a vertical line. If we take a\h\h look at the coding example beneath it, we can\h see that there's an example that says "three\h\h rectangles on top of each other." Let's go ahead and implement this.\h First, we will import VStack from UI. Next,

let's\h create a VStack as our parent component. Finally,\h\h let's take the ZStackswhich contain our\h cutoff and LFO sliders. Let's cut them,\h\h and let's put them inside the VStack. Now we see that our UI has updated,\h\h and we now have our filter cutff,\h which is on top of our LFO frequency.\h Now, let's return to KSP and implement a

callback\h that listens for changes in the LFO slider. Next,\h\h we start the command set_engine_par, just as we\h did for the last slider. Now we need the name of\h\h the engine parameter that we want to change. To the left in the drop-down menu,\h\h we see that there is a special section\h for modulation. We find the section\h\h for LFO

modulators and see that there's a\h parameter called ENGINE_PAR_MOD_FREQUENCY.\h The next parameter in set_engine_par is\h the value that we get from our slider.\h Next is the group slot where the engine\h parameter resides. LFO Sine is modifying\h\h our filter cutff in our Pro-53, which is\h inside group one, which means that the\h\h index is zero—the same as our last parameter.

The slot parameter is a little bit different\h\h this time. As you can see from the documentation,\h we need to use a special function for modulators\h\h and modulation intensities called get_mod_idx.\h Let's go ahead and click into this function.\h This returns the slot index of an internal\h modulator or external modulation slot. The first\h\h parameter is the group index. This

is the same as\h the index that we had before, which is index zero,\h\h since the modulator itself is inside group one.\h The second parameter asks for the modulator name.\h For this, we need to go back to the instrument\h itself. Let's go to the modulator, which is this\h\h LFO Sine. We click on this arrow—that\h will take us to

the bottom—and then,\h\h if we right-click on the modulator itself, we can\h see the name, which is LFO SINE, all in capitals.\h\h Let's go ahead and add that to our script. The function call is get_mod_idx.\h\h First parameter is our group, which is zero,\h and the second parameter is the modulator,\h\h which is LFO SINE. Make sure that's in quotes.

We still have one more parameter for our\h\h set_engine_par command. For the last\h parameter, if we wanted to get the\h\h parameter for this modulation amount, we could\h do this using get_target_idx. What we would do\h\h is right-click here, and this would give us\h the name of the parameter, which is LFO1.\h Notice that this is different than if we go\h

down to the bottom and right-click on it,\h\h and we see that the modulator name is LFO\h SINE. So it's very easy to get these two\h\h confused. Make sure that you know which\h parameter that you are trying to modulate.\h For this situation, we just need\h to set this parameter to -1.\h All right, we should be good to give

this a shot.\h Make sure that when you do any changes that you\h\h don't forget to hit the apply button, or else\h your changes won't be reflected in the instrument.\h Let's go to our instrument view. Let's\h go ahead and try our instrument. So we'll\h\h open up the filter, and now we'll\h try the modulation frequency. 🎵\h So we see

that both of these parameters are now\h working. There are many ways this example could\h\h be improved. For example, one of the first things\h I'd probably want to do is scale these parameters\h\h to a more appropriate amount. Currently, both\h of them are going between 0 and 1,000,000,\h\h but this is a simple demonstration that will\h help give you the

building blocks you need\h\h to take your creations even further. Let's use an image to finish off our\h\h user interface here. Komplete UI has an\h Image class that we can use for this. The\h\h first parameter for the image component is an\h image file path relative to the main file. I'll\h\h show you how to find that out right now.

First, we need an image. I'm using this\h\h tap_lo.png as my image. Second, we need to place\h it into our project folder. I'm going to put it\h\h in resources in pictures. Move the logo there. Going back to our documentation, the parameter\h\h is going to be a string that's an image file path\h relative to the main file. By "the

main file," it\h\h means the main.k. If we go back to Komplete\h Scripts, click in there, we see that main.k\h\h is within Komplete Scripts. So we need to find the\h path of the image relative to this main.k script.\h So we will go back a directory, then we will\h go into pictures, and then to tap_lo.png. I'll\h\h show you how

to do this in Komplete UI. First, let's import Image from UI. Next,\h\h I'll make another ZStack that has a red rectangle\h inside of it. You can see how the user interface\h\h has already changed from this new ZStack. Now, we just need to find the file path\h\h relative from main.k. So we will go back\h a directory. In code,

this is normally\h\h denoted by ../, then into the directory\h where our image is, which is in pictures,\h\h and finally, the name of the image itself. Now we see that our logo has now appeared.\h\h However, now that I'm seeing\h my logo, I want to change the\h\h background color. Let's go ahead and do that. We see from the color

documentation that a color\h\h can be specified a few different ways. One way\h is the way that is currently specified, which\h\h is using a hexadecimal integer. Another way that\h this can be specified is using red, green, blue.\h Since this is more intuitive, I'm going\h to use this, and I'm going to go for more\h\h of a gray color. All

right, here's what\h I've come up with. And as you can see,\h\h our logo now has a dark gray background, and\h I've done this using a different version of\h\h color that uses the red, green, and blue as\h parameters rather than a hexadecimal value.\h Congratulations, you've now finished\h your first custom Kontakt instrument.\h\h This is a great accomplishment, and\h I

invite you to share your creations.\h\h I'm curious to see what you've come up with. Before we sign off, I'd like to tell you a little\h\h more about some ways that you can get your Kontakt\h instrument out to the world. Letting others know\h\h about what you've built is just as important\h as the creative process itself, so stick around\h\h

just a little longer, and I'll fill you in. 🎵 When you develop with Kontakt, you're tapping\h\h into one of the largest sampler ecosystems\h in the world. Kontakt has tens of thousands\h\h of active users, ranging from hobbyists\h to professional composers and producers.\h\h By building your instrument in Kontakt, you're\h not just creating a tool—you're making it\h\h available to a

global audience of musicians\h already familiar with Kontakt's workflow.\h Whether you release a commercial library or a\h free instrument, Kontakt gives your creation\h\h instant credibility and accessibility within\h the music production community. You can choose\h\h to release your instrument independently,\h or you can apply to license your product for\h\h Kontakt Player to reach an even wider audience. By licensing your

product for Kontakt Player, you\h\h make it available to both full Kontakt users and\h free Kontakt Player users, drastically increasing\h\h your potential reach. This means your instrument\h can be installed and used by anyone, even if they\h\h haven't purchased the full version of Kontakt. Additionally, Native Instruments offers a partner\h\h program allowing developers to distribute\h their libraries through the NI

ecosystem\h\h and even get featured in Native Access. For\h developers looking to maximize their impact,\h\h Kontakt Player licensing is a game-changer. I hope you enjoyed this deep dive into\h\h creating your first Kontakt instrument. For more\h information on how to get started and connect, be\h\h sure to check out the Native Instruments website\h and the links in the video description

below.\h For now, we're signing off. Happy coding,\h and I look forward to seeing you again soon.
