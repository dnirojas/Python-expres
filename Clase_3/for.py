'''
Ejemplo de estructura de control for en Python
'''
conador = 5  # Inicialización del contador
for i in range(conador):  # Bucle que itera desde 0 hasta 4
    print("Iteración:", i)  # Imprimir el número de iteración
print("Bucle for terminado")  # Mensaje al finalizar el bucle

# Ejemplo de iteración sobre una lista
array = [1, 2, 3, 4, 5]  
array.append(6)  # Agregar un elemento al final de la lista
for i in range(len(array)):  # Iterar sobre los índices de la lista
    print("Elemento en el índice", i, ":", array[i])  # Imprimir el elemento en el índice actual