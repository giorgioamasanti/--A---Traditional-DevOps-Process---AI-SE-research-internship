import pygame

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
            elif event.key == pygame.K_UP:
                commands.append("rotate")
            elif event.key == pygame.K_s:
                commands.append("spawn")


def executeCommands(commands, activePiece):
    for c in commands:
        if c == "moveRight":
            activePiece.move(1)
        elif c == "moveLeft":
            activePiece.move(-1)
        elif c == "rotate":
            activePiece.rotate()
        elif c == "spawn":
            activePiece.spawnNewPiece()
    commands.clear()
