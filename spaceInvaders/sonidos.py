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
		
		self.movimiento_1=pygame.mixer.Sound( DIR_SONIDO + 'fastinvader1.wav')
		self.movimiento_2=pygame.mixer.Sound( DIR_SONIDO + 'fastinvader2.wav')
		self.movimiento_3=pygame.mixer.Sound( DIR_SONIDO + 'fastinvader3.wav')	
		self.movimiento_4=pygame.mixer.Sound( DIR_SONIDO + 'fastinvader4.wav')					
	
		
	
