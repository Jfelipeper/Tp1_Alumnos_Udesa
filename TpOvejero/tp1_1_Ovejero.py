import random
from tp1_funciones_Ovejero import simular
#inputs
estado = input("Ingrese el estado inicial (soleado, nublado, lluvioso, tormenta o nevado): ").lower()
n = input("Ingrese el número de simulaciones (Entero mayor a 0): ")

if n.isdecimal(): #verifico si el input es un número para convertirlo en int
    n = int(n)
    resultado = simular(estado, n)
    if n > 0:
        for numero, dia in enumerate(resultado):
            print(f"Día {numero}: {dia.capitalize()}")
    elif n <= 0 or type(n) is not int:
        print("La cantidad de días debe ser un entero positivo")
    else:
        print(resultado)
else:
    print("La cantidad de días debe ser un entero positivo")



