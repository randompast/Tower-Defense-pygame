import pygame

def draw_ui(pyg):
    my_font = pygame.font.SysFont('Comic Sans MS', 20)
    text_surface = my_font.render('Health: ' + str(pyg['player'].health), False, (0, 0, 0))
    pyg['DISPLAYSURF'].blit(text_surface, (0,0))