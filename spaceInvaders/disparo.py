import pygame
from pygame.sprite import Sprite

class Disparo(Sprite):#Heredamos de Sprite para simplificar los disparos
	""" implementa un disparo """
	def __init__(self,configuracion,pantalla,nave,tipo=True):
		""" inicializamos la super clase padre Sprite """

		super().__init__() #Python3		
		self.tipo=tipo #Tipo de disparo True Nave False Marciano		
		self.pantalla = pantalla
		
		#Crea un disparo inicialmente en (0,0) , en un rect x,y
		self.rect=pygame.Rect(0,0,configuracion.disparo_ancho,
										configuracion.disparo_alto)
										
		#centerx y top del disparo coinciden con los de la nave
		self.rect.centerx=nave.rect.centerx #centro
		self.rect.top=nave.rect.top #parte superior 
	
		#Guarda los disparos como un valor float, que recupera de y
		self.y=float(self.rect.y)
		
		#Color del disparo ,lo recupera de la configuracion
		self.color=configuracion.disparo_color
		
		#Velocidad del disparo , lo recupera de la configuracion
		self.velocidad=configuracion.disparo_velocidad
		
	def update(self):
		""" mueve ,actualiza el movimiento del disparo """
		if self.tipo:#Disparo de Nave
			self.y -=self.velocidad
		else: #Disparo Marciano
			self.y +=self.velocidad/5
		
		#actualiza la posicion en el rect  Y del disparo 
		self.rect.y=self.y
		
	def dibuja(self):		
		""" Dibuja el disparo en la pantalla """
		pygame.draw.rect(self.pantalla,self.color,self.rect)
		
