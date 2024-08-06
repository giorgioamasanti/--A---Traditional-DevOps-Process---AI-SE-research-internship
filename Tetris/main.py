import pygame, random
from game_render.gridRender import gridRender
from game_state.gridState import gridState
from game_state.activePiece import activePiece, Tetrominoes, active_colours
from user_inputs.commands import receiveInputs, executeCommands
from game_state.drop import dropperTimer
#from game_state.drop import checkForDrop


class main:
    def __init__(self):
        """ Initialize the game """
        pygame.init() #initialise game
        self.running = True
        self.clock = pygame.time.Clock()
        #grid properties
        self.gridShape = (10,20)
        self.cellSize = 36
        self.displaySurf = pygame.display.set_mode((self.gridShape[0]*self.cellSize, self.gridShape[1]*self.cellSize))
        #taking grid properties and defining an initial gridState
        self.gridState = gridState(self.gridShape, self.cellSize)
        self.activePiece = activePiece(random.choice(list(Tetrominoes.keys())), [4,4])
        #defining the commands list
        self.commands = []
        #defining the dropper timer
        self.dropperTimer = dropperTimer(dropInterval=0.5)

    
    def events(self):
        """ Handle user input and automated events """
        receiveInputs(self.commands, self.activePiece) # takes all the user inputs and places them onto a command stack
        executeCommands(self.commands, self.activePiece, self.gridState, self.dropperTimer) # executes the commands from the bottom of the stack - but if a collision would occur it doesn't execute the command
        self.dropperTimer.checkDrop(self.activePiece, self.gridState) # drops the active piece by 1 row when the drop interval has passed
        self.gridState.rowClear() # clears any full rows and moves above rows down

    def update(self):
        """ Update game state based on all the changes that just occurred"""
        self.gridState.updateGrid(self.activePiece) # updates the grid array with the active piece and solid pieces

    def render(self):
        """ Render game state """
        #renders the grid based on current grid state
        gridRender(self.gridState, self.displaySurf)
        pygame.display.update()

    def run(self):
        """ Run the game """

        #main game loop
        while self.running:
            self.events()
            self.update()
            self.render()
            self.clock.tick(60)

if __name__ == "__main__":
    """ Run the game """
    game = main()
    game.run()

