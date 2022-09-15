import pygame
import sys
from pygame.locals import *
from enemy import *
from init import clear
from events import event_handler
from grid import drawgrid, drawgrid_direct
from ui import draw_ui
from tower import tower_updater

def gameloop(pyg):
    pyg['enemies'] = [enemy(1, 2, [0, 0])]
    update_enemy_paths(pyg)
    while pyg['player'].health > 0:
        pygame.display.update()
        clear(pyg)
        drawgrid(pyg)
        drawgrid_direct(pyg)
        event_handler(pyg)
        # enemy_updater(pyg)
        pyg['enemies'][0].draw_path(pyg)
        tower_updater(pyg)
        draw_ui(pyg)
        pyg['FramePerSec'].tick(pyg['FPS'])
