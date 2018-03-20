"""Cheers! A simple text-based, escape-the-room-type, game. Have fun!"""
import items as it
import player as p


def word_wrap(target, numb=1):
    """Wrap text headings"""
    wrap = "=" * (len(target) * numb)

    print(wrap)
    print(target)
    print(wrap)


def title():
    """Intro"""
    intro = "\t**ThE CrAvInG**"
    grumble = "\n\t**grrRRrRrrRUmmMmMMble**\n"

    word_wrap(intro, 2)
    print("\n==The Story Thus Far==\n")
    print("\t**A bell sounds**")
    print(
        """
        You awaken unto an empty white room
        \twith no idea where you are or how you arrived.
        You look around, searching for any clue of what's going on,
        \tbut to no avail.
        You look down
        \tthankful that you're still, at least, in posession of your pants.
        """
    )
    print(grumble)
    print("Startled by the sudden noise, you scramble guardedly to your feet.")
    print(grumble)
    print(
        """
    That sound...that feeling...you recognize it.
    A cold realization sets in.
    ... .. .. ... .. .. ... .. ..
    You've developed a serious craving for twizzlers.
        """
    )
    word_wrap("Search your surroundings for a way to escape!")


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
        if it.WHITE_ORB in it.PACK.pocket:
            p.ROOMS[1]["orb"] = it.BLACK_ORB
        if it.TWIZZLERS in it.PACK.pocket:
            print("You sigh, blissfully, as you unwrap the pack of twizzlers.")
            print("Game Over!")
            break


# Start!!
title()
menu()
main()
