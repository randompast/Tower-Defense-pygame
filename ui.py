import pygame

def draw_ui(pyg):
    pygame.font.init()
    my_font = pygame.font.Font(pygame.font.get_default_font(), 20)
    text_surface = my_font.render('Health: ' + str(pyg.player.health), False, (0, 0, 0))
    pyg.DISPLAYSURF.blit(text_surface, (pyg.grid.res[0]//5,5))

    pyg.grid.draw_circ(pyg, pyg.goal, [0.5,0.5], 1, (140,100,200))
