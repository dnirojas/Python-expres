''''
crear un programa que pida 2 numeros y 
obtenga como resultado cual de ellos es pa
o si ambos lo son 
'''
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
if numero1 % 2 == 0 and numero2 % 2 == 0:
    print("Ambos números son pares.")
elif numero1 % 2 == 0 and numero2 % 2 != 0:
    print("El primero es par y el segundo impar.")
elif numero2 % 2 == 0 and numero1 % 2 != 0:
    print("El segundo es par y el primero impar.")
else:
    print("Ninguno de los números es par.")