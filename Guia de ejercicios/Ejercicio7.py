def verificar_parentesis(cadena):
    pila = []
    pares = {')': '(', '}': '{', ']': '['}

    for caracter in cadena:
        if caracter in pares.values():
            pila.append(caracter)
        elif caracter in pares.keys():
            if pila and pila[-1] == pares[caracter]:
                pila.pop()
            else:
                return False

    return pila == []

# Ejemplo de uso
cadena = "{[[()]}"
resultado = verificar_parentesis(cadena)
print("La cadena ", cadena," está balanceada: ", resultado)
