import pygame
import player_shoot
import player
import variables
import enemies
import random

pygame.init()

all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
injured_enemy_list = pygame.sprite.Group()
dead_player_list = pygame.sprite.Group()

player = player.Player()
all_sprites_list.add(player)

arrow = enemies.Arrow()
all_sprites_list.add(arrow)

pygame.display.set_caption("Space Commander")

background_image = pygame.image.load("space.jpg").convert()
 
# Loop until the user clicks the close button.
done = False
end = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

pygame.mixer.music.load("background_music.wav")
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

laser_sound = pygame.mixer.Sound("laser.wav")
font = pygame.font.SysFont('Calibri', 25, True, False)

while not done and variables.display_instructions == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            variables.instruction_page += 1
            if variables.instruction_page >= 4:
                variables.display_instructions = False
 
    # Set the screen background
    variables.screen.fill(variables.BLACK)
 
    if variables.instruction_page == 1:
        # Draw instructions, page 1
        # This could also load an image created in another program.
        # That could be both easier and more flexible.
 
        logo = pygame.image.load("logo.png")
        variables.screen.blit(logo, [0, 0])
 
        text = font.render("Click to continue", True, variables.BLACK)
        variables.screen.blit(text, [350, 670])
 
    if variables.instruction_page == 2:
        # Draw instructions, page 2
        title_screen = pygame.image.load("title_screen.png")
        variables.screen.blit(title_screen, [0, 0])
        
    if variables.instruction_page == 3:
        # Draw instructions, page 2
 
        instructions = pygame.image.load("instructions.png")
        variables.screen.blit(instructions, [0, 0]) 
        
        text = font.render("Click to continue", True, variables.WHITE)
        variables.screen.blit(text, [350, 670])         
        
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# -------- Main Program Loop -----------
while not done and not variables.dead:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.constants.USEREVENT:
            # Background Music
            pygame.mixer.music.load("background_music.wav")
            pygame.mixer.music.play()        
            
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so adjust speed.
            if event.key == pygame.K_a:
                player.image = pygame.image.load("space_ship_left.png")
                player.direction = "left"
                variables.x_speed = -5
                
            elif event.key == pygame.K_d:
                variables.x_speed = 5
                player.image = pygame.image.load("space_ship_right.png")
                player.direction = "right"
                
            elif event.key == pygame.K_w:
                variables.y_speed = -5
                
            elif event.key == pygame.K_s:
                variables.y_speed = 5
                
            elif event.key == pygame.K_SPACE:
                if not variables.dead:
                    laser_sound.play()
                    bullet = player_shoot.Player_Shoot(player.rect.x, player.rect.y, player.direction)
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)
                
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_a or event.key == pygame.K_d:
                variables.x_speed = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                variables.y_speed = 0
                
    # Change level
    if variables.in_between_levels >= True and player.rect.x > 900:
        variables.level_spawn = False
        variables.in_between_levels = False
        variables.level += 1
        player.rect.x = 0
        
    # Spawn Enemies              
    if variables.level == 1 and variables.level_spawn == False:
        variables.level_spawn = True
        
        for i in range(10):
            enemy = enemies.Enemy1()
            enemy_list.add(enemy)
            all_sprites_list.add(enemy)
            
    if variables.level == 2 and variables.level_spawn == False:
        variables.level_spawn = True
        
        for i in range(15):
            enemy = enemies.Enemy1()
            enemy_list.add(enemy)
            all_sprites_list.add(enemy)
            
    if variables.level == 3 and variables.level_spawn == False:
        variables.level_spawn = True
        
        for i in range(10):
            enemy = enemies.Enemy1()
            enemy_list.add(enemy)
            all_sprites_list.add(enemy)   
            
        for i in range(5):
            enemy = enemies.Enemy2()
            enemy_list.add(enemy)
            all_sprites_list.add(enemy)
            
            
    if variables.level == 4 and variables.level_spawn == False:
        variables.level_spawn = True
        
        for i in range(10):
            enemy = enemies.Enemy1()
            enemy_list.add(enemy)
            all_sprites_list.add(enemy)   
            
        for i in range(10):
            enemy = enemies.Enemy2()
            enemy_list.add(enemy)
            all_sprites_list.add(enemy)
            
    if variables.level == 5 and variables.level_spawn == False:
        variables.level_spawn = True
        
        for i in range(5):
            enemy = enemies.Enemy1()
            enemy_list.add(enemy)
            all_sprites_list.add(enemy)   
            
        for i in range(10):
            enemy = enemies.Enemy2()
            enemy_list.add(enemy)
            all_sprites_list.add(enemy)
            
        for i in range(5):
            enemy = enemies.Enemy3()
            enemy_list.add(enemy)
            all_sprites_list.add(enemy) 
            
    if variables.level == 6 and variables.level_spawn == False:
        variables.level_spawn = True  
            
        for i in range(10):
            enemy = enemies.Enemy2()
            enemy_list.add(enemy)
            all_sprites_list.add(enemy) 
            
        for i in range(10):
            enemy = enemies.Enemy3()
            enemy_list.add(enemy)
            all_sprites_list.add(enemy)
            
    if variables.level == 7 and variables.level_spawn == False:
        variables.level_spawn = True
        
        for i in range(1):
            boss = enemies.Boss()
            enemy_list.add(boss)
            all_sprites_list.add(boss)
            
            
    # Check if all enemies are dead
    for enemy in enemy_list:
        variables.health_total += enemy.health    
        
    if variables.health_total == 0:
        variables.in_between_levels = True  
        
    variables.health_total = 0

    # Bullet movement and detection if it goes off the screen
    for bullet in bullet_list:
        bullet.rect.x += bullet.x_change
        
    for enemy in enemy_list:
        enemy.rect.x += enemy.x_change    
        
    for bullet in bullet_list:
        if bullet.rect.x > 950:
            bullet_list.remove(bullet)
            
        elif bullet.rect.x < -50:
            bullet_list.remove(bullet)
            
    # Enemy movement and detection if it goes off the screen       
    if variables.level == 1 or variables.level == 2 or variables.level == 3 or variables.level == 4 or variables.level == 5 or variables.level == 6:   
        for enemy in enemy_list:
            if enemy.direction == "right":
                if enemy.rect.x > 1100:
                    enemy.rect.x = -500
                    enemy.choose2 = random.randrange(0, 2)
                    if enemy.choose2 == 0:
                        enemy.rect.y = random.randrange(0, 260)
                        
                    else:
                        enemy.rect.y = random.randrange(360, 630)                    
                            
            else:
                if enemy.rect.x < -200:
                    enemy.rect.x = 1400
                    enemy.choose2 = random.randrange(0, 2)
                    if enemy.choose2 == 0:
                        enemy.rect.y = random.randrange(0, 260)
                        
                    else:
                        enemy.rect.y = random.randrange(360, 630)                    
                    
    # Bullet and Enemy Detection
    for bullet in bullet_list:            
        injured_enemy_list = pygame.sprite.spritecollide(bullet, enemy_list, False)
        
        for enemy in injured_enemy_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            
    for enemy in injured_enemy_list:
        enemy.take_damage()
        
        if enemy.health <= 0:
            enemy_list.remove(enemy)
            all_sprites_list.remove(enemy)
            
        injured_enemy_list.remove(enemy)
        
    # Player death detection and reduction of lives    
    dead_player_list = pygame.sprite.spritecollide(player, enemy_list, False)
    
    for enemy in dead_player_list:
        variables.lives -= 1
        player.rect.x = 420
        player.rect.y = 330
        dead_player_list.remove(enemy)
        
    if variables.lives <= 0:
        variables.dead = True
    
    # Player Movement    
    if not variables.dead:
        player.rect.x += variables.x_speed
        player.rect.y += variables.y_speed
        
    # Level arrow appear / disappear
    if variables.in_between_levels == False:
        arrow.rect.x = 1000
        
    else:
        arrow.rect.x = 750
        
    # Player Detection if it goes off of screen
    if variables.in_between_levels == False:
        if player.rect.x > 806:
            player.rect.x = 806
            x_speed = 0
        
        elif player.rect.x < 0:
            player.rect.x = 0
            x_speed = 0
            
        elif player.rect.y > 664:
            player.rect.y = 664
            y_speed = 0
            
        elif player.rect.y < 0:
            player.rect.y = 0
            y_speed = 0
            
    # Boss Movement
    if variables.level == 7:
        if boss.direction == "right" and boss.rect.x >= 900:
            boss.direction = "left"
            boss.rect.x = 901
            boss.rect.y = random.randrange(0, 630)
            boss.x_change = -6
            boss.image = pygame.image.load("boss_left.png")
            
        elif boss.direction == "left" and boss.rect.x <= -277:
            boss.direction = "right"
            boss.rect.x = -278
            boss.rect.y = random.randrange(0, 630)
            boss.x_change = 6
            boss.image = pygame.image.load("boss_right.png")
            
    # Win/Loss Detection
    if variables.level >= 8:
        done = True
    
    elif variables.lives <= 0:
        variables.dead = True
 
    # Background image
    variables.screen.blit(background_image, [0, 0])
    
    # Draw all sprites
    all_sprites_list.draw(variables.screen)
    text = font.render("Lives Left: " + str(variables.lives), True, variables.WHITE)
    variables.screen.blit(text, [700, 10])
    
    text = font.render("Level: " + str(variables.level), True, variables.WHITE)
    variables.screen.blit(text, [550, 10])    
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)  

while not end:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
            
    variables.screen.fill(variables.WHITE)  
            
    if variables.level >= 8:
        win_screen = pygame.image.load("win_screen.png")
        variables.screen.blit(win_screen, [0, 0])
        
    else: 
        lose_screen = pygame.image.load("game_over.png")
        variables.screen.blit(lose_screen, [0, 0])
        
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)      
 
# Close the window and quit.
pygame.quit()