import random

climas = ["soleado", "nublado", "lluvioso", "tormenta", "nevado"]

while True:  #crea un bucle que termina cuando alguna condición dentro del while se cumpla
    estado_inicial = input("¿Cuál es el estado inicial del clima?: ").lower().strip()
    if estado_inicial in climas:
        break   #si el clima ingresado por el ususario esta en climas, rompe el bucle y sigue con el programa
    else:
        print("El estado ingresado no es válido, por favor ingrese otro.")   #si el clima ingresado no esta e climas, vuelve al bucle


cant_dias = int(input("Ingrese la cantidad de días (mayor a 1): "))
if cant_dias <= 0:
    cant_dias = 0 #Si l acantidad de días ingresada es negativa, se imprime solo el día cero

#Esta función devuelve la cantidad de climas que haya ingresado el ususario dependiendo de las probabilidades
from Tp1_Funciones_Gramajo import secuencia_entera

dias_final = secuencia_entera(estado_inicial, cant_dias)

for cantidad_ingresada, clima in enumerate(dias_final): #arranca a enumerar en cero la cantidad de días ingresada en la función
    print(f"{cantidad_ingresada}: {clima}") 