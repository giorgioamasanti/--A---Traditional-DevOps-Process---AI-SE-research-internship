import sys
import os
import unittest
from unittest.mock import Mock
# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from game_state.gridState import gridState
from game_state.activePiece import activePiece, Tetrominoes, active_colours
from game_state.drop import dropperTimer
import time

class Test_drop(unittest.TestCase):
    def test_drop(self):
        # Initialise piece on grid
        piece = activePiece("T", [0,4])
        grid = gridState([10,20], 20)        
        grid.solidArray = [[0 for x in range(grid.gridShape[0])] for y in range(grid.gridShape[1])]
        # Initialise dropper timer
        dropTimer = dropperTimer(0.75)
        # Mock objects for the missing arguments
        currentSessionScoreTable = Mock()
        ATHSobject = Mock()
        # Wait
        time.sleep(0.7)
        dropTimer.checkDrop(piece, grid, currentSessionScoreTable, ATHSobject)
        self.assertEqual(piece.coords, [0,4])
        time.sleep(0.1)
        dropTimer.checkDrop(piece, grid, currentSessionScoreTable, ATHSobject)
        self.assertEqual(piece.coords, [1,4])


if __name__ == "__main__":
    unittest.main()