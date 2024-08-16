import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import unittest
from persistence.all_time_hs import allTimeHighScores
import csv, datetime


# Import writer class from csv module
from csv import writer
 
# List that we want to add as a new row
List = [6, 'William', 5532, 1, 'UAE']
 
# Open our existing CSV file in append mode
# Create a file object for this file
with open("tests/test_persistence/test_high_scores.csv", 'a', newline='') as f_object:
 
    # Pass this file object to csv.writer()
    # and get a writer object
    writer_object = writer(f_object)
 
    # Pass the list as an argument into
    # the writerow()
    writer_object.writerow(List)
 
    # Close the file object
    f_object.close()