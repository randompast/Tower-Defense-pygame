import pygame
import sys
from pygame.locals import *
from enemy import enemy
from init import clear
from events import event_handler
from grid import drawgrid

def gameloop(pyg):
    # Beginning Game Loop
    enemyTimer = 0
    while True:
        pygame.display.update()
        clear(pyg)
        drawgrid(pyg)
        if int(pygame.time.get_ticks()/1000) > enemyTimer + 2:
            enemyTimer = int(pygame.time.get_ticks()/1000)
            e = enemy(1, 2, [0, 200])
            pyg['enemies'].append(e)
        event_handler(pyg)
        for e in pyg['enemies']:
            e.draw(pyg)
            e.update(pyg)
        for i, tower in enumerate(pyg['towers']):
            tower.draw(pyg)
        pyg['FramePerSec'].tick(pyg['FPS'])
