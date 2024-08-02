import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


import unittest
from game_state.activePiece import activePiece, Tetrominoes, active_colours
import pytest

class Test_activePiece(unittest.TestCase):
    def test_rotate(self):
        piece = activePiece("T", "b", [0,4])
        piece.rotate()
        self.assertEqual(piece.shape, [[0,1],[1,1],[0,1]])
        piece.rotate()
        self.assertEqual(piece.shape, [[1,1,1],[0,1,0]])
        piece.rotate()
        self.assertEqual(piece.shape, [[1,0],[1,1],[1,0]])
        piece.rotate()
        self.assertEqual(piece.shape, [[0,1,0],[1,1,1]])

    def test_recalculateDimensions(self):
        piece = activePiece("T", "b", [0,4])
        piece.recalculateDimensions()
        self.assertEqual(piece.width, 3)
        self.assertEqual(piece.height, 2)
        piece.rotate()
        piece.recalculateDimensions()
        self.assertEqual(piece.width, 2)
        self.assertEqual(piece.height, 3)
    
    def test_spawnNewPiece(self):
        piece = activePiece("T", "b", [0,4])
        piece.spawnNewPiece()
        self.assertIn(piece.letter, list(Tetrominoes.keys()))
        self.assertIn(piece.colour, list(active_colours.keys()))
        self.assertEqual(piece.coords, [0,4])

    def test_moveH(self):
        piece = activePiece("T", "b", [0,4])
        piece.moveH(1)
        self.assertEqual(piece.coords, [0,5])
        with pytest.raises(ValueError):
            piece.moveH(3)

    def test_moveV(self):
        piece = activePiece("T", "b", [0,4])
        piece.moveV(1)
        self.assertEqual(piece.coords, [1,4])
        with pytest.raises(ValueError):
            piece.moveV(3)


if __name__ == "__main__":
    unittest.main()


