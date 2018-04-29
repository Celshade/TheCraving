"""Cheers! A simple text-based, escape-the-room, game. Have fun!"""

import items as it
import player as p
import story as s


def word_wrap(target, numb=1):
    """Wrap text headings"""
    wrap = "=" * (len(target) * numb)

    print(wrap)
    print(target)
    print(wrap)


def title():
    """Introduce storyline"""
    actual_title = "\t **ThE CrAvInG**"

    print("\n" * 42)
    word_wrap(actual_title, 2)
    print(s.ALPHA_TEXT)
    print(s.GRUMBLE)
    print()
    print("Startled by the sudden noise, you scramble guardedly to your feet.")
    print()
    print(s.GRUMBLE)
    print(s.REALIZATION)
    word_wrap("Search your surroundings for a way to escape!")


def main():
    """Run game"""
    while True:
        player.stats()
        player.action()
        if it.WHITE_ORB in it.PACK.pocket:
            p.ROOMS[1]["orb"] = it.BLACK_ORB
        if it.TWIZZLERS in it.PACK.pocket:
            print(s.BETA_TEXT)
            print(s.OMEGA_TEXT)
            print(s.GRUMBLE)
            print(s.REALIZATION)
            print("Game Over!")
            break
    quit()


player = p.Player()
title()
player.menu()
main()
