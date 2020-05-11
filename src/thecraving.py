"""Primary module of TheCraving: initiate game and introduce storyline.

Functions:
    word_wrap(): Text wrapper.
    intro(): Provide story intro.
    outro(): Provide story outro.
    main(): Primary game-loop.
"""
import time
import signal
import sys

import items as it
import player as p
import story as s


def word_wrap(target: str, num: int=1) -> str:
    """Wrap text headings and return the formatted text.

    Args:
        target: The target text to be wrapped.
        num: The wrap multiplyer (default=1).
    """
    wrap = f"{'=' * len(target)}" * num
    return f"{wrap}\n{target}\n{wrap}"


def intro() -> None:
    """Introduce the storyline."""
    title = "\t **ThE CrAvInG**"

    # Clear the screen from any previous text.
    print("\n" * 42)
    print(word_wrap(title, 2))
    print(s.ALPHA_TEXT)
    print(f"{s.GRUMBLE}\n")
    print("Startled by the sudden noise, you scramble guardedly to your feet.")
    print(f"\n{s.GRUMBLE}")
    print(s.REALIZATION)
    print(s.THE_CRAVING)
    print(word_wrap("Search your surroundings for a way to escape!"))


def outro() -> None:
    """End the storyline."""
    print(s.BETA_TEXT)
    time.sleep(5)
    print(s.OMEGA_TEXT)
    time.sleep(5)
    print(s.GRUMBLE)
    time.sleep(1)
    print(s.REALIZATION)
    time.sleep(3)
    print(s.THE_CRAVING)
    time.sleep(2)
    print("Game Over!\nThanks for playing!\n")


def main() -> None:
    """Primary game-loop: run game."""
    player = p.Player()
    game_exit = False

    intro()
    player.options()
    # Prevent script breaking signals.
    signal.signal(signal.SIGBREAK, signal.SIG_IGN)
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    while game_exit is False:
        player.stats()
        player.action()
        if it.TWIZZLERS in it.PACK.pocket:
            outro()
            player.gg("Enter [E] to exit the game: ", 1)
            game_exit = True
    print("\nPeace!\n-Cel-")
    time.sleep(3)
    sys.exit()


main()
