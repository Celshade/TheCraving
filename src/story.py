"""Define constants which hold storyline text.

Functions:
    centered(): Center text
Attributes:
    ALPHA_TEXT (str): Intro text.
    BETA_TEXT (str): Twizzler discovery text.
    OMEGA_TEXT (str): Outro text.
    REALIZATION (str): Recognition text.
    THE_CRAVING (str): The craving text.
    GRUMBLE (str): Grumbling noise text.
    BOOK_d (str): BOOKSHELF 'descrip'.
    BOOK_s (str): BOOKSHELF 'special'.
    CAM_n (str): CAMERA_CRATE 'name'.
    CAM_d (str): CAMEERA_CRATE 'descrip'.
    CAM_s (str): CAMERA_CRATE 'special'.
    BUILD_n (str): BUILDING_MATERIALS 'name'.
    BUILD_d (str): BUILDING_MATERIALS 'descrip'.
    BUILD_s (str): BUILDING_MATERIALS 'special'.
    SHRINE_n (str): SHRINE 'name'.
    SHRINE_d (str): SHRINE 'descrip'.
    SHRINE_s (str): SRHINE 'special'.
    SHRINE_TEXT_BETA (str): Shrine activation text.
    SHRINE_TEXT_THETA (str): Activated Shrine description text.
    WORB_TEXT (str): White Room special text.
    EXITS (list[str]): List of alternate ending text.
    OPTIONS (str): Available input commands.
"""


def centered(text: str) -> str:
    """Return centered text.

    All text will be centered in reference to a max line length of 79.

    text: The text to be centered (supports multi-line).
    """
    formatted = []

    if '\n' in text:
        for line in text.split('\n'):
            if line == '':
                formatted.append('\n')
            formatted.append(line.center(79))
        return '\n'.join(formatted)
    return text.center(79)


# ### STORYLINE ### #
ALPHA_TEXT = centered("""
====Thus Far====

**A bell rings**

You open your eyes to an empty white room...
...with no idea where you are or how you arrived.
You look around, searching for any clue of what's going on...
...but all you see is a worn pack and a strange orb laying on the ground.
You look down and inspect yourself...
...thankful that you're still, at least, in posession of your pants.
""")

BETA_TEXT = centered("""
You sigh in relief, as you eagerly unwrap the [Pack of Twizzlers]...
As the sweetness hits your tastebuds, you feel a renewed surge of strength.
The room begins to come into focus, and your eyes adjust to the darkness.
You take notice of an aged wooden door just off to your left.
You test the door. It gives, easily, and you're blinded by sunlight pouring in.
You exit the compound and find yourself in a dense forest, when suddenly...
""")

OMEGA_TEXT = centered("""
You awaken, lying on your bed, with sunlight streaming in from the windows.
You notice that your trusty backpack is still slung across your shoulders.
You must have been so tired that you fell asleep with it on...
""")

REALIZATION = centered("""
That sound...that feeling...you recognize it.
..A cold realization settles in..
... ... ... .. ... .. ... ... ...
""")

THE_CRAVING = centered("You've developed a serious craving for twizzlers.")

GRUMBLE = centered("**grRRruMMmble**")

# ### SPECIAL TEXT ### #
BOOK_d = centered("A bookshelf housing old leather tomes.")

BOOK_s = centered("One of the books seems out of place...")

CAM_n = centered("Crate Full of Camera Parts")

CAM_d = centered("A crate filled with old camera parts.")

CAM_s = centered("An odd glow shines from beneath some fish lenses...")

BUILD_n = centered("Pile of Building Materials")

BUILD_d = centered("Building materials lie strewn about the room.")

BUILD_s = centered("You slip on something amidst the supplies...")

SHRINE_n = centered("Strange Looking Shrine")

SHRINE_d = centered("""
An ornate box sits atop an onyx pedestal. The box is sealed fast.
Eight perfectly smooth, sphere-shaped, recesses encircle the box - each
emitting a faint glow just like the orbs you carry...
""")

SHRINE_s = centered("As you open the box and reach inside...")

SHRINE_TEXT_BETA = centered("""
You place each of the colored orbs into place, on the pedestal.
The orbs pulse rythmically, in sync, and the box unseals with a feint *hiss*.
""")

SHRINE_TEXT_THETA = centered("""
An empty ornate box sits atop an onyx pedestal, encircled by 8 glowing orbs.
""")

WORB_TEXT = centered(
    "You hear a distant rumble and the [White Orb] flares brightly..."
)

# ### EXITS AND OPTIONS ### #
EXITS = [
    "\nYou succumb to your craving and pass out...",
    ("\nChuck Norris appears and roundhouse kicks you in the face."
     "\nAs your vision fades, you notice the scent of lilacs and justice..."),
    ("\nThe kool-aid man bursts through the walls with an 'OH, YEEEEAH!"
     "\nHe grins maliciously, pounces, and swallows you whole..."),
    "\nA noxious dart hits you in the buttocks - rendering you unconscious..."
]

OPTIONS = """
'Item' refers to unique, non-orb, [Items] that can be picked up.
'Orb' refers to the [Colored Orbs] encountered throughout the game.
'Object' refers to anything that is not an [Orb] or [Item].
* When in doubt, 'check' it out! *

  -------                 --------
  |Input|                 |Action|
  -------                 --------
> 'map'                   (Shows map of discovered rooms and current location.)
> 'options'               (Shows this list of available options)
> 'check [target]'        (Check 'object', 'item', or 'orb' for more details)
> 'go [direction]'        (Go 'north', 'south', 'east', or 'west')
> 'get item'              (Pick up a nearby [Item])
> 'get orb'               (Pick up a nearby [Orb])
> 'gg'                    (Quit game)
"""
