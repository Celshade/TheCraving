"""Define the game environment and Player functionality.

Classes:
    Player(object): Establish the Player and gameplay.
Attributes:
    ROOMS (dict): Game environment throughout which the Player interacts.
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
        start_line = '=' * 79
        end_line = '-' * 79
        loc = ROOMS[self.room]  # Current location
        print(f"\n{start_line}")
        print(s.centered(f"You find yourself in: *The {loc['name']}*"))
        print()

        if "object" in loc:
            print(s.centered(f"You catch sight of a {loc['object']} <Object>"))
        if "item" in loc:
            print(s.centered(f"You catch sight of a {loc['item']} <Item>"))
        if "orb" in loc:
            print(s.centered(f"You catch sight of a {loc['orb']} <Orb>"))
        print()

        if it.PACK in self.inventory:
            print(it.PACK.get_contents())

    def match(self, door: it.Door) -> bool:
        """Return True if the 'door' matches an Orb in the Pack, else False.

        Args:
            door: The Door to be matched.
        """
        return any([item.icolor() == door.icolor() for item in it.PACK.pocket])

    def options(self) -> None:
        """Display the main menu."""
        header = "Valid Commands"
        line = ('-' * len(header)).center(79)
        print(line)
        print("Valid Commands".center(79))
        print(line)
        print(s.OPTIONS)

        if it.PACK not in self.inventory:
            sub_header = "** Try typing 'check item' **"
            sub_line = ('-' * len(sub_header)).center(79)
            print(sub_line)
            print(sub_header.center(79))
            print(sub_line, end='\n\n')

    def check(self, obj: it.Item) -> None:
        """Check an object for any hidden clues.

        Args:
            obj: Item to be checked.
        """
        print()
        print(s.centered(f"You take a closer look at the {obj}...\n"))

        if type(obj) == it.Checkable:
            if not obj.checked():
                print(obj.info())

                if obj is it.SHRINE:
                    print(s.SHRINE_TEXT_BETA)
                    del it.PACK.pocket[:]

                new_obj = obj.hidden()
                discover = f"You discover a {new_obj} hidden inside the {obj}!"
                print(obj.hidden_text())
                print(discover.center(79))

                if type(new_obj) == it.Orb:
                    ROOMS[self.room]["orb"] = new_obj
                else:
                    ROOMS[self.room]["item"] = new_obj
            elif obj.checked() and obj is it.SHRINE:  # Handle activated shrine
                print(s.SHRINE_TEXT_THETA)
            else:
                print(obj.info())
        else:
            print(obj.info())

            if obj is it.PACK or obj is it.TWIZZLERS:
                print(s.centered("* Can be picked up with 'get item' *"))
            elif type(obj) == it.Orb and it.PACK in self.inventory:
                print(s.centered("* Can be picked up with 'get orb' *"))

    def go(self, direction: str) -> None:
        """Move in the specified direction.

        Args:
            direction: The direction to move the Player.
        """
        door = ROOMS[self.room][str(direction)]

        if door.lock_status(False):
            self.room = door.get_tag()
        else:
            print()
            print(f"You encounter {it.door_desc(door.icolor())}".center(79))

            if it.PACK in self.inventory and self.match(door):
                door.unlock()
                if door is not it.WHITE_DOOR:
                    self._discovered += 1
                self.room = door.get_tag()
            else:
                print("The door doesn't budge!".center(79))

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
        invalid = "\nThat's not a valid choice.".center(79)

        while True:
            try:
                exit_choice = input(text).lower()
                # Exit after completing the game.
                if phase == 1:
                    if exit_choice == "e":
                        break
                    else:
                        print(invalid)
                        continue
                # Exit before completing the game.
                elif exit_choice == "y":
                    print(s.EXITS[random.randint(0, 3)], end='\n\n')
                    sys.exit()
                elif exit_choice == "n":
                    break
                else:
                    print(invalid)
                    continue
            except EOFError:
                print(invalid)

    def action(self) -> None:
        """Establish Player action.

        The primary function which handles all in-game action.
        The function prompts a series of input choices which dictate
        what action the Player will take. Acceptable inputs are listed in the
        'options()' function and are otherwise known as valid commands.
        """
        invalid = '\n' + "That's not a valid command!".center(79)

        try:
            initial_input = input("\n> ")
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
                        print("It must have been your imagination".center(79))
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
                        print("There's no going that way!".center(79))
                # Pick up items and orbs.
                elif choice[0] == "get" and len(choice) > 1:
                    if choice[1] == "item" and "item" in location:
                        self.get("item")
                    elif choice[1] == "orb" and "orb" in location:
                        self.get("orb")
                    elif choice[1] == "object" and "object" in location:
                        print("You're going to need a bigger Pack!".center(79))
                    else:
                        print("It must have been a mirage...".center(79))
                # Exit the game.
                elif choice[0] == "gg":
                    self.gg("Do you wish to quit? Choose [Y] or [N]: ")
                else:
                    print(invalid)
                    print(
                        "Type 'options' to see available commands.".center(79))
            # When nothing at all is entered.
            else:
                print("Nary a whisper could be heard...".center(79))
        # Handle Control + [Key] commands.
        except (EOFError, IndexError):
            print(invalid)
