""" Peg Game with pygame"""

import pygame
from sys import exit

class Peg(pygame.sprite.Sprite):
    def __init__(self,xpos, ypos, id):
        super(Peg, self).__init__()
        self.image = pygame.image.load('graphics/peg.png').convert()
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        self.id = id
        self.linkReady = False
        self.links = []




#initilize pygame
pygame.init() 

#create screen, add title, add clock
size = (800,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Peg Game")
clock = pygame.time.Clock()

#initilize surfaces
title_font = pygame.font.Font(None, 50)
game_active = True

peg_list = pygame.sprite.Group()

#creating regular surfaces
test_surface = pygame.Surface((800,400))

triangle = pygame.image.load('graphics/triangle_full.png').convert()

text_surface = title_font.render('Peg Game',False,'Black') 







# # peg1_surface = pygame.image.load('graphics/peg.png').convert_alpha()
# # peg1_rect = peg1_surface.get_rect(center = (400,100))
# peg2_surface = pygame.image.load('graphics/peg.png').convert_alpha()
# peg2_rect = peg2_surface.get_rect(center = (370,150))
# peg3_surface = pygame.image.load('graphics/peg.png').convert_alpha()
# peg3_rect = peg3_surface.get_rect(center = (435, 150))
# peg4_surface = pygame.image.load('graphics/peg.png').convert_alpha()
# peg4_rect = peg4_surface.get_rect(center = (345,200))
# peg5_surface = pygame.image.load('graphics/peg.png').convert_alpha()
# peg5_rect = peg5_surface.get_rect(center = (400, 200))
# peg6_surface = pygame.image.load('graphics/peg.png').convert_alpha()
# peg6_rect = peg6_surface.get_rect(center = (465,200))
# peg7_surface = pygame.image.load('graphics/peg.png').convert_alpha()
# peg7_rect = peg7_surface.get_rect(center = (315, 250))
# peg8_surface = pygame.image.load('graphics/peg.png').convert_alpha()
# peg8_rect = peg8_surface.get_rect(center = (370,250))
# peg9_surface = pygame.image.load('graphics/peg.png').convert_alpha()
# peg9_rect = peg9_surface.get_rect(center = (435,250))
# peg10_surface = pygame.image.load('graphics/peg.png').convert_alpha()
# peg10_rect = peg10_surface.get_rect(center =(495,250))
# peg11_surface = pygame.image.load('graphics/peg.png').convert_alpha()
# peg11_rect = peg11_surface.get_rect(center = (285,300))
# peg12_surface = pygame.image.load('graphics/peg.png').convert_alpha()
# peg12_rect = peg12_surface.get_rect(center = (400, 300))
# peg13_surface = pygame.image.load('graphics/peg.png').convert_alpha()
# peg13_rect = peg13_surface.get_rect(center = (345,300))
# peg14_surface = pygame.image.load('graphics/peg.png').convert_alpha()
# peg14_rect = peg14_surface.get_rect(center = (465,300))
# peg15_surface = pygame.image.load('graphics/peg.png').convert_alpha()
# peg15_rect = peg15_surface.get_rect(center = (530,300))


#to keep game running until ended in loop
while True:
    #event loop (to check for all types of player input)
    for event in pygame.event.get(): #loops through all events
        if event.type == pygame.QUIT: #the x button on window
            pygame.quit() #opposite of pygame.init(). it unitializes everything
            exit() #will exit true loop. Without this pygame.quit() will cause error
        if game_active == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                peg_list.add(Peg(x,y,len(peg_list)+1))
                if event.button == 3:
                    peg_list.add(Peg(x,y,len(peg_list)+1))
                elif event.button == 1:
                    for peg in peg_list:
                        if peg.rect.collidepoint(pos):
                            peg.clicked = True
                elif event.button == 2:
                    for peg in peg_list:
                        if peg.rect.collidepoint(pos):
                            peg.linkReady = True
                            count = 0
                            links = []
                            for peg in peg_list:
                                if peg.linkReady == True:
                                    count +=1
                                    links.append(peg.id)
                            if count == 2:
                                for peg in peg_list:
                                    if peg.linkReady == True:
                                        peg.linkReady = False
                                        count += 1
                                        peg.links += links
            if event.type == pygame.MOUSEBUTTONUP:
                for peg in peg_list:
                    peg.clicked = False
                drag_id = 0
        
    for peg in peg_list:
        if peg.clicked == True:
            pos = pygame.mouse.get_pos()
            peg.rect.x = pos[0]-(peg.rect.width/2)
            peg.rect.y = pos[1]-(peg.rect.height/2)
            



    
        
    #     # screen.blit(peg1_surface, peg1_rect)
    #     screen.blit(peg2_surface, peg2_rect)
    #     screen.blit(peg3_surface, peg3_rect)
    #     screen.blit(peg4_surface, peg4_rect)
    #     screen.blit(peg5_surface, peg5_rect)
    #     screen.blit(peg6_surface, peg6_rect)
    #     screen.blit(peg7_surface, peg7_rect)
    #     screen.blit(peg8_surface, peg8_rect)
    #     screen.blit(peg9_surface, peg9_rect)
    #     screen.blit(peg10_surface, peg10_rect)
    #     screen.blit(peg11_surface, peg11_rect)
    #     screen.blit(peg12_surface, peg12_rect)
    #     screen.blit(peg13_surface, peg13_rect)
    #     screen.blit(peg14_surface, peg14_rect)
    #     screen.blit(peg15_surface, peg15_rect)
        
    #---Drawing Code----
    screen.fill('Black')    
    screen.blit(text_surface, (0,0))
    screen.blit(triangle, (0,3))
    
    # Updates the screen 
    pygame.display.update() #updates everything
    
    #-----Limits game to 60 fps------
    clock.tick(60) #tells that is should not run faster than 60 frames per second. 
    