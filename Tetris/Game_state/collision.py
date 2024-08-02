from game_state.activePiece import solid_colours, active_colours

class collisionError(Exception):
    def __init__(self, message=None):
        self.message = message
        super().__init__(self.message)  


def checkCollision(activePiece, gridState):
    """ Checks if a command would cause the active piece to go out of bounds or collide.
    Returns true if it would collide/go out of bounds
    Returns false otherwise
    """
    #check for collision with the walls
    if not(activePiece.coords[0] in range(0, gridState.gridShape[1]-activePiece.height+1) and activePiece.coords[1] in range(0, gridState.gridShape[0]-activePiece.width+1)):
        print("Out of bounds detected")
        return True

    #check for collision with solid blocks
    for i in range(activePiece.width):
        for j in range(activePiece.height):
            if activePiece.shape[j][i] != 0 and gridState.solidArray[activePiece.coords[0]+j][activePiece.coords[1]+i] != 0:
                print("Collided with block")
                return True   
     
    #no collisions
    return False


"""
    tryExecuteCommands(command, replica_piece)   #execute the command on the replica piece
    new_grid.updateGrid(replica_piece)  #update the grid with the new replica piece

    #check for collision difference between original and new grid
    for y in range(len(original_grid.array)):
        for x in range(len(original_grid.array[0])):
            if original_grid.solidArray[y][x] != 0 and new_grid.array[y][x] in active_colours.keys():
                print("Collision detected")
                return True
                #raise collisionError("Collision detected")
            else:
                return False
"""
    
    