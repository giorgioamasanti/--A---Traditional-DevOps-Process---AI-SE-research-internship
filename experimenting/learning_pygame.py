import pygame
from pygame.locals import *
import random

import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 540, 400
        self.commands = []
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        self._running = True
 
    def on_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                pygame.quit()
                break
            elif event.type == pygame.KEYDOWN:
                #self.commands.append("new_shape")
                pygame.draw.circle(self._display_surf, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (random.randint(0,540), random.randint(0,400)), 20)


    def on_loop(self):
        pass
    def on_render(self):
        pygame.draw.rect(self._display_surf, (0, 255, 255), (120,120,50,50))
        pygame.draw.circle(self._display_surf, (255, 0, 0), (300, 50), 20)
        pygame.display.update()
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            self.on_event()
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()