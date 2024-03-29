import sys
import random
import pygame
from pygame.locals import *

# on doit "initialiser" PyGame
pygame.init()

# et définir la taille de la fenêtre (400x400)
screen = pygame.display.set_mode((400, 400))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (225, 225, 0)
snake = [
(1, 2),
(2, 2),
(3, 2),
(4, 2),
(5, 2)
]
egg = (10, 10)
clock = pygame.time.Clock()
dx, dy = 1, 0
egg_lives = True

def drawcell(pos, color):
  x, y = pos
  for i in range(x, x+20):
    for j in range(y, y+20):
      screen.set_at((i, j), color)

def draw_snake(snake, color):
  for p in snake:
    pos = p[0] * 20, p[1] * 20
    drawcell(pos, color)

def draw_egg(p, color):
    pos = p[0] * 20, p[1] * 20
    drawcell(pos, color)

def move_snake(snake, dx, dy):
  swap = []
  for pos in snake:
    x, y = pos
    x += dx
    y += dy
    if x > 19 or x < 0:
      x = x%20
    if y > 19 or y < 0:
      y = y%20
    swap.append((x, y))
  return swap

def new_move_snake(snake, dx, dy):
  x, y = snake[-1]
  x += dx
  y += dy
  if x > 19 or x < 0:
    x = x%20
  if y > 19 or y < 0:
    y = y%20
  return snake[1:] + [(x, y)]

def place_egg():
  x, y = random.randrange(0, 20), random.randrange(0, 20)
  while (x, y) in snake:
      x, y = random.randrange(0, 20), random.randrange(0, 20)
  return x, y

def growth(snake):
  x, y = snake[0]
  return [(x-dx, y-dy)] + snake

def eog(snake):
  tetx, tety = snake[-1]
  if (tetx, tety) in snake[:-1]:
    print("Score=")
    print(len(snake))
    sys.exit()

t = 0

while True:
  dt = clock.tick(60)
  t += dt

  if t>200:
    t = 0
    screen.fill(BLACK)
    snake = new_move_snake(snake, dx, dy)
    draw_snake(snake, WHITE)
    if egg in snake:
      egg_lives = False
      print("Yum")
    elif egg_lives == True:
      draw_egg(egg, YELLOW)
    elif egg_lives == False:
      egg = place_egg()
      snake = growth(snake)
      egg_lives = True
      draw_egg(egg, YELLOW)
    pygame.display.update()

    eog(snake)

  for event in pygame.event.get(KEYDOWN):
    if event.key == K_e:
      # on quitte le programme lors d'un appui sur E
      sys.exit()
    elif event.key == K_UP and (dx, dy)!=(0, 1):
      dx, dy = 0, -1
    elif event.key == K_DOWN and (dx, dy)!=(0, -1):
      dx, dy = 0, 1
    elif event.key == K_LEFT and (dx, dy)!=(1, 0):
      dx, dy = -1, 0
    elif event.key == K_RIGHT and (dx, dy)!=(-1, 0):
      dx, dy = 1, 0

