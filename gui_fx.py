import pygame
from pygame.locals import *


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


        

    