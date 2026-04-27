import pygame
from sys import exit #terminate the program

GAME_WIDTH = 500
GAME_HEIGHT = 500

pygame.init()                                               #always needed to initialize pygame
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT)) #create game window
pygame.display.set_caption("Snake")                         #title of the window
clock = pygame.time.Clock()                                 #used for the frame rate

#game loop
while True:
    for event in pygame.event.get():    #listen for all user events (button, key, mouse)
        if event.type == pygame.QUIT:   #user clicks on x button of window
            pygame.quit()               #exit pygame
            exit()                      #terminate the python program completely

    pygame.display.update()             #refresh game window
    clock.tick(10)                      #10 frames per second (fps)