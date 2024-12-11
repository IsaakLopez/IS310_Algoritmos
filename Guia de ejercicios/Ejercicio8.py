class Pila():
    def __init__(self, size):
        self.__maxSize = size
        self.__item = [None] * size
        self.__nItems = 0
    
    def __len__(self):
        return self.__nItems
    
    def __str__(self):
        return str(self.__item[:self.__nItems])  

    def push(self, item):
        self.__item[self.__nItems] = item
        self.__nItems += 1

    def pop(self):
        Valor =  self.__item[self.__nItems-1]
        self.__item[self.__nItems-1] = None
        self.__nItems -= 1
        return Valor
    
    def peek(self):
        return self.__item[self.__nItems-1]

    def invertir(self):
        Invertida = " "
        for j in range(self.__nItems):
            Invertida += self.pop()
        
        return Invertida

cadena = "yo soy tu padre"

arr = Pila(len(cadena))


for j in cadena:
    arr.push(j)

print("La cadena es: ", cadena)
print("El arreglo contiene: ", arr)
print("La cadena invertida es: ", arr.invertir())