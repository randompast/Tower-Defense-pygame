import pygame

def tower_spawner(pyg, pos):
    gw, gh = pyg['SIZE']
    x, y = pos[0]//gw,  pos[1]//gh
    if not pyg['grid'][x][y]:
        pos = [x*gw, y*gh]
        pyg['towers'] += [tower(1, 2, pos)]
        pyg['grid'][x][y] = 1
        print(f'added tower at {x},{y}')

class tower():
    def __init__(self, damage, health, pos):
        self.damage = damage
        self.health = health
        self.pos = pos

    def draw(self, pyg):
        # left, top, width, height == self.pos + self.size
        pygame.draw.rect(pyg['DISPLAYSURF'], pyg['BLUE'], self.pos + pyg['SIZE'], 4)
