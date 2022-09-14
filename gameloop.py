import pygame, sys
from pygame.locals import *
from enemy import enemy
from init import clear
from events import event_handler
from grid import drawgrid
def gameloop(pyg):
    # Beginning Game Loop
    enemies = []
    enemyTimer = 0
    while True:
        if int(pygame.time.get_ticks()/1000) > enemyTimer + 2 :
            enemyTimer = int(pygame.time.get_ticks()/1000)
            enemies.append(enemy(1, 2, [0,200]))

        pygame.display.update()
        event_handler(pyg)
        for e in enemies:
            clear(pyg)
            drawgrid(pyg)
            e.draw(pyg)
            e.update(pyg)
        for i,tower in enumerate(pyg['towers']):
            tower.draw(pyg)
        pyg['FramePerSec'].tick(pyg['FPS'])
