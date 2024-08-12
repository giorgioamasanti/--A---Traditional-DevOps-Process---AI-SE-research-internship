import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


import unittest
from game_state.activePiece import activePiece, Tetrominoes, active_colours
import pytest
from game_state.gridState import gridState
from game_state.drop import dropperTimer
from user_inputs.commands import executeCommands

class Test_commands(unittest.TestCase):
    def test_drop_and_solidify(self):   #integration test between commands and activepiece
        #initialise piece on grid
        piece = activePiece("T", [0,4], "r")
        grid = gridState([10,20], 20)        
        grid.solidArray = [[0 for x in range(grid.gridShape[0])] for y in range(grid.gridShape[1])]
        dropTimer = dropperTimer()
        for i in range(20):
            executeCommands(["moveDown"], piece, grid, dropTimer)
        expectedArray = [[0 for x in range(grid.gridShape[0])] for y in range(grid.gridShape[1])]
        for i in range(4,7):
            expectedArray[19][i] = "R"
        expectedArray[18][5] = "R"
        self.assertEqual(grid.solidArray, expectedArray)

if __name__ == "__main__":
    unittest.main()