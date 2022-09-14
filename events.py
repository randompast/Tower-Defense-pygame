import pygame, sys
from pygame.locals import *


def event_handler(pyg):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print( pos, [ pos[0]//pyg["SIZE"][0] ,  pos[1]//pyg["SIZE"][1] ] )