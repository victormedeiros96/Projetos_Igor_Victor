class Torre:
	def __init__(self,altura=0,distancia=0):
		self.__distancia = distancia
		self.__altura = altura
	@property
	def distancia(self):
		return self.__distancia
	@distancia.setter
	def distancia(self,distancia):
		self.__distancia = distancia
	@property
	def altura(self):
		return self.__altura
	@altura.setter
	def altura(self,altura):
		self.__altura = altura
	def __str__(self):
		if (not(self.__distancia))and(not(self.__altura)):
			return "Torre nao definida."
		if self.__distancia:
			return f"Torre receptora a {self.__distancia/1e3:g} km de distancia da transmissora e {self.__altura} metros de altura."
		else:
			return f"Torre transmissora com {self.__altura} metros de altura."
