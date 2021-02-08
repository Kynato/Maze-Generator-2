# IMPORTS
from gui_fx import *
from maze import *

WINDOW_WIDTH = WINDOW_HEIGHT = 900
#WINDOW_HEIGHT = 500
clock = pygame.time.Clock()

# gui will be our graphics manager
gui = GUI(WINDOW_WIDTH, WINDOW_HEIGHT)

# SIZE OF THE MAZE
m = Maze(50, 50)
while(not m.FinishedGenerating()):
   m.BreakWalls()

while 1:
    for event in pygame.event.get():
       if event.type == pygame.QUIT: sys.exit()

    #m.BreakWalls()
    gui.DrawMaze(m)

    pygame.time.wait(100)
    pygame.display.flip()