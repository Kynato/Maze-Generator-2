import pygame
from pygame.locals import *
from maze import *
from maze_cell import *
import random as rd


class GUI:
    def __init__(self, w:int, h:int):
        # Initiate the pygame engine
        #pygame.init()
        pygame.font.init()
        pygame.display.set_caption('MAZE GENERATOR - Alan Hudela')

        self.width = w
        self.height = h
        self.state = True
        self.backgroundColor = pygame.Color(25, 25, 25)
        self.font = pygame.font.SysFont("segoeui", 46)

        # Set the size of game window
        self.screen = pygame.display.set_mode((w, h))
        # Background color
        self.screen.fill(self.backgroundColor)

    def RandomColor(self):
        lower_bound = 100
        upper_bound = 200

        return rd.randint(lower_bound, upper_bound), rd.randint(lower_bound, upper_bound), rd.randint(lower_bound, upper_bound)

    def DrawCell(self, c:Cell, position_x, position_y, cell_size, wall_thickness):

        r, g, b = self.RandomColor()
        rand_color = (r,g,b)

        wall_color = (120, 20, 50)
        floor_color = (20, 20, 20)

        floor_color = pygame.Color('0x000000')
        wall_color = pygame.Color('0x697dd1')
        bedrock_color = (0,0,0)

        # Draw boundaries (background of cell)
        if c.IsBedrock():
            pygame.draw.rect(self.screen, bedrock_color, pygame.Rect(position_x, position_y, cell_size, cell_size))
        else:
            pygame.draw.rect(self.screen, floor_color, pygame.Rect(position_x, position_y, cell_size, cell_size))
            # Draw walls around the cell
            if 'up' in c.walls:
                pygame.draw.rect(self.screen, wall_color, pygame.Rect(position_x, position_y, cell_size, wall_thickness))
            if 'left' in c.walls:
                pygame.draw.rect(self.screen, wall_color, pygame.Rect(position_x, position_y, wall_thickness, cell_size))
            if 'down' in c.walls:
                pygame.draw.rect(self.screen, wall_color, pygame.Rect(position_x, position_y+cell_size-wall_thickness+1, cell_size, wall_thickness))
            if 'right' in c.walls:
                pygame.draw.rect(self.screen, wall_color, pygame.Rect(position_x+cell_size-wall_thickness+1, position_y, wall_thickness, cell_size))
            
        
        

    def DrawMaze(self, m:Maze):
        cell_count = max(m.h_cells, m.v_cells)
        cell_size = self.height/cell_count
        wall_thickness = cell_size*0.05

        for row in range(m.v_cells):
            for col in range(m.h_cells):
                self.DrawCell(m.table[row][col], col*cell_size, row*cell_size, cell_size, wall_thickness)


    

    def generateBackground(self):
        boxSpacing = self.width/9
        lineThickness = self.width*0.005
        fatlineThickness = self.width*0.01
        offset = -(lineThickness/2)
        fatOffset = -(fatlineThickness/2)
        slimColor = (100,100,100)
        fatColor = (200,200,200)
        
        # Slim lines
        for i in range(10):
            # Horizontal lines
            pygame.draw.rect(self.screen, slimColor, pygame.Rect(offset + i * boxSpacing, 0, lineThickness, self.width))
            # Vertical lines
            pygame.draw.rect(self.screen, slimColor, pygame.Rect(0, offset+ i * boxSpacing, self.width, lineThickness))

        # Thicc lines
        for i in range(4):
            # Horizontal lines
            pygame.draw.rect(self.screen, fatColor, pygame.Rect(fatOffset + i * (boxSpacing*3), 0, fatlineThickness, self.width))
            # Vertical lines
            pygame.draw.rect(self.screen, fatColor, pygame.Rect(0, fatOffset+ i * (boxSpacing*3), self.width, fatlineThickness))

    def drawDigit(self, row:int, col:int, value:int):
        spacing = self.width/9
        horizontalOffset = spacing/2
        text = self.font.render(str(value), True, (120, 20, 150))
        self.screen.blit(text,
        (spacing * col + horizontalOffset - (text.get_width()/2), 
        spacing * row))

    def drawDigits(self, mtx):
        for row in range(9):
            for col in range(9):
                if mtx[row][col] != 0:
                    self.drawDigit(row, col, mtx[row][col])
                    
    def render(self, mtx):
        self.generateBackground()
        self.drawDigits(mtx)

    def drawButtons(self):
        bttHeight = self.height - self.width
        bttWidth = self.width/2
        bttCol = (50, 10, 80)

        txtCol = (100, 100, 100)

        # Solve button
        pygame.draw.rect(self.screen, bttCol, pygame.Rect(0, self.width, bttWidth, bttHeight))
        text = self.font.render("SOLVE", True, txtCol)
        solveTextX = bttWidth/2 - (text.get_width()/2)
        solveTextY = self.width + (bttHeight/2) - (text.get_height()/2)
        self.screen.blit(text, (solveTextX, solveTextY))

        # Exit button
        pygame.draw.rect(self.screen, bttCol, pygame.Rect(bttWidth, self.width, bttWidth, bttHeight))
        text = self.font.render("EXIT", True, txtCol)
        solveTextX = bttWidth/2 - (text.get_width()/2) + bttWidth
        solveTextY = self.width + (bttHeight/2) - (text.get_height()/2)
        self.screen.blit(text, (solveTextX, solveTextY))

    def whichButton(self, mousePos):
        if 0 <= mousePos[0] <= self.width/2 and self.width <= mousePos[1] <= self.height:
            return 0 # SOLVE
        elif self.width/2 <= mousePos[0] <= self.width and self.width <= mousePos[1] <= self.height:
            return 1 # EXIT


        

    