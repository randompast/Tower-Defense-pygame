import pygame

def draw_ui(pyg):
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 20)
    text_surface = my_font.render('Health: ' + str(pyg['player'].health), False, (0, 0, 0))
    pyg['DISPLAYSURF'].blit(text_surface, (0,0))

    worldpos = [ (1.5 + pyg['goal'][1]) * pyg['SIZE'][1], (1.5 + pyg['goal'][0]) * pyg['SIZE'][0] ]
    pygame.draw.circle(pyg['DISPLAYSURF'], (140,100,200), worldpos, 15)
