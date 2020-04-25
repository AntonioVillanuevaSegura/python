import sys
import pygame
from disparo import Disparo
from marciano import Marciano

def tecla_pulsada(evento,configuracion,pantalla,nave,disparos):
	""" respuesta a tecla pulsada """
	if evento.key==pygame.K_RIGHT:
		nave.derecha=True
		
	if evento.key==pygame.K_LEFT:
		nave.izquierda=True	
		
	elif evento.key==pygame.K_SPACE: #Disparo
		disparo=Disparo(configuracion,pantalla,nave)
		disparos.add(disparo) #Anade disparos al grupo
		
	elif evento.key==pygame.K_q:#QUIT salir
		sys.exit()
				
def tecla_liberada(evento,configuracion,pantalla,nave,disparos):
	""" respuesta a tecla pulsada """
	if evento.key==pygame.K_RIGHT:
		nave.derecha=False
		
	if evento.key==pygame.K_LEFT:
		nave.izquierda=False				
		
def analiza_eventos(configuracion,pantalla,nave,disparos):
	""" Analizamos teclas pulsadas o raton """

	#Mira eventos de teclado o raton		
	for evento in pygame.event.get():			
		#Salida del juego
		if evento.type==pygame.QUIT:
			sys.exit()
			
		elif evento.type==pygame.KEYDOWN:#tecla pulsada
			tecla_pulsada(evento,configuracion,pantalla,nave,disparos)
			
		elif evento.type==pygame.KEYUP:#tecla liberada
			tecla_liberada(evento,configuracion,pantalla,nave,disparos)			
			
def actualiza_pantalla(configuracion,pantalla,nave,marcianos,disparos):
	""" Actualiza imagenes en la pantalla """
	pantalla.fill(configuracion.color_pantalla)
	
	#Dibuja los disparos del Grupo sprite pygame
	for disparo in disparos.sprites():
		disparo.dibuja()
		
	nave.dibuja()
	
	#Draw() en un grupo dibuja cada elemento definido en rect 
	marcianos.draw (pantalla) #Emplea Group.Draw		
		
	#La version mas reciente la hace visible
	pygame.display.flip()

def actualiza_disparos(configuracion,pantalla,nave,marcianos,disparos):
	""" Actualiza ,limpia los disparos"""
	
	#actualiza las posiciones de los disparos 
	disparos.update()
	
	#Limita en pantalla los disparos
	for disparo in disparos.copy():
		if disparo.rect.bottom <=0: #La parte inf. llega al final
			disparos.remove(disparo) #elimina este disparo sale pantalla
			
	#Detecta la colision disparo con  marcianos
	colision=pygame.sprite.groupcollide (disparos,marcianos,True,True)
	
	if (len(marcianos) == 0): #Han sido todos aniquilados
		#Limpia disparos restantes y crear nueva flota
		crear_flota(configuracion,pantalla,nave,marcianos)

def cuantos_marcianos_x(configuracion,marciano_ancho):
	""" Determino el n° de marcianos por fila"""
	#Espacio entre  marcianos ,segun datos de la pantalla
	#El espaci x menos un marciano a cada lado
	disponible_x=configuracion.ancho_pantalla - (2 * marciano_ancho)	
	
	#Cuantos marcianos puedo colocar en x  
	n_marcianos_x=int (disponible_x / (2 * marciano_ancho))		
	
	return n_marcianos_x	

def cuantos_marcianos_y(configuracion,altura_nave,altura_marciano):
	""" Cuantas lineas de marcianos en Y podemos entrar """	
	disponible_y=(configuracion.alto_pantalla - (3 * altura_marciano)- altura_nave)
	num_lineas_marcianos= int ( disponible_y /(2* altura_marciano) )
	
	return  num_lineas_marcianos
	
def crear_marciano(configuracion,pantalla,marcianos,numero_marciano,fila):
	"""Creo un marciano y lo coloco en la fila """
	#Toma medidas del marciano
	marciano=Marciano(configuracion,pantalla)
	marciano_ancho=marciano.rect.width	
	
	marciano.x=marciano_ancho + (2 * marciano_ancho) * numero_marciano
	marciano.rect.x=marciano.x
	
	marciano.rect.y=marciano.rect.height +2 *marciano.rect.height* fila
	
	marcianos.add(marciano) #Lo anado al Grupo 	

def crear_flota(configuracion,pantalla,nave,marcianos):	
	""" Crea una flota de marcianos """
	#Creo un marciano de referencia para medidas 
	individuo=Marciano(configuracion,pantalla)	

	num_marcianos_x=cuantos_marcianos_x(configuracion,
												individuo.rect.width)
	num_lineas=cuantos_marcianos_y(configuracion,nave.rect.height,
												individuo.rect.height)
	
	#Creo la primera fila de marcianos, segun n_marcianos_x 
	for fila in range(num_lineas): #Numero de filas de marcianos
		for numero_marciano in range(num_marcianos_x): #Elems. en fila
			crear_marciano(configuracion,pantalla,marcianos,numero_marciano,fila)

def borde_flota(configuracion,marcianos):
	"""La flota de marcianos toca los bordes de la pantalla  """	
	for marciano in marcianos.sprites(): #Utiliza sprites del Group
		if marciano.borde():#Toca ?
			cambia_direccion_flota(configuracion,marcianos)
			break
			
def cambia_direccion_flota(configuracion,marcianos):		
	""" cambia la direccion de toda la flota de marcianos """
	
	for marciano in marcianos.sprites():
		marciano.rect.y +=configuracion.velocidad_flota
		
	configuracion.direccion_flota *=-1 #Aqui invierte el sentido !!!
	
def actualiza_marcianos(configuracion,marcianos):
	""" actualiza posiciones de la flota marcianera """
	borde_flota(configuracion,marcianos)	
	marcianos.update() #Utiliza la actualizacion desde Group()
