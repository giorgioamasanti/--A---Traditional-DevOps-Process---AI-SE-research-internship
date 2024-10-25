import sys
import os
# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame

def resource_path(relative_path):
    """ Get the absolute path to a resource, works for both dev and PyInstaller. """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class backgroundMusic():
    def __init__(self):
        self.file = resource_path("assets/music_and_sounds/background_music.mp3")
        self.background_music_playing = True
        pygame.mixer.music.load(self.file)
        pygame.mixer.music.play()

    def toggle_music(self):
        if self.background_music_playing == True:
            self.background_music_playing = False
            pygame.mixer.music.stop()
        elif self.background_music_playing == False:
            self.background_music_playing = True
            pygame.mixer.music.play()

    def check_music_toggle(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    self.toggle_music()
                    print("toggled music")
