import random
from tp1_funciones_Longhi import preguntar_clima, calcular_rachas, calcular_racha_mas_alta, calcular_rachas_de_3_dias, clima, soleado, nublado, lluvioso, tormenta, nevado

def simular_clima():
  '''Simula el comportamiento del clima por la cantidad de dias que ingresa el usuario 
  Imprime por consola el clima que haya tenido la racha mas larga
  Imprime por consola la cantidad de rachas de mas de 3 dias'''
  dias, clima_inicial = preguntar_clima(clima)
  clima_actual = clima_inicial
  lista_de_climas = []

  for i in range(dias):
    if clima_actual == 'soleado':
      clima_actual = random.choices(clima, weights=soleado)[0]
      lista_de_climas.append(clima_actual)
    elif clima_actual == 'nublado':
      clima_actual = random.choices(clima, weights=nublado)[0]
      lista_de_climas.append(clima_actual)
    elif clima_actual == 'lluvioso':
      clima_actual = random.choices(clima, weights=lluvioso)[0]
      lista_de_climas.append(clima_actual)
    elif clima_actual == 'tormenta':
      clima_actual = random.choices(clima, weights=tormenta)[0]
      lista_de_climas.append(clima_actual)
    else:
      clima_actual = random.choices(clima, weights=nevado)[0]
      lista_de_climas.append(clima_actual)
  
  rachas_soleado, rachas_nublado, rachas_lluvioso, rachas_tormenta, rachas_nevado = calcular_rachas(lista_de_climas)
  calcular_racha_mas_alta(rachas_soleado, rachas_nublado, rachas_lluvioso, rachas_tormenta, rachas_nevado)
  calcular_rachas_de_3_dias(rachas_soleado, rachas_nublado, rachas_lluvioso, rachas_tormenta, rachas_nevado)

simular_clima()