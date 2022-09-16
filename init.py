import pygame, sys
from pygame.locals import *
from player import player
from enemy import update_enemy_paths

def clear(pyg):
    pyg['DISPLAYSURF'].fill(pyg['WHITE'])

def initialize():
    # Initialize program
    pygame.init()
    # Assign some basic values
    pyg = {'FPS' : 30
        ,'FramePerSec' : pygame.time.Clock()
        ,'WHITE' : (255, 255, 255)
        ,'RED' : (255, 0, 0)
        ,'GREEN' : (0, 255, 0)
        ,'BLUE' : (0, 0, 255)
        ,'BLACK' : (0, 0, 0)
        ,'SCREENSIZE' : (500,500)
        ,'SIZE' : [50,50]
        ,'enemyTimer' : 0
        ,'paused' : False
        ,'goal' : [6,0]
    }

    pyg['DISPLAYSURF'] = pygame.display.set_mode(pyg['SCREENSIZE'])
    clear(pyg)
    pygame.display.set_caption('Tower Defense')

    sw,sh = pyg['SCREENSIZE']
    gw,gh = pyg['SIZE']
    pyg['grid'] = [ [0]*(sh//gh - 2) for i in range(sw//gw - 2) ]
    # pyg['grid'][3] = [None,None,None,0,0,0,0,0]
    # pyg['grid'] = [ [0]*8
    #                 ,[None]*7 + [0]
    #                 ,[0]*8
    #                 ,[0]+ [None]*7
    #                 ,[0]*8
    #                 ,[None]*7 + [0]
    #                 ,[0]*8
    #                 ,[0]+ [None]*7
    #              ]
    pyg['towers'] = []
    pyg['enemies'] = []
    pyg['player'] = player(3,2,0)
    update_enemy_paths(pyg)
    return pyg