"""Define the game environment and Player functionality.

Classes:
    Player(object): Establish the Player and gameplay.
Attributes:
    ROOMS (dict): Game environment throughout which the Player interacts.
    CHECKABLES (tuple): A tuple of Checkable objects.
    ORB_LIST (tuple): A tuple of Orbs.
"""
import sys
import time
import random

import items as it
import story as s
import cmap

# The actual game environment that a Player will navigate.
ROOMS = {
    1: {"name": "White Room",
        "north": it.BLUE_DOOR,
        "item": it.PACK, "orb": it.BLUE_ORB},
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

#  Useful constants for checking of objects and orbs.
CHECKABLES = (it.BOOKSHELF, it.CAMERA_CRATE, it.BUILDING_MATERIALS, it.SHRINE)
ORB_LIST = (it.BLUE_ORB, it.GREEN_ORB, it.PURPLE_ORB, it.RED_ORB,
            it.YELLOW_ORB, it.ORANGE_ORB, it.WHITE_ORB, it.BLACK_ORB)


class Player(object):
    """Define the Player and establish gameplay.

    Public Attributes:
        room (int): The current location.
        inventory (set): The base level of inventory.
    Public Methods:
        stats(): Show current location and information.
        match(): Match a Door to an Orb.
        options(): Display all available input commands.
        check(): Inspect an object, Item, or Orb for more detail.
        go(): Move in a direction.
        get(): Get an Item or Orb.
        gg(): Exit game.
        action(): Determine what action the Player takes.
    """

    def __init__(self, room: int = 1) -> None:
        """Construct Player.

        Args:
            room: The starting room number (default=1).
        """
        self.room = room
        self.inventory = set()
        self._discovered = 0  # The number of discovered ROOMS.
        self._CMAP = cmap.MiniMap(7, 7)  # Instantiate the map.

    def stats(self) -> None:
        """Broadcast current inventory and surroundings."""
        line_2 = "-" * 58
        location = ROOMS[self.room]

        print(f"\n{line_2}")
        print(f"You find yourself in: *The {location['name']}*")
        if it.PACK in self.inventory:
            print(it.PACK.get_contents())
        if "object" in location:
            print(f"You catch sight of a {location['object']}")
        if "item" in location:
            print(f"You catch sight of a {location['item']}")
        if "orb" in location:
            print(f"You catch sight of a {location['orb']}")
        print(f"{line_2}\n")

    def match(self, door: it.Door) -> bool:
        """Return True if the 'door' matches an Orb in the Pack, else False.

        Args:
            door: The Door to be matched.
        """
        for x in it.PACK.pocket:
            if x.icolor() == door.icolor():
                return True

    def options(self) -> None:
        """Display the main menu."""
        line_1 = "_" * 58
        line_2 = "-" * 14
        space = " " * 17

        print(f"\n{line_1}")
        print(f"{space}Valid Commands")
        print(f"{space}{line_2}")
        print(s.OPTIONS)
        if it.PACK not in self.inventory:
            print(f"{space}{line_2}")
            print("\n** Try typing 'check item' **")
        print(f"{line_1}\n\n")

    def check(self, obj: it.Item) -> None:
        """Check an object for any hidden clues.

        Args:
            obj: Item to be checked.
        """
        print(f"\nYou take a closer look at the {obj}...")
        print(obj.info())
        if obj is it.PACK or obj is it.TWIZZLERS:
            print("* Can be picked up with 'get item' *")
        elif obj in ORB_LIST and it.PACK in self.inventory:
            print("* Can be picked up with 'get orb' *")
        elif obj in CHECKABLES and obj.checked() is False:
            if obj is it.SHRINE:
                print(s.SHRINE_TEXT_BETA)
                it.SHRINE.descrip = s.SHRINE_TEXT_THETA
                del it.PACK.pocket[:]
            new_obj = obj.hidden()
            print(obj.hidden_text())
            print(f"You discover a {new_obj} hidden inside the {obj}!")

            if new_obj in ORB_LIST:
                ROOMS[self.room]["orb"] = new_obj
            else:
                ROOMS[self.room]["item"] = new_obj

    def go(self, direction: str) -> None:
        """Move in the specified direction.

        Args:
            direction: The direction to move the Player.
        """
        door = ROOMS[self.room][str(direction)]

        if door.lock_status(False):
            self.room = door.get_tag()
        elif door.lock_status(True):
            print(f"\nYou encounter {it.door_desc(door.icolor())}")
            if it.PACK in self.inventory and self.match(door):
                door.unlock()
                if door is not it.WHITE_DOOR:
                    self._discovered += 1
                self.room = door.get_tag()
            else:
                print("The door doesn't budge!")

    def get(self, target: str) -> None:
        """Pick up Items and Orbs.

        Args:
            target: The Item or Orb to be picked up.
        """
        location = ROOMS[self.room]

        if target == "item":
            if location["item"] is it.PACK:
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
                    print(f"\n{s.WORB_TEXT}")
                    ROOMS[1]["orb"] = it.BLACK_ORB
                del location["orb"]
            else:
                print("\nYou should have worn pants with pockets!")

    def gg(self, text: str, phase: int = 0) -> None:
        """Handle the game exit.

        Args:
            text: Text to be displayed upon exiting the game.
            phase: The game phase in which the function is called (default=0).
        """
        while True:
            try:
                exit_choice = input(text).lower()
                # Exit after completing the game.
                if phase == 1:
                    if exit_choice == "e":
                        break
                    else:
                        print("\nThat's not a valid choice.")
                        continue
                # Exit before completing the game.
                elif exit_choice == "y":
                    print(s.EXITS[random.randint(0, 3)])
                    time.sleep(3)
                    sys.exit()
                elif exit_choice == "n":
                    break
                else:
                    print("\nThat's not a valid choice.")
                    continue
            except EOFError:
                print("\n\nThat's not a valid choice.")

    def action(self) -> None:
        """Establish Player action.

        The primary function which handles all in-game action.
        The function prompts a series of input choices, which dictate
        what action the Player will take. Acceptable inputs are listed in the
        'options()' function and are otherwise known as valid commands.
        """
        try:
            initial_input = input("> ")
            location = ROOMS[self.room]

            if initial_input != "":
                choice = initial_input.lower().split()
                # Display the dungeon map.
                if choice[0] == "map":
                    self._CMAP.run(self._discovered, self.room)
                # List valid commands.
                elif choice[0] == "options":
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
                    self.gg("\nDo you wish to quit? Choose [Y] or [N]: ")
                else:
                    print("\nThat's not a valid command!")
                    print("Type 'options' to see available commands.")
            # When nothing at all is entered.
            else:
                print("\nNary a whisper could be heard...")
        # Handle Control + [Key] commands.
        except (EOFError, IndexError):
            print("\nThat's not a valid command!")
