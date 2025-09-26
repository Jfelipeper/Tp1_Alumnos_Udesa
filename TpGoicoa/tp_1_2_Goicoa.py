from random import choices
from tp_1_funciones_Goicoa import simulacion
dias = 500
condicion_inicial = 'Soleado'
call_funcion = simulacion(condicion_inicial,dias) #Toma como valor una lista con todas las condiciones dia por dia
diccionario = {'Soleados' : call_funcion.count('Soleado'),
               'Nublados': call_funcion.count('Nublado'),
               'Lluviosos': call_funcion.count('Lluvioso'),
               'Tormentosos': call_funcion.count('Tormenta'),
               'Nevados': call_funcion.count('Nevado') } #Cuenta en el total de simulados, la cantidad correspondiente a cada dia
lista = [diccionario['Soleados'],
         diccionario['Nublados'],
         diccionario['Lluviosos'],
         diccionario['Tormentosos'],
         diccionario['Nevados']] #Paso los datos del diccionario a esta lista, para poder contar mas facil cual fue la condicion mas repetida
print (f'Dias soleados: {diccionario["Soleados"]} {(diccionario["Soleados"]*100)/dias}%')
print (f'Dias nublados: {diccionario["Nublados"]} {(diccionario["Nublados"]*100)/dias}%')
print (f'Dias lluviosos: {diccionario["Lluviosos"]} {(diccionario["Lluviosos"]*100)/dias}%')
print (f'Dias tormentas: {diccionario["Tormentosos"]} {(diccionario["Tormentosos"]*100)/dias}%')
print (f'Dias nevados: {diccionario["Nevados"]} {(diccionario["Nevados"]*100)/dias}%') #Toda esta estructura muestra la cantidad de cada clima y el porcentaje del total que representa
if max(lista) == lista [0]: #Esto muestra al usuario cual fue el clima mas frecuente
    print (f'el clima mas frecuente fue: Soleado')
elif max(lista) == lista [1]:
    print (f'el clima mas frecuente fue: Nublado')
elif max(lista) == lista [2]:
    print(f'el clima mas frecuente fue: Lluvioso')
elif max(lista) == lista [3]:
    print(f'el clima mas frecuente fue: Tormenta')
else:
    print (f'el clima mas frecuente fue: Nevado')