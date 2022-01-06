# -*- coding: utf-8 -*-
"""
Pygame Notes v2.0
https://www.youtube.com/watch?v=AY9MnQ4x3zk

"""
#import libraries
import pygame #may have to be pip installed
from sys import exit #to exit game
from random import randint, choice

class Player(pygame.sprite.Sprite):
    """surface and rectangle combined"""
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0
        
        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.3)
        
                
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
    
    def apply_gravity(self):
        self.gravity +=1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
            
    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
            
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()
    
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        
        if type == 'fly':
            fly_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
            self.frames = [fly_1,fly_2]
            y_pos = 210
        else:
            snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1,snail_2]
            y_pos  = 300
            
        self.animation_index = 0
        
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))
        
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()    
        self.rect.x -= 6
        self.destroy()
        
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
            
        
# create score/time since start of current game
def display_score():
    """ function used to display time in game"""
    
    current_time = int(pygame.time.get_ticks()/ 1000)  - start_time #without -start_time it doesnt restart timer from restarting the game
    score_surface = test_font.render(f'Score: {current_time}', False, (64,64,64)) #f string converts it to string
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time
    

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            
            if obstacle_rect.bottom == 300: screen.blit(snail_surf, obstacle_rect)
            else: screen.blit(fly_surf, obstacle_rect)
        
        #copy each item in list that is above 0
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        
        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
            
    return True
                
def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group, False):
        obstacle_group.empty()
        return False
    else: return True
    
    
def player_animation():
    global player_surface, player_index
    
    if player_rect.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surface = player_walk[int(player_index)]
    #play walking animation if player is on floor
    
    #display jump if not on floor

    
#initilize pygame and its subparts
pygame.init()

#create window (width,height)
screen = pygame.display.set_mode((800, 400))
#name the window
pygame.display.set_caption("Title")
#limit frame rates
clock = pygame.time.Clock() #used in conjunction with clock.tick(60) at end of program

#create font for game to use
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

#set game to active
game_active = False
#set start time at 0
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.2)
bg_music.play(loops = -1)

player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()


#Obsticles


obstacle_rect_list = []


#intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2) #scales player image up to (width, height)
player_stand_rect = player_stand.get_rect(center = (400,200))

#intro text
intro_text = test_font.render('Runner', False, 'Black')
intro_instructions = test_font.render('Press Spacebar to jump', False, 'Black')
intro_rect = intro_text.get_rect(center = (400, 80))
instructions_rect = intro_instructions.get_rect(center = (400, 330))

#timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200)

#create background surfaces
sky_surface= pygame.image.load('graphics/Sky.png').convert() #converts the image to python can use more easily
ground_surface = pygame.image.load('graphics/ground.png').convert()


#game loop to keep game running until want to exit
while True:
    #event loop to check for all types of player input
    for event in pygame.event.get(): #loops through all events
        #exit game if click on x on window
        if event.type == pygame.QUIT:
            pygame.quit() #opposite of pygame.init(). Uninitilizes everthing pygame
            exit()
            
        #looping for when game is active
        if game_active == True:
            
            #create timed intervals where enemy spawns
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))
                
                    
        #for when game is over
        else:
            #replay game after it ends
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
               
                
                #used to restart timer to replay
                start_time = int(pygame.time.get_ticks()/ 1000) 
            
        
    #rest of game loop
    if game_active:
        #place surface on display surfaces
        screen.blit(ground_surface, (0,300))
        screen.blit(sky_surface, (0,0))
        
        #display score (call function)
        score = display_score()

        
        #make player move and jump

        player.draw(screen)
        #update the player to be able to move
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()
        
        
        #obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        #end game if player touches snail

        game_active = collision_sprite()
    # what happens when game ends
    else:
        screen.fill((94, 129,162)) 
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        
        # player_rect.midbottom = (80, 300)
        player_gravity = 0
        
        score_message = test_font.render(f'Score: {score}', False, (111,196,169))
        score_message_rect = score_message.get_rect(center = (400, 330))
        screen.blit(intro_text, intro_rect)
        
        if score == 0: screen.blit(intro_instructions, instructions_rect)
        else: screen.blit(score_message, score_message_rect)
    #update the display each loop
    pygame.display.update()
    
    #have the game not run faster than 60 frames per second
    clock.tick(60)
    
    
        
        