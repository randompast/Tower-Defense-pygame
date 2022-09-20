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
            tower_spawner(pyg, pos)
            print()
            for row in pyg['grid']:
                print([i if i == 0 else 1 for i in row])
        if event.type == pygame.KEYDOWN:
            mods = pygame.key.get_mods()
            if event.unicode == 'p': # and mods % 2 == 0:
                print("PAUSING")
                pyg['paused'] = not pyg['paused']