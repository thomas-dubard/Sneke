import sys
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
(1, 1),
(2, 1),
(2, 2),
(3, 2),
(4, 2),
(5, 2)
]
egg = (10, 10)
clock = pygame.time.Clock()
dx, dy = 1, 0

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

def move_snake():
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
  snake = swap

while True:
  clock.tick(60)
  screen.fill(BLACK)
  move_snake()
  draw_snake(snake, WHITE)
  draw_egg(egg, YELLOW)
  pygame.display.update()
  for event in pygame.event.get(KEYDOWN):
    if event.key == K_q:
      # on quitte le programme lors d'un appui sur Q
      sys.exit()