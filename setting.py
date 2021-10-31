import pygame
from pygame.locals import *


global FPS, SCREEN_RATIO, SCREEN_WIDTH, SCREEN_HEIGHT, font, white
global PIPE_GAP, PIPE_FREQUENCY, BG, GROUND_IMG, SCROLL_SPEED, GROUND_SCROLL, POP_SIZE
global MAX_PIPE, MAX_FITNESS

FPS = 60

SCREEN_RATIO = 0.7
SCREEN_WIDTH = SCREEN_RATIO * 864
SCREEN_HEIGHT = SCREEN_RATIO * 936

# define game variable
PIPE_GAP = 200
PIPE_FREQUENCY = 1600

# load images
BG = pygame.image.load('img/bg.png')
GROUND_IMG = pygame.image.load('img/ground.png')

SCROLL_SPEED = 4
GROUND_SCROLL = 0

POP_SIZE = 5

MAX_PIPE = 0
MAX_FITNESS = 0
