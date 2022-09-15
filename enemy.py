import pygame
from pathing import heapsolve
# from astar_mod import Astar

def enemy_updater(pyg):
    if int(pygame.time.get_ticks()/1000) > pyg['enemyTimer'] + 2:
        pyg['enemyTimer'] = int(pygame.time.get_ticks()/1000)
        e = enemy(1, 2, [0, 0])
        e.generate_path(pyg)
        # print(e.path)
        pyg['enemies'].append(e)
    for e in pyg['enemies']:
        if e.touchdown == False:
            e.draw(pyg)
            if not pyg['paused']:
                e.update(pyg)

def update_enemy_paths(pyg):
    # pyg['astar'] = Astar( pyg['grid'] )
    # print( pyg['astar'] )
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

    def draw(self, pyg):
        # left, top, width, height == self.pos + self.size
        worldpos = [ (1 + self.pos[0]) * pyg['SIZE'][0], (1 + self.pos[1]) * pyg['SIZE'][1] ]
        pygame.draw.rect(pyg['DISPLAYSURF'], pyg['RED'], worldpos + pyg['SIZE'], 4)

    def get_gridpos(self):
        x,y = self.pos
        return int(x+0.5), int(y+0.5)

    def generate_path(self, pyg):
        # pyg['astar'] = Astar( pyg['grid'] )
        # s = len( pyg['grid'] ) - 1
        # self.path = pyg['astar'].run(self.get_gridpos(),[0,7])
        self.path = heapsolve(pyg['grid'], self.pos, [7,0])
        # print(self.path)

    def dist(self):
        dx = self.path[0][0] - self.pos[0]
        dy = self.path[0][1] - self.pos[1]
        d = abs(dx) + abs(dy)

    # def prune(self):
    def draw_path(self, pyg):
        if self.path != None:
            for p in self.path:
                worldpos = [ (1 + p[1]) * pyg['SIZE'][0], (1 + p[0]) * pyg['SIZE'][1] ]
                pygame.draw.rect(pyg['DISPLAYSURF'], pyg['GREEN'], worldpos + pyg['SIZE'], 4)

    def update(self, pyg):
        # if self.pos[0] == self.path[-1][0] and self.pos[1] == self.path[-1][1]:
        if self.path:
            if len(self.path) == 1:
                self.touchdown = True
                print('enemies are getting through!!!')
                pyg['player'].health = pyg['player'].health - 1
            if len(self.path) > 0:
                direction = [ self.path[0][0] - self.pos[0], self.path[0][1] - self.pos[1]]
                dsum = abs(direction[0]) + abs(direction[1])
                if dsum < 0.1:
                    self.path = self.path[1:]
                    return
                # print( "*"*80 )
                # print( direction )
                direction[0] = direction[0]/dsum
                direction[1] = direction[1]/dsum
                # print( direction )
                self.pos[0] +=  direction[0] * 0.02
                self.pos[1] +=  direction[1] * 0.02
