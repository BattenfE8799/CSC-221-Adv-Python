"""
Pygame notes
"""

""" What makes a video game
1. Checking player input(the event loop)
2. Use that information to place elements on the screen
    creates 1 image
start at 1 again.
30-60 per min
"""

""" What pygame actually does
1. Pygame helps you draw images (and play sounds)
2. Check for player input (input() stops your code and thus is useless for games)
3. other gamedev tools like collisions, creating text, timers, etc.
"""

""" 
Not used for commercial games
"""

"""
used to help you learn how to solve a ton a problems, can easily switch to other engines
"""
""" Surfaces
display surface- game window anything displayed goes here
-- must be unique
-- is always visible
regular surface- a single image (something imported, rendered text, or a plain color)
--needs to be put on display surface to be visible
--- flexible amount, 
---only displayed when connect to the display surface
"""


"""
displaying:
    400 height 800 width/length
    its a coordinate system
    0,0 is in top left
    right is x
    down is y
    the surface coords is the top left of the surface
"""

""" creating text
1.create image of the text
2. place it on the display surface
1. create a font(text size and style)
2. write text on a surface
3. put surface on surface
"""
"""
animation:
screen.blit(snail_surface,(600,250)) numbers make it static
increase snail position by 1
"""

""" rectangles
1. precise positioning of surfaceses
2. basic collisions
3. drawing with pygame.draw
-
image information is placed on surface
position information is placed on a rectangle
use both to create sprites
----
can make using tupe (x,y) or indivudual values
"""
""" Collision
checking if 1 rectangle intersects with another
rect1.collidepoint((x,y)) 
--checks if one point collides with rectangle. used with mouse points
"""
""" Mouse
rect1.collidepoint((x,y))
getting mouse position by targeting with pygame.mouse or an event loop
pygame.mouse
gets info on where mouse is, clicks, visibility etc
event loop
gets mousemotion, clicks, etc
"""
"""Colors
1. RGB (red green blue) mix them and get custom color between 0 and 255 for each
2. Hexadecimal #rrggbb between 00 and ff
"""
"""movement of player
1. keyboard input
--pygame.key or loop
2. jump +gravity
3. creating a floor

most efficent for game
Button press then mouse position/collision = jump
not mouse pos/collision = jump
"""
"""
when using classes you want the controls inside the relevant class. pygame.mouse and pygame.keys are great for that
"""
"""
create floor:
    inefficeint by checking collision between player and floor
    
"""
"""TIME
pygame.time.get_ticks()
1.update score on every frame
2. put that on a surface
3. display that surface
"""
""" Transforming surfaces
how to scale, rotate etc surfaces


"""

""" displaying score in the game over screen
1. we store the score in a function
2. current_time needs to be global or returned
3. 

"""
"""Better enemy logic
spawning multiple obstacles
-timers
--create a customer user event that is triggered by pygame at certain time intervals
1. create custome event
2. tell pygame to trigger that event continuously
3. add code in the event loop

1.create a list of obstacle rectangles
2. everytime the timer triggers we add a new rectablge to that list
3. we move every rectangle in that list to the left on every frame
4. we delete rectangles too far left
"""

""" Sprite class
create sprite
place sprites in group or groupSingle
draw/update all sprites in that group

GROUPS:
    Group:
        A group for multiple sprites
    GroupSingle:
    a group for a single sprite
"""
#create a window 
import pygame
from sys import exit

def display_score():
    current = int(pygame.time.get_ticks()/ 1000) - start_time 
    # current = pygame.time.get_ticks() #gets time from when started, not when game restarts
    score_surface = test_font.render(f'{current}', False, (64,64,64)) #f string converts it to string
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    
    
    
    
    
pygame.init() #starts up pygame and all the sub-parts of it that you need to make a game


#creates window
#(width, height)
screen = pygame.display.set_mode((800, 400))# the display surface
pygame.display.set_caption("Runner") # creates title in screeen bar
clock = pygame.time.Clock() #used to limit frame rates

#test_font = pygame.font.Font(None, 50) #font type, font size #creates font surface
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) #can load font into game like graphic


game_active = False
start_time = 0


snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha() #removing alpha values from convert
# snail_x_pos = 600 #makes default x position 600
snail_rect = snail_surface.get_rect(bottomright = (600, 300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300)) # position, (x,y)draws rectangle around surface
player_gravity = 0 #putting negative would create jump
#intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand_scaled = pygame.transform.scale(player_stand, (200, 400)) #scales player image up to (width, height)
player_stand_rect = player_stand_scaled.get_rect(center = (400,200))


#creating regular surfaces
# test_surface = pygame.Surface((100,200)) #creates regular surface
# test_surface.fill('Red') #to add color to the created surface
sky_surface= pygame.image.load('graphics/Sky.png').convert() #converts the image to python can use more easily

ground_surface = pygame.image.load('graphics/ground.png').convert()

#score_surface = test_font.render('My game',False,'Black').convert() #text, AntiAliasing (smoothing edjes of text), color 
# score_surface = test_font.render('My game',False,(64,64,64)).convert() 
# score_rect = score_surface.get_rect(center = (400,50))


#to keep game running until ended in loop
while True:
    #event loop (to check for all types of player input)
    for event in pygame.event.get(): #loops through all events
        if event.type == pygame.QUIT: #the x button on window
            pygame.quit() #opposite of pygame.init(). it unitializes everything
            exit() #will exit true loop. Without this pygame.quit() will cause error
            
            
        # if event.type == pygame.MOUSEMOTION: #only triggers if mouse moves
        #     print(event.pos)
        # if event.type == pygame.MOUSEBUTTONDOWN: #could also be MOUSEBUTTONUP to check if released button
        #     print(event.pos)
        if game_active == True:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                    if player_rect.collidepoint(event.pos): #if mouse collides with player rectangle 
                        player_gravity = -20
            #check if any button was pressed then check if a speficic key was pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                        player_gravity = -20
                
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks()/ 1000) 
        # if event.type == pygame.KEYUP: 
        #     print('up') 
    
    if game_active:
        #places surface on display surface at coords
        screen.blit(ground_surface, (0,300))
        screen.blit(sky_surface, (0,0)) #stands for block image transer. puts 1 surface on another surface  
        
        # pygame.draw.rect(screen, '#c0e8ec',score_rect)
        # pygame.draw.rect(screen, '#c0e8ec',score_rect,10)
        # pygame.draw.rect(screen, 'Pink',score_rect)
        # pygame.draw.rect(screen, 'Pink',score_rect,10) # surface to draw, color, to draw the rectangle for score_rect
        #pygame.draw.line(screen,'Gold', (0,0), (800, 400), 10)
        #pygame.draw.line(screen, 'Gold', (0,0), pygame.mouse.get_pos(), 10) #surface to draw on, color, start point, end point (tuples), width
        #pygame.draw.ellipse(screen, 'Brown', pygame.Rect(left, top, width, height) )#creates circle
        # screen.blit(score_surface,score_rect)
        display_score()
        
        snail_rect.x -= 4
        if snail_rect.right <=0: snail_rect.left = 800 #works better with positioning
        #snail_x_pos -=4 #has the snail move by moving its position each time the loop runs
        #if snail_x_pos < -100: snail_x_pos = 800 #moves the snail to the right side of the screen after it goes to far left
        screen.blit(snail_surface,snail_rect) #creates snail enemy 
        
        #player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        #player_rect.left += 1 #makes player move to left automatically
        #print(player_rect.left) #used to measure positions
        screen.blit(player_surface,player_rect) #the position is deteremined by the rectangle
        
        #ends game if player touches snail
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((94,129,162)) 
        screen.blit(player_stand_scaled, player_stand_rect)
        
        #to access all the keys being pressed as dictionary and then searching for specific key being pressed
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print('Jump')
        
        #check collision
        # if player_rect.colliderect(snail_rect): #gives True or Faslse
        #     print('collision')
        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
        #     print(pygame.mouse.get_pressed())
        
        #draw all our elements
    pygame.display.update() #updates everything
    clock.tick(60) #tells that is should not run faster than 60 frames per second. 
    