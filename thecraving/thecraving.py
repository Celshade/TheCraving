"""Primary module of TheCraving: import additional modules and initiate game.

Functions:
    word_wrap(): Text wrapper.
    title(): Provides story intro.
    main(): Primary game-loop.
"""
#  Welcome to TheCraving!
#  This is a simple text-based, escape-the-room, game.
#  Have fun!
import items as it
import player as p
import story as s


def word_wrap(target, numb=1):
    """Wrap text headings.

    Args:
        target (str): The target text to be wrapped.
        numb (int): The wrap multiplyer (default=1).
    """
    wrap = "=" * (len(target) * numb)

    print(wrap)
    print(target)
    print(wrap)


def title():
    """Introduce storyline."""
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
    """Primary game-loop: run game."""
    while True:
        player.stats()
        player.action()
        if it.TWIZZLERS in it.PACK.pocket:
            print(s.BETA_TEXT)
            print(s.OMEGA_TEXT)
            print(s.GRUMBLE)
            print(s.REALIZATION)
            print("Game Over!")
            break
    quit()


#  Where it all begins.
player = p.Player()
title()
player.menu()
main()
