class Obstaculo:
	def __init__(self,distancia,altura):
		self.__distancia = distancia
		self.__altura = altura
	@property
	def distancia(self):
		return self.__distancia
	@property
	def altura(self):
		return self.__altura
	def __str__(self):
		return f"Obstaculo tem {self.__altura} m de altura e esta a {self.__distancia/1e3:g} km de distancia da torre."
class Obstaculos:
	def __init__(self):
		self.__obstaculos = list()
		self.__numero_obstaculos = 0
		self.__current = 0
	def __iter__(self):
		return self
	def __next__(self):
		if self.__current >= self.__numero_obstaculos:
			raise StopIteration
		else:
			self.__current += 1
			return self.__obstaculos[self.__current-1]
	def __len__(self):
		return self.__numero_obstaculos
	def __str__(self):
		if self.__numero_obstaculos:
			temp = "Obstaculos\n    altura(m)\t, distancia do obstaculo a torre transmissora (km)\n"
			for i in range(self.__numero_obstaculos):
				temp += f"{self.__obstaculos[i].altura:10g}\t, {self.__obstaculos[i].distancia/1e3}\n"
		else:
			temp = "Nao existem obstaculos definidos ainda."
		return temp
	@property
	def alturas(self):
		altura = list()
		for obstaculo in self.__obstaculos:
			altura.append(obstaculo.altura)
		return tuple(altura)
	@property
	def distancias(self):
		distancia = list()
		for obstaculo in self.__obstaculos:
			distancia.append(obstaculo.distancia)
		return tuple(distancia)

	def adicionar_obstaculo(self,distancia,altura):
		temp = Obstaculo(distancia,altura)
		self.__obstaculos.append(temp)
		self.__numero_obstaculos+=1

