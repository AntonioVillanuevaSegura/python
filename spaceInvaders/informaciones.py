import pygame.font
class Informaciones():
	""" Muestra informacion en pantalla marcadores p.e"""
	def __init__(self,configuracion,pantalla,marcador):
		
		self.pantalla=pantalla
		self.pantalla_rect=pantalla.get_rect() #rectangulo de pantalla
		self.configuracion=configuracion
		self.marcador=marcador	
		self.vidas=	configuracion.num_vidas #vidas naves	
		
		#Fuentes graficas
		self.color_texto=(255,255,255) #Blanco
		self.font = pygame.font.SysFont(None,48)
		
		#Carga y reescala la imagen de la nave
		self.imagen=pygame.transform.scale(pygame.image.load("imagenes/PlayerSprite.xpm") , (70,35)	)
		
		#Imagen inicial, puntuaciones
		self.actualiza()

	def dibuja(self):
		""" dibuja marcador """
		self.actualiza()
		
		self.pantalla.blit(self.imagen_informacion,(0,0)) #Informacion				
		self.pantalla.blit(self.imagen_informacion2,(50,30))#Puntuaciones
		self.pantalla.blit(self.imagen_vidas,(50,770))#Puntuaciones		
		
		#Numero de vidas de naves
		for x in range(self.marcador.num_vidas):
			self.pantalla.blit(self.imagen,(100+x*100,760))
		
		#Linea division , informativa debajo nave
		pygame.draw.line(self.pantalla, (255,255,255,255), (10, 750), (1190, 750), 4)		
		

	def actualiza(self):
		
		#str_puntuaciones=str(self.marcador.puntos_jugador1)
		str_informacion=5*" "+"SCORE<1>" +34*" "+ "HI-SCORE" +34*" "+"SCORE<2>"
		str_puntuaciones=5*" "+str(self.marcador.puntos_jugador1)
		str_puntuaciones+= 47*" "+str(self.marcador.puntos_score)
		#str_vidas=str(self.vidas)
		str_vidas=str(self.marcador.num_vidas)		

		#Referencias superiores
		self.imagen_informacion=self.font.render(str_informacion,True,
			self.color_texto,self.configuracion.color_pantalla)	
			
		#2a. linea con puntuaciones 	
		self.imagen_informacion2=self.font.render(str_puntuaciones,True,
			self.color_texto,self.configuracion.color_pantalla)		
			
		#3a. linea n° de vidas 	
		self.imagen_vidas=self.font.render(str_vidas,True,
			self.color_texto,self.configuracion.color_pantalla)							




