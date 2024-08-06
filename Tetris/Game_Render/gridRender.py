import pygame
from game_state.activePiece import all_colours

def gridRender(gridState, gridSurf):
    """ Render the grid: function which renders the grid based on the current gridState"""
    #black background
    gridSurf.fill((0,0,0))
    #grey background
    pygame.draw.rect(gridSurf, (50,50,50), (0,0,360,720))
    #black grid
    for x in range(0,gridState.gridShape[0]*gridState.cellSize, gridState.cellSize):
        for y in range(0, gridState.gridShape[1]*gridState.cellSize, gridState.cellSize):
            pygame.draw.rect(gridSurf, (0,0,0) , (x+1,y+1,gridState.cellSize-2,gridState.cellSize-2))
    
    #scanning through the grid and checking for any space which is not blank, and drawing the coloured squares there
    for X in range(0, 10):
        for Y in range(0, 20):
            cell_contents = gridState.array[Y][X]
            if cell_contents != 0:
                pygame.draw.rect(gridSurf, all_colours[cell_contents], (X*gridState.cellSize +1,Y*gridState.cellSize +1 ,gridState.cellSize -2,gridState.cellSize -2) )
    #pygame.display.update()

def scoreRender(gridState, gridSurf):
    """ Renders the current score in the top right corner"""
    font = pygame.font.Font("freesansbold.ttf", 30)
    text = font.render(f"Score: {gridState.score:04d}", True, (255,255,255), None)
    textRect = text.get_rect()
    textRect.topleft = (390,20)
    gridSurf.blit(text, textRect)

def mainGameRender(gridState, gridSurf):
    gridRender(gridState, gridSurf)
    scoreRender(gridState, gridSurf)
