import pygame, random
from game_render.gridRender import gridRender
from game_state.gridState import gridState
from game_state.activePiece import activePiece, Tetrominoes, colour
from user_inputs.commands import receiveInputs, executeCommands


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
        self.gridState = gridState(self.gridShape, self.cellSize, self.displaySurf)
        self.activePiece = activePiece(random.choice(list(Tetrominoes.keys())), random.choice(list(colour.keys())), [4,4])
        #defining the commands list
        self.commands = []

    
    def events(self):
        """ Handle game events """
        receiveInputs(self.commands, self.activePiece)
        executeCommands(self.commands, self.activePiece)

    def update(self):
        """ Update game state """
        self.gridState.updateGrid(self.activePiece)

    def render(self):
        """ Render game state """
        #renders the grid based on current grid state
        gridRender(self.gridState)
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

