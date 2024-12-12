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

    def mostrar_lista(self):
        elementos = []
        actual = self.punta
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos

def fusionar_listas(lista1, lista2):
    nodo_ficticio = Nodo(0)
    actual = nodo_ficticio

    nodo1 = lista1.punta
    nodo2 = lista2.punta

    while nodo1 and nodo2:
        if nodo1.valor < nodo2.valor:
            actual.siguiente = nodo1
            nodo1 = nodo1.siguiente
        else:
            actual.siguiente = nodo2
            nodo2 = nodo2.siguiente
        actual = actual.siguiente

    if nodo1:
        actual.siguiente = nodo1
    elif nodo2:
        actual.siguiente = nodo2

    lista_fusionada = ListaEnlazada()
    lista_fusionada.punta = nodo_ficticio.siguiente

    return lista_fusionada


lista1 = ListaEnlazada()
lista1.agregar_al_final(1)
lista1.agregar_al_final(3)
lista1.agregar_al_final(5)

lista2 = ListaEnlazada()
lista2.agregar_al_final(2)
lista2.agregar_al_final(4)
lista2.agregar_al_final(6)

lista_fusionada = fusionar_listas(lista1, lista2)
print("Lista fusionada:", lista_fusionada.mostrar_lista())