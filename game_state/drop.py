import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
from user_inputs.commands import executeCommands

class dropperTimer():
    def __init__(self, dropInterval = 0.75):
        self.dropInterval = dropInterval #time in seconds
        self.lastDropTime = time.time()
    
    def checkDrop(self, activePiece, gridState, currentSessionScoreTable):
        if time.time() >= self.lastDropTime + self.dropInterval:
            self.lastDropTime = time.time()
            executeCommands(["moveDown"], activePiece, gridState, self, mute=True, currentSessionScoreTable = currentSessionScoreTable)
