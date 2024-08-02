import pygame
from game_state.activePiece import all_colours

def gridRender(gridState, gridSurf):
        """ Render the grid: function which renders the grid based on the current gridState"""
        #white background
        gridSurf.fill((220,220,220))
        #black grid
        for x in range(0,gridState.gridShape[0]*gridState.cellSize, gridState.cellSize):
            for y in range(0, gridState.gridShape[1]*gridState.cellSize, gridState.cellSize):
                pygame.draw.rect(gridSurf, (0,0,0) , (x+1,y+1,gridState.cellSize-2,gridState.cellSize-2))
        
        #scanning through the grid and checking for any space which is not blank, and drawing the coloured squares there
        for X in range(0, 10):
            for Y in range(0, 20):
                cell_contents = gridState.array[Y][X]
                if cell_contents != 0:
                    pygame.draw.rect(gridSurf, all_colours[cell_contents], (X*gridState.cellSize,Y*gridState.cellSize,gridState.cellSize,gridState.cellSize) )
        pygame.display.update()