import pygame

pygame.init()

screen_width = 500
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
