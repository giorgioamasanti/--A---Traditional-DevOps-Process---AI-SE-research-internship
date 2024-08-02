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
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        #grid properties
        self.gridShape = (10,20)
        self.cellSize = 36
        self.displaySurf = pygame.display.set_mode((self.gridShape[0]*self.cellSize, self.gridShape[1]*self.cellSize))
        #taking grid properties and defining an initial gridState
        self.gridState = gridState(self.gridShape, self.cellSize)
        self.activePiece = activePiece(random.choice(list(Tetrominoes.keys())), random.choice(list(active_colours.keys())), [4,4])
        #defining the commands list
        self.commands = []
        #defining the dropper timer
        self.dropperTimer = dropperTimer(dropInterval=0.5)

    
    def events(self):
        """ Handle game events """
        receiveInputs(self.commands, self.activePiece)
        executeCommands(self.commands, self.activePiece, self.gridState)

    def update(self):
        """ Update game state """
        self.dropperTimer.checkDrop(self.activePiece, self.gridState)
        self.gridState.updateGrid(self.activePiece)

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
            self.clock.tick(30)

if __name__ == "__main__":
    """ Run the game """
    game = main()
    game.run()

