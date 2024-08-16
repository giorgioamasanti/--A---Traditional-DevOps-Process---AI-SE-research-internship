import csv

#file_path = "persistence/high_scores.csv"

class allTimeHighScores():
    def __init__(self, file_path = "persistence/high_scores.csv"):
        self.file_path = file_path

    def add_score_to_file(self, score, time):
        with open(self.file_path, "a", newline='') as f_object:
            w_object = csv.writer(f_object)
            w_object.writerow([score,time])
            f_object.close()

    def read_file(self, no_scores = 5):
        top_scores = []

        with open(self.file_path,"r") as f_object:
            r_object = csv.reader(f_object)
            for row in r_object:
                score_time_dict = { "score" : row[0], "time": row[1]}
                top_scores.append(score_time_dict)
        
        top_scores = sorted(top_scores, key=lambda x: int(x['score']), reverse = True)
        return top_scores[0:5]
    
    def cleanup_file(self, no_scores = 5):
        
        #storing the file contents
        top_scores = []
        with open(self.file_path,"r") as f_object:
            
            r_object = csv.reader(f_object)
            for row in r_object:
                score_time_dict = { "score" : row[0], "time": row[1]}
                top_scores.append(score_time_dict)
            
        #clearing the file
        f = open(self.file_path, "w+")
        f.close()

        #sorting out just the top 5
        top_scores = sorted(top_scores, key=lambda x: int(x['score']), reverse = True)
        top_scores = top_scores[0:no_scores]

        #writing back to the file
        with open(self.file_path, "a", newline='') as f_object:
            w_object = csv.writer(f_object)
            for i in top_scores:
                w_object.writerow([i["score"], i["time"]])
            f_object.close()

            