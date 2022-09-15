import pygame, sys
# from pygame.locals import *

def drawgrid(pyg):
    sw,sh = pyg['SCREENSIZE']
    gw,gh = pyg['SIZE']
    for x in range(1, sw//gw):
        spos = [x*gw, 0+gh]
        epos = [x*gw, sh-gh]
        pygame.draw.line(pyg['DISPLAYSURF'], pyg['BLACK'], spos, epos)
    for y in range(1, sh//gh):
        spos = [ 0+gw, y*gh]
        epos = [sw-gw, y*gh]
        pygame.draw.line(pyg['DISPLAYSURF'], pyg['BLACK'], spos, epos)
