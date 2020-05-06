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
		
		#TEST A BORRAR 
					
		#self.image.blit(self.disparo, [0,50] )
		
		#Posicion centerx del bunquer
		#self.rect.centerx=self.rect_pantalla.bottom
		
		#Valor decimal representando posicion central bunker
		#self.centro=float(self.rect.centerx)
		
		#Inicializo coordenada Y  segun configuracion
		self.rect.y= self.configuracion.bunker_y	

		self.rect.centerx=posicion
		
	def dibuja(self):
		""" Dibuja el bunker en su posicion """
		self.pantalla.blit(self.image,self.rect)

	def alcanzado(self,disparo):
		""" Coordenada Disparo en el bunker disparo  """
		#Analizar si puede descender mas 
		"""
		print ("B.left  = ",self.rect.left,"B.top  = ",self.rect.top," B.width ",self.rect.width,
		" ,D.left  = ",disparo.rect.left,"D.top  = ",disparo.rect.bottom," dibuja en ",disparo.rect.centerx,
		" , ",self.rect.top)		
		"""
		#Actualiza la imagen del bunker con el disparo recibido
		#self.image.blit(self.disparo, (disparo.rect.centerx,self.rect.top) )
		
		#Dibuja en la posicion inicial .... !!!!
		#self.image.blit(self.disparo, [0,50] )
		
		#reposicionar localmente el disparo
		
		xlocal = abs (disparo.rect.x - self.rect.x)
		print (xlocal)
		self.image.blit(self.disparo, [xlocal,0])		
		"""
		
		self.image.blit(self.disparo, [xlocal,self.rect.top])
"""
		
	def profundidad(self,disparo):
		""" mira si puede descender mas el disparo """
		
