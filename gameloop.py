import pygame
import sys
from pygame.locals import *
from enemy import enemy_updater
from init import clear
from events import event_handler
from grid import drawgrid
from ui import draw_ui
from tower import tower_updater

def gameloop(pyg):
    while pyg['player'].health > 0:
        pygame.display.update()
        clear(pyg)
        drawgrid(pyg)
        event_handler(pyg)
        pygame.font.init()
        enemy_updater(pyg)
        tower_updater(pyg)
        draw_ui(pyg)
        pyg['FramePerSec'].tick(pyg['FPS'])
