#-------------------------------------------------------------------------------
# Name:        perceptron.py
#
# Author:      inigo ozcoidi (oscoidi)
#
# Created:     6/11/2017
#-------------------------------------------------------------------------------

import math,random,os

class Perceptron():

	def __init__(self):
		self.alpha = 0.6 #factor de aprendizaje. Cuanto mayor es antes aprende pero tiene menor precision
		self.perceptron = [] # array que nos define el perceptron y por cada capa contiene un subarray de la siguiente forma: [numero neurons de la capa,[umbrales de actuacion(u)],[pesos(w)],[salidas de las neuronas(a)]]
		self.ntrain = 0 #numero de entrenamientos ejecutados
		os.chdir(os.getcwd()) #cambiamos el directorio de trabajo(debereis cambiarlo por la direccion donde guardeis el programa)
		self.cwd = os.getcwd()
		self.saveurl = self.cwd + '/perceptron.txt' #url donde guardaremos la red neuronal una vez entrenada
		self.trainingdata = self.cwd + '/entrenamientoperc.txt' #url donde tenemos la training data
		self.build() #construimos la red neuronal
		self.train() #entrenamos la red neuronal
		while True: #utilizamos la red neuronal
			for i in range(self.perceptron[0][0]):
				self.perceptron[0][3][i] = input('entrada ' + str(i) + ' : ')
			self.percep()

	def build(self): #funcion que construye la red neuronal
		print('***PERCEPTRON***')
		for i in range(input('numero de capas: ')):
			capa = []
			u = []
			w = []
			a = []
			capa.append(input('numero de neuronas en la capa ' + str(i) + ' : '))#anadimos el numero de neuronas de la capa
			for j in range(capa[0]):
				u.append(random.random()) #creamos umbrales de actuacion aleatorios
				a.append(random.random()) #creamos salidas aleatorias
				wc = []
				if i != 0:
					for k in range(self.perceptron[i-1][0]):
						wc.append(random.random()) #creamos pesos aleatorios
				w.append(wc)
			capa.append(u)
			capa.append(w)
			capa.append(a)
			self.perceptron.append(capa) #anadimos la capa a la red neuronal

	def percep(self):#funcion que calcula la salida de la red neuronal ante una serie de entradas
		print('salida de las neuronas capa 0:')
		print(self.perceptron[0][3])
		for k in range(len(self.perceptron)-1):
			for i in range(self.perceptron[k+1][0]):
				suma = 0
				for j in range(self.perceptron[k][0]):
					suma = suma + (self.perceptron[k][3][j] * self.perceptron[k+1][2][i][j])
				suma = suma + self.perceptron[k+1][1][i]
				suma = (1/( 1 + math.exp(-suma)))
				self.perceptron[k+1][3][i] = suma
			print('salida de las neuronas capa ' + str(k+1) + ' : ')
			print(self.perceptron[k+1][3])

	def train(self): #funcion que inicia el entrenamiento
		print('-+-Comienza el entrenamiento del perceptron-+-')
		for r in range(input('numero de veces que quiere repetir el entrenamiento: ')):
			self.readlines()
		self.save()

	def readlines(self): #lee la training data y llama a las funciones percep y backpropagation 
		entrenamiento = open(self.trainingdata,'r') #abrimos el archivo
		lineas = entrenamiento.readlines()
		entrenamiento.close()
		for i in range(len(lineas)):#leemos linea a linea
			self.ntrain += 1	
			print('***entrenamiento numero ' + str(self.ntrain) + ' ***')
			linea = lineas[i]
			boolean = False
			numero = ''
			k = 0
			se = []
			for x in range(self.perceptron[len(self.perceptron)-1][0]):
				se.append(0)
			for j in range(len(linea)):
				if linea[j]==']' and boolean:
					se[k] = numero
					numero = ''
					k = 0
				if linea[j]==']' and boolean == False:
					boolean = True
					self.perceptron[0][3][k] = float(numero)
					numero = ''
					k = 0
				if linea[j] != ',' and linea[j] != '[' and linea[j] != ']':
					numero = numero + linea[j]
				if linea[j] == ',' and boolean == False:
					self.perceptron[0][3][k] = float(numero)
					numero = ''
					k += 1
				if linea[j] == ',' and boolean:
					se[k] = float(numero)
					numero = ''
					k += 1
			se[self.perceptron[len(self.perceptron)-1][0]-1] = float(se[self.perceptron[len(self.perceptron)-1][0]-1])
			print('entrada: ' + str(self.perceptron[0][3]) + ' salida esperada: ' + str(se))
			self.percep() #calculamos las salidas que nos daria las entradas de la training data
			self.backpropagation(se) #calculamos los errores entre la salida esperada y la obtenida y realizamos las correciones oportunas.

	def backpropagation(self,se):
		#calculamos los erroes y realizamos las correcciones oportunas
		#empezamos por la ultima capa de neuronas
		deltam = []
		for k in range(self.perceptron[len(self.perceptron)-1][0]):

			deltam.append(self.perceptron[len(self.perceptron)-1][3][k]*(1 - self.perceptron[len(self.perceptron)-1][3][k]) * (self.perceptron[len(self.perceptron)-1][3][k] - float(se[k])))
			

			for n in range(self.perceptron[len(self.perceptron)-2][0]):
				self.perceptron[len(self.perceptron)-1][2][k][n] = self.perceptron[len(self.perceptron)-1][2][k][n] - self.alpha * deltam[k] * self.perceptron[len(self.perceptron)-2][3][n]
			self.perceptron[len(self.perceptron)-1][1][k] = self.perceptron[len(self.perceptron)-1][1][k] - self.alpha * deltam[k]
		#seguimos con las capas ocultas de neuronas
		for x in range(len(self.perceptron)-2):
			deltal = []
			sumatorio2 = 0
			for k in range(self.perceptron[len(self.perceptron)-2-x][0]):
				for c in range(self.perceptron[len(self.perceptron)-3-x][0]):
					for s in range(self.perceptron[len(self.perceptron)-1-x][0]):
						sumatorio2 = sumatorio2 + deltam[s] * self.perceptron[len(self.perceptron)-1-x][2][s][k]
				deltal.append((self.perceptron[len(self.perceptron)-2-x][3][k] * (1 - self.perceptron[len(self.perceptron)-2-x][3][k])) * sumatorio2)
				for n in range(self.perceptron[len(self.perceptron)-3-x][0]):
					self.perceptron[len(self.perceptron)-2-x][2][k][n] = self.perceptron[len(self.perceptron)-2-x][2][k][n] - self.alpha * deltal[k] * self.perceptron[len(self.perceptron)-3-x][3][n]
				self.perceptron[len(self.perceptron)-2-x][1][k] = self.perceptron[len(self.perceptron)-2-x][1][k] - self.alpha * deltal[k]
			deltam = deltal
	def save(self):
		#ahora guardamos nuestro perceptron para que el entrenamiento quede guardado
		print('entrenamiento finalizado...guardamos los resultados')
		entrenamiento = open(self.saveurl,'w')
		entrenamiento.write(str(self.perceptron))
		entrenamiento.close


		
if __name__ == "__main__":
    Perceptron()
