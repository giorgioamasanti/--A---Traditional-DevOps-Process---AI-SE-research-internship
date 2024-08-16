import sys
import os
# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pytest
from game_state.activePiece import activePiece

def test_piece_repetition():
    piece = activePiece('I', [0, 4])

    repetitions = 1000000  # Test over 1000 repetitions to be thorough
    last_two_pieces = []

    for _ in range(repetitions):
        piece.spawnNewPiece()
        current_piece = piece.letter

        if len(last_two_pieces) == 2:
            # Ensure the current piece is not the same as the last two
            assert not (current_piece == last_two_pieces[0] == last_two_pieces[1]), "A piece appeared more than twice in a row."

        # Update the last two pieces list
        if len(last_two_pieces) >= 2:
            last_two_pieces.pop(0)
        last_two_pieces.append(current_piece)


if __name__ == "__main__":
    pytest.main([__file__])
