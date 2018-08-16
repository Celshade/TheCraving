"""Create a callable map to display current location and explored rooms.

Classes:
    MiniMap(): Establish the map.
Attributes:
    WHITE: RGB white:
    BLUE: RGB blue:
    GREEN: RGB green.
    PURPLE: RGB purple.
    RED: RGB red.
    YELLOW: RGB yellow.
    ORANGE: RGB orange.
    BLACK: RGB black.
    GRAY: RGB gray.
"""
# import sys

import pygame

# Colors.
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (60, 255, 0)
PURPLE = (165, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)


class MiniMap(object):
    """Show a map of currently known rooms.

    Attributes:
        tilesize: Size of map tiles.
        width: Map width in tiles.
        height: Map height in tiles.
        MDWIDTH: Map width in pixels.
        MHEIGHT: Map height in pixels.
    Public Methods:
        start()
        render()
        run()
    """
    def __init__(self, tilesize: int, width: int, height: int) -> None:
        """The start() method will be called, upon instantiation, to speed up
        map rendering.
        """
        self.TSIZE = tilesize
        self.WIDTH = width
        self.HEIGHT = height
        self.MWIDTH = self.TSIZE * self.WIDTH
        self.MHEIGHT = self.TSIZE * self.HEIGHT
        self.start()

    def start(self) -> None:
        """Initiate pygame modules."""
        # call individual modules for speed boost
        pygame.__init__("display")
        pygame.__init__("event")
        pygame.__init__("draw")

    def render(self) -> None:
        """Render the map and update."""
        rect = pygame.draw.rect
        DSPLAY = pygame.display.set_mode((self.MWIDTH + 10, self.MHEIGHT + 10))

        pygame.display.set_caption("The C R A V I N G")
        # background
        DSPLAY.fill(BLACK)
        # ROOMS
        rect(DSPLAY, WHITE, (self.TSIZE * 3, self.TSIZE * 6, 60, 60), 1)
        rect(DSPLAY, BLUE, (self.TSIZE * 3, self.TSIZE * 4, 60, 60), 1)
        rect(DSPLAY, PURPLE, (self.TSIZE, self.TSIZE * 4, 60, 60), 1)
        rect(DSPLAY, GREEN, (self.TSIZE * 5, self.TSIZE * 4, 60, 60), 1)
        rect(DSPLAY, RED, (self.TSIZE, self.TSIZE * 2, 60, 60), 1)
        rect(DSPLAY, YELLOW, (self.TSIZE * 5, self.TSIZE * 2, 60, 60), 1)
        rect(DSPLAY, ORANGE, (self.TSIZE * 3, self.TSIZE * 2, 60, 60), 1)
        rect(DSPLAY, GRAY, (self.TSIZE * 3, 10, 60, 60), 1)
        # TODO edit self.render() to only show current/discovered room(s).

    def run(self) -> None:
        """Primary method: call, render(), and sweep up pygame."""
        while True:
            self.render()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        return False  # THIS LINE IS CRUCIAL
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    return False  # THIS LINE IS CRUCIAL
            pygame.display.update()
