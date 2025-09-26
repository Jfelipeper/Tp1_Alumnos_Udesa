from data import probabilidades_climas, climas
import random

#Funcion donde randomizamos el proximo clima segun el estado inicial ingresado por el usuario o dado directamente por el programa
def siguiente_clima (estado_inicial):
    estados = climas
    pesos = probabilidades_climas[estado_inicial]
    return random.choices(estados, weights=pesos)[0]



#Funcion para ir simulando el micro clima de la isla segun el clima inicial y la cantidad de dias dados
def simulador_climas (estado_inicial, dias):
    resultado = [estado_inicial]
    actual = estado_inicial
    for t in range(dias):
        actual = siguiente_clima(actual)
        resultado.append(actual)
    return resultado

#Funcion donde vemos las rachas de 4 dias consecutivos de un clima y la racha mas larga que hubo y de que clima fue la misma
def analizar_rachas (secuencia, minimo=4):
    total_rachas_de_4 = 0
    actual = secuencia[0]
    largo = 1
    max_largo = 1
    max_clima = actual

    for i in secuencia[1:]:
        if (i == actual):
            largo += 1
        else:
            if (largo >= minimo):
                total_rachas_de_4 +=1
            if (largo > max_largo):
                max_largo = largo
                max_clima = actual
        
            actual = i
            largo = 1 
    if (largo >= minimo):
        total_rachas_de_4 +=1
    if(largo > max_largo):
        max_largo = largo
        max_clima = actual
    
    return total_rachas_de_4, (max_largo, max_clima)