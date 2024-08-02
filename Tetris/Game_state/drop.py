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
