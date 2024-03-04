import pygame
import player
import variables

class Player_Shoot(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):            
        super().__init__()
        self.direction = direction
        
        if self.direction == "right":
            self.image = pygame.image.load("laser_right.png")
            self.rect = self.image.get_rect()
            self.rect.x = x + 90
            self.rect.y = y + 23
            self.x_change = 10
            
        else:
            self.image = pygame.image.load("laser_left.png")
            self.rect = self.image.get_rect()
            self.rect.x = x - 25
            self.rect.y = y + 23
            self.x_change = -10
        
        self.image.set_colorkey(variables.WHITE)
        
        def update(self):
            self.rect.x += self.x_change
            