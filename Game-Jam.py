#!/usr/bin/env python

import sys, pygame, random, time, math, glob, json
import random
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'

'''
with open ('z_dict.py') as json_data:
    world = json.load(json_data)
'''

class Background(pygame.sprite.Sprite):
                    def __init__(self, image_file, location):
                        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
                        self.image = pygame.image.load('room.jpg')
                        self.rect = self.image.get_rect()
                        self.rect.left, self.rect.top = location
        
class Game:
	def __init__(self, font, color, points_position, lives_position):
		self.font = font
		self.color = color
		self.points_position = points_position
		self.lives_position = lives_position
		
	def draw_points(self,screen,points):
		points = world['Begin']
		f = self.font.render(points,True,self.color)
		screen.blit(f,points_position)

	def draw_lives(self,screen,lives):
		lives = str(lives)
		f = self.font.render(lives,True,self.color)
		screen.blit(f,lives_position)

	
screen_size = (800,800)
BackGround = Background('room.jpg', [0,0])


def main():
	pygame.init()
	font = pygame.font.SysFont("arial",30)
	screen = pygame.display.set_mode(screen_size)
	'''
	pygame.mixer.music.load('Music.mp3')
	pygame.mixer.music.play(-1)

	'''
	
	Running = True
	while Running:
		screen.fill([255, 255, 255])
		screen.blit(BackGround.image, BackGround.rect)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
			if event.type == pygame.MOUSEMOTION:
				pos = pygame.mouse.get_pos()
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
			if event.type == pygame.KEYDOWN:
				keys = pygame.key.get_pressed()
		pygame.display.flip()


if __name__ == '__main__':
	main()


