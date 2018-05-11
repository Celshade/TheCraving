"""Define the Item class and all in-game items.

Classes:
    Item(object): Establish base Item class.
    Pack(Item): Establish Player inventory control.
    Checkable(Item): Define object which may hold an Item.
    Orb(Item): Define orbs.
    Door(Orb): Define doors.
Functions:
    door_desc(): Extended description for Door constructor.
Attributes:
    BLUE_ORB, GREEN_ORB, PURPLE_DOOR, RED_ORB, YELLOW_ORB,
    ORANGE_ORB, WHITE_ORB, BLACK_ORB
        (Orb): Orbs.
    BLUE_DOOR, GREEN_DOOR, PURPLE_DOOR, GREEN_DOOR, RED_DOOR,
    YELLOW_DOOR, ORANGE_DOOR, WHITE_DOOR, BLACK_DOOR
        (Door): Doors.
    PACK (Pack): A unique item.
    TWIZZLERS (Item): An item.
    BOOKSHELF (Checkable): An object.
    CAMERA_CRATE (Checkable): An object.
    BUILDING_MATERIALS (Checkable): An object.
    SHRINE (Checkable): An object.
"""
import story as s


class Item(object):
    """Define base Item class.

    Attributes:
        name (str): Name of Item.
        descrip (str): Description of Item.
        tag (int): Location identifyer.
    Public Methods:
        info(self)
        room_tag(self)

    This is a base class for all in-game items, intended to be subclassed for
    each unique SubClass(Item). Each SubClass will utilize the default
    attributes and methods defined in this class.
    """

    def __init__(self, name, descrip, tag):
        self.name = name
        self.descrip = descrip
        self.tag = tag

    def __repr__(self):
        """Return basic Item name."""
        return self.name

    def __str__(self):
        """Return formatted Item name."""
        return "[{}]".format(self.name)

    def info(self):
        """Return detailed description of Item."""
        return ("\n[{}]\n"
                + "=" * (len(self.name) + 2)
                + "\n{}").format(self.name, self.descrip)

    def room_tag(self):
        """Return original location of Item."""
        return self.tag


class Pack(Item):
    """Handle the inventory acquired by the Player.

    Attributes:
        pocket (list): Contains Items (default=[]).
    Public Methods:
        add_pack(self, obj)
        contents(self)

    Extend parent behavior while implementing new methods which interact with
    the unique 'pocket' attribute.
    """

    def __init__(self):
        super().__init__(name="Leather Pack",
                         descrip="Even the pockets have pockets!",
                         tag=1)
        self.pocket = []

    def add_pack(self, obj):
        """Add Item to the Pack.

        Args:
            obj (obj): Item to be added.
        """
        self.pocket.append(obj)

    def contents(self):
        """Return current iventory.

        Returns:
            Return 'pocket' content. If 'pocket' grows too large, the content
            string will be wrapped to the next line for readability.
        """
        if self.pocket == []:
            return "Inventory: Empty"
        elif len(self.pocket) > 4:
            return ("Inventory: {}\n".format(self.pocket[:4])
                    + (" " * 11) + "{}.".format(self.pocket[4:]))
        else:
            return "Inventory: {}".format(self.pocket)


class Checkable(Item):
    """Define an Item which may hold an additional hidden Item.

    Attributes:
        special (str): Special text to be triggered.
        obj (obj): A hidden Item.
        check_count (int): A useful counter.
    Public Methods:
        hidden(self)
        hidden_text(self)
        not_checked(self)

    Extend parent behavior while implementing new methods which interact
    with the hidden Item.
    """

    def __init__(self, name, descrip, tag, special, obj):
        super().__init__(name, descrip, tag)
        self.special = special
        self.obj = obj
        self.check_count = 0

    def hidden(self):
        """Return the hidden Item."""
        self.check_count += 1
        return self.obj

    def hidden_text(self):
        """Return special text, regarding the hidden Item."""
        return self.special

    def not_checked(self):
        """Return True if object has not been checked, else False."""
        if self.check_count > 0:
            return False
        else:
            return True


class Orb(Item):
    """Define Orbs.

    Attributes:
        color (str): The color of the Item.
    Public methods:
        icolor(self)

    Extend parent behavior while implementing a new method to interact with
    the unique 'color' attribute.
    """

    def __init__(self, name, descrip, tag, color):
        super().__init__(name, descrip, tag)
        self.color = color

    def icolor(self):
        """Return color of Item."""
        return self.color


class Door(Orb):
    """Define Doors.

    Attributes:
        lock (bool): Lock status of Door (default=True)
    Public methods:
        rezonate(self)
        lock_status(self, condition)
        unlock(self)

    Extend parent behavior, namely the 'color' attribute, as each Door is
    directly related to an Orb. New methods included in this class will return
    the status of the Door 'lock' and 'unlock' the door, based on a successful
    'color' match to an Orb in the Pack.
    """
    def __init__(self, name, descrip, tag, color, lock=True):
        super().__init__(name, descrip, tag, color)
        self.lock = lock

    def rezonate(self):
        """Rezonate with corresponding Orb."""
        print(("You raise the [{} Orb] in front of you.\nThe door vibrates "
               "in sync with the orb and begins to open!".format(self.color)))

    def lock_status(self, condition):
        """Return the status of a lock.

        Args:
            condition (bool): Condition to be checked for.
        Returns:
            True if condition is accurate, False otherwise."""
        if self.lock == condition:
            return True
        else:
            return False

    def unlock(self):
        """Unlock Door."""
        self.lock = False
        self.rezonate()


def door_desc(color):
    """Return Door(Orb) description text for use in constructor.

    Keyword arguments:
        color (str): the color attribute for Door(Orb).
    Returns:
        The extended description text for Door(Orb) formatted to color attr.
        """
    return "an imposing stone door with a dim {} aura.".format(color).lower()


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
CAMERA_CRATE = Checkable("Crate Full of Camera Parts",
                         "A crate filled with used camera parts.",
                         4,
                         "An odd glow shines from beneath some fish lenses...",
                         RED_ORB)
BUILDING_MATERIALS = Checkable("Pile of Building Materials",
                               "Building materials lie strewn about the room.",
                               6,
                               "You slip on something amidst the supplies...",
                               ORANGE_ORB)
SHRINE = Checkable("Strange Looking Shrine",
                   s.SHRINE_TEXT_ALPHA,
                   8,
                   "As you open the box and reach inside...",
                   TWIZZLERS)
