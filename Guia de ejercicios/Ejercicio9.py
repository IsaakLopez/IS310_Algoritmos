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
        if isinstance(item, (int, float)):
            self.__item[self.__nItems] = item
            self.__nItems += 1
        else:
            b = self.pop()
            a = self.pop()
            self.Operar(item ,a, b)

    def pop(self):
        Valor =  self.__item[self.__nItems-1]
        self.__item[self.__nItems-1] = None
        self.__nItems -= 1
        return Valor
    
    def peek(self):
        return self.__item[self.__nItems-1]

    def Operar(self, operando, a, b):
        if operando == '+':
            self.push(a+b)
        elif operando == '-':
            self.push(a-b)
        elif operando == '*':
            self.push(a*b)
        elif operando == '/':
            self.push(a/b)

arr = Pila(5)

for j in [7, 3, '-', 2, '*']:
    arr.push(j)

print("La pila al final contiene: ", arr)