class Marcador():
	""" Gestion de puntuaciones jugador o marcianos"""
	def __init__(self, configuracion):
		"""inicializa estadisticas """
		self.configuracion=configuracion
		self.reset()
		self.juego_activo=False #Inactivo por defecto
		self.puntos_marcianos=0
		self.puntos_jugador1=0
		self.puntos_jugador2=0
		self.puntos_score=0	
		self.num_vidas=	configuracion.num_vidas
		
	def reset(self):
		""" inicializa puntuaciones """
		#self.num_vidas=self.configuracion.num_vidas
		self.puntos_jugador1=0
		self.puntos_jugador2=0		
