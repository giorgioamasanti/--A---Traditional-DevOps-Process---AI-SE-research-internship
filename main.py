import pygame, random, time
from game_render.gridRender import mainGameRender
from game_state.gridState import gridState
from game_state.activePiece import activePiece, Tetrominoes, active_colours
from user_inputs.commands import receiveInputs, executeCommands
from game_state.drop import dropperTimer
from game_render.gameOverScreen import gameOverRender
from sfx.background_music import backgroundMusic
from game_state.high_score import scoreTable
from game_render.speed_up_render import speedUpRender 
from persistence.all_time_hs import allTimeHighScores


class main:
    def __init__(self):
        """ Initialize the game """
        pygame.init() #initialise game
        self.running = True
        self.clock = pygame.time.Clock()
        #grid properties
        self.gridShape = (10,20)
        self.cellSize = 36
        #initializing game window
        self.windowWidth = self.gridShape[0]*self.cellSize + 280
        self.windowHeight = self.gridShape[1]*self.cellSize
        self.displaySurf = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        #taking grid properties and defining an initial gridState
        self.gridState = gridState(self.gridShape, self.cellSize)
        self.activePiece = activePiece(random.choice(list(Tetrominoes.keys())), [4,4])
        #defining the commands list
        self.commands = []
        #defining the dropper timer
        self.dropperTimer = dropperTimer(dropInterval=0.40) # was 0.5 before
        #changing name of window
        pygame.display.set_caption("Tetris")
        #initializing background music
        self.b_music = backgroundMusic()
        #current session high score table
        self.currentSessionScoreTable = scoreTable()
        #print(f"Upon initialization: {self.currentSessionScoreTable}")
        self.speedUpTimer = time.time() - 2
        #initializing all time high score object
        self.ATHSobject = allTimeHighScores()

    def main_game_events(self):
        """ Handle user input and automated events """
        receiveInputs(self.commands, self.activePiece) # takes all the user inputs and places them onto a command stack
        executeCommands(self.commands, self.activePiece, self.gridState, self.dropperTimer, self.currentSessionScoreTable, self.ATHSobject, self.b_music ) # executes the commands from the bottom of the stack - but if a collision would occur it doesn't execute the command
        self.dropperTimer.checkDrop(self.activePiece, self.gridState, self.currentSessionScoreTable, self.ATHSobject) # drops the active piece by 1 row when the drop interval has passed
        self.gridState.rowClear(self.dropperTimer.dropInterval) # clears any full rows and moves above rows down
        self.dropperTimer.dropInterval = self.gridState.getNewDropTime()
        #print(self.dropperTimer.dropInterval)
        
    def main_game_update(self):
        """ Update game state based on all the changes that just occurred"""
        self.gridState.updateGrid(self.activePiece) # updates the grid array with the active piece and solid pieces
    
    def main_game_render(self):
        """ Render game state """
        #renders the grid and other stuff for main game
        mainGameRender(self.gridState, self.displaySurf, self.currentSessionScoreTable)
        #print(f"before flag check:{speedUpTimer}")
        if self.gridState.speedUpFlag:
            self.gridState.speedUpFlag = False
            self.speedUpTimer = time.time()
        if time.time() < self.speedUpTimer + 2:
            speedUpRender(self.displaySurf, self.gridState)
        pygame.display.update()

    def gameover_events(self):
        """ Handles exit events as well as new game input 'N' for when the game is in gameover state"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        #Reinitializing the gridState (i.e. going back into the main game mode)
                        self.gridState = gridState(self.gridShape, self.cellSize)
                        self.activePiece = activePiece(random.choice(list(Tetrominoes.keys())), [4,4])

    def gameover_render(self):
        """ Renders the game over screen"""
        gameOverRender(self.displaySurf, self.gridState, self.windowWidth, self.windowHeight)

    def run(self):
        """ Run the game """

        #main game loop
        while self.running:
            if self.gridState.gameState == "playing": 
                self.main_game_events()
                self.main_game_update()
                self.main_game_render()
            elif self.gridState.gameState == "game over":
                self.gameover_events()
                self.gameover_render()
            self.clock.tick(60)

if __name__ == "__main__":
    """ Run the game """
    game = main()
    game.run()

