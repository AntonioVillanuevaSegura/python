import pygame
import pygame.mixer
class Sonidos():
	""" Clase para los distintos sonidos del Juego"""

	def __init__(self):
		pygame.mixer.init()		
		self.sonido_disparo = pygame.mixer.Sound('sonidos/shoot.wav')
		self.sonido_explota = pygame.mixer.Sound('sonidos/explosion.wav')
	
		
	
