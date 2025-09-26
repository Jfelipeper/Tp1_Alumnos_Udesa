from data import climas, emojis_climas
from tp1_funciones_Bugna import simulador_climas

def ej_1 ():
    estado_inicial = input("Ingrese el estado inicial del clima: ").lower().strip()
    while (estado_inicial not in climas):
        print(f"Estado inicial invalido debe ser uno de estos: {[climas[0]]}, {[climas[1]]}, {[climas[2]]}, {[climas[3]]}, {[climas[4]]}")
        estado_inicial = input("Ingrese nuevamente el estado inicial del clima: ")
    dias = int(input("Ingrese la cantidad de dias que quieras simular: "))
    while(dias <= 0 ):
        print("La cantidad de dias ingresado debe ser un entero positivo")
        dias = int(input("Ingrese nuevamente la cantidad de dias que quieras simular: "))
    simulacion = simulador_climas(estado_inicial, dias)
    #este for recorre la simulacion de los climas, y va a asignandole a cada dia un clima usando las funciones del archivo
    for i, clima in enumerate(simulacion):
        icono = emojis_climas.get(clima, "")
        print(f"Dia {i}: {clima.capitalize()} {icono}") 

ej_1()
