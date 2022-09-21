import pygame
from enemy import update_enemy_paths

def tower_spawner(pyg, gpos):
    if pyg.grid.inbounds(gpos):
        if pyg.grid.grid[gpos[1]][gpos[0]] == 0:
            pyg.towers += [tower(1, 2, gpos)]
            pyg.grid.grid[gpos[1]][gpos[0]] = 1
            update_enemy_paths(pyg)
        else:
            for i in range(len(pyg.towers)):
                req = pyg.towers[i].pos[0] == gpos[0]
                yeq = pyg.towers[i].pos[1] == gpos[1]
                if req and yeq:
                    del pyg.towers[i]
                    pyg.grid.grid[gpos[1]][gpos[0]] = 0
                    update_enemy_paths(pyg)
                    return

def tower_updater(pyg):
    for i, tower in enumerate(pyg.towers):
        tower.draw(pyg)

class tower():
    def __init__(self, damage, health, pos):
        self.damage = damage
        self.health = health
        self.pos = pos

    def draw(self, pyg):
        pyg.grid.draw_circ(pyg, self.pos, [0.5,0.5], 1, (0,0,255))

    def update(self, pyg):
        # shoot at enemies? create projectiles?
        pass
