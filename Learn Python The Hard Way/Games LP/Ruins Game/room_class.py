import random
from player_class import Player
from monster_class import Sloth, Blob, Cyclops, Fairy, Beetle


class Room(object):
    # Sets player for all classes inherited from Room class
    player = Player()
    # Lists of monsters for formatting in print
    mons = ['Sloth', 'Blob', 'Cyclops', 'Fairy', 'Beetle']


class Fight(Room):
    def set_up(self):
        # pulls monster_list and room_list variable
        self.monsters = monster_list
        self.rooms = room_list
        # sends variables to called methods
        self.monster = self.get_monster()
        self.room = self.get_room()

    # pulls and pops the current list item
    def get_room(self):
        try:
            return self.rooms.pop(0)
        except IndexError:
            return None

    def get_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        print "The {} is attacking!".format(self.monster.name)
        dodge = raw_input("Dodge? Y or N? ").lower()
        if dodge == 'y':
            if self.player.dodge():
                print "You dodged the attack."
            else:
                print "You were hit."
                # player was hit and removes a HP
                self.player.hit_points -= 1
        elif dodge == 'n':
            print "You were hit."
            self.player.hit_points -= 1
        else:
            # runs method again
            self.monster_turn()

    def player_turn(self):
        player_choice = raw_input("[A]ttack, or [R]est? ").lower()
        if player_choice == 'a':
            print "ATTACK!"
            if self.monster.attack():
                if self.monster.dodge():
                    print "The {} dodged your attack.".format(self.monster.name)
                else:
                    if self.player.level_up():
                        self.monster.hit_points -= 2
                    else:
                        self.monster.hit_points -= 1
                    print "You hit the {} with your {}.".format(self.monster.name, self.player.weapon)
            else:
                print "You missed."
        elif player_choice == 'r':
            self.player.rest()
        else:
            self.player_turn()

    def enter(self):
        # pulls set up method for monsters and rooms
        self.set_up()

        # Checks to see if monster and player both are above 0 HP
        while self.monster.hit_points and self.player.hit_points > 0:
            print self.player
            print self.monster
            self.monster_turn()
            self.player_turn()
            print '\n' + '-' * 30

        # Runs if monster has died
        if self.monster.hit_points <= 0:
            self.player.experience += self.monster.experience
            print "You killed the {}!".format(self.monster.name)
            print self.player
            print '\n' + '-' * 30
            return self.room

        # Runs if player has died
        elif self.player.hit_points <= 0:
            print "You lost!"
            return 'death'


class Death(Room):
    death = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this."]

    def enter(self):
        # Randomly chooses line
        print Death.death[random.randint(1, len(self.death) - 1)]
        exit()


class Grocery(Room):
    def enter(self):
        print '\n\'RING...RING...\' It\'s a number you don\'t recognize, but you answer anyway. \'HELLO, {}!\n' \
              'This is King Swanson. We are in need of your help! THE PRINCESS HAS BEEN KIDNAPPED!!\n' \
              '\'Yes sir, I\'m on my way!\' Quickly you reach for your {}, thankfully you brought it with ' \
              'you.\n\n' \
              '\'ATTENTION ALL CUSTOMERS! WE HAVE LOCKED ALL DOORS FOR YOUR SAFETY. PLEASE REMAIN CALM, UNTIL\n' \
              'THE AUTHORITIES REPORT THAT THE TOWN IS SAFE AGAIN! There are 2 simple ways out of here, the\n' \
              '[R]oof or [F]ront door.\n'.format(self.player.name, self.player.weapon)

        choose = raw_input("> ").lower()
        if choose == 'r':
            return 'roof'
        elif choose == 'f':
            return 'front_door'
        else:
            print "Try again"
            return "grocery"


class Roof(Room):
    def enter(self):
        self.fight = Fight()
        print "\nTo get to the roof you have to go through the backroom. 'HUFF', quickly you turn to\n" \
              "the sound. From behind the meat slicer you see it, a giant {}.\n".format(self.mons[0])
        return self.fight.enter()


class FrontDoor(Room):
    def enter(self):
        self.fight = Fight()
        print "\nYou ignore the announcement that just came through the loud speakers and make a run for the \n" \
              "front doors. That's when you see it, just outside... its a giant {}! Grabbing a shopping cart, \n" \
              "you smash out the front doors. He turns and runs at you leaving footprints in the\n" \
              "parking lot concrete.".format(self.mons[0])
        return self.fight.enter()


class CenterTown(Room):
    def enter(self):
        self.fight = Fight()
        print "\n'BAM!' The {} hit the ground, you hear a scream coming from the center of town. You grab\n" \
              "your electric unicycle from the bike rack and make a run for it.\n\n" \
              "As you reach the center of the town you see that things do not look like as they should;\n" \
              "buildings are in different places, glass is everywhere, the sky is dark. 'AHHHH!!!' That\n" \
              "sounded like it came from the parking garage. Jumping off your electric unicycle and running\n" \
              "towards the scream, it suddenly gets very dark and purple. That's when you see it, a \n" \
              "slippery purple {}.".format(self.mons[0], self.mons[1])
        return self.fight.enter()


class Garage(Room):
    def enter(self):
        self.fight = Fight()
        print "\nThe {} splashes everywhere, and goo goes flying! 'HELP!' she screams the girl. Upon reaching her\n" \
              "you see that she is looking past you at something. Turning you see it too, a {}! Almost\n" \
              "laughing at the sight of it, you loose control and let it out grabbing your sides. The {}\n" \
              "becomes irate and runs toward you".format(self.mons[1], self.mons[2], self.mons[2])
        return self.fight.enter()


class HeadOut(Room):
    def enter(self):
        self.fight = Fight()
        print "\nNow that they {} is dead, you can run to the girl. She tells you that the town is \n" \
              "infested with monsters, and that the the princess has been kidnapped and is headed north.\n" \
              "Remembering your mission you run out of the garage and into the center of town. Still nothing\n" \
              "looks normal, everything has been mixed up again. Grabbing for your compass you see it\n" \
              "spinning in all directions, it can't seem to find north. 'BUZZZZZZ' 'What was that?!'\n" \
              "'SWOOOSH! A {} landed right in front of your face!".format(self.mons[2], self.mons[3])
        return self.fight.enter()


class LastFight(Room):
    def enter(self):
        self.fight = Fight()
        print "\nAnother scream grabs your attention, this time it was King Swanson. Reaching him, he tells\n" \
              "you that the monster took her that way. Rushing to save her, you see that she is under \n" \
              "the arm of a giant {}. Running as fast as you can, you reach them at the north gate of \n" \
              "town. The {} sees you and he throws her hard on the ground, see passes out. There is only\n" \
              "one choice, fight to the death.".format(self.mons[4], self.mons[4])
        return self.fight.enter()


class Castle(Room):
    def enter(self):
        print "\nSome how you managed to beat the {}! Picking up the princess you see that she is just waking,\n" \
              "and is not sure of what happened. You tell her that everything is ok, and taking her home.\n" \
              "When reaching the castle, the King sees the princess and filled with joy. 'Please stay and \n" \
              "eat with us, as we are celebrating your victory!'".format(self.mons[4])
        exit()


monster_list = [Sloth(), Blob(), Cyclops(), Fairy(), Beetle()]
room_list = ['center_town', 'garage', 'head_out', 'last_fight', 'castle']
