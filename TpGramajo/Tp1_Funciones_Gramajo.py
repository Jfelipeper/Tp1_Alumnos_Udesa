import random

climas = ["soleado", "nublado", "lluvioso", "tormenta", "nevado"]

primer_estado = "soleado"
cant_dias = 500
cant_dias2 = 10000

probabilidades = {
    "soleado": [60,30,5,3,2],
    "nublado": [40,30,20,5,5],
    "lluvioso": [10,30,40,15,5],
    "tormenta": [5,10,30,50,5],
    "nevado": [5,20,20,10,45],
}

def secuencia_entera(estado_inicial, cant_dias):
    """devuelve el clima aleatorio de la cantidad de días ingresada por el ususario, dependiendo del clima del anterior día"""
    aleatorio = [estado_inicial]
    for i in range (1, cant_dias+1): #el +1 lo agrego para que considere la cantidad de dias ingresada por el ususario sin contar el clima de indice cero
        prob = probabilidades[estado_inicial]
        siguiente_clima = random.choices(climas, weights=prob, k=1)[0]
        aleatorio.append(siguiente_clima) #al estado inicial se le pega el siguiente estado y se va formando una lista 
        estado_inicial = siguiente_clima #se actualiza el estado inicial en el bucle para que el prox clima considere el anterior
    return aleatorio   


#Las funciones pronostico y pronostico2 son las mismas pero cambian en la cantidad de días
def pronostico (primer_estado):
    """devuelve el clima aleatorio de 500 días, dependiendo del clima del anterior día"""
    variado = [primer_estado]
    for i in range (1, cant_dias): #no arranca desde cero porque tiene que ser la cant justa de días
        prob=probabilidades [primer_estado] #se fija en el clima que sea el primer estado
        siguiente_clima = random.choices(climas, weights=prob, k=1)[0] 
        variado.append(siguiente_clima) #Al primer estado se le agrega el siguiente clima
        primer_estado = siguiente_clima #El siguiente clima pasa a ser el primer estado para que la función se fije desde el ultimo clima
    return variado  

def pronostico2 (primer_estado):
    """devuelve el clima aleatorio de 10000 días, dependiendo del clima del anterior día"""
    variado = [primer_estado] 
    for i in range (1, cant_dias2):
        prob=probabilidades [primer_estado]
        siguiente_clima = random.choices(climas, weights=prob, k=1)[0]
        variado.append(siguiente_clima) 
        primer_estado = siguiente_clima
    return variado 
