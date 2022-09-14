import pygame, sys
from pygame.locals import *

def gameloop(pyg):
    # Beginning Game Loop
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pyg['FramePerSec'].tick(pyg['FPS'])
