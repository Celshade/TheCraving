"""Cheers! A simple text-based, escape-the-room-type, game. Have fun!"""
import items as it

def title():
    """Intro"""
    line_br = "=" * 25
    grumble = "\n**grrRRrRrrRUmmMmMMble**\n"

    print("\n" + line_br)
    print("**The Craving**")
    print(line_br + "\n")
    print("==The Story Thus Far==\n")
    print("**A bell sounds**")
    print("You awaken unto an empty white room, with no idea where you are or how you arrived.")
    print("You look around, searching for any clue of what's going on, but to no avail.")
    print("You look down, thankful that you're still, at least, in posession of your pants.")
    print(grumble)
    print("Startled by the sudden noise, you scramble guardedly to your feet.")
    print(grumble)
    print("That sound...that feeling...you recognize it.")
    print("A cold realization sets in.")
    print("... .. .. ... .. .. ... .. ..")
    print("You've developed a serious craving for twizzlers.")
    print(line_br)
    print("Search your surroundings for a way to escape!")

def menu():
    """Main Menu"""
    print("\nValid Commands:")
    print("'go [direction]' (north, south, east, or west)")
    print("'get item' (picks up nearby non-orb item")
    print("'get orb (picks up nearby orb)\n")

ROOMS = {
    1 : {"name" : "White Room", "north" : it.BLUE_DOOR,
         "item" : it.PACK, "orb" : it.BLUE_ORB},
    2 : {"name" : "Blue Room", "south" : it.WHITE_DOOR, "east" : it.GREEN_DOOR,
         "west" : it.PURPLE_DOOR, "orb" : it.GREEN_ORB},
    3 : {"name" : "Green Room", "west": it.BLUE_DOOR, "north" : it.YELLOW_DOOR,
         "orb" : it.PURPLE_ORB},
    4 : {"name" : "Purple Room", "east" : it.BLUE_DOOR, "north" : it.RED_DOOR,
         "orb" : it.RED_ORB},
    5 : {"name" : "Red Room", "south" : it.PURPLE_DOOR, "east" : it.RED_DOOR,
         "orb" : it.YELLOW_ORB},
    6 : {"name" : "Yellow Room", "south" : it.GREEN_DOOR,
         "west" : it.ORANGE_DOOR, "orb" : it.ORANGE_ORB},
    7 : {"name" : "Orange Room", "east" : it.YELLOW_DOOR,
         "west" : it.RED_DOOR, "north" : it.BLACK_DOOR, "orb" : it.WHITE_ORB},
    8 : {"name" : "Black Room", "south" : it.ORANGE_DOOR,
         "item" : it.TWIZZLERS}
}

class Player:
    """Establish Player gameplay"""
    curr_room = 1
    inventory = []

    @classmethod
    def stats(cls):
        """Current Status"""
        line_br2 = "-" * 30

        print("\n" + line_br2)
        print("You are in : " + ROOMS[Player.curr_room]["name"])
        if it.PACK in Player.inventory:
            print(it.PACK.contents())
        if "item" in ROOMS[Player.curr_room]:
            print("You catch sight of a %s" % (ROOMS[Player.curr_room]["item"].name))
        if "orb" in ROOMS[Player.curr_room]:
            print("You catch sight of a %s" % (ROOMS[Player.curr_room]["orb"].name))
        print(line_br2 + "\n")

    @classmethod
    def move(cls):
        """Move Player"""
        choice = input(">").lower().split()
        if choice[0] == "go":
            if choice[1] in ROOMS[Player.curr_room]:
            #door functionality here!
                Player.curr_room = ROOMS[Player.curr_room][choice[1]]
            else:
                print("You cannot go that way!\n")
        elif choice[0] == "get":
            if choice[1] == "item" and "item" in ROOMS[Player.curr_room]:
                if ROOMS[Player.curr_room]["item"] == it.PACK:
                    Player.inventory.append(it.PACK)
                else:
                    it.PACK.pocket += [ROOMS[Player.curr_room]["item"]]
                print("Picked up " + ROOMS[Player.curr_room]["item"].name + "!")
                print(ROOMS[Player.curr_room]["item"].info())
                del ROOMS[Player.curr_room]["item"]
            elif choice[1] == "orb" and "orb" in ROOMS[Player.curr_room]:
                if it.PACK in Player.inventory:
                    it.PACK.pocket += [ROOMS[Player.curr_room]["orb"]]
                    print("Picked up " + ROOMS[Player.curr_room]["orb"].name + "!")
                    print(ROOMS[Player.curr_room]["orb"].info())
                    del ROOMS[Player.curr_room]["orb"]
                else:
                    print("You should have worn the pants with pockets!")
            else:
                print("It must have been a mirage...")
        elif choice[0] != "go" or "get":
            print("That's not a valid command!")

def main():
    """Run game"""
    while True:
        Player.stats()
        Player.move()
        if it.TWIZZLERS in it.PACK.pocket:
            print("You sigh, blissfully, as you unwrap the pack of twizzlers.")
            print("Game Over!")
            break

#Start!!
title()
menu()
main()
