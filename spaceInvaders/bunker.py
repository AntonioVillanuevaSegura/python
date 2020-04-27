import pygame
from pygame.sprite import Sprite
class Bunker(Sprite):
	""" Bunker izquierda centro derecha"""
	def __init__(self,configuracion,pantalla,posicion):	
		super().__init__() #Al estilo python3 ...		
		
		#Configuracion dura
		self.configuracion=configuracion
		
		#Pantalla
		self.pantalla=pantalla		
		self.rect_pantalla=pantalla.get_rect() #rect de pantalla		
		
		#Carga la imagen del bunker
		self.image=pygame.image.load('imagenes/ShieldImage.xpm')				
		self.rect=self.image.get_rect() #rect del bunker
		
		#Posicion del bunquer
		self.rect.centerx=self.rect_pantalla.bottom
		
		#Valor decimal representando posicion central bunker
		self.centro=float(self.rect.centerx)
		
		#Inicializo coordenada Y  segun configuracion
		self.rect.y= self.configuracion.bunker_y	
			
		#Inicializo x sengun 0==izq 1==centro 2==derercha		
		if posicion==0:#IZQUIERDA
			self.rect.x= self.rect_pantalla.left+self.rect.width
		elif posicion==1:#CENTRO
			#self.rect.x= self.rect_pantalla.centerx-self.rect.width	
			self.rect.x= self.rect_pantalla.centerx	-(self.rect.width/2)
		elif  posicion==2:#DERECHA 2
			self.rect.x= self.rect_pantalla.right-2*self.rect.width						
		
		

	def dibuja(self):
		""" Dibuja el bunker en su posicion """
		self.pantalla.blit(self.image,self.rect)
		
		
	def update(self):
		""" actualiza el estado/pos del bunker """
		print ("update bunker")
	
	def modifica(self):
		print ("modifica imagen explosion ")

