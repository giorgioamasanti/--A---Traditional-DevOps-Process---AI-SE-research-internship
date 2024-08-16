import sys
import os
# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import datetime
from persistence.all_time_hs import allTimeHighScores 

#creating a round score object which stores the score and time info from each round
class roundScore():
    def __init__(self, score, time = None):
        self.score = score
        if time == None:
            self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.time = time

    def __repr__(self) -> str:
        return (f"Score: {self.score}; Time: {self.time}")

#creating a scoreTable object which has an attribute of a list of all score objects 
#we will create different instances of it for the current and all-time sessions
class scoreTable():
    def __init__(self) -> None:
        self.scoreObjects = []
        self.scores = []
        self.times = []
    
    def __repr__(self) -> str:
        return(str(self.scoreObjects))
    
    def add_score(self, roundScoreObject, ATHSobject = None): # ATHS object should be None if only when you don't want to add this score to the ATHS table (i.e. when you're rendering it and don't want to duplicate)
        #adding the score object to the list of score objects
        self.scoreObjects.append(roundScoreObject)
        self.scoreObjects.sort(key=lambda x: x.score, reverse=True)

        #adding the score value to the list of scores
        self.scores = []
        for object in self.scoreObjects:
            self.scores.append(object.score)
        
        #adding the time value to the list of times
        self.times = []
        for object in self.scoreObjects:
            self.times.append(object.time)
        
        #adding the score and time to the all time high score file
        if ATHSobject != None:
            ATHSobject.add_score_to_file(roundScoreObject.score, roundScoreObject.time)
    

        