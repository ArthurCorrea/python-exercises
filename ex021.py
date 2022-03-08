# Crie um programa que reproduza um áudio em MP3.
"""import os
import time
os.startfile(r'kalimba.mp3')
time.sleep(10)"""

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('kalimba.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()
