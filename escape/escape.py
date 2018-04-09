"""Cheers! A simple text-based, escape-the-room, game. Have fun!"""

import items as it
import player as p

player = p.Player()

grumble = "\n\t**grrRRrRrrRUmmMmMMble**\n"
text = """As the twizzlers hit your tastebuds, you feel a sudden
surge of strength well up within you. Your vision brightens and
your eyes began to adjust to the pitch darkness. A wooden door
materializes off to your left. The door gives, easily, and you are
temporarily blinded by sunshine from the outside. You exit the
compound unto a dense forest, when suddenly - ..."""

text_two = """You awaken, on your bed, with sunlight streaming in from
the window off to your left. You seem to have fallen asleep with your
backpack still slung across your shoulder."""


def word_wrap(target, numb=1):
    """Wrap text headings"""
    wrap = "=" * (len(target) * numb)

    print(wrap)
    print(target)
    print(wrap)


def outro():
    """Exit text"""
    print("""That sound...that feeling...you recognize it..
    ..A cold realization sets in.""")
    print("\n\t.. ... ... ... ... ... ... ..\n")
    print("You've developed a serious craving for twizzlers.\n")


def title():
    """Introduce storyline"""
    intro = "\t**ThE CrAvInG**"

    print("\n" * 50)
    word_wrap(intro, 2)
    print("\t  ==Thus Far==\n\n")
    print("\t**A bell sounds**")
    print("You awaken unto an empty white room..")
    print("..with no idea where you are or how you arrived.")
    print("You look around, searching for any clue of what's going on..")
    print("..but to no avail.")
    print("You look down and check yourself,")
    print("thankful that you're still, at least, in posession of your pants.")
    print(grumble)
    print("Startled by the sudden noise, you scramble guardedly to your feet.")
    print(grumble)
    outro()
    word_wrap("Search your surroundings for a way to escape!")


def main():
    """Run game"""
    while True:
        player.stats()
        player.action()
        if it.WHITE_ORB in it.PACK.pocket:
            p.ROOMS[1]["orb"] = it.BLACK_ORB
        if it.TWIZZLERS in it.PACK.pocket:
            print("You sigh, blissfully, as you unwrap the pack of twizzlers.")
            print()
            print(text)
            print(grumble)
            print(text_two)
            print(grumble)
            outro()
            print("Game Over!")
            break


# command > "ending" -> obtains twizzlers to trigger ending
# Start!!
title()
player.menu()
main()
