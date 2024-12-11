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

print("La primera persona que llego al banco se le dio el numero: A001")
arr.enqueue("A001")
print("La siguiente persona obtuvo el numero: B001")
arr.enqueue("Boo1")
print("La siguiente persona obtuvo el numero: C001")
arr.enqueue("C001")

print("El numero a pasar a la ventanilla es: ", arr.dequeue())
print("El numero a pasar a la ventanilla es: ", arr.dequeue())
print("Que numeros quedan en cola? : ", arr)
