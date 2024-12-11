from random import *

class arreglo():
    def __init__(self,size):
        self.__maxsize = size
        self.__item = [None] * size
        self.__nItems = 0

    def len(self):
        return self.__nItems
    
    def insert(self,elemento):
        self.__item[self.__nItems] = elemento
        self.__nItems += 1

    def maximo(self):
        maximo = 0
        for i in range(0, self.__nItems):
            if self.__item[i] > maximo:
                maximo = self.__item[i]
        return maximo

    def minimo(self):
        minimo = self.__item[0]
        for i in range(0, self.__nItems):
            if self.__item[i] < minimo:
                minimo = self.__item[i]
        return minimo
arr = arreglo(12)

print("El arreglo contiene los siguientes elementos: ")

for j in range(0, 12):
    elemento = randint(1,100)
    print(elemento)
    arr.insert(elemento)
    

print("El tamaño del arreglo: ", arr.len())
print("El valor maximo del arreglo es: ", arr.maximo())
print("El valor minimo del arreglo es: ", arr.minimo())
