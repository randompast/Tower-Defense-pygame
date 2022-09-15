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

def drawgrid_direct(pyg):
    gh, gw = len(pyg['grid']), len(pyg['grid'][0])
    for r in range( gh ):
        for c in range( gw ):
            if pyg['grid'][r][c] != 0:
                worldpos = [ (1 + c) * pyg['SIZE'][0]
                            ,(1 + r) * pyg['SIZE'][1] ]
                pygame.draw.rect(pyg['DISPLAYSURF'], pyg['BLUE'], worldpos + pyg['SIZE'], 4)
    # pygame.draw.rect(pyg['DISPLAYSURF'], pyg['BLUE'], [300,100] + pyg['SIZE'], 4)
