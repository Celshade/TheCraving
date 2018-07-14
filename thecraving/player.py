"""Define the game environment and Player functionality.

Classes:
    Player(): Establish the Player.
Functions:
    quit_game(): Exit the game.
Attributes:
    ROOMS (dict): Game environment throughout which the Player interacts.
    CHECKABLES (tuple): Checkable objects.
    ORB_LIST (tuple): Orb objects.
"""
import sys
import time

import items as it
import story as s


# The actual game environment a Player will navigate.
ROOMS = {
    1: {"name": "White Room",
        "north": it.BLUE_DOOR,
        "item": it.TWIZZLERS, "orb": it.BLUE_ORB},
    2: {"name": "Blue Room",
        "south": it.WHITE_DOOR, "east": it.GREEN_DOOR, "west": it.PURPLE_DOOR,
        "object": it.BOOKSHELF},
    3: {"name": "Green Room",
        "west": it.BLUE_DOOR, "north": it.YELLOW_DOOR,
        "orb": it.PURPLE_ORB},
    4: {"name": "Purple Room",
        "east": it.BLUE_DOOR, "north": it.RED_DOOR,
        "object": it.CAMERA_CRATE},
    5: {"name": "Red Room",
        "south": it.PURPLE_DOOR, "east": it.ORANGE_DOOR,
        "orb": it.YELLOW_ORB},
    6: {"name": "Yellow Room",
        "south": it.GREEN_DOOR, "west": it.ORANGE_DOOR,
        "object": it.BUILDING_MATERIALS},
    7: {"name": "Orange Room",
        "east": it.YELLOW_DOOR, "west": it.RED_DOOR, "north": it.BLACK_DOOR,
        "orb": it.WHITE_ORB},
    8: {"name": "Black Room",
        "south": it.ORANGE_DOOR,
        "object": it.SHRINE}
}
#  Useful constants for the checking of objects and orbs.
CHECKABLES = (it.BOOKSHELF, it.CAMERA_CRATE, it.BUILDING_MATERIALS, it.SHRINE)
ORB_LIST = (it.BLUE_ORB, it.GREEN_ORB, it.PURPLE_ORB, it.RED_ORB,
            it.YELLOW_ORB, it.ORANGE_ORB, it.WHITE_ORB, it.BLACK_ORB)


class Player(object):
    """Define the Player and establish gameplay.

    Attributes:
        room: The current location (default=1).
        inventory:  Base level inventory (default=set()).
    Public methods:
        stats()
        match()
        options()
        check()
        go()
        get()
        gg()
        action()
    """
    def __init__(self, room: int=1, inventory: set=set()) -> object:
        self.room = room
        self.inventory = inventory

    def stats(self) -> None:
        """Broadcast current inventory and surroundings."""
        line_2 = "-" * 58
        location = ROOMS[self.room]

        print("\n" + line_2)
        print("You find yourself in: The " + location["name"])
        if it.PACK in self.inventory:
            print(it.PACK.contents())
        if "object" in location:
            print(f"You catch sight of a {location['object']}")
        if "item" in location:
            print(f"You catch sight of a {location['item']}")
        if "orb" in location:
            print(f"You catch sight of a {location['orb']}")
        print(line_2 + "\n")

    def match(self, door: it.Door) -> bool:
        """Check PACK for Orb >> Door match.

        Args:
            door: The Door to be matched.
        Returns:
            Return True if a match is found, False otherwise.
        """
        for x in it.PACK.pocket:
            if x.icolor() == door.icolor():
                return True

    def options(self) -> None:
        """Display main menu."""
        line_1 = "_" * 58
        space = " " * 17

        print("\n" + line_1)
        print(space + "Valid Commands")
        print(space + "--------------"
              "\n> 'options'                  (List commands)"
              "\n> 'check [target]'           ('object', 'item', 'orb')"
              "\n> 'go [direction]'           (north, south, east, or west)"
              "\n> 'get item'                 (Pick up nearby non-orb item)"
              "\n> 'get orb'                  (Pick up nearby orb)"
              "\n> 'gg'                       (Quit game)")
        print(line_1 + ("\n" * 2))

    def check(self, obj: [it.Item]) -> None:
        """Check Object for hidden details.

        Args:
            obj: Item to be checked.
        """
        print(f"\nYou take a closer look at the {obj}...")
        print(obj.info())
        if obj in CHECKABLES and obj.not_checked():
            if obj == it.SHRINE:
                print(s.SHRINE_TEXT_BETA)
                del it.PACK.pocket[:]
            new_obj = obj.hidden()
            print(obj.hidden_text())
            print(f"You discover a {new_obj} hidden inside the {obj}!")
            if new_obj in ORB_LIST:
                ROOMS[self.room]["orb"] = new_obj
            else:
                ROOMS[self.room]["item"] = new_obj

    def go(self, direction: str) -> None:
        """Move in desired direction.

        Args:
            direction: Direction the Player wishes to move in.
        """
        door = ROOMS[self.room][str(direction)]

        if door.lock_status(False):
            self.room = door.room_tag()
        elif door.lock_status(True):
            print("\nYou encounter " + it.door_desc(door.icolor()))
            if it.PACK in self.inventory and self.match(door):
                door.unlock()
                self.room = door.room_tag()
            else:
                print("The door doesn't budge!")

    def get(self, target: str) -> None:
        """Pick up Items and Orbs.

        Args:
            target: The Item or Orb to be picked up.
        """
        location = ROOMS[self.room]

        if target == "item":
            if location["item"] == it.PACK:
                self.inventory.add(it.PACK)
            else:
                it.PACK.add_pack(location["item"])
            print(f"\nPicked up {location['item']}!")
            print(location["item"].info())
            del location["item"]
        elif target == "orb":
            if it.PACK in self.inventory:
                it.PACK.add_pack(location["orb"])
                print(f"\nPicked up {location['orb']}!")
                print(location["orb"].info())
                # Proc a special event for WHITE_ORB.
                if location["orb"] == it.WHITE_ORB:
                    print(s.WORB_TEXT)
                    ROOMS[1]["orb"] = it.BLACK_ORB
                del location["orb"]
            else:
                print("\nYou should have worn pants with pockets!")

    def gg(self, text: str, phase: int=0) -> None:
        """Handle the game exit.

        Args:
            text: Text to be displayed upon exiting the game.
            phase: The phase in which the function is called.
        """
        while True:
            exit_choice = input(text).lower()
            if phase == 1:
                # Give the player time to scroll back through their journey.
                if exit_choice == "r":
                    break
                else:
                    print("\nPlease enter [R] when you're ready to exit: ")
                    continue
            elif exit_choice == "y":
                print("\nThe craving overwhelms you and you pass out...")
                time.sleep(2)
                sys.exit()
            elif exit_choice == "n":
                break
            else:
                print("\nThat's not a valid choice.")
                continue

    def action(self) -> None:
        """Establish Player action.

        This is the primary function which handles all in-game decisions.
        The function prompts a series of input 'choices', which dictate
        what action the Player will take. Acceptable inputs are listed in the
        'menu()' function and are otherwise known as valid commands.
        """
        initial_input = input("> ")
        location = ROOMS[self.room]

        if initial_input != "":
            choice = initial_input.lower().split()
            # List valid commands.
            if choice[0] == "options":
                self.options()
            # Check an object, item, or orb.
            elif choice[0] == "check" and len(choice) > 1:
                if choice[1] == "object" and choice[1] in location:
                    self.check(location["object"])
                elif choice[1] == "item" and choice[1] in location:
                    self.check(location["item"])
                elif choice[1] == "orb" and choice[1] in location:
                    self.check(location["orb"])
                else:
                    print("\nIt must have been your imagination")
            # Move the player.
            elif choice[0] == "go" and len(choice) > 1:
                if choice[1] == "north" and choice[1] in location:
                    self.go("north")
                elif choice[1] == "east" and choice[1] in location:
                    self.go("east")
                elif choice[1] == "south" and choice[1] in location:
                    self.go("south")
                elif choice[1] == "west" and choice[1] in location:
                    self.go("west")
                else:
                    print("\nThere's no going that way!")
            # Pick up items and orbs.
            elif choice[0] == "get" and len(choice) > 1:
                if choice[1] == "item" and "item" in location:
                    self.get("item")
                elif choice[1] == "orb" and "orb" in location:
                    self.get("orb")
                elif choice[1] == "object" and "object" in location:
                        print("\nYou're going to need a bigger Pack!")
                else:
                    print("\nIt must have been a mirage...")
            # Exit the game.
            elif choice[0] == "gg":
                self.gg("Are you sure you wish to quit? Choose [Y] or [N]: ")
            else:
                print("\nThat's not a valid command!")
        # When nothing at all is entered.
        else:
            print("\nNary a whisper could be heard...")
