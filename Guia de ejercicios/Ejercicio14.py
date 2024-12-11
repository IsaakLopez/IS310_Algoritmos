from random import *
class Cola():
    def __init__(self, size):
        self.__maxSize = size
        self.__item = [None] * size
        self.__nItems = 0
        self.__front = 0
        self.__tras = -1
    
    def __len__(self):
        return self.__nItems
    
    def __str__(self):
        return str(self.__item[:self.__nItems])  

    def enqueue(self, item):
        self.__tras += 1
        if self.__tras == self.__maxSize:
            self.__tras = 0
        self.__item[self.__tras] = item
        self.__nItems += 1

    def dequeue(self):
        Valor =  self.__item[self.__front]
        self.__item[self.__front]
        self.__front += 1
        if self.__front == self.__maxSize:
            self.__front = 0
        self.__nItems -= 1
        return Valor
    
    def peek(self):
        return self.__item[self.__front]
    
    def organizar_pares(self):
        pares=[]
        impares = []

        for j in range(self.__nItems):
            numero = self.dequeue()            
            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares.append(numero)
        return pares + impares


arr = Cola(5)

for j in range(5):
    arr.enqueue(randint(0,100))

print("Los numero en cola son: ", arr)
print("los numero organizados qeudarian: ", arr.organizar_pares())