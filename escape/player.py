"""Module: Define Player and Rooms"""

import items as it
import story as s


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
CHECKABLES = (it.BOOKSHELF, it.CAMERA_CRATE, it.BUILDING_MATERIALS, it.SHRINE)
ORB_LIST = (it.BLUE_ORB, it.GREEN_ORB, it.PURPLE_ORB, it.RED_ORB,
            it.YELLOW_ORB, it.ORANGE_ORB, it.WHITE_ORB, it.BLACK_ORB)


class Player():
    """Establish Player gameplay"""
    def __init__(self, room=1, inventory=set()):
        self.room = room
        self.inventory = inventory

    def menu(self):
        """List main menu"""
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
        print(line_1 + "\n")

    def stats(self):
        """Broadcast current status"""
        line_2 = "-" * 30
        location = ROOMS[self.room]

        print("\n" + line_2)
        print("You are in : " + location["name"])
        if it.PACK in self.inventory:
            print(it.PACK.contents())
        if "object" in location:
            print("You catch sight of a {}".format(location["object"]))
        if "item" in location:
            print("You catch sight of a {}".format(location["item"]))
        if "orb" in location:
            print("You catch sight of a {}".format(location["orb"]))
        print(line_2 + "\n")

    def match(self, door):
        """Check PACK for Orb match"""
        for x in it.PACK.pocket:
            if x.icolor() == door.icolor():
                return True

    def move(self, direction):
        """Move in desired direction"""
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

    def check(self, obj):
        """Check Object for hidden Items"""
        print("\nYou take a closer look at the {}...".format(obj))
        print(obj.info())
        if obj in CHECKABLES and obj.not_checked():
            if obj == it.SHRINE:
                print(s.SHRINE_TEXT_BETA)
                del it.PACK.pocket[:]
            new_obj = obj.hidden()
            print(obj.hidden_text())
            print(("You discover a {} "
                   "hidden inside the {}!").format(new_obj, obj))
            if new_obj in ORB_LIST:
                ROOMS[self.room]["orb"] = new_obj
            else:
                ROOMS[self.room]["item"] = new_obj
        else:
            return None

    def action(self):
        """Establish Player action"""
        choice = input("> ").lower().split()
        location = ROOMS[self.room]

        if choice[0] == "options":
            self.menu()
        elif choice[0] == "check" and len(choice) > 1:
            if choice[1] == "object" and choice[1] in location:
                self.check(location["object"])
            elif choice[1] == "item" and choice[1] in location:
                self.check(location["item"])
            elif choice[1] == "orb" and choice[1] in location:
                self.check(location["orb"])
            else:
                print("\nIt must have been your imagination")
        elif choice[0] == "go" and len(choice) > 1:
            if choice[1] == "north" and choice[1] in location:
                self.move("north")
            elif choice[1] == "east" and choice[1] in location:
                self.move("east")
            elif choice[1] == "south" and choice[1] in location:
                self.move("south")
            elif choice[1] == "west" and choice[1] in location:
                self.move("west")
            else:
                print("\nThere's no going that way!")
        elif choice[0] == "get" and len(choice) > 1:
            if choice[1] == "item" and "item" in location:
                if location["item"] == it.PACK:
                    self.inventory.add(it.PACK)
                else:
                    it.PACK.add_pack(location["item"])
                print("\nPicked up {}!".format(location["item"]))
                print(location["item"].info())
                del location["item"]
            elif choice[1] == "orb" and "orb" in location:
                if it.PACK in self.inventory:
                    it.PACK.add_pack(location["orb"])
                    print("\nPicked up {}!".format(location["orb"]))
                    print(location["orb"].info())
                    del location["orb"]
                else:
                    print("\nYou should have worn the pants with pockets!")
            elif choice[1] == "object" and "object" in location:
                    print("\nYou're going to need a bigger Pack!")
                    return None
            else:
                print("\nIt must have been a mirage...")
        elif choice[0] == "gg":
            while choice[0] == "gg":
                exit_choice = input("\nAre you sure you wish to quit?"
                                    " Choose [Y] or [N]: ").lower()
                if exit_choice == "y":
                    quit()
                elif exit_choice == "n":
                    break
                else:
                    print("\nThat's not a valid choice.")
                    continue
        else:
            print("\nThat's not a valid command!")
