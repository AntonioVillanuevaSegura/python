import pygame
import pygame.mixer
DIR_SONIDO = "sonidos/"
class Sonidos():
	""" Clase para los distintos sonidos del Juego"""
	
	def __init__(self):
		pygame.mixer.init()		
		self.sonido_disparo =pygame.mixer.Sound( DIR_SONIDO + 'shoot.wav')
		self.sonido_explota = pygame.mixer.Sound (DIR_SONIDO + 'explosion.wav')
		self.marciano_explota =pygame.mixer.Sound( DIR_SONIDO + 'invaderkilled.wav')
	
		
	
