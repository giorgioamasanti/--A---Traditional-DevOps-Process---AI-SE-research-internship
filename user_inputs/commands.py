import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from game_state.collision import checkCollision
import copy

def receiveInputs(commands, activePiece):
    #take the inputs and put them into a commands list
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                commands.append("moveRight")
            elif event.key == pygame.K_LEFT:
                commands.append("moveLeft")
            elif event.key == pygame.K_DOWN:
                commands.append("moveDown")
            elif event.key == pygame.K_UP:
                commands.append("rotate")
            elif event.key == pygame.K_s:
                commands.append("spawn")


def executeCommands(commands, activePiece, gridState, dropperTimer):
    dummyPiece = copy.deepcopy(activePiece)
    dummyGrid = copy.deepcopy(gridState)

    for c in commands:
        if c == "moveRight":
            dummyPiece.moveH(1)
        elif c == "moveLeft":
            dummyPiece.moveH(-1)
        elif c == "moveDown":
            dummyPiece.moveV(1)
        elif c == "rotate":
            dummyPiece.rotate()
        elif c == "spawn":
            dummyPiece.spawnNewPiece()
        else:
            raise KeyError(f"No command called {c}")


        if checkCollision(dummyPiece,dummyGrid) == True and c == "spawn":
            print("GAMEOVER!!!")
            gridState.gameOver()
        elif checkCollision(dummyPiece, dummyGrid) == True:
            if c == "moveDown":
                activePiece.solidify(gridState, dropperTimer)
                #print("*** piece solidified ***")
            else:
                pass
                #print("=====collision detected, not executing command=====")
        else:
            #print("+++ no collision detected, executing command +++")
            if c == "moveRight":
                activePiece.moveH(1)
            elif c == "moveLeft":
                activePiece.moveH(-1)
            elif c == "moveDown":
                activePiece.moveV(1)
            elif c == "rotate":
                activePiece.rotate()
            elif c == "spawn":
                activePiece.spawnNewPiece()

    commands.clear()

