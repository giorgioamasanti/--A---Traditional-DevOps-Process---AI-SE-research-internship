import sys
import os
# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# solid pieces and active pieces render the same, but are defined by different letters in the arrays:
# active pieces: cyan = 'c', blue = 'b', orange = 'o', yellow = 'y', green = 'g', purple = 'p', red = 'r'
# solid pieces: cyan = 'C', blue = 'B', orange = 'O', yellow = 'Y', green = 'G', purple = 'P', red = 'R'
import numpy as np
from sfx.gameplay_sfx import sfx
from game_state.high_score import roundScore, scoreTable

#dictionary mapping the number of rows cleared to the score it adds
rowscleared_to_scores = {0: 0,
                        1: 40,
                        2: 100,
                        3: 300,
                        4: 1200}

scores_to_drop_delay = {0: 0.7,
                        100: 0.6,
                        200: 0.5,
                        400: 0.4,
                        800: 0.3,
                        1600: 0.2,
                        3200: 0.1}

class gridState:
    def __init__(self, gridShape, cellSize):
        """ Defining the grid class and its properties: parameters which define the current state of the grid 
        gridShape: tuple with two elements defining the shape of the grid (x,y), e.g. (10,20) means a 10x20 grid
        cellSize: integer defining the size of each cell in pixels
        displaySurf: instance of surface class, the surface on which we will render the grid"""
        self.gridShape = gridShape
        self.cellSize = cellSize
        self.width = gridShape[0]*cellSize
        self.height = gridShape[1]*cellSize
        #array to represent the grid cells
        self.array = [[0 for x in range(gridShape[0])] for y in range(gridShape[1])]
        #array to represent the solidified cells - should contain "0" for an empty cell and a capital letter to represent a filled, solid cell
        self.solidArray = [[0 for x in range(gridShape[0])] for y in range(gridShape[1])]

        self.gameState = "playing"

        #the current game score
        self.score = 0

        self.speedUpFlag = False


    def updateGrid(self, activePiece):
        """ Updating grid array in 3 stages: 1) empty grid, 2) solid blocks, 3) active piece """
        #empty grid
        self.array = [[0 for x in range(self.gridShape[0])] for y in range(self.gridShape[1])]
        #adding solidified cells
        for x in range(self.gridShape[0]):
            for y in range(self.gridShape[1]):
                if self.solidArray[y][x] != 0:
                    self.array[y][x] = self.solidArray[y][x]
        #adding active piece
        for i in range(activePiece.width):
             for j in range(activePiece.height):
                if activePiece.shape[j][i] == 1:
                    self.array[activePiece.coords[0]+j][activePiece.coords[1]+i] = activePiece.colour
        #print(f"Piece at {activePiece.coords}")

    def checkRowClear(self):
        """ Scans the current solid array for any full rows, returns a list containing the indices of any full rows (rows are indexed 0 (top) to 19 (bottom))"""
        full_rows = []
        for row in range(len(self.solidArray)):
            full = all(self.solidArray[row][column] != 0 for column in range(len(self.solidArray[0])))
            if full:
                full_rows.append(row)
                #print(f"Index of row which is full: {row}")
        self.score += rowscleared_to_scores[len(full_rows)]
        return full_rows
    
    def clearFullRows(self, full_rows):
        """ Takes a list of the full rows and clears them and moves all above rows down"""
        for full_row in full_rows:
            for i in np.arange(full_row, 0, -1):
                self.solidArray[i] = self.solidArray[i-1]
            self.solidArray[0] = [0 for _ in range(len(self.solidArray[1]))]
        
        #sfx
        if len(full_rows) > 0:
            sfx("line_clear")

    def getNewDropTime(self):
        delay = 0
        for i in sorted(scores_to_drop_delay.keys()):
            if self.score >= i:
                delay = scores_to_drop_delay[i]
        return delay
    
    def rowClear(self, dropTimeAttribute):
        """ Brings together checkRowClear and clearFullRows"""
        full_rows = self.checkRowClear()
        if len(full_rows) > 0:
            self.clearFullRows(full_rows)
            if self.getNewDropTime() < dropTimeAttribute:
                self.speedUpFlag = True

    def gameOver(self, currentSessionScoreTable, ATHSobject):
        roundScoreObject = roundScore(self.score)
        currentSessionScoreTable.add_score(roundScoreObject, ATHSobject)
        self.gameState = "game over"
        print(currentSessionScoreTable.scoreObjects)
    
    

    #def updateDropTime(self, dropTimeAttribute):
        newDropTime = self.getNewDropTime()
        dropTimeAttribute = newDropTime
        print(f"newDropTime: {newDropTime}")
        print(f"dropTimeAttribute: {dropTimeAttribute}")
    


        

