import random

#DATOS
clima = ['soleado', 'nublado', 'lluvioso', 'tormenta', 'nevado']
soleado = [60,30,5,3,2]
nublado = [40,30,20,5,5]
lluvioso = [10,30,40,15,5]
tormenta = [5,10,30,50,5]
nevado = [5,20,20,10,45]

#FUNCIONES EJERCICIO 1
def preguntar_clima(clima):
  '''Le pide al usuario que complete con un estado inicial y una cantidad de dias hasta que los datos sean validos'''
  clima_inicial = input("Ingrese el estado inicial: ").lower()
  while(clima_inicial not in clima):
    print('El estado inicial debe ser uno de: soleado, nublado, lluvioso, tormenta, nevado')
    clima_inicial = input("Ingrese el estado inicial: ")

  dias = int(input("Ingrese la cantidad de dias: "))
  while(dias <= 0):
    print('La cantidad de días debe ser un entero positivo')
    dias = int(input("Ingrese la cantidad de dias: "))
  
  return dias, clima_inicial

#FUNCIONES EJERCICIO 2
def clima_mas_frecuente(dias_soleado, dias_nublado, dias_lluvioso, dias_tormenta, dias_nevado):
  '''Toma como parametros la cantidad de días de cada clima
  Calcula cual fue el clima mas frecuente y lo imprime por consola
  Tambien tiene en cuenta en caso de que haya empates y te imprime todos los climas que hayan tenido la misma cantidad de dias'''
  dias_climas = {
      "☀️ Soleado": dias_soleado,
      "☁️ Nublado": dias_nublado,
      "🌧️ Lluvioso": dias_lluvioso,
      "⛈️ Tormenta": dias_tormenta,
      "❄️ Nevado": dias_nevado
  }

  maximo = max(dias_climas.values())

  mas_frecuentes = []
  for clima, dias in dias_climas.items():
      if dias == maximo:
          mas_frecuentes.append(clima)

  if len(mas_frecuentes) == 1:
      print("\nEl clima más frecuente fue:", mas_frecuentes[0])
  else:
    dias_climas_empate = ''
    if len(mas_frecuentes) == 2:
        dias_climas_empate = f'{mas_frecuentes[0]} y {mas_frecuentes[1]}'
    elif len(mas_frecuentes) == 3:
        dias_climas_empate = f'{mas_frecuentes[0]}, {mas_frecuentes[1]} y {mas_frecuentes[2]}'
    elif len(mas_frecuentes) == 4:
        dias_climas_empate = f'{mas_frecuentes[0]}, {mas_frecuentes[1]}, {mas_frecuentes[2]} y {mas_frecuentes[3]}'
    elif len(mas_frecuentes) == 5:
        dias_climas_empate = f'{mas_frecuentes[0]}, {mas_frecuentes[1]}, {mas_frecuentes[2]}, {mas_frecuentes[3]} y {mas_frecuentes[4]}'

    print(f'Los climas mas frecuentes fueron: {dias_climas_empate}')

#FUNCIONES EJERCICIO 3
def calcular_rachas (lista_de_climas):
  '''Toma como parametro una lista que tiene todos los climas en x dias
  Evalua si es que algun clima esta en racha y va sumando cada racha a su respectiva lista
  Devuelve las listas de rachas de cada clima'''
  rachas_soleado = []
  rachas_nublado = []
  rachas_lluvioso = []
  rachas_tormenta = []
  rachas_nevado = []
  racha = {
            'soleado': 0,
            'nublado': 0,
            'lluvioso': 0,
            'tormenta': 0,
            'nevado': 0
            }
  for i in range(len(lista_de_climas)):
    if lista_de_climas[i] == lista_de_climas[i-1]:
      racha[lista_de_climas[i]] += 1
    else:
      racha[lista_de_climas[i]] = 1

    if lista_de_climas[i] == 'soleado':
      rachas_soleado.append(racha['soleado'])
    elif lista_de_climas[i] == 'nublado':
      rachas_nublado.append(racha['nublado'])
    elif lista_de_climas[i] == 'lluvioso':
      rachas_lluvioso.append(racha['lluvioso'])
    elif lista_de_climas[i] == 'tormenta':
      rachas_tormenta.append(racha['tormenta'])
    elif lista_de_climas[i] == 'nevado':
      rachas_nevado.append(racha['nevado'])
    
  return rachas_soleado, rachas_nublado, rachas_lluvioso, rachas_tormenta, rachas_nevado

def calcular_racha_mas_alta(rachas_soleado, rachas_nublado, rachas_lluvioso, rachas_tormenta, rachas_nevado):
  '''Toma como parametros las rachas de cada clima
  Calcula cual clima fue el que tuvo la racha mas alta
  Imprime por consola cual fue el que tuvo la racha mas larga
  Tambien tiene en cuenta en caso de que haya empates y te imprime todos los climas que hayan tenido la racha mas larga'''
  rachas_maximas = {
      "☀️ Soleado": max(rachas_soleado) if rachas_soleado else 0,
      "☁️ Nublado": max(rachas_nublado) if rachas_nublado else 0,
      "🌧️ Lluvioso": max(rachas_lluvioso) if rachas_lluvioso else 0,
      "⛈️ Tormentoso": max(rachas_tormenta) if rachas_tormenta else 0,
      "❄️ Nevado": max(rachas_nevado) if rachas_nevado else 0
  }

  racha_maxima = max(rachas_maximas.values())

  climas_con_maxima = []
  for clima, racha in rachas_maximas.items():
      if racha == racha_maxima:
          climas_con_maxima.append(clima)

  if len(climas_con_maxima) == 1:
    print(f'\nRacha mas larga: {racha_maxima} días de {climas_con_maxima[0]}')
  else:
    climas_empate = ''
    if len(climas_con_maxima) == 2:
      climas_empate = f'{climas_con_maxima[0]} y {climas_con_maxima[1]}'
    elif len(climas_con_maxima) == 3:
      climas_empate = f'{climas_con_maxima[0]}, {climas_con_maxima[1]} y {climas_con_maxima[2]}'
    elif len(climas_con_maxima) == 4:
      climas_empate = f'{climas_con_maxima[0]}, {climas_con_maxima[1]}, {climas_con_maxima[2]} y {climas_con_maxima[3]}'
    elif len(climas_con_maxima) == 5:
      climas_empate = f'{climas_con_maxima[0]}, {climas_con_maxima[1]}, {climas_con_maxima[2]}, {climas_con_maxima[3]} y {climas_con_maxima[4]}'

    print(f'\nRacha mas larga: {racha_maxima} días de {climas_empate}')

def calcular_rachas_de_3_dias(rachas_soleado, rachas_nublado, rachas_lluvioso, rachas_tormenta, rachas_nevado):
  '''Toma como parametros las rachas de cada clima
  Calcula todas las rachas distintas que sean mayores a 3
  Imprime por consola la cantidad de rachas distintas mayores a 3 hubo'''
  rachas_mas_de_3 = 0
  for i in rachas_soleado:
    if i == 4:
      rachas_mas_de_3 +=1 

  for i in rachas_nublado:
    if i == 4:
      rachas_mas_de_3 +=1 

  for i in rachas_lluvioso:
    if i == 4:
      rachas_mas_de_3 +=1 

  for i in rachas_tormenta:
    if i == 4:
      rachas_mas_de_3 +=1 

  for i in rachas_nevado:
    if i == 4:
      rachas_mas_de_3 +=1 

  print(f'Rachas de mas de 3 días: {rachas_mas_de_3}')