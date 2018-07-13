"""Define constants which hold storyline text.

Attributes:
    ALPHA_TEXT (str): Intro text.
    BETA_TEXT (str): Twizzler discovery text.
    OMEGA_TEXT (str): Outro text.
    REALIZATION (str): Recognition text.
    THE_CRAVING (str): The craving text.
    GRUMBLE (str): Grumbling noise text.
    WHITE_ORB_TEXT (str): White Room special text.
    SHRINE_TEXT_ALPHA (str): Shrine description text.
    SHRINE_TEXT_BETA (str): Shrine activation text.
    EXITS (list[str]): List of alternate ending text.
"""
ALPHA_TEXT = """
\n\t====Thus Far====\n
\n\t**A bell rings**\n
You awaken unto an empty white room..
..with no idea where you are or how you arrived.
You look around, searching for any clue of what's going on..
..but all you see is a worn pack and a strange orb on the ground.
You look down and check yourself over..
..thankful that you're still, at least, in posession of your pants.
"""

BETA_TEXT = """
You sigh, as you eagerly unwrap the [Pack of Twizzlers]...
As the sweetness hits your tastebuds, you feel a renewed surge of strength.
The room begins to come into focus, as your eyes adjust to the darkness.
You take notice of an aged wooden door just off to your left.
You test the door. It gives, easily, and you're blinded by sunlight pouring in.
You exit the compound and find yourself in a dense forest, when suddenly...
"""

OMEGA_TEXT = """
You awaken, lying on your bed, with sunlight streaming in from the windows.
You notice that your leather backpack is still slung across your shoulders.
You must have been so tired that you fell asleep with it on...
"""

REALIZATION = """
That sound...that feeling...you recognize it.
\t..A cold realization settles in..
\t... ... ... .. ... .. ... ... ...
"""

THE_CRAVING = """
You've developed a serious craving for twizzlers.
"""

GRUMBLE = "\t\t**grRRruMMmble**"

WORB_TEXT = "You hear a distant rumble and the [White Orb] flares brightly..."

SHRINE_TEXT_ALPHA = """
An ornate box sits atop an onyx pedestal. The box is sealed fast.
Eight perfectly smooth, sphere-shaped, recesses encircle the box.
You notice each indent emitting a faint glow just like the orbs you carry...
"""

SHRINE_TEXT_BETA = """
You place each of the colored orbs in their corresponding niche.
The orbs pulse rythmically, in sync, and the box unseals with a feint *hiss*.
"""

EXITS = [
    "You succumb to your craving and pass out...",
    ("Chuck Norris appears and roundhouse kicks you in the face."
     "\nAs your vision fades, you notice the scent of lilacs and justice..."),
    ("The kool-aid man bursts through the walls with an 'OH, YEEEEAH!"
     "\nHe grins maliciously, pounces, and swallows you whole..."),
    "A noxious dart hits you in the buttocks - rendering you unconscious..."
]
