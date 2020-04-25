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
		
		#Configuracion de la nave
		#Factor desplazamiento X de la nave
		self.desplazamiento_nave=3
		
		#Configuracion de los Disparos
		self.disparo_velocidad=20
		self.disparo_ancho=3
		self.disparo_alto=15
		self.disparo_color=(255,255,255) #255,255,255 BLANCO
		
		#Configuracion marcianos
		self.velocidad_marciano=1
		self.velocidad_flota=10
		self.direccion_flota=1 # -1 izquierda 1 derecha
		self.cambia_imagen=10
		
		#Sonidos
		#pygame.mixer.set_num_channels(10)  # default is 8
		#pygame.mixer.Channel(0).play(pygame.mixer.Sound('sound\gun_fire.wav'))
		#pygame.mixer.Channel(1).play(pygame.mixer.Sound('sound\enemy_hit.wav'))
		#pygame.mixer.init()
		#self.sonido_disparo = pygame.mixer.Sound('sonidos/shoot.wav')
		#self.sonido_explota = pygame.mixer.Sound('sonidos/explosion.wav')		
		#self.sonido_disparo=pygame.mixer.music.load('sonidos/shoot.wav')
		#self.sonido_explota=pygame.mixer.music.load('sonidos/explosion.wav')		
		#pygame.mixer.music.play(0)
