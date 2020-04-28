import pygame.font
class Informaciones():
	""" Muestra informacion en pantalla marcadores p.e"""
	def __init__(self,configuracion,pantalla,marcador):
		
		self.pantalla=pantalla
		self.pantalla_rect=pantalla.get_rect() #rectangulo de pantalla
		self.configuracion=configuracion
		self.marcador=marcador
		
		#Fuentes graficas
		self.color_texto=(255,255,255) #Blanco
		self.font = pygame.font.SysFont(None,48)
		
		#Imagen inicial, puntuaciones
		self.puntuacion_inicial()

	def dibuja(self):
		""" dibuja marcador """
		self.pantalla.blit(self.imagen_marcador,self.marcador_rectangulo)
		

	def puntuacion_inicial(self):
		
		#str_puntuaciones=str(self.marcador.puntos_jugador1)
		str_puntuaciones=5*" "+"SCORE<1>" +34*" "+ "HI-SCORE" +34*" "+"SCORE<2>"+ 34*" "
		+10*" "+str(self.marcador.puntos_jugador1)+" -------------"

		self.imagen_marcador=self.font.render(str_puntuaciones,True,
			self.color_texto,self.configuracion.color_pantalla)
		
		#Muestra puntuaciones en la parte superior
		self.marcador_rectangulo = self.imagen_marcador.get_rect() #Rect imagen	
		self.marcador_rectangulo.left = self.pantalla_rect.left  #izquierda
		#self.marcador_rectangulo.top = 20



