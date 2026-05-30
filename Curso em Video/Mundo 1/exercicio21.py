# É necessário instalar a biblioteca pygame para rodar esse código, para tal, rode um terminale em seu vscode 
import pygame
pygame.init()
pygame.mixer.music.load("Faint.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue