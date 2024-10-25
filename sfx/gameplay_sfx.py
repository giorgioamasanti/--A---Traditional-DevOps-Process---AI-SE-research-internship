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

pygame.mixer.init()

#dictionary which maps name of sound effect to the path to that file
sound_library = {"game_over": resource_path("assets/music_and_sounds/game_over.mp3"),
                 "move_piece": resource_path("assets/music_and_sounds/move_piece.mp3"),
                 "rotate_piece": resource_path("assets/music_and_sounds/rotate_piece.mp3"),
                 "line_clear": resource_path("assets/music_and_sounds/line_clear.mp3"),
                 "solidify": resource_path("assets/music_and_sounds/solidify.mp3")}

def sfx(sound):

    if sound in sound_library.keys():
        effect = pygame.mixer.Sound(sound_library[sound])
        effect.play()
    else:
        return KeyError(f"{sound} is not a recognised sound")