"""Define the Item class and all in-game items.

Classes:
    Item(object): Establish base class for Items.
    Pack(Item): Establish Player inventory control.
    Checkable(Item): Define object which may hold an Item.
    Orb(Item): Define orbs.
    Door(Orb): Define doors.
Functions:
    door_desc(): Extended description for Door constructor.
Attributes:
    BLUE_ORB (Orb): Blue Orb.
    GREEN_ORB (Orb): Green Orb.
    PURPLE_DOOR (Orb): Purple Orb
    RED_ORB (Orb): Red Orb.
    YELLOW_ORB (Orb): Yellow Orb.
    ORANGE_ORB (Orb): Orange Orb.
    WHITE_ORB (Orb): White Orb.
    BLACK_ORB (Orb): Black Orb.
    ---------
    BLUE_DOOR (Door): Blue Door.
    GREEN_DOOR (Door): Green Door.
    PURPLE_DOOR (Door): Purple Door.
    RED_DOOR (Door): Red Door.
    YELLOW_DOOR (Door): Yellow Door.
    ORANGE_DOOR (Door): Orange Door.
    WHITE_DOOR (Door): White Door.
    BLACK_DOOR (Door): Black Door.
    ----------
    PACK (Pack): A unique container-type Item.
    TWIZZLERS (Item): The ultimate Item.
    BOOKSHELF (Checkable): An interactive object.
    CAMERA_CRATE (Checkable): An interactive object.
    BUILDING_MATERIALS (Checkable): An interactive object.
    SHRINE (Checkable): An interactive object.
"""
import story as s


class Item(object):
    """Define base Item class.

    Attributes:
        name: Name of Item.
        descrip: Description of Item.
        tag: Location identifyer.
    Public Methods:
        info()
        room_tag()

    Provide a base class for all in-game items; intended to be subclassed for
    each unique SubClass(Item). Each SubClass will utilize the base
    attributes and methods defined in this class.
    """
    def __init__(self, name: str, descrip: str, tag: int) -> object:
        self.name = name
        self.descrip = descrip
        self.tag = tag

    def __repr__(self) -> str:
        """Return basic Item name."""
        return self.name

    def __str__(self) -> str:
        """Return formatted Item name."""
        return f"[{self.name}]"

    def info(self) -> str:
        """Return a detailed description of Item."""
        header = f"\n[{self.name}]"
        wrap = f"\n{'=' * (len(header) - 1)}"

        return f"{wrap}{header}{wrap}\n{self.descrip}"

    def room_tag(self) -> int:
        """Return original location of Item."""
        return self.tag


class Pack(Item):
    """Handle the inventory acquired by the Player.

    Attributes:
        pocket (list): Container for picked up Items (default=[]).
    Public Methods:
        add_pack()
        contents()

    Extend parent behavior while implementing new methods which interact with
    the unique 'pocket' attribute.
    """
    def __init__(self) -> Item:
        super().__init__(name="Leather Pack",
                         descrip="Even the pockets have pockets!",
                         tag=1)
        self.pocket = []

    def add_pack(self, obj: Item) -> None:
        """Add an Item to the Pack.

        Args:
            obj: Item to be added.
        """
        self.pocket.append(obj)

    def contents(self) -> str:
        """Return current iventory.

        Returns:
            Return 'pocket' content. If 'pocket' grows too large, the content
            string will be wrapped to the next line for readability.
        """
        if self.pocket == []:
            return "Inventory: Empty"
        elif len(self.pocket) > 4:
            return (f"Inventory: {self.pocket[:4]}\n"
                    + f"{' ' * 11}{self.pocket[4:]}.")
        else:
            return f"Inventory: {self.pocket}"


class Checkable(Item):
    """Define a container object which may hold a hidden Item.

    Attributes:
        special: Special text to be triggered.
        obj: The contained hidden Item.
        check_count (int): A useful counter (default=0).
    Public Methods:
        hidden()
        hidden_text()
        not_checked()

    Extend parent behavior while implementing new methods which interact
    with the hidden Item.
    """
    def __init__(self, name, descrip, tag, special: str, obj: Item) -> Item:
        super().__init__(name, descrip, tag)
        self.special = special
        self.obj = obj
        self.check_count = 0

    def hidden(self) -> Item:
        """Return the hidden Item."""
        self.check_count += 1
        return self.obj

    def hidden_text(self) -> str:
        """Return special text, regarding the hidden Item."""
        return self.special

    def not_checked(self) -> bool:
        """Return True if object has not been checked, else False."""
        if self.check_count > 0:
            return False
        else:
            return True


class Orb(Item):
    """Define in-game Orbs.

    Attributes:
        color: The color of the Item.
    Public methods:
        icolor()

    Extend parent behavior while implementing a new method to interact with
    the unique 'color' attribute.
    """
    def __init__(self, name, descrip, tag, color: str) -> Item:
        super().__init__(name, descrip, tag)
        self.color = color

    def icolor(self) -> str:
        """Return color of Item."""
        return self.color


class Door(Orb):
    """Define in-game Doors.

    Attributes:
        lock: Lock status of Door (default=True)
    Public methods:
        rezonate()
        lock_status()
        unlock()

    Extend parent behavior, namely the 'color' attribute, as each Door is
    directly related to an Orb. New methods included in this class will return
    the status of the Door and unlock the door, based on a successful
    'color' match to an Orb in the Pack.
    """
    def __init__(self, name, descrip, tag, color, lock: bool=True) -> Item:
        super().__init__(name, descrip, tag, color)
        self.lock = lock

    def rezonate(self) -> str:
        """Rezonate with corresponding Orb."""
        return (f"You raise the [{self.color} Orb] in front of you."
                "\nThe orb flares brilliantly and the door grinds open!")

    def lock_status(self, condition: bool) -> bool:
        """Return the status of a lock.

        Args:
            condition: Condition to be checked for.
        Returns:
            Return True if condition is accurate, False otherwise.
        """
        if self.lock == condition:
            return True
        else:
            return False

    def unlock(self) -> None:
        """Unlock Door."""
        self.lock = False
        print(self.rezonate())


def door_desc(color: str) -> str:
    """Return Door() description text for use in its constructor.

    Args:
        color: the color attribute for Door().
    Returns:
        The extended description text for Door() formatted to color attr.
    """
    return f"an imposing stone door with a dim *{color.lower()}* aura."


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
                      "A bookshelf housing old leather tomes.",
                      2,
                      "One of the books seems out of place...",
                      GREEN_ORB)
CAMERA_CRATE = Checkable("Crate Full of Camera Parts",
                         "A crate filled with old camera parts.",
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
