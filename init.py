import pygame, sys
from pygame.locals import *

def clear(pyg):
    pyg['DISPLAYSURF'].fill(pyg['WHITE'])

def initialize():
    # https://coderslegacy.com/python/python-pygame-tutorial/

    # Initialize program
    pygame.init()

    # Assign some basic values
    pyg = {'FPS' : 30
        ,'FramePerSec' : pygame.time.Clock()
        ,'WHITE' : (255, 255, 255)
        ,'RED' : (255, 0, 0)
        ,'SCREENSIZE' : (500,500)
    }

    pyg['DISPLAYSURF'] = pygame.display.set_mode(pyg['SCREENSIZE'])
    clear(pyg)
    pygame.display.set_caption('Tower Defense')

    return pyg