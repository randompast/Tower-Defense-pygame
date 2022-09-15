import pygame
import sys
from pygame.locals import *
from enemy import enemy
from init import clear
from events import event_handler
from grid import drawgrid

def gameloop(pyg):
    enemyTimer = 0
    while pyg['player'].health > 0:
        pygame.display.update()
        clear(pyg)
        drawgrid(pyg)
        pygame.font.init()
        my_font = pygame.font.SysFont('Comic Sans MS', 20)
        text_surface = my_font.render('Health: ' + str(pyg['player'].health), False, (0, 0, 0))
        pyg['DISPLAYSURF'].blit(text_surface, (0,0))
        if int(pygame.time.get_ticks()/1000) > enemyTimer + 2:
            enemyTimer = int(pygame.time.get_ticks()/1000)
            e = enemy(1, 2, [0, 200])
            pyg['enemies'].append(e)
        event_handler(pyg)
        for e in pyg['enemies']:
            if e.touchdown == False:
                e.draw(pyg)
                e.update(pyg)
        for i, tower in enumerate(pyg['towers']):
            tower.draw(pyg)
        pyg['FramePerSec'].tick(pyg['FPS'])
