"""Cheers! A simple text-based, escape-the-room, game. Have fun!"""

import items as it
import player as p
import story as s

player = p.Player()


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
    print(s.intro)
    print(s.grumble)
    print("Startled by the sudden noise, you scramble guardedly to your feet.")
    print(s.grumble)
    print(s.outro)
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
            print(s.text_alpha)
            print(s.grumble)
            print(s.text_beta)
            print(s.grumble)
            print(s.realization)
            print("Game Over!")
            break
    quit()


title()
player.menu()
main()
