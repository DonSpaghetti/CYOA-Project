# Hierarchy:
#
# Map
# Engine
# Scene
#     Death
#     Scene 0: That Time I Got Reincarnated as a Self-Aware Trope
#     Scene 1: The Jungle and The Poop Monkey
#     Scene 2: Answer Some Riddles and Get a COOL SWORD!
#     Scene 3: The Demon Chicken
#     Scene 4: Shokugeki at High Noon (or, The Perfect Breakfast Taco)
#     Scene 5: END-TANKS FOR NOTHING
#     Scene 6: END-For The Good of The Realm
#     Scene 7: END-(as Nick Frost): "Pub?"

from sys import exit
from random import randint
from textwrap import dedent

status = []
inventory = ['hopes and dreams']
bar = '|X X X X X|'


class Scene(object):
    def enter(self):
        print("This is a class that establishes the framework for our scenes.")
        print("We'll use it to ENTER scenes by calling this method.")
        print("Then, the engine will bring up the scene we want, according to the map!")
        print("At least, I think that's how it works.")
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Death(Scene):
    def enter(self):
        print("You die! There is nothing but the void to greet you this time.")
        exit(1)


class Reincarnate(Scene):
    def enter(self):
        print(dedent("""
            You led a boring life! One day, you were killed by a falling coconut. It wasn't even organic.
            Damn GMO coconuts! You wake up in a dark, mist-filled chamber. 
            
            
            A deity appears before you, and says you get one more chance - just one. 
            If you die again, it can't be bothered with you."""))

        status.append('reincarnated')
        print(f"Your status is {status}.")
        status.pop(0)
        print(f"Your health is {bar}.")
        print(f"Your inventory is {inventory}.")
        return 'jungle'


class Jungle(Scene):
    def enter(self):
        print(dedent("""
            ...The mist parts in front of you to reveal a rough dirt path through a lush jungle. 
            You hear faint, girlish laughter in the distance. As you step into this new world and walk along the path,
            a monkey flings poo at your head.
            """))
        if randint(1, 20) >= 12:
            print(dedent("""He hits! You are covered in poo. Gross!"""))
            status.append('poo')
            print(f"Your status is {status}.")
            health = bar[0:8]+'  |'
            print(f"Your health is {health}.")
            inventory.remove('hopes and dreams')
            print(f'You have lost your hopes and dreams. Your inventory is {inventory}.')

        else:
            print("He misses, screeches, and runs off. What a jerk!")

        return 'jungle2'


class JungleTwo(Scene):

    def enter(self):

        if 'poo' in status:
            print(dedent("""
                After walking further down the jungle path, you come across an ancient tree surrounded by dozens
            of orbiting lights. One of these lights rushes to greet you with a giggle. As it draws near, you
            notice it's a tiny, glowing fairy. However, it takes one whiff of you, runs away, and hides. It wants
            nothing to do with you! You stink of monkey poop.
            
            
            You continue through the forest, finding a river to clean yourself up in.
            You are no longer covered in poo. Eventually, you find your way out and come to the nearest town."""))
            status.remove('poo')

            return 'chicken'

        else:

            print(dedent("""
                After walking further down the jungle path, you come across an ancient tree surrounded by dozens
                of orbiting lights. One of these lights rushes to greet you with a giggle. 
                
                
                As it draws near, you notice it's a tiny, glowing fairy. 
                "HUMAN, MY NAME...STEVE. WELCOME BIG TREE LAND!" it bellows ungracefully. "YOU WANT ADVENTURE NOW? 
                HURR HURR, EAT BERRY FROM TREE." You walk up and notice a purple berry hanging delicately from 
                a low branch. Do you eat it?"""))

            action = input("> ")

            if action.lower() == 'yes':
                print(dedent("""You shrink! Tiny human!!!"""))
                status.append('TINY!')
                print(f"Your status is {status}.")
                return 'riddles'

            elif action.lower() == 'no':
                print(dedent("""Steve laughs and says "TAKE CHANCE WITH MONKEY THEN!" You are shown back to the path. 
                """))

                return 'jungle3'


class JungleThree(Scene):
    def enter(self):
        if randint(1, 10) <= 8:

            print(dedent("""You find a banana tree. Pick bananas?"""))

            action = input("> ")
            if action.lower() == 'yes':
                print(dedent("""Okay! How many? The tree is full of bananas, but you figure you can only carry up to 5.
                Maybe 6, if you're adventurous. ( ͡° ͜ʖ ͡°)."""))
                action = input("> ")
                if action.lower() <= '5':
                    print("You pick " + action + " bananas!")
                    inventory.append(action + ' bananas')
                    print(f"Your inventory is {inventory}.")

                    return 'junglefinal'

                elif action.lower() == '6':
                    print(dedent("""You pick 5 bananas, and store them in your pockets. 
                    
                        The sixth banana, you manage
                        to stuff down the front of your pants, like a pistol. Banana Gunslinger! Where did you think
                        it was gonna go!?"""))
                    inventory.append('5 bananas' + 'Gun-nana')
                    print(f"Your inventory is {inventory}.")

                    return 'junglefinal'

                elif action.lower() > '5':
                    print("You picked too many bananas! Some drop to the floor, because you can only carry 5.")
                    inventory.append('5 bananas')
                    print(f"Your inventory is {inventory}.")

                    return 'junglefinal'

                else:
                    print("Please enter a number!")
                    return 'jungle3'

            elif action.lower() == 'no':
                print("You continue through the jungle, not picking any bananas.")
                return 'junglefinal'

            else:
                print("Please choose yes or no!")

                return 'jungle3'


# TODO fix banana system below


class JungleFinal(Scene):
    def enter(self):
        print(dedent("""
            The monkey waits for you near the end of the jungle. He holds a rock menacingly. What would you like to do?
            You can try to FIGHT, PERSUADE, or ATTEMPT A BRIBE."""))

        action = input("> ")

        if action.lower() == 'fight':

            print("You fight! He gets in a few hits, but eventually routs after you deliver a right hook.")
            health = bar[0:8] + '  |'
            print(f"Your health is {health}")

            return 'chicken'

        elif action.lower() == 'persuade':

            print("You attempt to reason with the monkey. He doesn't understand, and hits you with the rock.")

            return 'death'

        elif action.lower() == 'attempt a bribe':
            if '1 bananas' or '2 bananas' or '3 bananas' or '4 bananas' or '5 bananas' in inventory:
                print("You bribe it with your bananas, and are able to pass!")

                return 'chicken'
            else:
                print(dedent("""You have nothing to bribe with! Monkey throws the rock at you while you rummage in
            your pockets."""))

                return 'death'

        else:

            print("Please choose to FIGHT, PERSUADE, or ATTEMPT A BRIBE.")

            return 'junglefinal'


class Tree(Scene):
    def enter(self):
        print(dedent("""
            You shrink down to the size of a thimble, and are dragged inside the tree by the fairies. Time for some
            riddles! Riddle 1 - Not chest or box is now discussed. Money can be held in it, but within it 
            there is rust."""))
        action = input("> ")

        if action.lower() == 'trust':
            print("Very good! Riddle 2 - Feed me and I live, give me to drink and I die. What am I?")
            action = input("> ")

            if action.lower() == 'fire':
                print(dedent("""
                    VERY GOOD INDEED! Last riddle - I pass before the sun, yet make no shadow. What am I?"""))
                action = input("> ")

                if action.lower() == 'wind':
                    print("CONGRATULATIONS YOU GET A COOL SWORD!!!")
                    inventory.append('COOL SWORD')
                    print(f"Your inventory is: {inventory}.")

                    return 'chicken'

                elif action.lower() == 'the wind':
                    print("CONGRATULATIONS YOU GET A COOL SWORD!!!")
                    inventory.append('COOL SWORD')
                    print(f"Your inventory is: {inventory}.")
                    status.remove('TINY!')

                    return 'chicken'

                else:
                    print(dedent("""
                        Incorrect! But as Meat Loaf says: 'Two outta three ain't bad' - so the fairies
                        let you live, and you escape the jungle alive, but empty handed. Eventually, you arrive in 
                        a small but friendly town. Perhaps too friendly..."""))
                    status.remove('TINY!')
                    return 'chicken'

            else:
                print("Incorrect! The fairies devour you. Steve have full belly this day! Hurr.")
                return 'death'

        else:
            print("Incorrect! The fairies devour you. Steve have full belly this day! Hurr.")
            return 'death'

# NEEDS WORK BELOW TO INCORPORATE COMBAT SYSTEM


class DemonChicken(Scene):
    def enter(self):
        print(dedent("""
            You pass a chicken in town. Something strikes you as odd about it, so you turn around and glance back.
            It returns your glance with a glowing red eye, menacing you with its gaze. Fight it?"""))
        action = input("> ")

        if action.lower() == 'yes' and 'COOL SWORD' in inventory:
            print(dedent("""
                You lop the demon chicken's head off with your COOL SWORD! Unfortunately, the town turns out to be
                full of evil cultists, and you've killed their mascot. They challenge you to a cooking contest."""))
            return 'chopped'
        elif action.lower() == 'yes' and 'COOL SWORD' not in inventory:
            print("You fight the chicken bare handed and lose!")
            return 'death'
        elif action.lower() == 'no':
            print("You decide not to fight the demon chicken.")
            return 'pub'

        else:
            print("Please answer yes or no.")
            return 'chicken'


class Shokugeki(Scene):
    def enter(self):
        print(dedent("""
            A horrified onlooker screams "THEY'VE KILLED CHARLES!!!" and an alarm is raised. The sheriff arrests you,
            and informs you that your trial will consist of a cooking contest in the morning. After a cold, damp
            night in jail, you awake and are led out into the town square, where the local Magistrate stands in front
            of a bunch of crates and some workstations. A crowd has gathered, and applauds when he unveils the crates
            with a flourish.
            
            "TODAY.....YOU FACE ME IN A COOKING CONTEST...FOR YOUR LIFE! You must use these ingredients to create
            the perfect breakfast taco! Our town's Sheriff, Doctor, and Banker will preside as judges. There will be
            30 minutes for each of us to create a taco using the following ingredients:"
            
            """))

        ingredient_list = ['tortillas', 'chorizo', 'bell peppers', 'onion', 'eggys', 'chicken', 'chipotle chili sauce',
                           'lime crema', 'sour cream', 'bacon', 'hot sauce', 'maple syrup', 'lobster', 'cabbage',
                           'bananas']

# INGREDIENT SELECTION NOW WORKS, SHOUTOUT TO LIST COMPREHENSION FOR BEING GREAT

        print(ingredient_list)
        print("Please choose your ingredients.")
        action = input("> ")
        ingredient_selection = action.split(",")

        if [x for x in ingredient_list if any(x in item for item in ingredient_selection)] == \
                ['tortillas', 'chorizo', 'eggys']:

            print('DI MOOOOLTO BENE! THIS IS IT! THE ULTIMATE BREAKFAST TACO!')

            return 'a_prize'

        else:

            print('The Magistrate makes a way better taco! YOU HAVE BEEN CHOPPED!')

            return 'death'


class Pub(Scene):

    def enter(self):
        print(dedent("""
            You wisely decide not to fight the demon chicken. Instead, you valiantly retreat to the nearest pub, aptly
            named 'The Wingchester'. And hey, EVERY NIGHT is 50 cent wing night here! Nice.
            
            Can't be fighting demons, that'll make you late for dinner!
            
            Unfortunately, it seems that the demon chicken has a hobby....and that hobby is RAISING ZOMBIES.
            
            
            You're halfway through your 15th wing when a loud BLAM! hits the pub's front door. It's only a matter
            of time until the zombies make their way in...what would you like to do?! (You can FIGHT, RUN, HIDE, or 
            CONTINUE EATING)"""))
        action = input("> ")

        if action.lower() == 'fight' and 'COOL SWORD' in inventory:
            print(dedent("""
                There are""" + str(randint(2,10)) + """zombies! Fortunately, you're able to kill them with the 
                COOL SWORD in your inventory. The bystanders are so grateful, they offer you free beer for life! 
                Nice!"""))
            return 'finished'

        elif action.lower() == 'fight':
            print(dedent("""There are """ + str(randint(2, 10)) + """zombies! But you don't have a sword! You manage to 
            stab one in the head before being overwhelmed! They devour you - looks like it's 50 cent HUMAN night at 
            THIS BAR!"""))
            return 'death'
        elif action.lower() == 'run':
            print("You run! A master of the 'tactical retreat', I see. Unfortunately, in your haste, you slip and fall.")
            return 'death'

        elif action.lower() == 'hide':
            print("You hide in the bathroom. Seriously? What kind of hero are you!?")
            return 'pub2'

        elif action.lower() == 'continue eating':
            print(dedent("""
                You're not gonna let some silly zombies distract you from dinner. You munch on another delicious wing
                as the zombies force their way in, tearing through the door first, and then several patrons. You 
                lick wing sauce from your fingers in complete apathy. I guess nihilism is a hell of a drug."""))
            return 'pub2'
        else:
            print("please choose to FIGHT, RUN, HIDE, or CONTINUE EATING.")
            return 'pub'


class PubTwo(Scene):

    def enter(self):
        print(dedent("""
            The bartender takes a beautiful antique rifle off the wall behind the bar and works the lever action.
            With careful aim, he shoots the zombies in the head before they're able to wipe out the entire bar.
            """))

        return 'finished'


class Tanks(Scene):
    def enter(self):
        print(dedent("""
            As a prize, the villagers give you....a tank! Yes, that's right. A tank. Do you want to use it 
            to destroy the evil cultists and their town, or drive into the sunset?"""))

        action = input("> ")

        if 'destroy' in action.lower():
            print(dedent("""
                You fire up the tank's engine with a deep rumble and gas it, crushing the nearest house
                in a roar of splinters. Only rubble is left. You rotate the turret towards the Magistrate's house.
                'THIS IS WHAT LOSERS GET! DON'T YOU UNDERSTAND THAT CHORIZO IS THE ULTIMATE BREAKFAST TACO ADDITION?!' 
                you yell, and fire the cannon with a BOOOOOM! His house explodes into a million pieces. 
                
                Flooring the gas again, you crush a statue, five market stalls, and an outhouse on your way out.
                You can sleep well tonight, knowing that justice has been done this day."""))

            return 'finished'

        elif 'drive' in action.lower():
            print(dedent("""
                Despite being in command of a 50 ton behemoth, you don't let the power go to your head. Without 
                resorting to violence, you make your way out of town, riding into the distance, underneath a blazing
                red sky. Until the next adventure!"""))

            return 'finished'

        else:
            print('please rephrase to include either destroy or drive')
            return 'a_prize'


class Finished(Scene):

    def enter(self):
        print("You won! People stand around you saying 'Congratulations!'")
        return 'finished'


class Map(object):

    scenes = {
        'jungle': Jungle(),
        'jungle2': JungleTwo(),
        'finished': Finished(),
        'redo': Reincarnate(),
        'riddles': Tree(),
        'death': Death(),
        'chicken': DemonChicken(),
        'chopped': Shokugeki(),
        'a_prize': Tanks(),
        'pub': Pub(),
        'pub2': PubTwo(),
        'jungle3': JungleThree(),
        'junglefinal': JungleFinal(),
        #etc
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


the_map = Map('redo')
the_game = Engine(the_map)
the_game.play()
