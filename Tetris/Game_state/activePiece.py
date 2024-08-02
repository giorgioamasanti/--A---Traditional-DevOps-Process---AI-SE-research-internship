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

active_colours = {'b': (0,0,255), 'r': (255,0,0), 'g': (0,255,0), 'y': (255,255,0), 'o': (255,165,0), 'p': (128,0,128), 'c': (0,255,255)}
solid_colours = {'B': (0,0,150), 'R': (150,0,0), 'G': (0,150,0), 'Y': (150,150,0), 'O': (150,100,0), 'P': (75,0,75), 'C': (0,150,150)}
all_colours = active_colours | solid_colours

class activePiece:
    """Class to define all the properties of an active tetromino piece"""
    def __init__(self, letter, colour, coords):
        self.letter = letter
        self.shape = Tetrominoes[self.letter] #2D (or 1D for "I") array representing the shape
        self.width = len(self.shape[0])
        self.height = len(self.shape)
        self.colour = colour
        self.coords = coords #e.g [0,4] is 0 rows down, 4 columns across - representing the top-left square of the shape
    
    def __str__(self):
        """Print function (for debugging)"""
        return f"Shape = {self.shape};  Coords = {self.coords}"

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
        print("rotated piece")

    def spawnNewPiece(self):
        self.letter = random.choice(list(Tetrominoes.keys()))
        self.shape = Tetrominoes[self.letter] #2D (or 1D for "I") array representing the shape
        self.recalculateDimensions()
        self.colour = random.choice(list(active_colours.keys()))
        self.coords = [0,4] #spawn point
    
    def moveH(self, direction):
        if direction not in [-1,1]:
            raise ValueError("Direction must be -1 or 1")

        #direction is: -1 for left, +1 for right
        self.coords[1] += direction

    def moveV(self, direction):
        if direction not in [-1,1]:
            raise ValueError("Direction must be -1 or 1")
        
        #direction is: -1 for up, +1 for down
        self.coords[0] += direction





