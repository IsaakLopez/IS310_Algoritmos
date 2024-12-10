from random import *

class Arreglo():
    def __init__(self, size):
        self.__maxSize = size
        self.__item = [None] * size
        self.__nItems = 0
    
    def insertar(self, item):
        self.__item[self.__nItems] = item
        self.__nItems += 1

    def __len__(self):
        return self.__nItems
    

    def killDuplicados(self):
        conteo = 0
        for j in range(self.__nItems):
            for i in range(j+1, self.__nItems):
                if self.__item[j] == self.__item[i]:
                    self.__item[i] = None                   

        return [x for x in self.__item if x is not None]

    
size = int(input("Ingrese el tamaño de el arreglo: "))
arr = Arreglo(size)

print("El arreglo contiene: ")

for j in range(0, size):
    elemento = randint(0,100)
    arr.insertar(elemento)
    print(elemento)

print("El arreglo inicialmente tiene: ", len(arr))

print("El nuevo arreglo sin duplicados es: ", arr.killDuplicados())

print("El arreglo sin duplicados tiene: ", len(arr.killDuplicados()))
