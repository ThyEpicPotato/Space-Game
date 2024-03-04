import pygame
import variables
import random

class Enemy1(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.choose1 = random.randrange(0, 2)
        self.choose2 = random.randrange(0, 2) 
        self.health = 1
        
        if self.choose1 == 0:
            self.direction = "right"
            
        else:
            self.direction = "left"
            
        if self.direction == "right":
            self.image = pygame.image.load("enemy1_right.png")
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(-1800, -200)
            self.x_change = 4
            
            if self.choose2 == 0:
                self.rect.y = random.randrange(0, 260)
                
            else:
                self.rect.y = random.randrange(360, 630)
            
        else:
            self.image = pygame.image.load("enemy1_left.png")
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(1000, 2800)
            self.x_change = -4
            
            if self.choose2 == 0:
                self.rect.y = random.randrange(0, 260)
                
            else:
                self.rect.y = random.randrange(360, 630)            
            
    def take_damage(self):
        self.health -= 1
            
class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.choose1 = random.randrange(0, 2)
        self.choose2 = random.randrange(0, 2) 
        self.health = 2
                
        if self.choose1 == 0:
            self.direction = "right"
            
        else:
            self.direction = "left"
                
        if self.direction == "right":
            self.image = pygame.image.load("enemy2_right.png")
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(-1800, -200)
            self.rect.y = random.randrange(0, 630)
            self.x_change = 4
            
            if self.choose2 == 0:
                self.rect.y = random.randrange(0, 260)
                
            else:
                self.rect.y = random.randrange(360, 630)            
            
        else:
            self.image = pygame.image.load("enemy2_left.png")
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(1000, 2800)
            self.rect.y = random.randrange(0, 630)
            self.x_change = -4
            
            if self.choose2 == 0:
                self.rect.y = random.randrange(0, 260)
                
            else:
                self.rect.y = random.randrange(360, 630)            
            
    def take_damage(self):
        self.health -= 1
        
class Enemy3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.choose1 = random.randrange(0, 2)
        self.choose2 = random.randrange(0, 2) 
        self.health = 3
                
        if self.choose1 == 0:
            self.direction = "right"
            
        else:
            self.direction = "left"
                
        if self.direction == "right":
            self.image = pygame.image.load("enemy3_right.png")
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(-1800, -200)
            self.rect.y = random.randrange(0, 630)
            self.x_change = 4
            
            if self.choose2 == 0:
                self.rect.y = random.randrange(0, 260)
                
            else:
                self.rect.y = random.randrange(360, 630)            
            
        else:
            self.image = pygame.image.load("enemy3_left.png")
            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(1000, 2800)
            self.rect.y = random.randrange(0, 630)
            self.x_change = -4
            
            if self.choose2 == 0:
                self.rect.y = random.randrange(0, 260)
                
            else:
                self.rect.y = random.randrange(360, 630)            
            
    def take_damage(self):
        self.health -= 1
        
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 10        
        self.direction = "left"
        self.image = pygame.image.load("boss_left.png")
        self.rect = self.image.get_rect()
        self.rect.x = 901
        self.rect.y = random.randrange(0, 630)
        self.x_change = -6
            
    def take_damage(self):
        self.health -= 1
        
class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("arrow.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 312.5
        