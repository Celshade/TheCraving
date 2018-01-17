"""Cheers! A simple text-based, escape-the-room-type, game. Have fun!"""

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


def main():
    """Core gameplay and varriables"""
    def stats():
        """Current Status"""
        line_br2 = "-" * 30

        print("\n" + line_br2)
        print("You are in : " + rooms[current_room]["name"])
        if "pack" in bag:
            print("Inventory: " + str(hide(bag, "pack")))
        if "item" in rooms[current_room]:
            print("You catch sight of a %s" % (rooms[current_room].get("item")))
        print(line_br2 + "\n")

    current_room = 1
    bag = []
    rooms = {
        1 : {"name" : "White Room", "north" : 2, "item" : "pack"},
        2 : {"name" : "Blue Room", "south" : 1, "east" : 3},
        3 : {"name" : "Black Room", "west": 2, "north" : 4},
        4 : {"name" : "Amber Room", "south" : 3, "item" : "twizzlers"}
    }
    while True:
        stats()

        move = input(">").lower().split()
        if move[0] == "go":
            if move[1] in rooms[current_room]:
                current_room = rooms[current_room][move[1]]
            else:
                print("You cannot go that way!\n")
        elif move[0] == "get":
            if "item" in rooms[current_room] and move[1] in rooms[current_room]["item"]:
                bag += [move[1]]
                print("Picked up " + move[1] + "!")
                del rooms[current_room]["item"]
            else:
                print("It must have been a mirage...")
        elif move[0] != "go" or "get":
            print("That's not a valid command!")

        if "twizzlers" in bag:
            print("You sigh, blissfully, as you unwrap the pack of twizzlers.")
            print("Game Over!")
            break


#Start!!
title()
menu()
main()
