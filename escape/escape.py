"""Cheers! A simple text-based, escape-the-room, game. Have fun!"""

import items as it
import player as p

player = p.Player()

text_zero = """\n\t  ==Thus Far==\n\n
\t**A bell sounds**
You awaken unto an empty white room..
..with no idea where you are or how you arrived.
You look around, searching for any clue of what's going on..
..but to no avail. All you see are stark white walls, a bag, and a strange orb.
You look down and check yourself..
..thankful that you're still, at least, in posession of your pants."""

text_one = """As the twizzlers hit your tastebuds, you feel a sudden
surge of strength well up within you. Your vision brightens and
your eyes began to adjust to the pitch darkness. An aged wooden door
materializes just off to your left. The door gives, easily, and you are
temporarily blinded by sunshine pouring in from the outside. You exit the
compound unto a dense forest, when suddenly - ..."""

text_two = """You awaken, lying on your bed, with sunlight streaming in from
the windows to your left. You notice that your backpack is still slung across
your shoulders. You must have been so tired that you forgot to shrug it off.
"""
outro = """That sound...that feeling...you recognize it..
\t..A cold realization sets in.
\n\t.. ... ... ... ... ... ... ..\n
You've developed a serious craving for twizzlers.\n"""
grumble = "\n\t**grrRRrRrrRUmmMmMMble**\n"


def word_wrap(target, numb=1):
    """Wrap text headings"""
    wrap = "=" * (len(target) * numb)

    print(wrap)
    print(target)
    print(wrap)


def title():
    """Introduce storyline"""
    actual_title = "\t **ThE CrAvInG**"

    print("\n" * 50)
    word_wrap(actual_title, 2)
    print(text_zero)
    print(grumble)
    print("Startled by the sudden noise, you scramble guardedly to your feet.")
    print(grumble)
    print(outro)
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
            print(text_one)
            print(grumble)
            print(text_two)
            print(grumble)
            print(outro)
            print("Game Over!")
            break


# command > "ending" -> obtains twizzlers to trigger ending
# Start!!
title()
player.menu()
main()
