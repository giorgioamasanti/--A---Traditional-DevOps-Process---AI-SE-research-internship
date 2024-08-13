import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

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

def mainGameRender(gridState, gridSurf, currentSessionScoreTable):
    gridRender(gridState, gridSurf)
    scoreRender(gridState, gridSurf)
    currentScoreTableRender(currentSessionScoreTable, gridSurf)

def currentScoreTableRender(currentSessionScoreTable, gridSurf):
    cells_in_table = 5
    cell_height = 40
    table_width = 240
    table_top_left = (380,140)

    scoresOnTable = currentSessionScoreTable.scores[0:cells_in_table]
    timesOnTable = currentSessionScoreTable.times[0:cells_in_table]

    #pygame.draw.rect(gridSurf, (50,50,50), (380,100,table_width,cell_height), 2)
    
    font = pygame.font.Font("freesansbold.ttf", 28)
    highscores_text = font.render("HIGH SCORES", True, (255,255,255), None)
    highscores_textRect = highscores_text.get_rect()
    highscores_textRect.center = (table_top_left[0] + table_width/2 , table_top_left[1] - 40 + cell_height/2)
    gridSurf.blit(highscores_text, highscores_textRect)

    font = pygame.font.Font("freesansbold.ttf", 17)
    current_session_text = font.render("CURRENT SESSION", True, (255,255,255), None)
    current_session_textRect = current_session_text.get_rect()
    current_session_textRect.center = (table_top_left[0] + table_width/2 , table_top_left[1] + cell_height/2)
    gridSurf.blit(current_session_text, current_session_textRect)

    for i in range(cells_in_table):
        if i % 2 == 0:
            tablecolour = (25,25,25) #dark grey
        else:
            tablecolour = (50,50,50) #light grey
        pygame.draw.rect(gridSurf, tablecolour, (table_top_left[0],table_top_left[1] + cell_height*(i+1),table_width,cell_height))

    for i in range(len(scoresOnTable)):
        font = pygame.font.Font("freesansbold.ttf", 17)
        score = font.render(f"{scoresOnTable[i]:04d}", True, (255,255,255), None)
        scoreRect = score.get_rect()
        scoreRect.center = (table_top_left[0]+25,table_top_left[1] + cell_height*(i+1.5))
        gridSurf.blit(score, scoreRect)

        dt = font.render(f"{timesOnTable[i]}", True, (255,255,255), None)
        dtRect = dt.get_rect()
        dtRect.center = (table_top_left[0]+25+125,table_top_left[1] + cell_height*(i+1.5))
        gridSurf.blit(dt, dtRect)
    



    