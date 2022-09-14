import pygame, sys
from pygame.locals import *
from enemy import enemy
from init import clear
from events import event_handler

def gameloop(pyg):
    # Beginning Game Loop
    e = enemy(1, 2, [100,100])
    while True:
        pygame.display.update()
        event_handler(pyg)

        clear(pyg)
        e.draw(pyg)
        e.update(pyg)

        pyg['FramePerSec'].tick(pyg['FPS'])
