import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pygame
from game_state.collision import checkCollision
import copy
from sfx.gameplay_sfx import sfx

userInputKeys = {pygame.K_RIGHT: "moveRight",
                 pygame.K_LEFT: "moveLeft",
                 pygame.K_DOWN: "moveDown",
                 pygame.K_UP: "rotate",
                 pygame.K_s: "spawn",
                 pygame.K_m: "musicToggle"}

def receiveInputs(commands, activePiece):
    #take the inputs and put them into a commands list
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
            break
        elif event.type == pygame.KEYDOWN:
            if event.key in userInputKeys.keys():
                commands.append(userInputKeys[event.key])



def executeCommands(commands, activePiece, gridState, dropperTimer, currentSessionScoreTable = None, ATHSobject = None, b_music = None, mute = False ):
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
        elif c == "musicToggle":
            b_music.toggle_music()
        else:
            raise KeyError(f"No command called {c}")


        if checkCollision(dummyPiece,dummyGrid) == True:
            if c == "spawn":
                print("GAMEOVER!!!")
                #print(f"Passed to executeCommands: {currentSessionScoreTable}")
                sfx("game_over")
                gridState.gameOver(currentSessionScoreTable, ATHSobject)
            elif c == "moveDown":
                activePiece.solidify(gridState, dropperTimer, currentSessionScoreTable, ATHSobject)
                #print("*** piece solidified ***")
            else:
                pass
                #print("=====collision detected, not executing command=====")
        else:
            #print("+++ no collision detected, executing command +++")
            if c == "moveRight":
                activePiece.moveH(1)
                #sfx("move_piece")
            elif c == "moveLeft":
                activePiece.moveH(-1)
                #sfx("move_piece")
            elif c == "moveDown":
                activePiece.moveV(1)
                #if mute == False:
                    #sfx("move_piece")
            elif c == "rotate":
                activePiece.rotate()
                #sfx("rotate_piece")
            elif c == "spawn":
                activePiece.spawnNewPiece()

    commands.clear()

