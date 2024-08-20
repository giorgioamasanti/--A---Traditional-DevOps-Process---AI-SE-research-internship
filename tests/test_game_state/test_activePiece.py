import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


import unittest
from game_state.activePiece import activePiece, Tetrominoes, active_colours
import pytest
from game_state.gridState import gridState
from game_state.drop import dropperTimer

class Test_activePiece(unittest.TestCase):
    def test_rotate(self):
        piece = activePiece("T", [0,4])
        piece.rotate()
        self.assertEqual(piece.shape, [[0,1],[1,1],[0,1]])
        piece.rotate()
        self.assertEqual(piece.shape, [[1,1,1],[0,1,0]])
        piece.rotate()
        self.assertEqual(piece.shape, [[1,0],[1,1],[1,0]])
        piece.rotate()
        self.assertEqual(piece.shape, [[0,1,0],[1,1,1]])

    def test_recalculateDimensions(self):
        piece = activePiece("T", [0,4])
        piece.recalculateDimensions()
        self.assertEqual(piece.width, 3)
        self.assertEqual(piece.height, 2)
        piece.rotate()
        piece.recalculateDimensions()
        self.assertEqual(piece.width, 2)
        self.assertEqual(piece.height, 3)
    
    def test_spawnNewPiece(self):
        piece = activePiece("T", [0,4])
        piece.spawnNewPiece()
        self.assertIn(piece.letter, list(Tetrominoes.keys()))
        self.assertIn(piece.colour, list(active_colours.keys()))
        self.assertEqual(piece.coords, [0,4])
    
    def test_no_three_consecutive_pieces(self):
        piece = activePiece()
        piece.last_two_pieces = []  # Reset the history for the test

        # Simulate spawning pieces multiple times
        for _ in range(100):
            piece.spawnNewPiece()
            if len(piece.last_two_pieces) == 2:
                self.assertNotEqual(piece.last_two_pieces[0], piece.last_two_pieces[1])

    def test_moveH(self):
        piece = activePiece("T", [0,4])
        piece.moveH(1)
        self.assertEqual(piece.coords, [0,5])
        with pytest.raises(ValueError):
            piece.moveH(3)

    def test_moveV(self):
        piece = activePiece("T", [0,4])
        piece.moveV(1)
        self.assertEqual(piece.coords, [1,4])
        with pytest.raises(ValueError):
            piece.moveV(3)
    
    def test_solidify(self):
        # Initialize piece on grid
        piece = activePiece("T", [9,4], "r")
        grid = gridState([10,20], 20)        
        grid.solidArray = [[0 for x in range(grid.gridShape[0])] for y in range(grid.gridShape[1])]
        dropTimer = dropperTimer()
        
        # Expected array
        expectedArray = [[0 for x in range(grid.gridShape[0])] for y in range(grid.gridShape[1])]
        for i in range(4,7):
            expectedArray[10][i] = "R"
        expectedArray[9][5] = "R"

        # Solidify + spawn new piece
        piece.solidify(grid, dropTimer, None, None)  # Pass None for the missing arguments
        
        # Assertions
        self.assertEqual(grid.solidArray, expectedArray)
        self.assertEqual(piece.coords, [0,4])
        

if __name__ == "__main__":
    unittest.main()

