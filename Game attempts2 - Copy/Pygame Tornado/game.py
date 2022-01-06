""" Tornado Game with pygame"""

import pygame
from sys import exit

#initilize pygame
pygame.init() 

#create screen, add title, add clock
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Tornado")
clock = pygame.time.Clock()

#initilize surfaces
title_font = pygame.font.Font(None, 50)
game_active = True
keys = pygame.key.get_pressed()

#creating regular surfaces
test_surface = pygame.Surface((800,500))

bedroom_surface = pygame.image.load('graphics/bedroom.png').convert()

text_surface = title_font.render('Tornado',False,'Black') 

player_surface = pygame.image.load('graphics/player.png').convert_alpha()
player_rect = player_surface.get_rect(center = (489, 187))

snake_surface = pygame.image.load('graphics/snape.png').convert()
snake_rect = snake_surface.get_rect(center = (287,111))


#to keep game running until ended in loop
while True:
    #event loop (to check for all types of player input)
    for event in pygame.event.get(): #loops through all events
        if event.type == pygame.QUIT: #the x button on window
            pygame.quit() #opposite of pygame.init(). it unitializes everything
            exit() #will exit true loop. Without this pygame.quit() will cause error
        if event.type == pygame.MOUSEMOTION: #only triggers if mouse moves
            print(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and snake_rect.collidepoint(event.pos):
            snake_rect = (700, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            snake_rect = snake_surface.get_rect(center = (287,111))                                    
            
        #if player clicks with mouse on object to pick up
    if game_active == True:
        screen.blit(test_surface, (0,0))
        screen.blit(bedroom_surface, (0,0))
        screen.blit(snake_surface, snake_rect)
        screen.blit(player_surface, player_rect)
        
        


    pygame.display.update() #updates everything
    clock.tick(60) #tells that is should not run faster than 60 frames per second. 
    