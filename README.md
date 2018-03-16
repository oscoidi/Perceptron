# Perceptrón
Perceptrón diseñado con la idea de asimilar los conceptos escondidos detras del algoritmo _backpropagation_. Además lo he programado de la manera mas general posible pudiendose utilizar como libreria  para resolver multiples problemas en caso de que asi se desee.
Para ejemplificar el funcionamiento del programa, la red neuronal recibirá dos números (entre 0 y 1) y deberá decidir cuál de los dos es mayor (`salida = 1` si el primero es mayor que el segundo, `salida = 0` en caso contrario).
El paquete consta de tres archivos:
  - `perceptron.py` es el programa de python que nos realizará todos los cálculos y nos generará la red neuronal. Deberemos cambiar       el url donde estamos trabajando en función de dónde guardemos el programa. 
  El programa nos preguntará cuántas capas queremos que tenga la red y cuántas neuronas tiene cada capa. Por ultimo nos preguntará cuántas veces queremos pasar la _training data_.
  - `perceptron.txt` es un archivo de texto vacío donde se guardará la estructura de la red neuronal una vez entrenada.
  - `entrenamientoperc.txt` es un archivo de texto donde se guardan los datos de entrenamiento. El formato de la _data training_ consta de dos arrays, uno con las entradas y otro con las salidas esperadas:
  
  ```python
  [entrada1,entrada2,...,entradan][salida1,salida2,...,salidan]
  ```
  para este ejemplo: 
  
  ```python
  [0.9,0.1][1]
```
