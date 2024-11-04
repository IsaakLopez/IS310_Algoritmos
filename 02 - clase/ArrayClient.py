import Array

maxSize = 100                    
arr = Array.Array(maxSize)      

opcion = input("Ingrese su opcion pila/cola: ")

if opcion in ["pila", "cola"]:
    print("La ", opcion, "es la siguiente: ", arr.traverse())    
        
    tipo = 1 if opcion == "pila" else 2
        
    contImpar, contPar, sumaImpar, sumaPar = arr.detParidad(tipo)
        
    print("La cuenta de numero impares es: ", contImpar)
    print("La cuenta de numero pares es: ", contPar)
    print("La suma de los numeros impares es: ", sumaImpar)
    print("La suma de los numeros pares es: ", sumaPar)
else:
    print("Seleccion no valida")

