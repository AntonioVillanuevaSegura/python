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
		
		#Sonido danza marciana
		
		self.sonido_movimiento=1 #Sonido que se ejecuta hay cuatro
		self.sonido_tempo=0 		
		
		self.movimiento_1=pygame.mixer.Sound( DIR_SONIDO + 'fastinvader1.wav')
		self.movimiento_1.set_volume(0.1)

		self.movimiento_2=pygame.mixer.Sound( DIR_SONIDO + 'fastinvader2.wav')
		self.movimiento_2.set_volume(0.1)
				
		self.movimiento_3=pygame.mixer.Sound( DIR_SONIDO + 'fastinvader3.wav')	
		self.movimiento_3.set_volume(0.1)		
		
		self.movimiento_4=pygame.mixer.Sound( DIR_SONIDO + 'fastinvader4.wav')					
		self.movimiento_4.set_volume(0.1)		
		
	def danza_marciana(self,factor):
		""" sonido danza marcianos"""
		#print ("musica ",self.sonido_tempo)
		
		if self.sonido_tempo>36// factor :
			self.sonido_tempo=0
			#Sonidos movimiento, danza marcianera
			#pygame.mixer.stop()
			if self.sonido_movimiento==1:
				self.movimiento_1.play()	
				
			if self.sonido_movimiento==2:
				self.movimiento_2.play()	
				
			if self.sonido_movimiento==3:
				self.movimiento_3.play()										

			if self.sonido_movimiento==4:
				self.movimiento_4.play()					
		
			#Tipo de sonido relacionado al movimiento
			if self.sonido_movimiento<6:	
				self.sonido_movimiento+=1
			else:
				self.sonido_movimiento=1
		else:
			self.sonido_tempo+=1		
		
	
		
	
