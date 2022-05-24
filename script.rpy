# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define X = Character("...")

define MC = Character("You", color="#a64270")

define JT = Character("Jett", color="#42a669")
define LE = Character("Leroy", color="#9A98B9")
define A = Character("Aaron", color="#6782BD")
define AD = Character("Andrew", color="#BD6D67")
define G = Character("Gregory", color="#B4C990")
define AN = Character("Anna", color="#C9BA90")

define R = Character("Random")
define Both = Character("Both")

# The game starts here.

label start:

    scene out

    play music "audio/bgm1.mp3"

   # Show a background. This uses a placeholder by default, but you can
   # add a file (named either "bg room.png" or "bg room.jpg") to the
   # images directory to show it.
   # This shows a character sprite. A placeholder is used, but you can
   # replace it by adding a file named "eileen happy.png" to the images
   # directory.
   # These display lines of dialogue.

    X "It was a rainy day in X city"

    X "with thunder creeping up now and then, you felt caressed by the soft sound of the rain."

    X "The radio spoke on this rainy day. It spoke of the missing victims around X district."

    X "All of them were women."

    X "All of them were around your age too."

    X "It was said that apparently, some sicko has been targeting women for his own desires."

    X "It is currently unknown of the details behind the kidnappings."

    X "All you know, is that you don't wanna be the next victim."

    X "Lots of other things have been happening too."

    X "People in the area have been reporting strange figures lurking within the fog and shadows."

    X "People have always been scared of these things."

    X "Even when technology was only just born, and during ancient times, people came up with strange mythology to explain these phenomena"

    X "It is possible that these things, if true, are a result of some unholy presence"

    X "But this doesn't sound that scary. Actually, it all sounds made up"

    X "But you care about the people, especially since there are feeble souls who are faint of heart."

    X "These things could be true, but only heaven could tell"

    X "Suddenly..."

    X "You're hungry."

    X "You don't wanna go outside, but you're out of food."

    X "You got up and made the decision."

    X "You ended up going to the convenience store for a noodle cup."

    X "you headed out the door of your apartment and used the elevator to go to floor 1"

    scene lobby

    X "It was very crowded and busy, people were bumping into you, making faces as if it was your fault."

    show placeholder

    R "Hey! Watch it girlie!"

    hide placeholder

    MC "I...!"

    MC "...F-forgive m-m-me!"

    X "Your face got all puffy from the sharp tone of the man and the guilt you experienced. You wished it were less busy today."

    X "Apparently, some celebrity made their way into the building, or you think so"

    X "Regardless, you wanted to get your noodle cup and get back to relaxing in your appartment."

label outside:

    play sound wind fadeout 1

    scene city2

    play music "audio/bgm9.mp3"

    X "You finally made it outside, the air was unusual, as if anything here wasn't mysterious already."

    X "There was this strange fog that seemed to cover up a large majority of the buildings nearby."

    X "You couldn't seem to tell if you were about to get ran over in the road or bump into another person again."

    X "With both fears in mind, you carefully walk through the fog of the city."

    MC "!!!"

    X "You fell"

    X "And even though it happened, you didn't feel the ground."

    X "You saw what seemed to be dark-cocoa-colored hair and a strange fuzzy texture."

    X "It was a man. He was pretty-looking but it was a man."

    show jett blank

    JT "..."

    hide jett blank

    MC "......"

    X "Both of you looked at eachother with emotionless eyes."

    X "Snapping back to your senses you nod a sorry and left to voyage through the fog again."

    X "Talking to people was always a problem for you, ever since a child you were a mute."

    X "You made some friends over your lifetime but the friendships faded away with age."

    X "People don't always stay the same, keeping up with trends is a risk no one should be willing to take."

    X "Unfortunately, it took your friends. It wasn't like you were that close anyway, you were still shy."

    X "Now you stay secluded in your newly renovated apartment with a bed and a tv."

    X "And of course your phone."

    X "Somehow, without getting ran over or bumping into someone, you found the convenience store that sells your favorite items."

    X "The favorite noodle cup you wanted."

    play sound storebell

    X "In the convience store"

    X "While entering the store, a delicious aroma appeared in the air."

    X "It was live food being made in the store, the foods weren't suitable to your liking, fried this and that, but no fried foods you liked."

    X "There was smoothie, slushie, and coffee machines that looked appealing."

    X "But you came for the noodle cup!"

    X "Ending your stay to the store, you paid the cashier and left."

    play music "audio/bgm5.mp3"

    X "Something else didn't leave."

    X "It was the man from earlier.."

    X "standing outside the store..."

    X "You relunctently looked at him...."

    show jett blank

    JT "...."

    JT "......."

    JT "..You know, it's not safe for women like you to be alone like this."

    X "You were confused for a second, but you knew exactly what he meant."

    MC "...I"

    MC "I am aware"

    MC "I was hungry..."

    JT "Hungry?"

    MC "Y-yes..?"

    JT "Hungry..."

    JT "Me too"

    JT "Hey..."

    hide jett blank

    MC "?"

    show jett blank

    JT "Don't worry, you won't be hungry anymore."

    MC "??"

    JT "Because I will stuff you!"

    MC "???"

    JT "Uhh, I mean..."

    JT "Hey, I know this place that sells really nice food. The chef there is a bit younger than average chefs but he is skilled."

    JT "I tried some bread he made and I was satisfied."

    MC "Oh..."

    MC "Hey.."

    MC "Will there be... people?"

    JT "Probably"

    MC ":["

    JT "Oh.."

    JT "Don't worry, you won't be afraid there."

    MC "????"

    JT "Because I will protect you!"

    MC "Oh!"

    JT "I am...going to follow you for a bit, if you don't mind."

    MC "I am very confused"

    JT "There's no need to be, I won't hurt you."

    MC "H-how...do I know for sure?"

    JT "Because I know the guy behind the kidnappings. Personally."

    play music "audio/bgm11.mp3"

    hide jett blank

    MC "Oh...Uhmm"

    show jett blank

    JT "I know that's not a good thing to hear..."

    X "You felt worried, you didn't know this man, and he just invited you to a lunch from nowhere."

    X "And he knows the man terrorizing women
."
    JT "I...want to know your name!"

    JT "..."

    JT "Oh"

    JT "My name is Jett"

    MC "Oh um, My name is -"

    JT "Hmm?"

    MC "Uhm"

    play music "audio/bgm8.mp3"

    JT "There's a few others in the mansion. The owner there is named Aaron."

    JT "He is a little strict but he just wants to see the best in everyone."

    JT "It's hard now considering that the world is different than it used to be."

    hide jett blank

    MC "Yeah...I can tell"

    MC "I miss the older days when people were more logical and had heart"

    MC "I can't do anything like I used to without feeling like someone will treat me like I don't matter"

    MC "Or people just acting like absolute fools of themselves and putting their foolishness towards others"

    show jett blank

    JT "They want to make you feel like your nothing but trash..."

    MC "And as long as we exist within their radius..."

    Both "Then they'll treat us awfully"

    JT "I feel...a sense of familiarity"

    MC "Hm?"

    JT "Even if I don't know you, I would like to"

    JT "So..."

    JT "Would you like to go to the mansion?"

label mansion choice:

    hide jett blank

    menu:

        "Sure":
            jump choice1_yes

        "I'll think about it":
            jump choice1_no

    label choice1_yes:

        $ menu_flag = True

        JT "Ok, I'll lead the way"

        MC "Wait"

        JT "?"

        MC "I would like to, but I need to grab some essentials"

        JT "Alright, you know where to find me"

        MC "Actually-"

        JT "See you later!"

        X "Jett walks away into the fog"

        jump choice1_done

    label choice1_no:

        $ menu_flag = False

        show jett blank

        JT "It's ok if you aren't ready, I know you would need time to think this out"

        MC "So..then what happens when I decide to go with you?"

        JT "I would find you"

        JT "And you would find me"

        MC "Huh...?"

        JT ":)"

        hide jett blank

        jump choice1_done

    label choice1_done:

        # ... the game continues here.

    X "You seem to have a connection with Jett, he seems to understand you unlike most people"

    X "Even though you haven't really talked to him because of your shyness, you can tell that you connect with him on a different level."

    play music "audio/bgm4.mp3"

    scene city2
    with Dissolve(.5)

    scene black

label outside:

    X "-The next day-"

    scene city2

    show andrew blank:
        xalign 0.25
        yalign 1.0

    AD "It's always so foggy here, can't ever see nothin'"

    show gregory blank:
        xalign 0.75
        yalign 1.0

    G "Maybe choose another city to explore in then"

    AD "Ah whatever"

    G "But I get what you mean, I can't see anything either"

    G "I read a little about this city, there's some rumors that something lurks within the fog"

    AD "Sounds like made up crud!"

    AD "Greggie, you don't really believe in stuff like that, do you?"

    show gregory blank:
        xalign 5.0
        yalign 1.0

    G "I told you to stop calling me that, and anyway to answer your question..."

    G "I'll believe it when I see it"

    show andrew blank:
        xalign 0.25
        yalign 1.0

    show gregory blank:
        xalign 0.75
        yalign 1.0

    AD "Ehh, good enough for a answer for me!"

    G "I don't have to follow you always you know? I have my own view on things"

    G "The stuff I read about is really-"

    hide andrew blank

    hide gregory blank

    LE "Oi!"

    show gregory blank

    G "!"

    X "There was a strange man hidden through the fog, he was a little taller than Andrew and Gregory"

    show andrew blank

    AD "You shaky punk, he just can't see us, that's all"

    hide andrew

    LE "Are you stupid? or deaf? Answer me!"

    G "Are you impatient and rude? Almost gave me a heart attack!"

    AD "sigh..."

    show leroy blank

    LE "Sorry bout' that!"

    LE "I just wanted to know if you too were...human"

    show andrew blank

    AD "Were human alright"

    G "Wait, there's non-human things here?!"

    LE "Oh there's all sorts of things here"

    AD "If this is another attempt to spook my friend, it's working, but I prohbit you from continuing any further"

    LE "What are you gonna do about it?"

    AD "..."

    G "...!"

    AD "I'll whoop you visible through the fog!"

    LE "Heh, no need for that"

    X "The strange man jumps from the roof of a short buliding nearby"

    LE "How do you do, friends?"

    AD "We are not friends with you! And just because I can see you clearly doesn't mean I won't still beat you blue!"

    LE "If a battle is what you desire, I will give you one"

    AD "Bring it on!"

    hide andrew

    scene black

    play music "audio/bgm13.mp3"

    X "The strange man quickly disposed of Gregory and Andrew"

    play music "audio/bgm12.mp3"

    scene city2
    with Dissolve(.5)

    scene out

label room:

    X "You thought about what Jett had said before"

    X "He seems to be your only friend at this moment"

    MC "..."

    MC "I think..."

    MC "I think I'll go to the mansion"

    MC "But I don't know the address..."

    MC "He said we'll find eachother"

    MC "What if he was lying?"

    MC "Last time I trusted a boy..."

    MC "It.. didn't end well"

    MC "..."

    MC "I don't think I want to remember that..."

    MC "Hm... But I want to go to the mansion and eat tasty bread"

    MC "That is, if Jett is real and telling the truth"

    X "You were about to get up to use the bathroom"

    X "When..."

    MC "A text?"

    MC "This must be the address"

    MC "It seems far though"

    MC "If this is Jett, I will save the contact"

    MC "Hmm.."

    MC "I don't have a car...Oh well"

    MC "Without getting lost, I will go and find the mansion"

    X "You packed your stuff and you went out again"

    scene black
    with Dissolve(.5)

    play music "audio/bgm9.mp3"

    scene city2

    MC "It seems quiet again, I don't like this feeling"

    MC "I guess I will look at the address again"

    MC "Oh?"

    play music "audio/bgm7.mp3"

    AD "Ergh!"

    G "Erf!"

    X "You saw two men lying in distress on the ground, there was no fatal injuries that you could see"

    X "But you knew they were in pain"

    AD "Who was that guy???"

    G "What guy?"

    AD "Yeah...maybe it was our imagination"

    AD "..."

    AD "......"

    AD "You idiot!"

    AD "That tall guy!"

    G "I- Oh!"

    G "That guy! I don't know where he went"

    AD "Dangit!!"

    AD "Heh, I know that once I do find him, It'll be his end!"

    G "You're not gonna kill him, are you?"

    AD "Nah! Come on Greggie, you know how I do things!"

    G "Which is exactly why my feelings of regret from coming here orbit more than my feelings of physical pain"

    AD "Sigh..."

    play music "audio/bgm8.mp3"

    G "Hey, is that a woman?"

    AD "She has hair and wears pink, why wouldn't that be a girlie?"

    G "I- You know what I mean! I think it's unusual to find normal people here, especially a girl."

    G "I thought everyone was too scared to come out"

    AD "Sorry, my friend here has never seen a female before. I am Andrew"

    AD "And sorry for not introducing ourselves earlier"

    AD "We came to this city to find something"

    AD "And this 'something' requires going to some sort of mansion"

    MC "Oh, uh..."

    MC "I umm, am also going to a mansion..."

    G "Andrew, I think she is shy"

    AD "Yeah I can see that"

    AD "Don't strain yourself, missy-miss. I won't pressure you into talking or anything"

    MC "Oh, I am ok"

    MC "But do you know where this mansion is?"

    X "You show them the address you were sent"

    AD "Uhh.."

    AD "Greggie, you're good with those numbers and words! Where is this place?"

    G "If I am correct, this is the same place we're going to"

    AD "Really...?"

    G "Yeah, it is"

    MC "Then...Could I go with you two?"

    X "Andrew and Gregory looked at eachother with a questionable look, Gregory made indirect eye contact"

    MC "I can't see through the fog and...I don't think I want to go alone"

    MC "You two are the second person(s) to tell me it is unsafe outside"

    MC "I am aware that there is a strange man hurting women located somewhere in this city"

    G "Yeah, it probably isn't safe out here"

    AD "Sure you can come with us! Any woman is a queen in my eyes!"

    G "Hmm..."

    AD "What?"

    G "Sounds like something you wouldn't normally say"

    AD "Err- First impressions..!"

    MC "I think the mansion is that way"

    AD "Oh yeah, let's go!"

    G "To the mansion!"

    X "You smile calmly at Andrew and Gregory"

    X "You all went to find the mansion"

    scene black dissolve(0.5)

    play music "audio/bgm14.mp3"

    scene forest

    X "it was over noon"

    X "You, Andrew, and Gregory were trying to find the mansion"

    x "The address was very odd placed and sounded unfamilar to the usual street addresses"

    x "You grew concered but Andrew and Gregory were calm"

    MC "Hey...do you guys really know where the mansion is?"

    G "I am sure with enough time and diligence, we will be able to find it"

    MC "Oh, because I am not used to these coordinates..."

    AD "Just leave it to Greggie, he knows this stuff really well!"

    MC "A-alright..."

    scene forest2

    G "I think it's up ahead"

    AD "Really? How far?"

    G "I just said that it was up ahe-"

    AD "Look!"

    MC "It's beautiful...!"

    MC "And that also means that Jett wasn't lying either, at least I hope not"

    MC "It may look pretty on the outside but who knows what is behind those doors..."

    scene mansion door

    AD "Yeah"

    AD "Say though, who is Jett?"

    G "A friend?"

    MC "Jett is my new friend, he told me to come here to this mansion"

    MC "He also said that a man named Aaron owns it"

    AD "You know, The mansion and coordinates are real.."

    AD "But Miss, don't go and trust any ol' buster that says to go to some mansion"

    MC "I am aware to not to trust strangers"

    G "You act like as if you're her father or something...Sheesh!"

    AD "I just-"

    AD "It's really, really, not safe out here..."

    AD "I met a woman around here earlier, and next thing I know is that she is on the news!"

    AD "I especielly don't wanna be falsely accused as being the guy who's commited those crimes"

    AD "Because Gregory wasn't here with me when this happened"

    G "I've been around you all day!"

    AD "That's how fast it happened"

    MC "I'm sorry Andrew If you feel I am accusing of something or being a burden...."

    AD "..."

    AD "....."

    AD "Hahaha! You are definitely a different kind of breed!"

    MC "??"

    G "Uh, don't mind him"

    G "Anyway, the mansion! Let's...knock on the doors? I guess?"

    X "You all attempted to knock on the door to the mansion"

    x "..."

    X "There was no answer.."

    X "You all stood for a few moments"

    X "The door opened"

    play music "audio/bgm19.mp3"

    X "There was a blonde hair man guarding the doors, he had a strained look on his face"

    A "Hmm?"

    MC "H-hello?"

    MC "We were looking for the owner of this mansion?"

    A "I'm right here!"

    X "The man's strained look had changed to a friendly one"

    A "I'm sure you all are Jett's aquaintence's?"

    AD "That name keeps popping up again and again..."

    A "Jett is.."

    A "Someone who helps maintain this place"

    G "Are you guys the ones who clean out homes so someone else can move in?"

    A "N-no"

    A "I own this place by my birthright!"

    X "You, Andrew, and Gregory looked at eachother with strange looks"

    A "Uh"

    A "Anyway, come in! It's nice and there are places to sit"

    X "You all went in the mansion, there was no sign of Jett but you are happy to know all this is real and happening"

    G "It's cold in here..."

    A "..."

    A "...We keep it that way"

    AD "Really now?"

    A "Yeah"

    A "Any concerns?"

    AD "..."

    A "I thought so"
