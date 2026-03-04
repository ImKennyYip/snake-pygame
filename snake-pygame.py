import pygame
from sys import exit #terminate the program
import random

ROWS = 25
COLS = ROWS
TILE_SIZE = 25
WINDOW_WIDTH = TILE_SIZE * COLS #25*25 = 625
WINDOW_HEIGHT = TILE_SIZE * ROWS #25*25 = 625

pygame.init() #always needed to initialize pygame
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake") #title of the window
clock = pygame.time.Clock() #used for the frame rate

def get_random(limit):
    return random.randint(0, limit-1) * TILE_SIZE

snake = []
snake.append(pygame.Rect(get_random(COLS), get_random(ROWS), TILE_SIZE, TILE_SIZE)) #head
snake_velocity = (0, 0) #(velocity x, velocity y)
food = pygame.Rect(get_random(COLS), get_random(ROWS), TILE_SIZE, TILE_SIZE)

while True: #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #user clicks the X button in window
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
        #if event.key == pygame.K_UP or event.key ==  pygame.K_w):
            if event.key in (pygame.K_UP, pygame.K_w):
                snake_velocity = (0, -TILE_SIZE)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                snake_velocity = (0, TILE_SIZE)
            elif event.key in (pygame.K_LEFT, pygame.K_a):
                snake_velocity = (-TILE_SIZE, 0)
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                snake_velocity = (TILE_SIZE, 0)
    #move
    for i in range(len(snake)-1, 0, -1):
        snake[i] = snake[i-1].copy()
    snake[0].move_ip(snake_velocity)

    if snake[0].center == food.center:
        snake.append(food)
        food = pygame.Rect(get_random(COLS), get_random(ROWS), TILE_SIZE, TILE_SIZE)

    if not window.get_rect().contains(snake[0]):
        snake.clear()
        snake.append(pygame.Rect(get_random(COLS), get_random(ROWS), TILE_SIZE, TILE_SIZE))
        food = pygame.Rect(get_random(COLS), get_random(ROWS), TILE_SIZE, TILE_SIZE)

    #draw
    window.fill("black")
    for snake_part in snake:
        pygame.draw.rect(window, "cyan", snake_part)
    pygame.draw.rect(window, "yellow", food)

    pygame.display.update()
    clock.tick(20) #10 frames per second (fps)