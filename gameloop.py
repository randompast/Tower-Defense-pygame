import pygame
import sys
from pygame.locals import *
from events import event_handler
from ui import draw_ui
from tower import tower_updater
from enemy import enemy_updater

def gameloop(pyg):
    while pyg.player.health > 0:
        pygame.display.update()
        pyg.clear((255,255,255,40))
        pyg.grid.draw_grid_lines(pyg)
        pyg.grid.draw_grid(pyg)
        event_handler(pyg)
        draw_ui(pyg)
        tower_updater(pyg)
        enemy_updater(pyg)
        pyg.FramePerSec.tick(pyg.FPS)
