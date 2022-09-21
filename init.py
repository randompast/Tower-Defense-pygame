import pygame, sys
from pygame.locals import *
from player import player
from grid import grid

class gamestate():
    def __init__(self):
        self.FPS = 30
        self.FramePerSec = pygame.time.Clock()

        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.BLACK = (0, 0, 0)

        self.enemyTimer = 0
        self.paused = False
        self.goal = [6,0]

        pygame.display.set_caption('Tower Defense')
        self.grid = grid((8,8), (50,50), (10,20),(30,40))
        self.DISPLAYSURF = pygame.display.set_mode(self.grid.res)
        self.DISPLAYSURF.set_alpha(10)
        self.towers = []
        self.enemies = []
        self.player = player(3,2,0)

    def clear(self, color):
        background = pygame.Surface(self.grid.res).convert_alpha()
        pygame.draw.rect(background,color,[0,0]+self.grid.res)
        # pygame.draw.rect(background,(255,255,255,100),(0,0,40,40))
        # pygame.draw.rect(background,(255,0,255),(120,120,50,50))
        # self.DISPLAYSURF.fill(color)
        self.DISPLAYSURF.blit(background,(0,0))
