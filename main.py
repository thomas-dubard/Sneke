import sys
import pygame
from pygame.locals import *

# on doit "initialiser" PyGame
pygame.init()

# et définir la taille de la fenêtre (400x400)
screen = pygame.display.set_mode((400, 400))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (125, 125, 0)
snake = [
(1, 1),
(2, 1),
(2, 2),
(3, 2),
(4, 2),
(5, 2)
]
egg = (10, 10)

def drawcell(pos, color):
  x, y = pos
  for i in range(x, x+20):
    for j in range(y, y+20):
      screen.set_at(pos, color)
  pygame.display.update()

def draw_snake(snake, color):
  for p in snake:
    pos = p[0] * 20, p[1] * 20
    drawcell(pos, color)

def draw_egg(pos, color):
  drawcell(pos, color)

while True:
  screen.fill(BLACK)
  draw_snake(snake, WHITE)
  draw_egg(egg, YELLOW)
  pygame.display.update()
  for event in pygame.event.get(KEYDOWN):
    if event.key == K_q:
      # on quitte le programme lors d'un appui sur Q
      sys.exit()