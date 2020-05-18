from numpy import roots,sqrt,array,log10
from scipy.special import fresnel as integral_de_fresnel
class Gume_De_Faca:
	def __init__(self,tx,rx,obstaculos,frequencia):
		self.__tx = tx
		self.__rx = rx
		for obstaculo in obstaculos:
			self.__obstaculo = obstaculo
		self.__frequencia = frequencia
		self.__c = 3e8
		self.__L,self.__elipsoide_utilizado = self.__perdas()
	@property
	def L(self):
		return self.__L
	@property
	def elipsoide(self):
		return self.__elipsoide_utilizado
	def __distancias_corrigidas(self,raio_da_terra):
		raizes = roots([1,-3*self.__rx.distancia/2,-(1e3*raio_da_terra*(self.__tx.altura+self.__rx.altura)-self.__rx.distancia*self.__rx.distancia/2),1e3*raio_da_terra*self.__tx.altura*self.__rx.distancia])
		d1 = (raizes[(raizes>0)*(raizes<self.__rx.distancia)])
		d2 = self.__rx.distancia-d1
		return d1,d2
	def __alturas_corrigidas(self,d1,d2):
		altura_transmissor = self.__tx.altura - d1**2/17e6
		altura_receptor = self.__rx.altura - d2**2/17e6;
		return altura_receptor,altura_transmissor
	def __perdas(self):
		raio_da_terra = 6.37e3 #a' = raio_da_terra*1000
		distancia_1,distancia_2 = self.__distancias_corrigidas(raio_da_terra)
		altura_receptor,altura_transmissor = self.__alturas_corrigidas(distancia_1,distancia_2)
		auxiliar = self.__obstaculo.distancia if self.__rx.altura>self.__tx.altura else (self.__rx.distancia-self.__obstaculo.distancia)
		altura_visada = abs(altura_receptor-altura_transmissor)/self.__rx.distancia*auxiliar+min([altura_transmissor,altura_receptor])
		elipsoide_de_fresnel = sqrt(self.__c/self.__frequencia*self.__obstaculo.distancia*(self.__rx.distancia-self.__obstaculo.distancia)/self.__rx.distancia)
		if (altura_visada-elipsoide_de_fresnel)<self.__obstaculo.altura:
			elipsoide_utilizado = 1
		else:
			elipsoide_de_fresnel = sqrt(2*self.__c/self.__frequencia*self.__obstaculo.distancia*(self.__rx.distancia-self.__obstaculo.distancia)/self.__rx.distancia)
			if (altura_visada-elipsoide_de_fresnel)<self.__obstaculo.altura:
				elipsoide_utilizado = 2
			else:
				elipsoide_de_fresnel = sqrt(3*self.__c/self.__frequencia*self.__obstaculo.distancia*(self.__rx.distancia-self.__obstaculo.distancia)/self.__rx.distancia)
				elipsoide_utilizado = 3
		Vo = sqrt(2)*(self.__obstaculo.altura-altura_visada)/elipsoide_de_fresnel
		C,S = integral_de_fresnel(Vo)
		L = -20*log10(1/sqrt(2)*sqrt((1/2-C)**2+(1/2-S)**2))
		return (L[0],elipsoide_utilizado)
