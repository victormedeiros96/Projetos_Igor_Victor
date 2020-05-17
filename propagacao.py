from obstaculo import Obstaculos
from torre import Torre
class Propagacao:
	def __init__(self,tx,rx,frequencia,obstaculos):
		self.__tx = tx
		self.__rx = rx
		self.__obstaculos = obstaculos
		self.__frequencia = frequencia
	def potencia_tx(self):
		numero_obstaculos = len(self.__obstaculos)
		print(numero_obstaculos)
		# if numero_obstaculos == 1:
			# GumedeFaca
		# elif (numero_obstaculos>2) and (min(distancia_obstaculos)>0.1*d):
			# EpsteinPeterson
		# else:
			# JacqesDeygout
def main():
	obstaculos = Obstaculos()
	obstaculos.adicionar_obstaculo(20e3,420)
	obstaculos.adicionar_obstaculo(60e3,500)
	tx = Torre(380)
	rx = Torre(400,90e3)
	frequencia = 300e6 # 300 MHz
	calculo = Propagacao(tx,rx,frequencia,obstaculos)
	print(calculo.potencia_tx())
if __name__=="__main__":
	main()
