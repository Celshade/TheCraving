"""Module: Define Items"""

import story as s


class Item(object):
    """Define basic Item"""
    def __init__(self, name, descrip, tag):
        self.name = name
        self.descrip = descrip
        self.tag = tag

    def __repr__(self):
        """Return basic Item name"""
        return self.name

    def __str__(self):
        """Return true Item name"""
        return "[{}]".format(self.name)

    def info(self):
        """Return detailed description"""
        return ("\n[{}]\n"
                + "=" * (len(self.name) + 2)
                + "\n{}").format(self.name, self.descrip)

    def room_tag(self):
        """Return original location of Item"""
        return self.tag


class Pack(Item):
    """Define Pack"""
    def __init__(self):
        super().__init__(name="Leather Pack",
                         descrip="Even the pockets have pockets!",
                         tag=1)
        self.pocket = []

    def add_pack(self, obj):
        self.pocket.append(obj)

    def contents(self):
        """Return current iventory"""
        if self.pocket == []:
            return "Inventory: Empty"
        elif len(self.pocket) > 4:
            return ("Inventory: {}\n".format(self.pocket[:4])
                    + (" " * 11) + "{}.".format(self.pocket[4:]))
        else:
            return "Inventory: {}".format(self.pocket)


class Checkable(Item):
    """Define Checkable Item"""
    def __init__(self, name, descrip, tag, special, obj):
        super().__init__(name, descrip, tag)
        self.special = special
        self.obj = obj
        self.check_count = 0

    def hidden(self):
        """Return that which lies beneath"""
        self.check_count += 1
        return self.obj

    def hidden_text(self):
        """Return special text"""
        return self.special

    def not_checked(self):
        """Return True if obj has not been checked"""
        if self.check_count > 0:
            return False
        else:
            return True


class Orb(Item):
    """Define Orbs"""
    def __init__(self, name, descrip, tag, color):
        super().__init__(name, descrip, tag)
        self.color = color

    def icolor(self):
        """Return color"""
        return self.color


class Door(Orb):
    """Define Doors"""
    def __init__(self, name, descrip, tag, color, lock=True):
        super().__init__(name, descrip, tag, color)
        self.lock = lock

    def rezonate(self):
        """Rezonate with Orb"""
        print(("You raise the [{} Orb] in front of you.\nThe door vibrates "
               "in sync with the orb and begins to open!".format(self.color)))

    def lock_status(self, condition):
        """Return status of lock"""
        if self.lock == condition:
            return True
        else:
            return False

    def unlock(self):
        """Unlock Door"""
        self.lock = False
        self.rezonate()


def door_desc(color):
    """Return Door encounter description text"""
    return "an impossing stone door with a dim {} aura.".format(color).lower()


# Orbs
BLUE_ORB = Orb("Blue Orb", "A glowing blue orb", 2, "Blue")
GREEN_ORB = Orb("Green Orb", "A glowing green orb", 2, "Green")
PURPLE_ORB = Orb("Purple Orb", "A glowing purple orb", 3, "Purple")
RED_ORB = Orb("Red Orb", "A glowing red orb", 4, "Red")
YELLOW_ORB = Orb("Yellow Orb", "A glowing yellow orb", 5, "Yellow")
ORANGE_ORB = Orb("Orange Orb", "A glowing orange orb", 6, "Orange")
WHITE_ORB = Orb("White Orb", "A glowing white orb", 7, "White")
BLACK_ORB = Orb("Black Orb", "A glowing black orb", 1, "Black")
# Doors
BLUE_DOOR = Door("Blue Door", door_desc("blue"), 2, "Blue")
GREEN_DOOR = Door("Green Door", door_desc("green"), 3, "Green")
PURPLE_DOOR = Door("Purple Door", door_desc("purple"), 4, "Purple")
RED_DOOR = Door("Red Door", door_desc("red"), 5, "Red")
YELLOW_DOOR = Door("Yellow Door", door_desc("yellow"), 6, "Yellow")
ORANGE_DOOR = Door("Orange Door", door_desc("orange"), 7, "Orange")
WHITE_DOOR = Door("White Door", door_desc("white"), 1, "White")
BLACK_DOOR = Door("Black Door", door_desc("black"), 8, "Black")
# Items
PACK = Pack()
TWIZZLERS = Item("Pack of Twizzlers", "The tastiest of tasty snacks!", 8)
BOOKSHELF = Checkable("Bookshelf",
                      "An bookshelf housing old leather tomes.",
                      2,
                      "One of the books seems out of place...",
                      GREEN_ORB)
SHRINE = Checkable("Ancient Looking Shrine",
                   s.SHRINE_TEXT_ALPHA,
                   8,
                   "As you open the box and reach inside, you find...",
                   TWIZZLERS)
