import random
from tp1_funciones_Longhi import preguntar_clima, clima_mas_frecuente, clima, soleado, nublado, lluvioso, tormenta, nevado

def simular_clima():
  '''Simula el comportamiento del clima por la cantidad de dias ingresada por el usuario 
  Imprime por consola el clima o los climas mas frecuentes'''
  dias, clima_inicial = preguntar_clima(clima)
  dias_soleado = 0
  dias_nublado = 0
  dias_lluvioso = 0
  dias_tormenta = 0
  dias_nevado = 0
  clima_actual = clima_inicial
  for i in range(dias):
    if clima_actual == 'soleado':
      clima_actual = random.choices(clima, weights=soleado)[0]
      dias_soleado+=1
    elif clima_actual == 'nublado':
      clima_actual = random.choices(clima, weights=nublado)[0]
      dias_nublado+=1
    elif clima_actual == 'lluvioso':
      clima_actual = random.choices(clima, weights=lluvioso)[0]
      dias_lluvioso+=1
    elif clima_actual == 'tormenta':
      clima_actual = random.choices(clima, weights=tormenta)[0]
      dias_tormenta+=1
    else:
      clima_actual = random.choices(clima, weights=nevado)[0]
      dias_nevado+=1
  
  print(f'Días soleados: {dias_soleado} ({round((dias_soleado/dias)*100, 2)}%) \nDías nublados: {dias_nublado} ({round((dias_nublado/dias)*100, 2)}%) \nDías lluviosos: {dias_lluvioso} ({round((dias_lluvioso/dias)*100, 2)}%) \nDías tormentosos: {dias_tormenta} ({round((dias_tormenta/dias)*100, 2)}%) \nDías nevados: {dias_nevado} ({round((dias_nevado/dias)*100,2)}%)')
  clima_mas_frecuente(dias_soleado, dias_nublado, dias_lluvioso, dias_tormenta, dias_nevado)

simular_clima()


