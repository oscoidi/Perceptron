# Perceptron
Perceptron diseñado con la idea de asimilar los conceptos escondidos detras del algoritmo backpropagation.
Para ejemplificar el funcionamiento del programa la red neuronal recibira dos numeros(entre 0 y 1) y debera decidir cual de los dos es mayor(salida = 1 si el primero es mayor que el segundo, 0 en caso contrario.)
El paquete consta de tres archivos:
  - perceptron.py es el programa de python que nos realizara todos los calculos y nos generara la red neuronal. Deberemos cambiar       el url donde estamos trabajando en funcion de donde guardemos el programa. 
  El programa nos preguntara cuantas capas queremos que tenga la red y cuantas neuronas tiene cada capa. Por ultimo nos preguntara cuantas veces queremos pasar la training data.
  - perceptron.txt es un archivo de texto vacio donde se guardara la estructura de la red neuronal una vez entrenada
  - entrenamientoperc.txt es un archivo de texto donde se guarda los datos de entrenamiento. El formato de la data training consta de dos arrays uno con las entradas y otro con las salidas esperadas: [entrada1,entrada2,...,entradan][salida1,salida2,...,salidan]
  para este ejemplo: [0.9,0.1][1]

