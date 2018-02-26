"""Cheers! A simple text-based, escape-the-room-type, game. Have fun!"""
import items as it
import player as p

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

def main():
    """Run game"""
    player = p.Player()
    while True:
        player.stats()
        player.action()
        if it.TWIZZLERS in it.PACK.pocket:
            print("You sigh, blissfully, as you unwrap the pack of twizzlers.")
            print("Game Over!")
            break

#Start!!
title()
menu()
main()
