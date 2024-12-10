from random import *

class Arreglo():
    def __init__(self, size):
        self.__maxSize = size
        self.__item = [None] * size
        self.__nItems = 0
    
    def __len__(self):
        return self.__nItems
    
    def push(self, item):
        self.__item[self.__nItems] = item
        self.__nItems += 1

    def pop(self):
        valor = self.__item[self.__nItems-1]
        self.__item[self.__nItems-1] = None
        self.__nItems -= 1
        return valor
    
    def __str__(self):
        return str(self.__item[:self.__nItems])  

size = int(input("Ingrese el tamaño de el arreglo: "))
arr = Arreglo(size)

print("El arreglo contiene: ")

for j in range(0, size):
    elemento = randint(0,100)
    arr.push(elemento)
    print(elemento)


print("La pila queda asi: ", arr)
print("Eliminando el primer valor de salida de la pila: ", arr.pop())
print("La pila queda asi: ", arr)
print("Agrego un nuevo valor a la pila: 777") 
arr.push(777)
print("La pila queda asi: ", arr)
