from random import *

class Arreglo():
    def __init__(self, size):
        self.__maxSize = size
        self.__item = [None] * size
        self.__nItems = 0
    
    def insertar(self, item):
        self.__item[self.__nItems] = item
        self.__nItems += 1

    def invertir(self):
        invertido = []
        for j in range(self.__nItems - 1, -1, -1):
            invertido.append(self.__item[j])
        return invertido
    
size = int(input("Ingrese el tamaño de el arreglo: "))
arr = Arreglo(size)

print("El arreglo contiene: ")

for j in range(0, size):
    elemento = randint(0,100)
    arr.insertar(elemento)
    print(elemento)


print("El arreglo ya invertido es: ", arr.invertir())
