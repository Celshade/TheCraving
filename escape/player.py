"""Module: Define self"""

import items as it


ROOMS = {
    1: {"name": "White Room",
        "north": it.BLUE_DOOR,
        "item": it.PACK, "orb": it.BLUE_ORB},
    2: {"name": "Blue Room",
        "south": it.WHITE_DOOR, "east": it.GREEN_DOOR,
        "west": it.PURPLE_DOOR,
        "orb": it.GREEN_ORB},
    3: {"name": "Green Room",
        "west": it.BLUE_DOOR, "north": it.YELLOW_DOOR,
        "orb": it.PURPLE_ORB},
    4: {"name": "Purple Room",
        "east": it.BLUE_DOOR, "north": it.RED_DOOR,
        "orb": it.RED_ORB},
    5: {"name": "Red Room",
        "south": it.PURPLE_DOOR, "east": it.ORANGE_DOOR,
        "orb": it.YELLOW_ORB},
    6: {"name": "Yellow Room",
        "south": it.GREEN_DOOR, "west": it.ORANGE_DOOR,
        "orb": it.ORANGE_ORB},
    7: {"name": "Orange Room",
        "east": it.YELLOW_DOOR, "west": it.RED_DOOR,
        "north": it.BLACK_DOOR,
        "orb": it.WHITE_ORB},
    8: {"name": "Black Room",
        "south": it.ORANGE_DOOR,
        "item": it.TWIZZLERS}
}


class Player():
    """Establish Player gameplay"""
    def __init__(self):
        self.room = 1
        self.inventory = []
        self.location = ROOMS[self.room]

    def menu(self):
        """List main menu"""
        line_1 = "_" * 47
        space = " " * 17

        print("\n" + line_1)
        print(space + "Valid Commands")
        print("> 'options'       (Lists valid commands)")
        print("> 'check [object]'(Look closer at an object)")
        print("> 'go [direction]'(north, south, east, or west)")
        print("> 'get item'      (Picks up nearby non-orb item)")
        print("> 'get orb'       (Picks up nearby orb)")
        print("> 'gg'            (Quit game)")
        print(line_1 + "\n")

    def stats(self):
        """Current Status"""
        line_2 = "-" * 30

        print("\n" + line_2)
        print("You are in : " + self.location["name"])
        if it.PACK in self.inventory:
            print(it.PACK.contents())
        if "item" in self.location:
            print("You catch sight of %s" % (self.location["item"]))
        if "orb" in self.location:
            print("You catch sight of %s" % (self.location["orb"]))
        print(line_2 + "\n")

    def match(self, door):
        """Check for Orb match"""
        for x in it.PACK.pocket:
            if x.icolor() == door.icolor():
                return True

    def move(self, direction):
        """Move in desired direction"""
        door = self.location[str(direction)]

        if door.lock_status(False):
            self.room = door.room_tag()
        elif door.lock_status(True):
            print("You encounter " + door.description)
            if it.PACK in self.inventory and self.match(door):
                door.unlock()
                self.room = door.room_tag()
            else:
                print("The door doesn't budge!")

    def action(self):
        """Control Player"""
        choice = input("> ").lower().split()
        choices = ("options", "check", "go", "get", "gg")

        if choice[0] == "options":
            self.menu()
        elif choice[0] == "check":
            pass
        elif choice[0] == "go":
            if choice[1] == "north" and choice[1] in self.location:
                self.move("north")
            elif choice[1] == "east" and choice[1] in self.location:
                self.move("east")
            elif choice[1] == "south" and choice[1] in self.location:
                self.move("south")
            elif choice[1] == "west" and choice[1] in self.location:
                self.move("west")
            else:
                print("You cannot go that way!\n")
        elif choice[0] == "get":
            if choice[1] == "item" and "item" in self.location:
                if self.location["item"] == it.PACK:
                    self.inventory.append(it.PACK)
                else:
                    it.PACK.pocket += [self.location["item"]]
                print("Picked up " + self.location["item"].name + "!")
                print(self.location["item"].info())
                del self.location["item"]
            elif choice[1] == "orb" and "orb" in self.location:
                if it.PACK in self.inventory:
                    it.PACK.pocket += [self.location["orb"]]
                    print("Picked up " + self.location["orb"].name + "!")
                    print(self.location["orb"].info())
                    del self.location["orb"]
                else:
                    print("You should have worn the pants with pockets!")
            else:
                print("It must have been a mirage...")
        while choice[0] == "gg":
            exit_choice = input(
                "Are you sure you wish to quit? Choose [Y] or [N]: ").lower()
            if exit_choice == "y":
                quit()
            elif exit_choice == "n":
                break
            else:
                print("That's not a valid choice.")
                continue
        if choice[0] not in choices:
            print("That's not a valid command!")


P1 = Player()
