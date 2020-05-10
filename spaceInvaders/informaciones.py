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
		self.actualiza()

	def dibuja(self):
		""" dibuja marcador """
		self.actualiza()
		
		self.pantalla.blit(self.imagen_informacion,(0,0)) #Informacion		
		
		self.pantalla.blit(self.imagen_informacion2,(50,30))#Puntuaciones	
		#Linea antes de la nave 
		pygame.draw.line(self.pantalla, (255,255,255,255), (10, 730), (1190, 730), 4)		
		

	def actualiza(self):
		
		#str_puntuaciones=str(self.marcador.puntos_jugador1)
		str_informacion=5*" "+"SCORE<1>" +34*" "+ "HI-SCORE" +34*" "+"SCORE<2>"
		str_puntuaciones=5*" "+str(self.marcador.puntos_jugador1)
		str_puntuaciones+= 47*" "+str(self.marcador.puntos_score)

		#Referencias superiores
		self.imagen_informacion=self.font.render(str_informacion,True,
			self.color_texto,self.configuracion.color_pantalla)	
			
		#2a. linea con puntuaciones 	
		self.imagen_informacion2=self.font.render(str_puntuaciones,True,
			self.color_texto,self.configuracion.color_pantalla)					




