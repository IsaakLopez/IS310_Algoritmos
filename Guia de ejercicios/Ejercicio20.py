class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(valor)
            else:
                self._insertar_recursivo(valor, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(valor)
            else:
                self._insertar_recursivo(valor, nodo.derecha)

    def recorrer_inorder(self, nodo):
        if nodo is not None:
            self.recorrer_inorder(nodo.izquierda)
            print(nodo.valor, end=' ')
            self.recorrer_inorder(nodo.derecha)

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, nodo):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar_recursivo(valor, nodo.izquierda)
        else:
            return self._buscar_recursivo(valor, nodo.derecha)

# Ejemplo de uso
arbol = ArbolBinario()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(2)
arbol.insertar(7)
arbol.insertar(12)
arbol.insertar(20)

print("Recorrido inorder:")
arbol.recorrer_inorder(arbol.raiz)

nodo_encontrado = arbol.buscar(7)
if nodo_encontrado:
    print("\nElemento ", nodo_encontrado.valor,  "encontrado en el árbol.")
else:
    print("\nElemento no encontrado en el árbol.")
