import pygame, sys
# from pygame.locals import *

def drawgrid(pyg):
    sw,sh = pyg['SCREENSIZE']
    gw,gh = pyg['SIZE']
    for x in range(sw//gw):
        spos = [x*gw, 0]
        epos = [x*gw, sh]
        pygame.draw.line(pyg['DISPLAYSURF'], pyg['BLACK'], spos, epos)
    for y in range(sh//gh):
        spos = [0 , y*gh]
        epos = [sw, y*gh]
        pygame.draw.line(pyg['DISPLAYSURF'], pyg['BLACK'], spos, epos)
