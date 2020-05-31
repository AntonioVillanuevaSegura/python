import pygame
from pygame.sprite import Sprite

class Bunker(Sprite):
	""" Bunker izquierda centro derecha"""
	def __init__(self,configuracion,pantalla,posicion):	
		""" inicializamos la super clase padre Sprite """

		super().__init__() #Python3	
		#pygame.sprite.Sprite.__init__(self)		
		
		#Configuracion 
		self.configuracion=configuracion

		#Carga la imagen del bunker
		self.image=pygame.image.load('imagenes/ShieldImage.xpm').convert_alpha()
						
		#Defino el rectangulo que define  esta imagen
		self.rect= (self.image).get_rect()		
		
		#Pantalla
		self.pantalla=pantalla		
		self.rect_pantalla=pantalla.get_rect() #rect de pantalla		
				
		#Disparo en el bunker
		self.disparo=pygame.image.load('imagenes/bomba.xpm').convert_alpha()	
		
		#Inicializo coordenada Y  segun configuracion
		self.rect.y= self.configuracion.bunker_y	

		self.rect.centerx=posicion
		
	def dibuja(self):
		""" Dibuja el bunker en su posicion """
		self.pantalla.blit(self.image,self.rect)

	def alcanzado(self,disparo,disparos,tipo=True):
		""" Coordenada Disparo en el bunker disparo  """
		
		#Analizar hasta donde puede descender el disparo 		
		y=self.profundidad(disparo,tipo)
				
		#Si no encuentra obstaculo hasta la base lo elimina

		if tipo:#Disparo de un marciano
			if y < self.rect.height -1:
				disparos.remove(disparo)
		else:#Disparo de la nave
			if y > 0:
				disparos.remove(disparo)			
			
			
		#La posicion local en eje X del disparo respecto al Bunker 0
		xlocal = abs (disparo.rect.x - self.rect.x)

		if tipo:
			self.image.blit(self.disparo, [xlocal,y])		
		else:
			#pygame.transform.flip(L_SQUIR_IMG, True, False)
			self.image.blit(pygame.transform.flip(self.disparo,False,True),
							[xlocal-5,y-22])
		
	def profundidad(self,disparo,tipo=True):
		""" mira si puede descender mas el disparo """
		blanco=(255,255,255,255) #Color Blanco del bunker
		xlocal = abs (disparo.rect.x - self.rect.x)

		if tipo:
			ylocal = 0
		else:			
			ylocal=self.rect.height-1
			
		y=ylocal
		
		#Analiza la vertical Y del bunker en esta coordenada
		if tipo:#Disparo marciano
			while y < (self.rect.height -1) :
				if self.image.get_at( (xlocal,y) )==blanco:
					return y
				y+=1
				
		else:#Disparo de la nave
			while y > 0 :
				if self.image.get_at( (xlocal,y) )==blanco:
					return y
				y-= 1			
			
				
		return y	
	
