from obstaculo import Obstaculos
from torre import Torre
from gume_de_faca import Gume_De_Faca
from numpy import atan,sin,cos,log10
class Propagacao:
	def __init__(self,tx,rx,frequencia,obstaculos):
		self.__tx = tx
		self.__rx = rx
		self.__obstaculos = obstaculos
		self.__frequencia = frequencia
		self.potencia_tx()
	def potencia_tx(self):
		numero_obstaculos = len(self.__obstaculos)
		print(numero_obstaculos)
		print(min(self.__obstaculos.distancias))
		if numero_obstaculos == 1:
			metodo = Gume_De_Faca(self.__tx,self.__rx,self.__obstaculos,self.__frequencia)
			L = metodo.L
			# print(metodo.L,metodo.elipsoide)
		# elif (numero_obstaculos>2) and (min(distancia_obstaculos)>0.1*d):
			# EpsteinPeterson
		# else:
			# JacqesDeygout
		comprimento_de_onda = 3e8/self.__frequencia
		ganho_das_antenas = 15 # dBi
		sensibilidade_do_receptor = -55 #dBm
		snr = 30 #dB
		Pr = sensibilidade - snr
		teta = atan((hT+hR)/d);
		xen = sqrt((10-0.54j)-(cos(teta)).^2);
		fi = 2*hR*hT/d;
		gama = (sin(teta)-xen)/(sin(teta)+xen);
		var = sqrt(1+abs(gama)^2+2*abs(gama)*cos(fi));
		P = 10*log10(4*pi*(d^2+abs(hT-hR)^2)/(var^2)/30/1e3/lambda/lambda);
		Pt = Pr -2*G +20*log10(4*pi/lambda) -L +P;
def main():
	obstaculos = Obstaculos()
	# obstaculos.adicionar_obstaculo(20e3,420)
	obstaculos.adicionar_obstaculo(60e3,500)
	tx = Torre(380)
	rx = Torre(400,90e3)
	frequencia = 300e6 # 300 MHz
	calculo = Propagacao(tx,rx,frequencia,obstaculos)
if __name__=="__main__":
	main()
