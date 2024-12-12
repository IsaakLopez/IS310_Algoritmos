class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.punta = None

    def agregar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.punta:
            self.punta = nuevo_nodo
            return
        actual = self.punta
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def eliminar_elemento(self, valor):
        actual = self.punta
        previo = None
        while actual and actual.valor != valor:
            previo = actual
            actual = actual.siguiente
        if not actual:
            return False  # El elemento no fue encontrado
        if not previo:
            self.punta = actual.siguiente
        else:
            previo.siguiente = actual.siguiente
        return True

    def buscar_elemento(self, valor):
        actual = self.punta
        while actual and actual.valor != valor:
            actual = actual.siguiente
        return actual is not None

    def mostrar_lista(self):
        elementos = []
        actual = self.punta
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos

    def invertir(self):
        previo = None
        actual = self.punta
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = previo
            previo = actual
            actual = siguiente
        self.punta = previo

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar_al_final(1)
lista.agregar_al_final(2)
lista.agregar_al_final(3)
print("Lista original:", lista.mostrar_lista())

lista.invertir()
print("Lista invertida:", lista.mostrar_lista())
