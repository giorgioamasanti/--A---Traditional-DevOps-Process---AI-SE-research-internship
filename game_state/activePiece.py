import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import random
import time
from user_inputs.commands import executeCommands
from sfx.gameplay_sfx import sfx


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
solid_colours = {'B': (0,0,255), 'R': (255,0,0), 'G': (0,255,0), 'Y': (255,255,0), 'O': (255,165,0), 'P': (128,0,128), 'C': (0,255,255)}
all_colours = active_colours | solid_colours
active_to_solid_colour_map = {'b':'B', 'r':'R', 'g':'G', 'y':'Y', 'o':'O', 'p':'P', 'c':'C'}
shape_to_colour_map = {'I':'c', 'J':'b', 'T':'p', 'L':'o', 'O':'y', 'S':'g', 'Z':'r'}

class activePiece:
    """Class to define all the properties of an active tetromino piece"""
    def __init__(self, letter, coords, colour = None):
        self.letter = letter
        self.shape = Tetrominoes[self.letter] #2D (or 1D for "I") array representing the shape
        self.width = len(self.shape[0])
        self.height = len(self.shape)
        self.last_two_pieces = []
        if colour == None:
            self.colour = shape_to_colour_map[self.letter]
        else:
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
        while True:
            new_piece = random.choice(list(Tetrominoes.keys()))
            if len(self.last_two_pieces) < 2 or new_piece != self.last_two_pieces[-1] or new_piece != self.last_two_pieces[-2]:
                break
        
        self.letter = new_piece
        self.shape = Tetrominoes[self.letter]  # 2D (or 1D for "I") array representing the shape
        self.recalculateDimensions()
        self.colour = shape_to_colour_map[self.letter]
        self.coords = [0, 4]  # spawn point
        
        # Update the last_two_pieces list
        if len(self.last_two_pieces) >= 2:
            self.last_two_pieces.pop(0)  # Remove the oldest piece
        self.last_two_pieces.append(self.letter)
    
    
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

    def solidify(self, gridState, dropperTimer, currentSessionScoreTable, ATHSobject):
        for i in range(self.width):
            for j in range(self.height):
                if self.shape[j][i] != 0:
                    gridState.solidArray[self.coords[0]+j][self.coords[1]+i] = active_to_solid_colour_map[self.colour]
        dropperTimer.lastDropTime = time.time()

        #sfx
        sfx("solidify")
        executeCommands(["spawn"], self, gridState, dropperTimer, currentSessionScoreTable, ATHSobject=ATHSobject)





