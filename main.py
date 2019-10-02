import sys
import pygame
from pygame.locals import *

# on doit "initialiser" PyGame
pygame.init()

# et définir la taille de la fenêtre (400x400)
screen = pygame.display.set_mode((400, 400))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

while True:
  screen.fill(BLACK)
  screen.set_at((10, 100), WHITE)
  pygame.display.update()
  for event in pygame.event.get(KEYDOWN):
    if event.key == K_q:
      # on quitte le programme lors d'un appui sur Q
      sys.exit()