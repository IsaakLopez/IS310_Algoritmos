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

    def eliminar_duplicados(self):
        if not self.punta:
            return
        actual = self.punta
        while actual:
            corredor = actual
            while corredor.siguiente:
                if corredor.siguiente.valor == actual.valor:
                    corredor.siguiente = corredor.siguiente.siguiente
                else:
                    corredor = corredor.siguiente
            actual = actual.siguiente

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar_al_final(1)
lista.agregar_al_final(2)
lista.agregar_al_final(3)
lista.agregar_al_final(2)
lista.agregar_al_final(3)
lista.agregar_al_final(4)
print("Lista con duplicados:", lista.mostrar_lista())

lista.eliminar_duplicados()
print("Lista sin duplicados:", lista.mostrar_lista())
