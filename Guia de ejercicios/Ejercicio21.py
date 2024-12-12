class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def altura(arbol):
    if arbol is None:
        return 0
    else:
        # Altura del subárbol izquierdo
        altura_izquierda = altura(arbol.izquierdo)
        # Altura del subárbol derecho
        altura_derecha = altura(arbol.derecho)
        # La altura del árbol es 1 más la altura del subárbol más alto
        return max(altura_izquierda, altura_derecha) + 1

# Ejemplo de uso:
raíz = Nodo(1)
raíz.izquierdo = Nodo(2)
raíz.derecho = Nodo(3)
raíz.izquierdo.izquierdo = Nodo(4)
raíz.izquierdo.derecho = Nodo(5)

print("La altura del árbol es:", altura(raíz))
