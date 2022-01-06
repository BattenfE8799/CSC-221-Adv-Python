# -*- coding: utf-8 -*-
"""
Using pygame to create peg game
"""
# Import a library of functions called 'pygame'
import pygame
from math import pi
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = [400, 300]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Example code for the draw module")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    screen.fill(WHITE)
 
    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, BLUE, [[200, 35], [50, 250], [350, 250]], 5)
    #circles first row
    pygame.draw.circle(screen, BLACK, [200, 90], 10)
    #second row
    pygame.draw.circle(screen, BLACK, [180, 122], 10)
    pygame.draw.circle(screen, BLACK, [220, 122], 10)
    #thrid row
    pygame.draw.circle(screen, BLACK, [200, 150], 10)
    pygame.draw.circle(screen, BLACK, [160, 150], 10)
    pygame.draw.circle(screen, BLACK, [240, 150], 10)
    #fourth row
    pygame.draw.circle(screen, BLACK, [140, 182], 10)
    pygame.draw.circle(screen, BLACK, [180, 182], 10)
    pygame.draw.circle(screen, BLACK, [220, 182], 10)
    pygame.draw.circle(screen, BLACK, [260, 182], 10)    
    #fifth row
    pygame.draw.circle(screen, BLACK, [120, 214], 10)
    pygame.draw.circle(screen, BLACK, [160, 214], 10)
    pygame.draw.circle(screen, BLACK, [240, 214], 10)
    pygame.draw.circle(screen, BLACK, [200, 214], 10)
    pygame.draw.circle(screen, BLACK, [280, 214], 10)

    
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
