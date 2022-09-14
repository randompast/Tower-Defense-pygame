import pygame

class enemy():
    def __init__(self, damage, health, pos):
        self.damage = damage
        self.health = health
        self.pos = pos
        self.size = [50,50]

    def draw(self, pyg):
        # left, top, width, height == self.pos + self.size
        pygame.draw.rect(pyg['DISPLAYSURF'], pyg['RED'], self.pos + pyg['SIZE'], 4)

    def update(self, pyg):
        self.pos = [ (v+3)%pyg['SCREENSIZE'][i] for i,v in enumerate(self.pos)]