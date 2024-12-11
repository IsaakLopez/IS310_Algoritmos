from random import *

class Arreglo():
    def __init__(self, size):
        self.__maxSize = size
        self.__item = [None] * size
        self.__nItems = 0
    
    def insertar(self, item):
        self.__item[self.__nItems] = item
        self.__nItems += 1

    def buscar(self, item):
        conteo = 0
        for j in range(0, self.__nItems):
            if self.__item[j] == item:
                conteo += 1
        return conteo
    
size = int(input("Ingrese el tamaño de el arreglo: "))
arr = Arreglo(size)

print("El arreglo contiene: ")

for j in range(0, size):
    elemento = randint(0,100)
    arr.insertar(elemento)
    print(elemento)

print("Al buscar el elemento [1] obtuvimos: ", arr.buscar(1), "resultados.")
