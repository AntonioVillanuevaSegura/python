class Marcador():
	""" Gestion de puntuaciones jugador o marcianos"""
	def __init__(self, configuracion):
		"""inicializa estadisticas """
		self.configuracion=configuracion
		self.reset()
		self.juego_activo=False #Inactivo por defecto
		
	def reset(self):
		""" inicializa puntuaciones """
		self.num_vidas=self.configuracion.num_vidas
