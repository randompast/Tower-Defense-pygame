import pygame
from enemy import update_enemy_paths


class tower():
    def __init__(self, damage, health, pos, speed, range):
        self.damage = damage
        self.health = health
        self.pos = pos
        self.speed = speed
        self.range = range

    def draw(self, pyg):
        pyg.grid.draw_circ(pyg, self.pos, [0.5, 0.5], 1, (0, 0, 255))

    def shoot(self, pyg, enemy_index):
        if not pyg.paused and int(pygame.time.get_ticks()/1000):
            print('shooting enemy')
            pyg.enemies[enemy_index].health = pyg.enemies[enemy_index].health - self.damage
            if pyg.enemies[enemy_index].health < 1:
                print('enemy as been destroyed')
                del pyg.enemies[enemy_index]
            # find nearest enemy

    def find_nearest_enemy(self, pyg):
        for enemy_index, e in enumerate(pyg.enemies):
            print(self.pos)
            print(enemy_index)
            if self.range > (self.pos[0] - pyg.enemies[enemy_index].pos[0]):
                self.shoot(pyg, enemy_index)


def tower_spawner(pyg, gpos):
    if pyg.grid.inbounds(gpos):
        if pyg.grid.grid[gpos[1]][gpos[0]] == 0:
            pyg.towers += [tower(1, 1, gpos, 1, 2)]
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
        tower.find_nearest_enemy(pyg)
