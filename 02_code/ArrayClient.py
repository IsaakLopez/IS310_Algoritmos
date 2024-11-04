import Array
maxSize = 10                    # Max size of the array
arr = Array.Array(maxSize)      # Create an array object

   
arr.insert(77)                  # Insert 10 items
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(12)
arr.insert("bar")
arr.insert(77)


print("Array containing", len(arr), "items", arr.traverse())

print("Search for 12 returns", arr.search(12))

print("Search for 12.34 returns", arr.search(12.34))

print("Deleting 0 returns", arr.delete(0))
print("Deleting 17 returns", arr.delete(17))

print("Setting item at index 3 to 33")
arr.set(3, 33)

print("Array after deletions has", len(arr), "items", arr.traverse())


#Ejercicio 2.1
print("The Max Number in the array is: ", arr.getMaxNum())


#Practica Clase
print("The Average in the array is: ", arr.getPromed())


#Ejercicio 2.2
print("La eliminacion del maximo numero es: ", arr.deleteMaxNUmber())

print("Array after deletions Max Number has", len(arr), "items", arr.traverse())

#Practica en clase
print("los numeros pares en el arreglo son: ", arr.getPair(0))

print("los numeros impares pares en el arreglo son: ", arr.getPair(1))

print("los elementos con cedenas de texto en el arreglo son: ", arr.getWords())


#Ejercicio 2.4
arr.eliminar_duplicados()
print("Los elementos sin duplicados son: ",arr.traverse())

