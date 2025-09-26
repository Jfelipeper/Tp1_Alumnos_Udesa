import random
from tp1_funciones_Longhi import preguntar_clima, clima, soleado, nublado, lluvioso, tormenta, nevado

def simular_clima():
  '''Simula el comportamiento del clima por la cantidad de dias ingresada por el usuario 
  Imprime por consola el clima por la cantidad de dias ingresados por el usuario'''
  dias, clima_inicial = preguntar_clima(clima)
  clima_actual = clima_inicial
  for i in range(dias):
    if(clima_actual == 'soleado'):
      print(f'dia {i+1}: ☀️ {clima_actual.capitalize()}')
      clima_actual = random.choices(clima, weights=soleado)[0]
    elif(clima_actual == 'nublado'):
      print(f'dia {i+1}: ☁️ {clima_actual.capitalize()}')
      clima_actual = random.choices(clima, weights=nublado)[0]
    elif(clima_actual == 'lluvioso'):
      print(f'dia {i+1}: 🌧️ {clima_actual.capitalize()}')
      clima_actual = random.choices(clima, weights=lluvioso)[0]
    elif(clima_actual == 'tormenta'):
      print(f'dia {i+1}: ⛈️ {clima_actual.capitalize()}')
      clima_actual = random.choices(clima, weights=tormenta)[0]
    else:
      print(f'dia {i+1}: ❄️ {clima_actual.capitalize()}')
      clima_actual = random.choices(clima, weights=nevado)[0]

simular_clima()