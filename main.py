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

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        bird_dy = -10
bird_dy += gravity
  bird_y += bird_dy
  pipe_x += pipe_dy
  if pipe_x < -pipe_width:
    pipe_x = screen_width
    score += 1
  if bird_y < 0 or bird_y > screen_height:
    pygame.quit()
    quit()
  if pipe_x < 200 and (bird_y < pipe_gap_y or bird_y > pipe_gap_y + gap_size):
    pygame.quit()
    quit()

   screen.fill((135, 206, 250))
  pygame.draw.rect(screen, (0, 255, 0), (pipe_x, 0, pipe_width, pipe_gap_y))
  pygame.draw.rect(screen, (0, 255, 0),
                   (pipe_x, pipe_gap_y + gap_size, pipe_width,
                    screen_height - pipe_gap_y - gap_size))
  pygame.draw.circle(screen, (255, 255, 0),
                     (int(screen_width / 2), int(bird_y)), 20)
  score_text = font.render("Score: " + str(score), True, (255, 255, 255))
  screen.blit(score_text, (10, 10))

  pygame.display.update()

  clock.tick(60)
