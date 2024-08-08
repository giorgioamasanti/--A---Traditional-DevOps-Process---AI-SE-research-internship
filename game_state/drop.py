import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
from user_inputs.commands import executeCommands

class dropperTimer():
    def __init__(self, dropInterval):
        self.dropInterval = dropInterval
        self.lastDropTime = time.time()
    
    def checkDrop(self, activePiece, gridState):
        if time.time() >= self.lastDropTime + self.dropInterval:
            self.lastDropTime = time.time()
            executeCommands(["moveDown"], activePiece, gridState, self)
