import pygame, sys
from pygame.locals import *
from tower import tower_spawner

def event_handler(pyg):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            mods = pygame.key.get_mods()
            if event.key == 27:
                pygame.quit()
                sys.exit()
            if event.unicode == 'p': # and mods % 2 == 0:
                pyg.paused = not pyg.paused
                print(f"Paused? {pyg.paused}")
            if event.unicode == 'l': # and mods % 2 == 0:
                for e in pyg.enemies:
                    print(e.path)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            gpos = pyg.grid.mouse_to_grid(pos)
            tower_spawner(pyg, gpos)
            pyg.grid.print()
