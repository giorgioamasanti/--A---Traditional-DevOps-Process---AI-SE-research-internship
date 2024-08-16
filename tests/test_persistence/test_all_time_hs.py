import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import unittest
from persistence.all_time_hs import allTimeHighScores
import csv, datetime

class Test_allTimeHighScores(unittest.TestCase):
    def test_add_score_to_file(self):
        #clearing the test csv file
        filename = "tests/test_persistence/test_high_scores.csv"
        f = open(filename, "w+")
        f.close()

        ATHS = allTimeHighScores(file_path=filename)
        ATHS.add_score_to_file(100, "2024-08-16 11:26:45")
        ATHS.add_score_to_file(120, "2024-08-16 11:26:46")
        ATHS.add_score_to_file(140, "2024-08-16 11:26:47")

        #reading and placing into a list of lists
        with open(filename, "r") as f_object:
            file_contents = []
            r_object = csv.reader(f_object)
            for row in r_object:
                file_contents.append(row)
        
        #assertions
        self.assertEqual(file_contents[0], ["100", "2024-08-16 11:26:45"])
        self.assertEqual(file_contents[1], ["120", "2024-08-16 11:26:46"])
        self.assertEqual(file_contents[2], ["140", "2024-08-16 11:26:47"])

    def test_read_file(self):
        #clearing the test csv file
        filename = "tests/test_persistence/test_high_scores.csv"
        f = open(filename, "w+")
        f.close()

        ATHS = allTimeHighScores(file_path=filename)
        ATHS.add_score_to_file(100, "2024-08-16 11:26:45")
        ATHS.add_score_to_file(120, "2024-08-16 11:26:46")
        ATHS.add_score_to_file(140, "2024-08-16 11:26:47")
        ATHS.add_score_to_file(80, "2024-08-16 11:26:48")
        ATHS.add_score_to_file(1000, "2024-08-16 11:26:49")
        ATHS.add_score_to_file(140, "2024-08-16 11:26:50")

        top_scores = ATHS.read_file()

        self.assertEqual(top_scores[0], {"score":"1000", "time":"2024-08-16 11:26:49"})
        self.assertEqual(top_scores[1], {"score":"140", "time":"2024-08-16 11:26:47"})
        self.assertEqual(top_scores[2], {"score":"140", "time":"2024-08-16 11:26:50"})
        self.assertEqual(top_scores[3], {"score":"120", "time":"2024-08-16 11:26:46"})
        self.assertEqual(top_scores[4], {"score":"100", "time":"2024-08-16 11:26:45"})
        self.assertEqual(len(top_scores),5)
        self.assertEqual(len(top_scores[0].keys()), 2)
    
    def test_cleanup_file(self):
        #clearing the test csv file
        filename = "tests/test_persistence/test_high_scores.csv"
        f = open(filename, "w+")
        f.close()

        #filling cv test file
        ATHS = allTimeHighScores(file_path=filename)
        ATHS.add_score_to_file(100, "2024-08-16 11:26:45")
        ATHS.add_score_to_file(120, "2024-08-16 11:26:46")
        ATHS.add_score_to_file(140, "2024-08-16 11:26:47")
        ATHS.add_score_to_file(80, "2024-08-16 11:26:48")
        ATHS.add_score_to_file(1000, "2024-08-16 11:26:49")
        ATHS.add_score_to_file(140, "2024-08-16 11:26:50")

        #executing command        
        ATHS.cleanup_file()

        #reading contents of file
        top_scores = []

        with open(filename,"r") as f_object:
            r_object = csv.reader(f_object)
            for row in r_object:
                score_time_dict = { "score" : row[0], "time": row[1]}
                top_scores.append(score_time_dict)
        
        self.assertEqual(top_scores[0], {"score":"1000", "time":"2024-08-16 11:26:49"})
        self.assertEqual(top_scores[1], {"score":"140", "time":"2024-08-16 11:26:47"})
        self.assertEqual(top_scores[2], {"score":"140", "time":"2024-08-16 11:26:50"})
        self.assertEqual(top_scores[3], {"score":"120", "time":"2024-08-16 11:26:46"})
        self.assertEqual(top_scores[4], {"score":"100", "time":"2024-08-16 11:26:45"})
        self.assertEqual(len(top_scores),5)
        self.assertEqual(len(top_scores[0].keys()), 2)

if __name__ == "__main__":
    unittest.main()