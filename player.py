import pygame
import player_shoot
import variables

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.direction = "right"
        self.image = pygame.image.load("space_ship_right.png")
        self.image.set_colorkey(variables.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 420
        self.rect.y = 330        