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

arr = Cola(5)

print("Ponemos en cola: 5 valores")
arr.enqueue("A001")
arr.enqueue("B001")
arr.enqueue("C001")
arr.enqueue("A002")
arr.enqueue("B002")

print("la cola quedaria asi: ", arr)

print("Desencolamos el numeros: ", arr.dequeue())
print("Desencolamos el numeros: ", arr.dequeue())

print("Agrego mas datos a la cola: ")
arr.enqueue("C002")
arr.enqueue("A003")

print("Cuantos numero hay en cola: ", arr)
print("El siguiente numero en salir es: ", arr.peek())
