import datetime

#creating a round score object which stores the score and time info from each round
class roundScore():
    def __init__(self, score):
        self.score = score
        self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#creating a scoreTable object which has an attribute of a list of all score objects 
#we will create different instances of it for the current and all-time sessions
class scoreTable():
    def __init__(self) -> None:
        self.scoreObjects = []
        self.scores = []
        self.times = []
    
    def add_score(self, roundScoreObject):
        self.scoreObjects.append(roundScoreObject)
        self.scoreObjects.sort(key=lambda x: x.score, reverse=True)

        self.scores = []
        for object in self.scoreObjects:
            self.scores.append(object.score)
        
        self.times = []
        for object in self.scoreObjects:
            self.times.append(object.time)
        