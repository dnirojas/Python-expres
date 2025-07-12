'''
ejemplos de listas en python 
''' 

array = [1, "futbol", 5, True,{9,0,54}, False, 3.14, "hola", 2.5]
print(array)

print(array[0])  # Acceso al primer elemento
print(array[1])  # Acceso al segundo elemento 
print(array[0:3])  # Acceso a los primeros tres elementos
print(len(array))  # Longitud de la lista
array.append("nuevo elemento")  # Agregar un nuevo elemento al final
print(array)
array.insert(2, "insertado")  # Insertar un elemento en la posición 2
print(array)
array.extend([10, 20, 30])  # Agregar varios elementos al final
print(array)
array.remove("futbol")  # Eliminar un elemento específico
print(array)
array.pop(3)  # Eliminar el elemento en la posición 3
print(array)
array.clear()  # Limpiar la lista
print(array)
array = [1, "futbol", 5, True,{9,0,54}, False, 3.14, "hola", 2.5]
array1 = [1, 2, 3, 4, 5]
array2 = array + array1  # Concatenar dos listas
print(array2)
print("futbol" in array2)  # Verificar si un elemento está en la lista
print(array2.index("futbol"))  # Obtener el índice de un elemento
print(array2.count(1))  # Contar cuántas veces aparece un elemento
array4 = [1,2,3,4,5]
array4.reverse()  # Invertir el orden de los elementos
print(array4)
array5 = [1,5,3,2,4]
array5.sort()  # Ordenar la lista
print(array5)

