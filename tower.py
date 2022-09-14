import pygame

def tower_spawner(pyg, pos):
    sw, sh = pyg['SCREENSIZE']
    gw, gh = pyg['SIZE']
    x, y = pos[0]//gw,  pos[1]//gh
    Mx, My = sw//gw,  sh//gh
    pos = [x*gw, y*gh]
    if 0 < y < My - 1 and 0 < x < Mx - 1:
        if pyg['grid'][x][y] == 0:
            pyg['towers'] += [tower(1, 2, pos)]
            pyg['grid'][x][y] = 1
        else:
            for i in range(len(pyg['towers'])):
                xeq = pyg['towers'][i].pos[0] == pos[0]
                yeq = pyg['towers'][i].pos[1] == pos[1]
                if xeq and yeq:
                    del pyg['towers'][i]
                    pyg['grid'][x][y] = 0
                    return

class tower():
    def __init__(self, damage, health, pos):
        self.damage = damage
        self.health = health
        self.pos = pos

    def draw(self, pyg):
        # left, top, width, height == self.pos + self.size
        pygame.draw.rect(pyg['DISPLAYSURF'], pyg['BLUE'], self.pos + pyg['SIZE'], 4)
