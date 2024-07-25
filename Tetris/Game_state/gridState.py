class gridState:
    def __init__(self, gridShape, cellSize, displaySurf):
        """ Defining the grid class and its properties: parameters which define the current state of the grid """
        self.gridShape = gridShape
        self.cellSize = cellSize
        self.displaySurf = displaySurf
        #array to represent the grid cells
        self.array = [[0 for x in range(gridShape[0])] for y in range(gridShape[1])]
        #array to represent the solidified cells
        self.solidArray = [[0 for x in range(gridShape[0])] for y in range(gridShape[1])]

    def updateGrid(self, activePiece):
        """ Updating grid in 3 stages: 1) empty grid, 2) solid blocks, 3) active piece """
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
                 
        

        

