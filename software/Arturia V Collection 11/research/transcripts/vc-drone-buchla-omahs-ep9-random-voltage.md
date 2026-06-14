https://www.youtube.com/watch?v=37gVT8RHV0E
One Man And His Songs · Arturia Buchla Easel V Tutorial Ep#9 - Random Voltage & MIDI Connections · 2021-01-28

hello and welcome back to the buckle easel tutorial series today we're going to deal with uh all of 
the interface elements that we haven't dealt with in the primary um control panel let's start with 
the midi connections these are all pretty straightforward so we can whistle through these velocity 
allows us to play a really soft note and a really loud note level and then the increased velocity 
adds a modulation amount to that pitch don't forget these control inputs are basically how much 
more do we add on to our base starting position that's what we're really doing when we move this 
slider modulation wheel is similarly simple there's my wheel going up and here's my wheel coming 
back down obviously i'm doing all of this on pitch there's my modulation wheel at the top and then 
coming back down and finally key follow now key follow is quite shallow this is the only one of the 
three that i think it's really worth spending any time talking about because we want to know how 
much of an effect um this output jack is having well it turns out to be roughly equivalent to about 
a semitone per octave so we've just got this tone humming away in the background now with no 
modulation sources on it whatsoever and having just played a c1 on the keyboard that's the output 
that's the control voltage currently being output by this key follow jack and that turns out to 
increase the pitch of the tone by just over a semitone it's kind of a sharp d flat if i now uh 
press c2 so c2 is the natural tone there it is drop the key follow modulation back in and now we're 
about two two and a half semitones another octave up and we're now like three three and a half 
semitones as c4 again naturally there's your standard bass c4 drop your key following you're up to 
about five flat semitones and then finally there's uh about six semitones it never really occurred 
to me to do it but you could probably figure out the total octave span to uh to have the key follow 
increase the control voltage by exactly one octave it might it might be 10. finally we've got our 
random voltage generator i've just set it to keyboard mode to start the uh the demonstration with 
we've got four different output sockets now each one of these different output sockets generates a 
different random control voltage every time it's triggered they'll trigger at the same time but 
they generate a different random voltage and you can use that for different modules so let's start 
off nice and simple here's our base c tone and as i increase my modulation i'm going to get a 
random sound random tone random amount of modulation every time i press a key on the keyboard i'm 
pressing c2 here each time so the note that we're here is never going to be lower than c2 because 
the modulation effect is always adding to the current baseline control voltage and with a setting 
round about here our range is going to go from c2 to c3 so that's the highest highest of the notes 
that's all very well and good for static like keyboard generated random voltages but things get 
more interesting when we bring some kind of cycling process in so if i turn it into pulsar instead 
now every time the pulsar triggers fires we're going to get a different random voltage and what 
it's really cool to do is take two outputs from the same socket send one through the inverter and 
now we've got the two different oscillators playing in opposite directions they're always playing 
random voltages now the pulsar and the sequencer as far as the random voltage generator are 
concerned are just delivery mechanisms they're just firing the random voltage generator so both of 
these things currently being sent to pulsar there's no difference there it's stuck again now i take 
over the process by pressing my put keys in the sequencer it's like torture isn't it are actually 
having the same effect the reason why we've got two different controls obviously they can be timed 
differently at the moment the sequential the the sequence is taking its timing off the pulsar but 
it doesn't need to if we fire that off the clock instead and make the clock really fast and the 
pulse is still doing its thing and the sequencer is doing its thing finally the purple output 
sockets the word press gives you some clues to what these are these are poly pressure so if i take 
an output from one of these and get my note going so there's a regular c3 and press into the key 
just about up to the next c so it's basically operating at the same range as the envelope generator 
gates are is basically like a 1 volt equivalent when the when the poly pressure gate is fully open 
so short and sweet one for you today and that's that section dealt with in the next video we'll 
deal with the keyboard section and that will be the all of the controls of the primary interface 
done hope you'll join me then thanks very much for watching 