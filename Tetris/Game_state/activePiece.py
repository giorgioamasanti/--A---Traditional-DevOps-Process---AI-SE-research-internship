import numpy as np
import random

Tetrominoes = {"I": [[1,1,1,1]],
               "L": [[0,0,1],
                     [1,1,1]],
                "J": [[1,0,0],
                     [1,1,1]],
                "T": [[0,1,0],
                     [1,1,1]],
                "O": [[1,1],
                     [1,1]],
                "S": [[0,1,1],
                     [1,1,0]],
                "Z": [[1,1,0],
                     [0,1,1]],}

colour = {'b': (0,0,255), 'r': (255,0,0), 'g': (0,255,0)}


class activePiece:
    """Class to define all the properties of an active tetromino piece"""
    def __init__(self, letter, colour, coords):
        self.letter = letter
        self.shape = Tetrominoes[self.letter] #2D (or 1D for "I") array representing the shape
        self.width = len(self.shape[0])
        self.height = len(self.shape)
        self.colour = colour
        self.coords = coords #e.g [0,4] is 0 rows down, 4 rows across - representing the top-left square of the shape
    
    def recalculateDimensions(self):
        """Method to recalculate the dimensions of the piece"""
        self.width = len(self.shape[0])
        self.height = len(self.shape)

    def rotate(self):
        """Method to define the rotation of a piece"""
        #print(f"shape = {self.shape}")
        original_width = len(self.shape[0])
        original_height = len(self.shape)
        newArray = [[0 for x in range(original_height)] for y in range(original_width)]
        #print(f"newArray = {newArray}")
        #print(f"original_width = {original_width}")
        #print(f"original_height = {original_height}")
        for i in range(original_width):
            for j in range(original_height): 
                newArray[i][j] = self.shape[j][original_width-i-1]
        self.shape = newArray
        self.recalculateDimensions()

    def spawnNewPiece(self):
        self.letter = random.choice(list(Tetrominoes.keys()))
        self.shape = Tetrominoes[self.letter] #2D (or 1D for "I") array representing the shape
        self.recalculateDimensions()
        self.colour = random.choice(list(colour.keys()))
        self.coords = [0,4] #spawn point
    
    def move(self, direction):
        #direction is -1 for left, 1 for right
        self.coords[1] += direction




