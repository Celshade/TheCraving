"""Module: Define Player"""
import items as it


ROOMS = {
    1 : {"name" : "White Room",
         "north" : it.BLUE_DOOR,
         "item" : it.PACK, "orb" : it.BLUE_ORB
        },
    2 : {"name" : "Blue Room",
         "south" : it.WHITE_DOOR, "east" : it.GREEN_DOOR,
         "west" : it.PURPLE_DOOR, 
         "orb" : it.GREEN_ORB
        },
    3 : {"name" : "Green Room",
         "west": it.BLUE_DOOR, "north" : it.YELLOW_DOOR,
         "orb" : it.PURPLE_ORB
        },
    4 : {"name" : "Purple Room",
         "east" : it.BLUE_DOOR, "north" : it.RED_DOOR,
         "orb" : it.RED_ORB
        },
    5 : {"name" : "Red Room",
         "south" : it.PURPLE_DOOR, "east" : it.ORANGE_DOOR,
         "orb" : it.YELLOW_ORB
        },
    6 : {"name" : "Yellow Room",
         "south" : it.GREEN_DOOR, "west" : it.ORANGE_DOOR,
         "orb" : it.ORANGE_ORB
        },
    7 : {"name" : "Orange Room",
         "east" : it.YELLOW_DOOR, "west" : it.RED_DOOR,
         "north" : it.BLACK_DOOR,
         "orb" : it.WHITE_ORB
        },
    8 : {"name" : "Black Room",
         "south" : it.ORANGE_DOOR,
         "item" : it.TWIZZLERS
        }
}


class Player():
    """Establish Player gameplay"""
    room = 1
    inventory = []

    @classmethod
    def stats(cls):
        """Current Status"""
        line_br2 = "-" * 30

        print("\n" + line_br2)
        print("You are in : " + ROOMS[Player.room]["name"])
        if it.PACK in Player.inventory:
            print(it.PACK.contents())
        if "item" in ROOMS[Player.room]:
            print("You catch sight of %s" % (ROOMS[Player.room]["item"].name))
        if "orb" in ROOMS[Player.room]:
            print("You catch sight of %s" % (ROOMS[Player.room]["orb"].name))
        print(line_br2 + "\n")

    @classmethod
    def match(cls, door):
        """Check for Orb match"""
        for x in it.PACK.pocket:
            if x.icolor() == door.icolor():
                return True
            else:
                continue

    @classmethod
    def move(cls, direction):
        """Move in desired direction"""
        door = ROOMS[Player.room][str(direction)]

        if door.lock_status() == False:
            Player.room = door.room_tag()
        elif door.lock_status() == True:
            if it.PACK in Player.inventory and Player.match(door):
                door.unlock()
                Player.room = door.room_tag()
            else:
                print("The door doesn't budge!")

    @classmethod
    def action(cls):
        """Control Player"""
        choice = input(">").lower().split()
        location = ROOMS[Player.room]

        if choice[0] == "go":
            if choice[1] == "north" and choice[1] in location:
                Player.move("north")
            elif choice[1] == "east" and choice[1] in location:
                Player.move("east")
            elif choice[1] == "south" and choice[1] in location:
                Player.move("south")
            elif choice[1] == "west" and choice[1] in location:
                Player.move("west")
            else:
                print("You cannot go that way!\n")
        elif choice[0] == "get":
            if choice[1] == "item" and "item" in location:
                if location["item"] == it.PACK:
                    Player.inventory.append(it.PACK)
                else:
                    it.PACK.pocket += [location["item"]]
                print("Picked up " + location["item"].name + "!")
                print(location["item"].info())
                del location["item"]
            elif choice[1] == "orb" and "orb" in location:
                if it.PACK in Player.inventory:
                    it.PACK.pocket += [location["orb"]]
                    print("Picked up " + location["orb"].name + "!")
                    print(location["orb"].info())
                    del location["orb"]
                else:
                    print("You should have worn the pants with pockets!")
            else:
                print("It must have been a mirage...")
        elif choice[0] != "go" or "get":
            print("That's not a valid command!")
