import pygame, sys
from pygame.locals import *


def event_handler(pyg):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
