import sys
import os
# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import unittest
import time
from game_state.high_score import roundScore, scoreTable

class Test_scoreTable(unittest.TestCase):
    def test_add_score(self):
        score_table = scoreTable()
        r1 = roundScore(10)
        r2 = roundScore(100)
        r3 = roundScore (20)

        for i in [r1, r2, r3]:
            score_table.add_score(i)
        
        self.assertEqual(score_table.scoreObjects, [r2, r3, r1])
        self.assertEqual(score_table.scores,[100,20,10])


if __name__ == "__main__":
    unittest.main()
