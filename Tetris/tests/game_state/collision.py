#1. place a piece near left edge, try to move it left, check that it is still in the same place
    #same but rotate
#2. Same for right edge
#3. Same for bottom edge

#4. Place a piece next to a solid block, try to move it and rotate it, check that it is still in the same place

import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import unittest
from game_state.gridState import gridState
from game_state.activePiece import activePiece, Tetrominoes, active_colours
from user_inputs.commands import executeCommands

class Test_gridState(unittest.TestCase):
    def test_leftEdgeCollision(self):
        piece = activePiece("I", "r", [0,0])
        grid = gridState([10,20], 20)
        grid.solidArray = [[0 for x in range(grid.gridShape[0])] for y in range(grid.gridShape[1])]
        grid.updateGrid(piece)
        executeCommands(["moveLeft"], piece, grid)
        self.assertEqual(piece.coords, [0,0])
    
    def test_rightEdgeCollision(self):
        piece = activePiece("I", "r", [0,0])
        grid = gridState([10,20], 20)
        grid.solidArray = [[0 for x in range(grid.gridShape[0])] for y in range(grid.gridShape[1])]
        grid.updateGrid(piece)
        executeCommands(["rotate"], piece, grid)
        piece.coords = [0,9]
        executeCommands(["moveRight"], piece, grid)
        self.assertEqual(piece.coords, [0,9])
        executeCommands(["rotate"], piece, grid)
        self.assertEqual(piece.coords, [0,9])
        self.assertEqual(piece.shape, [[1],[1],[1],[1]])

    def test_bottomEdgeCollision(self):
        piece = activePiece("I", "r", [19,0])
        grid = gridState([10,20], 20)
        grid.solidArray = [[0 for x in range(grid.gridShape[0])] for y in range(grid.gridShape[1])]
        grid.updateGrid(piece)
        executeCommands(["rotate"], piece, grid)
        self.assertEqual(piece.coords, [19,0])
        self.assertEqual(piece.shape, [[1,1,1,1]])
        executeCommands(["moveDown"], piece, grid)
        self.assertEqual(piece.coords, [19,0])

    def test_solidBlockCollision(self):
        piece = activePiece("I", "r", [0,0])
        grid = gridState([10,20], 20)
        grid.solidArray = [[0 for x in range(grid.gridShape[0])] for y in range(grid.gridShape[1])]
        for i in range(15,20):
            grid.solidArray[i][5] = "R"
        grid.updateGrid(piece)

        executeCommands(["rotate"], piece, grid)
        piece.coords = [15,4]
        executeCommands(["moveRight"], piece, grid)
        self.assertEqual(piece.coords, [15,4])
        executeCommands(["rotate"], piece, grid)
        self.assertEqual(piece.coords, [15,4])
        self.assertEqual(piece.shape, [[1],[1],[1],[1]])



if __name__ == "__main__":
    unittest.main()