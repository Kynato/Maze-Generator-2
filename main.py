# IMPORTS
from gui_fx import *
from maze import *

WINDOW_WIDTH = WINDOW_HEIGHT = 900
#WINDOW_HEIGHT = 500
clock = pygame.time.Clock()

# gui will be our graphics manager
gui = GUI(WINDOW_WIDTH, WINDOW_HEIGHT)

m = Maze(20, 20)



while 1:
    for event in pygame.event.get():
       if event.type == pygame.QUIT: sys.exit()

    gui.DrawMaze(m)
    pygame.time.wait(100)
    pygame.display.flip()