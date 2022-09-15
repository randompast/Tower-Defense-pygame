import pygame
from astar_python import Astar

def enemy_updater(pyg):
    if int(pygame.time.get_ticks()/1000) > pyg['enemyTimer'] + 2:
        pyg['enemyTimer'] = int(pygame.time.get_ticks()/1000)
        e = enemy(1, 2, [0, 3])
        e.generate_path(pyg)
        pyg['enemies'].append(e)
    for e in pyg['enemies']:
        if e.touchdown == False:
            e.draw(pyg)
            e.update(pyg)

def update_enemy_paths(pyg):
    pyg['astar'] = Astar(pyg['grid'])
    for e in pyg['enemies']:
        e.generate_path(pyg)

class enemy():
    def __init__(self, damage, health, pos):
        self.damage = damage
        self.health = health
        self.pos = pos
        self.size = [50,50]
        self.touchdown = False
        self.path = []
        self.steps = 0

    def draw(self, pyg):
        # left, top, width, height == self.pos + self.size
        worldpos = [ self.pos[0]*pyg['SIZE'][0], self.pos[1]*pyg['SIZE'][1] ]
        pygame.draw.rect(pyg['DISPLAYSURF'], pyg['RED'], worldpos + pyg['SIZE'], 4)

    def get_gridpos(self):
        x,y = self.pos
        return int(x), int(y)

    def generate_path(self, pyg):
        self.path = pyg['astar'].run(self.get_gridpos(),[4,7])

    def update(self, pyg):
        self.steps += 0.01
        if self.steps > 1:
            self.steps = 0
            self.path = self.path[1:]

        # if self.pos[0] == self.path[-1][0] and self.pos[1] == self.path[-1][1]:
        if len(self.path) < 2 and not self.touchdown:
            self.touchdown = True
            print('enemies are getting through!!!')
            pyg['player'].health = pyg['player'].health - 1
        else:
            self.pos[0] = self.path[0][0] * (1 - self.steps) + self.steps * self.path[1][0]
            self.pos[1] = self.path[0][1] * (1 - self.steps) + self.steps * self.path[1][1]