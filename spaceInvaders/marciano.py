import pygame
from pygame.sprite import Sprite
import random
from sonidos import Sonidos #Sonidos Juego

class Marciano(Sprite):
	""" Modelizamos un simple marciano ,heredamos de Sprite """
	def __init__(self,configuracion,pantalla,fila=0):
		""" Inicializo la super clase Sprite """
		super().__init__() #Al estilo python3 ...
	
		self.pantalla=pantalla
		self.pantalla_rect=pantalla.get_rect()
		self.configuracion=configuracion
		self.fila=fila #Nos va servir para dar la puntuacion 
		
		self.sonido=Sonidos() #Instancia de sonidos
		self.sonido_movimiento=1 #Sonido que se ejecuta hay cuatro
		self.sonido_tempo=0 
		
		#Cargo imagenes que utiliza el marciano
		#Segun la fila da el tipo de Alien
		if fila==0:
			ALIEN0="imagenes/Alien3.xpm"
			ALIEN1="imagenes/Alien3b.xpm"
		elif fila==1 or fila==2:
			ALIEN0="imagenes/Alien1.xpm"
			ALIEN1="imagenes/Alien1b.xpm"	
		else:
			ALIEN0="imagenes/Alien0.xpm"
			ALIEN1="imagenes/Alien0b.xpm"					
		
		#Carga imagenes a utilizar 
		self.imageA=pygame.image.load(ALIEN0)			
		self.imageB=pygame.image.load(ALIEN1)			
		self.explosion=pygame.image.load('imagenes/AlienExplode.xpm')
		
		
		self.cambia_imagen=configuracion.cambia_imagen #cada cuanto cambia
		self.frame_imagen=1
		
		#imagen de referencia	
		self.image=pygame.image.load(ALIEN0)
		
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
		
		self.imagen() #Cambia imagen segun paso
		
		#self.musica()
			
	def borde(self):
		""" Si un marciano toca un borde de la pantalla cambia """
		#pantalla_rect=self.pantalla.get_rect() #Recupera rect. pantalla
		
		#El rectangulo.derecho del marciano ha superado el bord. derecho
		if self.rect.right >= self.pantalla_rect.right:
			return True
			
		elif self.rect.left <= 0:#El marciano ha llegado a x==0 ?			
			return True
		
		return False

	def imagen(self):
		""" gestiona el cambio de imagen """
		#Actualiza imagen
		if self.cambia_imagen ==0 : #Ha llegado a 0
			self.cambia_imagen=40
			if self.frame_imagen==1:
				self.image=self.imageA
				self.frame_imagen=2
			else:
				self.image=self.imageB
				self.frame_imagen=1		
							
			
		self.cambia_imagen -=1		
			
	def disparo(self):
		""" crea un disparo aleatorio """
		if random.randint(0,100)<=1:
			return True
		return False 

	def explota (self):
		""" explosion marciano """
		self.pantalla.blit(self.explosion,self.rect)
		pygame.display.flip()
		
	def musica(self):
		""" sonido danza marcianos"""
		#print ("musica ",self.sonido_tempo)
		
		if self.sonido_tempo>35 :
			self.sonido_tempo=0
			#Sonidos movimiento, danza marcianera
			#pygame.mixer.stop()
			if self.sonido_movimiento==1:
				self.sonido.movimiento_1.play()	
				
			if self.sonido_movimiento==2:
				self.sonido.movimiento_2.play()	
				
			if self.sonido_movimiento==3:
				self.sonido.movimiento_3.play()										

			if self.sonido_movimiento==4:
				self.sonido.movimiento_4.play()					
		
			#Tipo de sonido relacionado al movimiento
			if self.sonido_movimiento<6:	
				self.sonido_movimiento+=1
			else:
				self.sonido_movimiento=1
		else:
			self.sonido_tempo+=1
		
