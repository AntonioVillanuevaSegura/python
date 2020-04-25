import pygame.font
class Boton():
	""" boton de play """
	def __init__(self,configuracion,pantalla,texto):
		""" Inicializa un boton """
		self.pantalla=pantalla
		self.pantalla_rect=pantalla.get_rect()
		
		#Dimensiones ,propiedades boton
		self.x ,self.y =200,50
		self.color_txt=(255,255,255) #Texto Blanco 
		self.color_boton=(0,255,0) #Boton color 
		self.font =pygame.font.SysFont(None,48)
		
		#Crea el rect del boton y lo centra en la pantalla		
		self.rect=pygame.Rect(0,0,self.x,self.y)
		self.rect.center=self.pantalla_rect.center
		
		#Texto mensaje
		self.mensaje(texto)
		
	def mensaje(self,texto):
		""" Muestra el texto en el boton"""
		self.imagen_txt=self.font.render(texto,True,
								self.color_txt,self.color_boton)
		self.imagen_txt_rect=self.imagen_txt.get_rect()
		self.imagen_txt_rect.center=self.rect.center
	
	def dibuja(self):
		""" Dibuja el boton """
		self.pantalla.fill(self.color_boton,self.rect)
		self.pantalla.blit(self.imagen_txt,self.imagen_txt_rect)
		
		
		
