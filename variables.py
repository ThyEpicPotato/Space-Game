import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
x_speed = 0
y_speed = 0
size = (900, 700)
level = 1
screen = pygame.display.set_mode(size)
dead = False
in_between_levels = False
level_spawn = False
health_total = 1
lives = 3
display_instructions = True
instruction_page = 1