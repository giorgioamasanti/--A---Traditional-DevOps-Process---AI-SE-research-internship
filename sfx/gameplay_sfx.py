import sys
import os
# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame


pygame.mixer.init()

#dictionary which maps name of sound effect to the path to that file
sound_library = {"game_over": "assets/music_and_sounds/game_over.mp3",
                 "move_piece": "assets/music_and_sounds/move_piece.mp3",
                 "rotate_piece": "assets/music_and_sounds/rotate_piece.mp3",
                 "line_clear": "assets/music_and_sounds/line_clear.mp3",
                 "solidify": "assets/music_and_sounds/solidify.mp3"}

def sfx(sound):

    if sound in sound_library.keys():
        effect = pygame.mixer.Sound(sound_library[sound])
        effect.play()
    else:
        return KeyError(f"{sound} is not a recognised sound")