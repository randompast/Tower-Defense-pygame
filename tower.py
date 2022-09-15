import pygame
from enemy import update_enemy_paths

def tower_spawner(pyg, pos):
    sw, sh = pyg['SCREENSIZE']
    gw, gh = pyg['SIZE']
    c, r = pos[0]//gh, pos[1]//gw
    Mr, Mc = sw//gw,  sh//gh
    pos = [c*gw, r*gh]
    if 0 < c < Mc - 1 and 0 < r < Mr - 1:
        if pyg['grid'][r-1][c-1] == 0:
            pyg['towers'] += [tower(1, 2, pos)]
            pyg['grid'][r-1][c-1] = None
            update_enemy_paths(pyg)
        else:
            for i in range(len(pyg['towers'])):
                req = pyg['towers'][i].pos[0] == pos[0]
                yeq = pyg['towers'][i].pos[1] == pos[1]
                if req and yeq:
                    del pyg['towers'][i]
                    pyg['grid'][r-1][c-1] = 0
                    return

def tower_updater(pyg):
    for i, tower in enumerate(pyg['towers']):
        tower.draw(pyg)

class tower():
    def __init__(self, damage, health, pos):
        self.damage = damage
        self.health = health
        self.pos = pos

    def draw(self, pyg):
        # left, top, width, height == self.pos + self.size
        pygame.draw.rect(pyg['DISPLAYSURF'], pyg['BLUE'], self.pos + pyg['SIZE'], 4)

    def update(self, pyg):
        # shoot at enemies? create projectiles?
        pass
