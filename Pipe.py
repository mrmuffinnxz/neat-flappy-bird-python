import pygame
from pygame.locals import *
import setting

class Pipe(pygame.sprite.Sprite):

	def __init__(self, x, y, position):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("img/pipe.png")
		self.rect = self.image.get_rect()
		#position variable determines if the pipe is coming from the bottom or top
		#position 1 is from the top, -1 is from the bottom
		if position == 1:
			self.image = pygame.transform.flip(self.image, False, True)
			self.rect.bottomleft = [x, y - int(setting.PIPE_GAP / 2)]
		elif position == -1:
			self.rect.topleft = [x, y + int(setting.PIPE_GAP / 2)]

	def update(self):
		self.rect.x -= setting.SCROLL_SPEED
		if self.rect.right < 0:
			self.kill()