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
    
    def visita(self, url):
        self.push(url)

    def regresar(self):
        self.pop()

arr = Pila(5)

arr.visita("https://campusvirtual.unah.edu.hn/login/index.php")
arr.visita("https://campusvirtual.unah.edu.hn/my/")
arr.visita("https://campusvirtual.unah.edu.hn/course/view.php?id=57513")
print("Actualmente estas en: ", arr.peek())

print("Regresamos a la pagina anterior: ") 
arr.regresar()
print("Actualmente estas en: ", arr.peek())

print("Regresamos a la pagina anterior: ") 
arr.regresar()
print("Actualmente estas en: ", arr.peek())

