import pygame
class Nave():
	""" Nave jugador space invaders"""
	def __init__(self,configuracion,pantalla):
		
		self.pantalla=pantalla
		
		#Lee configuracion 
		self.configuracion=configuracion
		
		#Carga la imagen de la nave
		self.imagen=pygame.image.load('imagenes/PlayerSprite.xpm')
		
		self.rect=self.imagen.get_rect() #rect de la nave
		self.rect_pantalla=pantalla.get_rect() #rect pantalla
		
		#Nave inicial ,en el CENTRO y INFERIOR de la pantalla
		self.rect.centerx=self.rect_pantalla.bottom
		self.rect.bottom=self.rect_pantalla.bottom
		
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