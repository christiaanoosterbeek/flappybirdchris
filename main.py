import pygame

pygame.init()

screen_width = 500
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

gravity = 0.5
bird_y = 200
bird_dy = 0
pipe_x = 500
pipe_dy = -3
gap_size = 150
pipe_width = 50
pipe_gap_y = 300
score = 0
font = pygame.font.SysFont(None, 40)
