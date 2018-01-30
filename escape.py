"""Cheers! A simple text-based, escape-the-room-type, game. Have fun!"""
import items

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
    print("Valid Commands:")
    print("'go [direction]' (north, south, east, or west)")
    print("'get [item]'\n\n")

def hide(list_x, hidden):
    """Hides an item in a list"""
    for i in list_x:
        if i != hidden:
            return i

ROOMS = {
    1 : {"name" : "White Room", "north" : 2, "item" : PACK},
    2 : {"name" : "Blue Room", "south" : 1, "east" : 3, "west" : 4, "item" : GREEN_ORB},
    3 : {"name" : "Green Room", "west": 2, "north" : 6, "item" : PURPLE_ORB},
    4 : {"name" : "Purple Room", "east" : 2, "north" : 5, "item" : RED_ORB},
    5 : {"name" : "Red Room", "south" : 4, "east" : 7, "item" : YELLOW_ORB},
    6 : {"name" : "Yellow Room", "south" : 3, "west" : 7, "item" : ORANGE_ORB},
    7 : {"name" : "Orange Room", "east" : 6, "west" : 5, "north" : 8, "item" : WHITE_ORB},
    8 : {"name" : "Black Room", "south" : 7, "item" : TWIZZLERS}
}

class Player:
    """Establish Player gameplay"""
    curr_room = 1
    bag = []

    @classmethod
    def stats(cls):
        """Current Status"""
        line_br2 = "-" * 30

        print("\n" + line_br2)
        print("You are in : " + ROOMS[Player.curr_room]["name"])
        if "pack" in Player.bag:
            print("Inventory: " + str(hide(Player.bag, "pack")))
        if "item" in ROOMS[Player.curr_room]:
            print("You catch sight of a %s" % (ROOMS[Player.curr_room].get("item")))
        print(line_br2 + "\n")

    @classmethod
    def move(cls):
        """Move Player"""
        choice = input(">").lower().split()
        if choice[0] == "go":
            if choice[1] in ROOMS[Player.curr_room]:
                Player.curr_room = ROOMS[Player.curr_room][choice[1]]
            else:
                print("You cannot go that way!\n")
        elif choice[0] == "get":
            if "item" in ROOMS[Player.curr_room] and choice[1] in ROOMS[Player.curr_room]["item"]:
                Player.bag += [choice[1]]
                print("Picked up " + choice[1] + "!")
                del ROOMS[Player.curr_room]["item"]
            else:
                print("It must have been a mirage...")
        elif choice[0] != "go" or "get":
            print("That's not a valid command!")

def main():
    """Run game"""
    while True:
        Player.stats()
        Player.move()
        if "twizzlers" in Player.bag:
            print("You sigh, blissfully, as you unwrap the pack of twizzlers.")
            print("Game Over!")
            break

#Start!!
title()
menu()
main()
