# solid pieces and active pieces render the same, but are defined by different letters in the arrays:
# active pieces: cyan = 'c', blue = 'b', orange = 'o', yellow = 'y', green = 'g', purple = 'p', red = 'r'
# solid pieces: cyan = 'C', blue = 'B', orange = 'O', yellow = 'Y', green = 'G', purple = 'P', red = 'R'
import numpy as np

class gridState:
    def __init__(self, gridShape, cellSize):
        """ Defining the grid class and its properties: parameters which define the current state of the grid 
        gridShape: tuple with two elements defining the shape of the grid (x,y), e.g. (10,20) means a 10x20 grid
        cellSize: integer defining the size of each cell in pixels
        displaySurf: instance of surface class, the surface on which we will render the grid"""
        self.gridShape = gridShape
        self.cellSize = cellSize
        #array to represent the grid cells
        self.array = [[0 for x in range(gridShape[0])] for y in range(gridShape[1])]
        #array to represent the solidified cells - should contain "0" for an empty cell and a capital letter to represent a filled, solid cell
        self.solidArray = [[0 for x in range(gridShape[0])] for y in range(gridShape[1])]
        

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
        for row in self.solidArray:
            full = all(row[column] != 0 for column in range(len(self.solidArray[0])))
            if full:
                full_rows.append(self.solidArray.index(row))
        return full_rows
    
    def clearFullRows(self, full_rows):
        """ Takes a list of the full rows and clears them and moves all above rows down"""
        for full_row in full_rows:
            for i in np.arange(full_row, 0, -1):
                self.solidArray[i] = self.solidArray[i-1]
            self.solidArray[0] = [0 for _ in range(len(self.solidArray[1]))]

    def rowClear(self):
        """ Brings together checkRowClear and clearFullRows"""
        full_rows = self.checkRowClear()
        self.clearFullRows(full_rows)

        

