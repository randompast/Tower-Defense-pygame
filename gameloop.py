import pygame, sys
from pygame.locals import *
from enemy import enemy
from init import clear
from events import event_handler
from grid import drawgrid

def gameloop(pyg):
    # Beginning Game Loop
    e = enemy(1, 2, [0,200])
    while True:
        pygame.display.update()
        event_handler(pyg)

        clear(pyg)
        drawgrid(pyg)
        e.draw(pyg)
        e.update(pyg)

        pyg['FramePerSec'].tick(pyg['FPS'])
