from Shortcuts import *

import pygame
from pygame.locals import *

import sys


SCREEN = pygame.display.setmode((500,400),0,32)
pygame.display.set_caption("QFC: Quest For Civilization")

loaded = Load_all_Images('png', 'media/') #Shortcuts
sound = Load_all_Sound(('mp3', 'ogg'), 'media/')

while 1:
  for evt in pygame.event.get():
    if event.type == QUIT:
      sys.exit()
  Update(SCREEN, loaded, sound)
