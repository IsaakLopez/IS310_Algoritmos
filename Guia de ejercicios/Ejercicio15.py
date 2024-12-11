from random import *
class Cola():
    def __init__(self, size):
        self.__maxSize = size
        self.__item = [None] * size
        self.__nItems = 0
        self.__front = 0
        self.__tras = -1
        self.__impares = []
    
    def __len__(self):
        return self.__nItems
    
    def __str__(self):
        return str(self.__item[:self.__nItems] + self.__impares)  

    def enqueue(self, item):
        if item % 2 == 0:
            self.__tras += 1
            if self.__tras == self.__maxSize:
                self.__tras = 0
            self.__item[self.__tras] = item
            self.__nItems += 1
        else:
            self.__impares.append(item)

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

arr = Cola(5)

for j in range(5):
    elemento = randint(0,100)
    arr.enqueue(elemento)
    print(elemento)

print("Los numero en cola son: ", arr)
