import sys
import os
# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import datetime

#creating a round score object which stores the score and time info from each round
class roundScore():
    def __init__(self, score):
        self.score = score
        self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
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
    
    def add_score(self, roundScoreObject):
        self.scoreObjects.append(roundScoreObject)
        self.scoreObjects.sort(key=lambda x: x.score, reverse=True)

        self.scores = []
        for object in self.scoreObjects:
            self.scores.append(object.score)
        
        self.times = []
        for object in self.scoreObjects:
            self.times.append(object.time)
        