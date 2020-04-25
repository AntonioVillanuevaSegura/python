"""Space Invaders version Python3 por Antonio Villanueva Segura """
""" pip3 install pygame"""
#https://github.com/thepasterover/alien_invasion/issues/1
import pygame

from configuracion import Configuracion #Configuracion del juego
from nave import Nave #importa Nave Jugador
import funciones as func #Importa funciones
from pygame.sprite import Group # Para guardar disparos y alien
from disparo import Disparo
from marciano import Marciano

#http://www.pygame.org/docs/tut/SpriteIntro.html

def run():
	""" Inicio del juego y crea el screen del juego """
	
	pygame.init()
	
	
	configuracion=Configuracion() #Configuracion inicial del juego
	
	#Lee la configuracion de pantalla 
	pantalla=pygame.display.set_mode((configuracion.ancho_pantalla,
										configuracion.alto_pantalla))
	
	pygame.display.set_caption(configuracion.nombre)#Nombre del juego
	
	#Crea una instancia de una nave
	nave= Nave(configuracion,pantalla)
	
	#Crea una instancia de un marciano
	marciano=Marciano(configuracion,pantalla)
	
	#Creo la flota de marcianos
	marcianos=Group()
	
	#Crea la flota de marcianos
	func.crear_flota(configuracion,pantalla,nave,marcianos)
	
	#Guarda los disparos en un grupo de pygame.sprite
	disparos=Group()
		
	#Bucle principal
	while True:
		
		#Mira eventos de teclado o raton		
		func.analiza_eventos(configuracion,pantalla,nave,disparos)
				
		#Dibuja la nave del jugador
		nave.actualiza()
		
		#Actualiza TODOS los disparo en el GROUP pero es un disparo
		func.actualiza_disparos(configuracion,pantalla,nave,marcianos,disparos) #Este update() esta en la clase disparo
		
		func.actualiza_marcianos(configuracion,marcianos)
		
		func.actualiza_pantalla(configuracion,pantalla,nave,marcianos,disparos)
		
		#Muestra en pantalla
		pygame.display.flip()

run()
