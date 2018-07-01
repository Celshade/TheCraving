"""Primary module of TheCraving: import additional modules and initiate game.

Functions:
    word_wrap(): Text wrapper.
    intro(): Provides story intro.
    main(): Primary game-loop.
"""
import items as it
import player as p
import story as s


def word_wrap(target: str, num=1) -> str:
    """Wrap text headings.

    Args:
        target: The target text to be wrapped.
        num (int): The wrap multiplyer (default=1).
    Returns:
        The wrapped target text.
    """
    wrap = "=" * (len(target) * num)
    return wrap + "\n" + target + "\n" + wrap


def intro() -> None:
    """Introduce storyline."""
    title = "\t **ThE CrAvInG**"

    print("\n" * 42)
    print(word_wrap(title, 2))
    print(s.ALPHA_TEXT)
    print(s.GRUMBLE + "\n")
    print("Startled by the sudden noise, you scramble guardedly to your feet.")
    print("\n" + s.GRUMBLE)
    print(s.REALIZATION)
    print(word_wrap("Search your surroundings for a way to escape!"))


def main() -> None:
    """Primary game-loop: run game."""
    player = p.Player()

    intro()
    player.menu()
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


main()
