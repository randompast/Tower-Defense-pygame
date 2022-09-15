import pygame

class enemy():
    def __init__(self, damage, health, pos):
        self.damage = damage
        self.health = health
        self.pos = pos
        self.size = [50,50]
        self.touchdown = False

    def draw(self, pyg):
        # left, top, width, height == self.pos + self.size
        pygame.draw.rect(pyg['DISPLAYSURF'], pyg['RED'], self.pos + pyg['SIZE'], 4)

    def update(self, pyg):
        self.pos = [self.pos[0]+5, self.pos[1]]
        if self.pos[0] > pyg['SCREENSIZE'][0] :
            self.touchdown = True
            print('enemies are getting through!!!')
            pyg['player'].health = pyg['player'].health - 1
