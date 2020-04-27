"""Space Invaders version Python3 por Antonio Villanueva Segura """
""" http://computerarcheology.com/Arcade/SpaceInvaders/Code.html"""
""" pip3 install pygame"""
#https://github.com/thepasterover/alien_invasion/issues/1
import pygame

from configuracion import Configuracion #Configuracion del juego
from nave import Nave #importa Nave Jugador
import funciones as func #Importa funciones
from pygame.sprite import Group # Para guardar disparos y alien
from disparo import Disparo
from marciano import Marciano
from marcador import Marcador #Puntuaciones
from boton import Boton #Boton play
from bunker import Bunker

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
	#marciano=Marciano(configuracion,pantalla)
	
	#Creo la flota de marcianos
	marcianos=Group()
	
	#Crea la flota de marcianos
	func.crear_flota(configuracion,pantalla,nave,marcianos)
	
	#Guarda los disparos en un grupo de pygame.sprite
	disparos=Group()
	
	#Guarda los disparos marcianos en un grupo de pygame.sprite
	disparosM=Group()	
	
	#puntuaciones inicializa puntuaciones , n naves etc 
	marcador=Marcador(configuracion)
	
	#Crea un boton de play
	boton=Boton(configuracion,pantalla,"Juega")
	
	#Crea un bunker
	#bunker=Bunker(configuracion,pantalla,2)
	bunkers=Group()
	func.crear_bunkers(configuracion,pantalla,bunkers)
		
		
	#Bucle principal
	while True:
		
		#Mira eventos de teclado o raton		
		func.analiza_eventos(configuracion,pantalla,marcador,boton,nave,disparos)
					
		if marcador.juego_activo: #Juego activo ?Todas las vidas ?
			#Dibuja la nave del jugador
			nave.actualiza()
			
			#Actualiza TODOS los disparo en el GROUP pero es un disparo
			func.actualiza_disparos(configuracion,pantalla,nave,marcianos,disparos) #Este update() esta en la clase disparo
			
			func.actualiza_marcianos(configuracion,marcador,pantalla,nave,marcianos,disparos)			
			
			#Actualiza disparos Marcianos
			#func.actualiza_disparosMarcianos(configuracion,pantalla,nave,marcianos,disparosM) #Este update() esta en la clase disparo						
			
		func.actualiza_pantalla(configuracion,pantalla,marcador,nave,marcianos,disparos,boton,bunkers)
		
		#Muestra en pantalla
		pygame.display.flip()

run()
