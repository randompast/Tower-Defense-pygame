import pygame
from pathing import heapsolve
import random

def enemy_updater(pyg):
    if not pyg.paused and int(pygame.time.get_ticks()/1000) > pyg.enemyTimer + 1:
        if len( pyg.enemies ) < 5:
            pyg.enemyTimer = int(pygame.time.get_ticks()/1000)
            e = enemy(1, 2, [0, 0])
            e.generate_path(pyg)
            pyg.enemies.append(e)
        # else:
        #     pyg.enemies[0].randomize_position(pyg)
        #     pyg.enemies[0].generate_path(pyg)
    for i,e in enumerate(pyg.enemies):
        if e.touchdown == False:
            e.draw(pyg)
            e.draw_path(pyg)
            if not pyg.paused:
                e.update(pyg)
        else:
            del pyg.enemies[i]

def update_enemy_paths(pyg):
    for e in pyg.enemies:
        e.generate_path(pyg)

class enemy():
    def __init__(self, damage, health, pos):
        self.damage = damage
        self.health = health
        self.pos = pos
        self.size = [5,5]
        self.touchdown = False
        self.path = []
        self.speed = 0.04

    def draw(self, pyg):
        pyg.grid.draw_circ(pyg, self.pos, [0.5,0.5], 0.5, (255,0,0))
        # pyg.grid.draw_circ(pyg, self.get_gridpos(), [0.5,0.5], 0.5, (255,0,0))

    def get_gridpos(self):
        r,c = self.pos
        return int(c+0.5), int(r+0.5)

    def generate_path(self, pyg):
        self.path = [i[::-1] for i in heapsolve(pyg.grid.grid, self.get_gridpos(), pyg.goal[::-1])]
        self.prune()

    def randomize_position(self, pyg):
        self.pos[0] = random.randint(0, len(pyg.grid)-1)
        self.pos[1] = random.randint(0, len(pyg.grid)-1)
        if pyg.grid[self.pos[1]][self.pos[0]] != 0:
            # print(f"collision at {self.pos}")
            self.randomize_position(pyg)

    def random_walk(self):
        self.pos[0] += random.uniform(-1,1)*self.speed
        self.pos[1] += random.uniform(-1,1)*self.speed

    def distance(self, a, b):
        dx = a[0] - b[0]
        dy = a[1] - b[1]
        return abs(dx) + abs(dy)

    def dist(self):
        return self.distance(self.pos, self.path[0])

    def velocity(self):
        if len( self.path ) > 0:
            dx = self.path[0][0] - self.pos[0]
            dy = self.path[0][1] - self.pos[1]
            d = abs(dx) + abs(dy)
            if d > 0:
                return [self.speed*dx/d, self.speed*dy/d]
        return [-10,-10]

    def prune(self):
        if self.dist() < 1 and len(self.path) > 1:
            # print('pruning')
            self.path = self.path[1:]
            self.prune()

    def draw_path(self, pyg):
        if self.path != None:
            for x,y in self.path:
                pyg.grid.draw_circ(pyg, [x,y], [0.5,0.5], 0.1, (0,200,0,10))

    def update(self, pyg):
        if self.path[-1][0] == pyg.goal[0] and self.path[-1][1] == pyg.goal[1]:
            if self.distance(self.pos, pyg.goal) < self.speed and self.touchdown == False:
                self.touchdown = True
                print('enemies are getting through!!!')
                pyg.player.health = pyg.player.health - 1
            if len(self.path) > 0:
                v = self.velocity()
                if sum(v) > -20 and self.dist() > self.speed:
                    self.pos[0] +=  v[0]
                    self.pos[1] +=  v[1]
                if len(self.path) > 1 and self.dist() <= self.speed:
                    self.path = self.path[1:]
