import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import unittest
from game_state.gridState import gridState
from game_state.activePiece import activePiece, Tetrominoes, active_colours

class Test_gridState(unittest.TestCase):
    def test_updateGrid(self):
        piece = activePiece("T", [0,4])
        grid = gridState([10,20], 20)
        grid.solidArray = [[0 for x in range(grid.gridShape[0])] for y in range(grid.gridShape[1])]
        grid.updateGrid(piece)
        expected_array = [[0 for x in range(10)] for y in range(20)]
        expected_array[0][4] = 0
        expected_array[0][5] = "p"
        expected_array[0][6] = 0
        expected_array[1][4] = "p"
        expected_array[1][5] = "p"
        expected_array[1][6] = "p"
        self.assertEqual(grid.array,expected_array)

    def test_checkRowClear(self):
        grid = gridState([10,20], 20)
        grid.solidArray = [[0 for x in range(grid.gridShape[0])] for y in range(grid.gridShape[1])]
        for i in range(18,20):
            grid.solidArray[i] = ['R' for x in range(grid.gridShape[0])]
        for i in range(9):
            grid.solidArray[17][i] = 'R'

        self.assertEqual(grid.checkRowClear(), [18,19])
        grid.rowClear()
        expectedArray = [[0 for x in range(grid.gridShape[0])] for y in range(grid.gridShape[1])]
        for i in range(9):
            expectedArray[19][i] = 'R'
        self.assertEqual(grid.solidArray, expectedArray)

    def test_getNewDropTime(self):
        grid = gridState([10,20], 20)
        grid.score = 0
        self.assertEqual(grid.getNewDropTime(), 0.7)
        grid.score = 20
        self.assertEqual(grid.getNewDropTime(), 0.7)
        grid.score = 100
        self.assertEqual(grid.getNewDropTime(), 0.6)
        grid.score = 120
        self.assertEqual(grid.getNewDropTime(), 0.6)
        grid.score = 200
        self.assertEqual(grid.getNewDropTime(), 0.5)
        grid.score = 600
        self.assertEqual(grid.getNewDropTime(), 0.3)
        grid.score = 800
        self.assertEqual(grid.getNewDropTime(), 0.2)
        grid.score = 1000
        self.assertEqual(grid.getNewDropTime(), 0.1)
        grid.score = 1200
        self.assertEqual(grid.getNewDropTime(), 0.1)
        grid.score = 0
        self.assertEqual(grid.getNewDropTime(), 0.7)
        

if __name__ == "__main__":
    unittest.main()