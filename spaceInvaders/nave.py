import pygame
from pygame.sprite import Sprite
from time import sleep #retardo entre juegos 

class Nave(Sprite):
	""" Nave jugador space invaders"""
	def __init__(self,configuracion,pantalla):
		super().__init__() #Al estilo python3 ...		
		
		self.pantalla=pantalla
		
		#Lee configuracion 
		self.configuracion=configuracion
		
		#Carga la imagen de la nave
		self.imagen=pygame.image.load('imagenes/PlayerSprite.xpm')
		self.imagenExp1=pygame.image.load('imagenes/PlayerSprite0.xpm')
		self.imagenExp2=pygame.image.load('imagenes/PlayerSprite1.xpm')	
				
		
		self.rect=self.imagen.get_rect() #rect de la nave
		self.rect_pantalla=pantalla.get_rect() #rect pantalla
		
		#Nave inicial ,en el CENTRO y INFERIOR de la pantalla
		self.rect.centerx=self.rect_pantalla.bottom
		#self.rect.bottom=self.rect_pantalla.bottom
		self.rect.y=configuracion.posicion_ny
		
		#Valor decimal representando la posicion central de la nave
		self.centro=float(self.rect.centerx)
		
		#Flags de movimiento <-izquierda derecha ->
		self.izquierda=False
		self.derecha=False
		
	def dibuja(self):
		""" Dibuja la nave en su posicion """
		self.pantalla.blit(self.imagen,self.rect)
		
	def actualiza(self):
		 """ Actualiza la posicion de la nave ,mira flags"""
		 
		 #if self.derecha and self.rect.right <self.pantalla.right:# DERECHA 
		 if (self.derecha and 
			self.rect.right < self.rect_pantalla.right):# DERECHA 		 
				
			 self.centro += self.configuracion.desplazamiento_nave 

		 if (self.izquierda and
			self.rect.left > 0):# IZQUIERDA 
			 self.centro -= self.configuracion.desplazamiento_nave 	
			 		 		
		 #Ahora actualiza el rect del objeto		
		 self.rect.centerx=self.centro
		 
	def centra (self):
		""" centra en el centro de la pantalla ,la nave """
		self.centro=(self.pantalla.get_rect()).centerx
		
	def explota (self):
		""" explosion nave  """
		self.pantalla.blit(self.imagenExp1,self.rect)
		pygame.display.flip()
		sleep(0.1)
		self.pantalla.blit(self.imagenExp2,self.rect)
		pygame.display.flip()				
		sleep(0.1)
		
		
						
		
