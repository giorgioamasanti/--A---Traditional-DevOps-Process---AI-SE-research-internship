import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pygame

def speedUpRender(displaySurface, gridState):
    """ Render the speed up message"""
    transparent_background = pygame.Surface((gridState.width, gridState.height))
    transparent_background.set_alpha(1)
    transparent_background.fill((100,100,100))
    displaySurface.blit(transparent_background, (0,0))

    #SPEEDING UP
    font = pygame.font.Font("freesansbold.ttf", 30)
    speed_up_text = font.render("SPEEDING UP", True, (255,0,0), None)
    speed_up_textRect = speed_up_text.get_rect()
    speed_up_textRect.center = (gridState.width/2,gridState.height/2)
    displaySurface.blit(speed_up_text, speed_up_textRect)
