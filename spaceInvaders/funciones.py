import sys
import pygame
from disparo import Disparo
from marciano import Marciano
from bunker import Bunker
from time import sleep #retardo entre juegos 

def tecla_pulsada(evento,configuracion,pantalla,nave,disparos,sonidos):
	""" respuesta a tecla pulsada """

	if evento.key==pygame.K_RIGHT:
		nave.derecha=True
		
	if evento.key==pygame.K_LEFT:
		nave.izquierda=True	
		
	elif evento.key==pygame.K_SPACE: #Disparo
		disparo=Disparo(configuracion,pantalla,nave)
		disparos.add(disparo) #Anade disparos al grupo
		pygame.mixer.stop()
		sonidos.sonido_disparo.play()
		
	elif evento.key==pygame.K_q:#QUIT salir
		sys.exit()
				
def tecla_liberada(evento,configuracion,pantalla,nave,disparos):
	""" respuesta a tecla pulsada """
	if evento.key==pygame.K_RIGHT:
		nave.derecha=False
		
	if evento.key==pygame.K_LEFT:
		nave.izquierda=False				
		
def analiza_eventos(configuracion,pantalla,marcador,boton,nave,disparos,sonidos):
	""" Analizamos teclas pulsadas o raton """

	#Mira eventos de teclado o raton		
	for evento in pygame.event.get():			
		#Salida del juego
		if evento.type==pygame.QUIT:
			sys.exit()
		elif evento.type==pygame.MOUSEBUTTONDOWN: #Boton PLAY pulsado ?
			raton_x,raton_y=pygame.mouse.get_pos()
			boton_play(marcador,boton,raton_x,raton_y)
				
		elif not marcador.juego_activo : #No sigas no jugamos 			
				return 
			
		elif evento.type==pygame.KEYDOWN:#tecla pulsada
			tecla_pulsada(evento,configuracion,pantalla,nave,disparos,sonidos)
				
		elif evento.type==pygame.KEYUP:#tecla liberada
			tecla_liberada(evento,configuracion,pantalla,nave,disparos)			
			
def actualiza_pantalla(configuracion,pantalla,informacion,
			marcador,nave,marcianos,disparos,disparosM,boton,bunkers):
	""" Actualiza imagenes en la pantalla """
	pantalla.fill(configuracion.color_pantalla)
	
	#Dibuja los disparos del Grupo sprite pygame de la nave
	for disparo in disparos.sprites():
		disparo.dibuja()
		
	#Dibujar los disaparos del Grupo sprite pygame de los marcianos	
	for disparo in disparosM.sprites():
		disparo.dibuja()	
		
	nave.dibuja()
	
	#Dibujar bunker	
	bunkers.draw(pantalla)
	
	#Draw() en un grupo dibuja cada elemento definido en rect 
	marcianos.draw (pantalla) #Emplea Group.Draw		
		
	#Dibujar el boton si el juego esta inactivo  
	if not marcador.juego_activo:
		boton.dibuja()
	
	#Muestra la informacion de las puntuaciones , marcadores en pantalla
	informacion.dibuja()
	
	#Pantalla puntuaciones
	informacion.dibuja()
						
	#La version mas reciente la hace visible
	pygame.display.flip()

def actualiza_disparos(configuracion,marcador,pantalla,nave,marcianos,disparos,bunkers,sonidos):
	""" Actualiza ,limpia los disparos"""
	
	#actualiza las posiciones de los disparos 
	disparos.update()
	
	#Limita en pantalla los disparos
	for disparo in disparos.copy():
		if disparo.rect.bottom <=0: #La parte inf. llega al final
			disparos.remove(disparo) #elimina este disparo sale pantalla
			
			
	#Detecta la colision disparo con bunker
	colision=pygame.sprite.groupcollide (bunkers,disparos,False,False)	
	
	#El bunker ha recibido un disparo 
	if (colision):
		
		#La key (bunker) ha sido alcanzada con un disparo
		x=colision.items()
		
		#Analiza keys(bunker) con los values(disparos)
		for keys , values  in x:
			keys.alcanzado(values[0],disparos,False)
	
	
	
			
	#Detecta la colision disparo con  marcianos
	colision=pygame.sprite.groupcollide (disparos,marcianos,True,True)
	
	#Marciano alcanzado disparo cambio de imagen 
	if colision:
		x=colision.items()

		for values in x: #mira marciano
			values[1][0].explota()
			#Puntuacion segun fila del rango , 0=30 1-2=20 3-4=10
			fila=values[1][0].fila
			if fila==0:
				marcador.puntos_jugador1+=30 #Fila 0 30 ptos.
			if fila==1 or fila==2:
				marcador.puntos_jugador1+=20 #Fila 0 20 ptos.
			if fila==3 or fila==4:
				marcador.puntos_jugador1+=10 #Fila 0 10 ptos.				
			
		if (marcador.puntos_score <	marcador.puntos_jugador1):
			marcador.puntos_score=marcador.puntos_jugador1
			
		sonidos.marciano_explota.play()
		
	if (len(marcianos) == 0): #Han sido todos aniquilados
		#Limpia disparos restantes y crear nueva flota
		crear_flota(configuracion,pantalla,nave,marcianos)
		
def actualiza_disparosMarcianos(configuracion,marcador,pantalla,bunkers,nave,marcianos,disparos,sonidos):
	""" Actualiza ,limpia los disparos marcianos"""
	pantalla_rect=pantalla.get_rect()#Rectangulo que representa la pantalla	
	
	#actualiza las posiciones de los disparos 
	disparos.update()
	
	#Recorre los disparos 
	for disparo in disparos.copy():
		#configuracion.posicion_ny-20
		#if disparo.rect.bottom >=pantalla_rect.bottom: #La parte inf. llega al final
		if disparo.rect.bottom >=configuracion.posicion_ny+50: #La parte inf. llega al final		
			disparos.remove(disparo) #elimina este disparo sale pantalla
			
			
	#Colision disparo con bunker ,disparo desaparece 
	colision=pygame.sprite.groupcollide(bunkers,disparos,False,False)	
	
	#El bunker ha recibido un disparo 
	if (colision):
		
		#La key (bunker) ha sido alcanzada con un disparo
		x=colision.items()
		
		#Analiza keys(bunker) con los values(disparos)
		for keys , values  in x:
			keys.alcanzado(values[0],disparos)
			
	#Detecta colision del sprite nave con algun disparo , True se elimina disparo
	colision=pygame.sprite.spritecollide (nave,disparos,True)
	
	#Han alcanzado la nave ?
	if colision:		
		nave_alcanzada (configuracion,marcador,pantalla,nave,marcianos,disparos,sonidos,bunkers)
	
def crear_marciano(configuracion,pantalla,marcianos,numero_marciano,fila):
	"""Creo un marciano y lo coloco en la fila """
	offset_x=configuracion.marciano_offset_x
	
	offset_superior=configuracion.offset_superior #Deja un espacio superior de margen
	
	#Toma medidas del marciano
	marciano=Marciano(configuracion,pantalla,fila)
	marciano_ancho=marciano.rect.width	
	
	#Espaciado entre marcianos en X en la Fila
	marciano.x=offset_x+ marciano_ancho + ( marciano_ancho * numero_marciano)
	marciano.rect.x=marciano.x
	
	#Espaciado entre marcianos en Y vertical 
	marciano.rect.y=offset_superior +marciano.rect.height + 1.5 * marciano.rect.height * fila
	
	marcianos.add(marciano) #Lo anado al Grupo 	

def crear_flota(configuracion,pantalla,nave,marcianos):	
	""" Crea una flota de marcianos """

	num_marcianos_x=configuracion.num_marcianos_fila #11 segun original									
	num_lineas=configuracion.num_marcianos_vertical #5 segun original
	
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
	
def actualiza_marcianos(configuracion,marcador,pantalla,nave,marcianos,disparos,disparosM,bunkers,sonidos):
	""" actualiza posiciones de la flota marcianera """
	borde_flota(configuracion,marcianos)	
	marcianos.update() #Utiliza la actualizacion desde Group()
	
	#Detecta colision de un marciano con la nave
	if pygame.sprite.spritecollideany(nave,marcianos):
		#print ("Nave tocada ")
		nave_alcanzada(configuracion,marcador,pantalla,nave,marcianos,disparos,bunkers)
		
	#Mira si los marcianos han llegado abajo 
	marcianos_abajo(configuracion,marcador,pantalla,nave,marcianos,disparos,bunkers,sonidos)
	
	#Marciano efectua disparo ? ,
	for marciano in marcianos.copy():
		if marciano.disparo() and len (disparosM ) <configuracion.numero_disparos_simultaneos:
			#print ("Dispara marciano ",marciano.rect.x)
			disparosM.add(Disparo(configuracion,pantalla,marciano,False)) #Anade disparos al grupo
			
	#Adapta la velocidad de forma proporcional al n° de marcianos

	velocidad=configuracion.num_marcianos_fila * configuracion.num_marcianos_vertical/len(marcianos)
	
	sonidos.danza_marciana(velocidad)

	configuracion.incrementa_velocidad(velocidad)

def nave_alcanzada(configuracion,marcador,pantalla,nave,marcianos,disparos,sonidos,bunkers):	
	""" La nave ha sido alcanzado por los marcianos """

	sonidos.sonido_explota.play()
	nave.explota()
	sleep(0.5)	

	#Vacia los disparos pendientes y marcianos 
	marcianos.empty()
	disparos.empty()
	bunkers.empty()
	
	#Crea una nueva flota , nuevo juego
	crear_flota(configuracion,pantalla,nave,marcianos)
	
	#crea bunkers
	crear_bunkers(configuracion,pantalla,bunkers)
	
	#recentra la nave
	nave.centra()
	
	#Puntuaciones , marcador
	marcador.reset()

	
	if marcador.num_vidas>1:#Si quedan vidas puede seguir jugando
		marcador.num_vidas -=1 #una vida menos 
		
		sleep(0.5)
	else:
		marcador.juego_activo=False 
		marcador.num_vidas=configuracion.num_vidas #Retoma el n° de naves

def marcianos_abajo(configuracion,marcador,pantalla,nave,marcianos,disparos,bunkers,sonidos):
	"""Han llegado abajo los marcianos  """
	#pantalla=pantalla.get_rect() #obtengo el rectangulo de pantalla
	
	#Recorro la marcianada , a ver si toca la parte inferior de la panta
	for marciano in marcianos.sprites():
		#if marciano.rect.bottom >=pantalla.bottom:
		if marciano.rect.bottom >=configuracion.posicion_ny-20:		
			""" si llegan abajo han ganado , nave alcanzada """
			nave_alcanzada(configuracion,marcador,pantalla,nave,marcianos,disparos,sonidos,bunkers) 
			break
		
def boton_play(marcador,boton,raton_x,raton_y):
	""" ha sido pulsado el boton PLAY """
	if boton.rect.collidepoint(raton_x,raton_y):
		marcador.juego_activo=True
		
def crear_bunkers(configuracion,pantalla,bunkers):
	""" Crea los 3 bunkers del juego"""
	ancho =configuracion.ancho_pantalla
	for posicion in range(ancho//5,ancho,ancho//5):
		bunker=Bunker ( configuracion,pantalla,posicion)
		bunkers.add(bunker) 	
