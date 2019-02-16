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
bar = 'XXXXX'
# Work out health bar to fight demon chicken
# Possibly health = [X|X|X|X|X] and .pop / .append for 'X' in list?


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
        print("You die! God doesn't care this time. Yare yare daze.")
        exit(1)


class Reincarnate(Scene):
    def enter(self):
        print(dedent("""
            You led a boring life! One day, you were killed by a falling coconut. It wasn't even organic.
            Damn GMO coconuts! You wake up in a dark, mist-filled chamber. God tells you you're pathetic and to try
            again, but only once. If you die again, he can't be bothered with you."""))
        status.append('reincarnated')
        print(f"Your status is {status}.")
        status.pop(0)
        print(f"Your health is {bar}.")
        print(f"Your inventory is {inventory}.")
        return 'jungle'


class Jungle(Scene):
    def enter(self):
        print(dedent("""
            ...The mist parts in front of you to reveal a rough dirt path through a lush forest. 
            You hear faint, girlish laughter in the distance. As you step into this new world and walk along the path,
            a monkey flings poo at your head.
            """))
        if randint(1, 20) >= 12:
            print(dedent("""He hits! You are covered in poo. Gross!"""))
            status.append('poo')
            print(f"Your status is {status}.")
            health = bar[:-1]
            print(f"Your health is {health}.")
            inventory.remove('hopes and dreams')
            print(f'You have lost your hopes and dreams. Your inventory is {inventory}.')

        else:
            print("He misses, screeches, and runs off. What a jerk!")

        print(dedent("""
            After walking further down the jungle path, you come across an ancient tree surrounded by dozens
            of orbiting lights. One of these lights rushes to greet you with a giggle. As it draws near, you
            notice it's a tiny, glowing fairy. "HUMAN, MY NAME...CHONK. WELCOME BIG TREE LAND!" it bellows
            ungracefully. "YOU WANT ADVENTURE NOW? HURR HURR, EAT BERRY FROM TREE." You walk up and notice
            a purple berry hanging delicately from a low branch. Do you eat it?"""))

        action = input("> ")

        if action.lower() == 'yes':
            print(dedent("""You shrink! Tiny human!!!"""))
            status.append('TINY!')
            print(f"Your status is {status}.")
            return 'riddles'

        elif action.lower() == 'no':
            print(dedent("""Chonk laughs and says "TAKE CHANCE WITH MONKEY THEN!" Monkey hits you and you die."""))
            return 'death'


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

                    return 'chicken'

                else:
                    print(dedent("""
                        Incorrect! But as Meat Loaf says: 'Two outta three ain't bad' - so the fairies
                        let you live, and you escape the jungle alive, but empty handed. Eventually, you arrive in 
                        a small but friendly town. Perhaps too friendly..."""))
                    return 'chicken'

            else:
                print("Incorrect! The fairies devour you. Chonk have full belly this day! Hurr.")
                return 'death'

        else:
            print("Incorrect! The fairies devour you. Chonk have full belly this day! Hurr.")
            return 'death'

# NEEDS WORK BELOW


class DemonChicken(Scene):
    def enter(self):
        print(dedent("""
            You pass a chicken in town. Something strikes you as odd about it, so you turn around and glance back.
            It returns your glance with a glowing red eye, menacing you with its gaze. Fight it?"""))
        action = input("> ")

        if action.lower() == 'yes' and 'COOL SWORD' in inventory:
            print(dedent("""
                You lop the demon chicken's head off with your COOL SWORD! Unfortunately, the town turns out to be
                full of Satanists, and you've killed their mascot. They challenge you to a cooking contest."""))
            return 'finished'
        elif action.lower() == 'yes' and 'COOL SWORD' not in inventory:
            print("You fight the chicken bare handed and lose!")
            return 'death'
        elif action.lower() == 'no':
            print("You decide not to fight the demon chicken.")
            return 'finished'


class Finished(Scene):

    def enter(self):
        print("You won! People stand around you saying 'Congratulations!'")
        return 'finished'


class Map(object):

    scenes = {
        'jungle': Jungle(),
        'finished': Finished(),
        'redo': Reincarnate(),
        'riddles': Tree(),
        'death': Death(),
        'chicken':DemonChicken(),
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
