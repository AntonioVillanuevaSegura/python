import pygame
class Configuracion():
	""" Clase para guardar configuraciones del juego """
	def __init__(self):
		""" Inicializa la configuracion del juego  """
		#Configuracion pantalla
		self.nombre="Space Invaders"
		self.ancho_pantalla=1200
		self.alto_pantalla=800
		self.color_pantalla=(0,0,0) #0,0,0 es NEGRO
		self.offset_superior=100 #Donde empieza la flota de marcianos		
		
		#Configuracion de la nave
		#Factor desplazamiento X de la nave
		self.desplazamiento_nave=3
		self.num_vidas=3 #NUMERO DE VIDAS DEL JUGADOE 
		self.posicion_ny=700 #Posicion Y de la nave
		
		#Configuracion de los Disparos
		self.disparo_velocidad=20	
		self.disparo_ancho=3
		self.disparo_alto=15
		self.disparo_color=(255,255,255) #255,255,255 BLANCO
		
		#Configuracion marcianos
		self.velocidad_marciano=1
		self.velocidad_flota=10
		self.direccion_flota=1 # -1 izquierda 1 derecha
		self.cambia_imagen=20
		self.marciano_offset_x=75 #Centrado de la flota en la pantalla
		self.numero_disparos_simultaneos=2 #Cuantos disparos a la vez		
				
		self.num_marcianos_fila=11
		self.num_marcianos_vertical=5
		
		self.espacio_x=1 #Espaciado en la fila entre marcianos
		self.espacio_y=1.5#Espaciado vertical en Y entre marcianos
				
		#Bunkers
		self.bunker_y=600
		
	def incrementa_velocidad(self,velocidad=1):
		""" incrementa velocidad del juego"""
		self.velocidad_marciano =velocidad -0.6
		#self.velocidad_flota	+=2	
