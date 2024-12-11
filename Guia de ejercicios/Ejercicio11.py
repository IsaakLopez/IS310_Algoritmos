from random import *
class Cola():
    def __init__(self, size):
        self.__maxSize = size
        self.__item = [None] * size
        self.__nItems = 0
    
    def __len__(self):
        return self.__nItems
    
    def __str__(self):
        return str(self.__item[:self.__nItems])  

    def enqueue(self, item):
        self.__item[self.__nItems] = item
        self.__nItems += 1

    def dequeue(self):
        Valor =  self.__item[0]
        del self.__item[0]
        self.__nItems -= 1
        return Valor
    
    def peek(self):
        return self.__item[0]

arr = Cola(5)

for j in range(5):
    arr.enqueue(randint(0,100))

print("Asi quedaria la cola: ", arr)
print("El proximo valor en salir sería: ", arr.peek())
print("Sacamos el valor proximo a salir de la cola: ", arr.dequeue())
print("Asi quedaria la cola: ", arr)
