import pygame, sys
from pygame.locals import *
from enemy import enemy
from init import clear

def gameloop(pyg):
    # Beginning Game Loop
    e = enemy(1, [100,100])
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        clear(pyg)
        e.draw(pyg)
        e.update(pyg)
        pyg['FramePerSec'].tick(pyg['FPS'])
