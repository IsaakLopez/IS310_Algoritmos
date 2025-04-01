from random import *

class arreglo(): #Esta clase guarda el arreglo
    def __init__(self,size):
        self.__maxsize = size
        self.__item = [None] * size
        self.__nItems = 0

    def len(self):
        return self.__nItems
    
    def insert(self,elemento):
        self.__item[self.__nItems] = elemento
        self.__nItems += 1

    def suma(self):
        suma = 0
        for j in range(0, self.__nItems):
            suma += self.__item[j]       

        return suma

arr = arreglo(12)

print("el arreglo contiene los siguientes elementos: ")

for j in range(0, 12):
    elemento = randint(1,100)
    print(elemento)
    arr.insert(elemento)
    

print("tamaño de arreglo: ", arr.len())
print("la suma de los elementos del arreglo da: ", arr.suma())
