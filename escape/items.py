"""Module: Define Items"""

class Item(object):
    """Define basic Item"""
    def __init__(self, name, description, room_tag):
        self.name = name
        self.description = description
        self.room_tag = room_tag

    def __repr__(self):
        """Return Item name"""
        return self.name

    def info(self):
        """Return full Item description"""
        return "{}\n^->{}".format(self.name, self.description)

    def tag(self):
        """Return a ROOM ID"""
        return self.room_tag

class Pack(Item):
    """Define Pack"""
    def __init__(self):
        super().__init__(name="Bottomless Pack", description="Even the pockets have pockets!", room_tag=1)
        self.pocket = []

    def contents(self):
        """Print iventory"""
        return "Inventory: {}".format(self.pocket)

class Orb(Item):
    """Define Orbs"""
    def __init__(self, name, description, color):
        super().__init__(name, description)
        self.color = color

    def rezonate(self):
        """Rezonate Orb with Door"""
        return "A pulsating {} light shines from within the orb.".format(self.color)

class Door(Orb):
    """Define Doors"""
    def __init__(self, name, description, room_tag, color):
        super().__init__(name, description, room_tag, color)
        self._lock = True
    
    @property
    def lock(self):
        """Return Door status"""
        return self._lock
    
    @lock.setter
    def lock(self, false):
        """Unlock Door"""
        for item in Pack().pocket:
            if item.color == self.color:
                self._lock = False
            else:
                print("The door doesn't budge.")

        
#Items
PACK = Pack()
TWIZZLERS = Item("Twizzlers", "The tastiest of tasty snacks!", 8)
#Orbs
BLUE_ORB = Orb("Blue Orb", "A glowing blue orb", "blue")
GREEN_ORB = Orb("Green Orb", "A glowing green orb", "green")
PURPLE_ORB = Orb("Purple Orb", "A glowing purple orb", "purple")
RED_ORB = Orb("Red Orb", "A glowing red orb", "red")
YELLOW_ORB = Orb("Yellow Orb", "A glowing yellow orb", "yellow")
ORANGE_ORB = Orb("Orange Orb", "A glowing orange orb", "orange")
WHITE_ORB = Orb("White Orb", "A glowing white orb", "white")
BLACK_ORB = Orb("Black Orb", "A glowing black orb", "black")
#Doors
BLUE_DOOR = Door("Blue Door", "An impossing door with a feint blue glow.", 2, "blue")
GREEN_DOOR = Door("Green Door", "An impossing door with a feint green glow.", 3, "green")
PURPLE_DOOR = Door("Purple Door", "An impossing door with a feint purple glow.", 4, "purple")
RED_DOOR = Door("Red Door", "An impossing door with a feint red glow.", 5, "red")
YELLOW_DOOR = Door("Yellow Door", "An impossing door with a feint yellow glow.", 6, "yellow")
ORANGE_DOOR = Door("Orange Door", "An impossing door with a feint orange glow.", 7, "orange")
WHITE_DOOR = Door("White Door", "An impossing door with a feint white glow.", 1, "white")
BLACK_DOOR = Door("Black Door", "An impossing door with a feint black glow.", 8, "black")
