from data import climas, emojis_climas
from tp1_funciones_Bugna import simulador_climas, analizar_rachas

def ej_3 ():
    estado_inicial = input("Ingrese el estado inicial del clima: ").lower().strip()
    while (estado_inicial not in climas):
        print(f"Estado inicial invalido debe ser uno de estos: {[climas[0]]}, {[climas[1]]}, {[climas[2]]}, {[climas[3]]}, {[climas[4]]}")
        if(estado_inicial not in climas):
            estado_inicial = input("Ingrese nuevamente el estado inicial del clima: ")
    dias = 10000
    #Simulacion simula la fluctuacion del clima en la isla
    simulacion = simulador_climas(estado_inicial, dias)
    #Analizamos las distintas posibilidades de rachas de 4 dias o mas y la racha maxima, y nos dice de que clima es la racha maxima
    total_rachas_de_4,(largo_max, clima_max) = analizar_rachas(simulacion)
    if(clima_max == "soleado"):
        print(f"Racha mas larga: {largo_max} dias de {emojis_climas["soleado"]}  {clima_max} ")
    elif(clima_max == "nublado"):
        print(f"Racha mas larga: {largo_max} dias de {emojis_climas["nublado"]}  {clima_max} ")
    elif(clima_max == "lluvioso"):
        print(f"Racha mas larga: {largo_max} dias de {emojis_climas["lluvioso"]}  {clima_max} ")
    elif(clima_max == "tormenta"):
        print(f"Racha mas larga: {largo_max} dias de {emojis_climas["tormenta"]}  {clima_max} ")
    else:
        print(f"Racha mas larga: {largo_max} dias de {emojis_climas["nevado"]}  {clima_max} ")
    print(f"Racha de mas de 3 dias = {total_rachas_de_4}")
ej_3()