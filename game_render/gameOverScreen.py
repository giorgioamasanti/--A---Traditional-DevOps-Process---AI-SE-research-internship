import pygame

def gameOverRender(displaySurface, gridState, windowWidth, windowHeight):
    """ Render the game over screen"""
    transparent_background = pygame.Surface((windowWidth, windowHeight))
    transparent_background.set_alpha(3)
    transparent_background.fill((100,100,100))
    displaySurface.blit(transparent_background, (0,0))

    #GAME OVER
    font = pygame.font.Font("freesansbold.ttf", 45)
    text = font.render("GAME OVER", True, (255,255,255), None)
    textRect = text.get_rect()
    textRect.center = (windowWidth/2,windowHeight/2 - 30)
    displaySurface.blit(text, textRect)
    #Press "N"
    font2 = pygame.font.Font("freesansbold.ttf", 20)
    text2 = font2.render('Press "N" to play again', True, (255,255,255), None)
    textRect2 = text2.get_rect()
    textRect2.center = (windowWidth/2,windowHeight/2 + 60)
    displaySurface.blit(text2, textRect2)
    #Score
    font2 = pygame.font.Font("freesansbold.ttf", 20)
    text2 = font2.render(f'Score: {gridState.score}', True, (255,255,255), None)
    textRect2 = text2.get_rect()
    textRect2.center = (windowWidth/2,windowHeight/2 + 20)
    displaySurface.blit(text2, textRect2)


    pygame.display.update()