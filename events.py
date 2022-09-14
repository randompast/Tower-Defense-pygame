import pygame, sys
from pygame.locals import *
from tower import tower_spawner

def event_handler(pyg):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # print( pos, [ x, y ] )
            tower_spawner(pyg, pos)
