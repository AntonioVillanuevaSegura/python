import pygame
from pygame.sprite import Sprite

class Marciano(Sprite):
	""" Modelizamos un simple marciano ,heredamos de Sprite """
	def __init__(self,configuracion,pantalla):
		""" Inicializo la super clase Sprite """
		super().__init__() #Al estilo python3 ...
		self.pantalla=pantalla
		self.configuracion=configuracion
		
		#Cargo la 1a. imagen del marciano 
		self.image=pygame.image.load('imagenes/Alien0.xpm')	
		
		#Defino el rectangulo que define  esta imagen
		self.rect=self.image.get_rect()
		
		#Inicializo x,y con una coordenada de base,segun rectangulo
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		
		#Posicion exacta del marciano
		self.x =float(self.rect.x)
		
	def dibuja(self):
		""" Dibuja el marciano en su posicion actual """
		self.pantalla.blit(self.image,self.rec)
	
	def update(self):
		"""Mueve el marciano derecha o izquierda  segun 1 o -1"""		
		self.x +=(self.configuracion.velocidad_marciano
								*self.configuracion.direccion_flota)							
		self.rect.x = self.x
	
	def borde(self):
		""" Si un marciano toca un borde de la pantalla cambia """
		pantalla_rect=self.pantalla.get_rect() #Recupera rect. pantalla
		
		#El rectangulo.derecho del marciano ha superado el bord. derecho
		if self.rect.right >= pantalla_rect.right:
			return True
			
		elif self.rect.left <= 0:#El marciano ha llegado a x==0 ?
			
			return True
		
		return False
			
			
