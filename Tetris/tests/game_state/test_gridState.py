import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import unittest
from game_state.gridState import gridState
from game_state.activePiece import activePiece, Tetrominoes, active_colours
import pytest

class Test_gridState(unittest.TestCase):
    def test_updateGrid(self):
        piece = activePiece("T", "b", [0,4])
        grid = gridState([10,20], 20)
        grid.solidArray = [[0 for x in range(grid.gridShape[0])] for y in range(grid.gridShape[1])]
        grid.updateGrid(piece)
        expected_array = [[0 for x in range(10)] for y in range(20)]
        expected_array[0][4] = 0
        expected_array[0][5] = "b"
        expected_array[0][6] = 0
        expected_array[1][4] = "b"
        expected_array[1][5] = "b"
        expected_array[1][6] = "b"
        self.assertEqual(grid.array,expected_array)

if __name__ == "__main__":
    unittest.main()