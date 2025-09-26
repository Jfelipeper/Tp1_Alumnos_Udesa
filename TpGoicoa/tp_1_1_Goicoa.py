import random
from tp_1_funciones_Goicoa import simulacion
estado_inicial = input('Ingrese el estado inicial del clima: ').capitalize() #Le aplico .capitalize() para que, aunque el usuario escriba 'soleado' en minusculas, al igualarlo a 'Soleado' me de True
periodo = int(input('Ingrese la cantidad de dias: '))
call_funcion = simulacion(estado_inicial,periodo) #Llamo a mi funcion que simula los dias introduciendole los datos introducidos por el usuario
print (f'Dia 0: {estado_inicial}')
for num,clima_hoy in enumerate(call_funcion,1): #Le aplico enumerate a mi lista que contiene todos los resultados arrancando en 1. Luego desempaqueto la lista de tuplas que sale del enumerate en dos variables nuevas, para poder printearlo como se pide
    print(f'Dia {num}: {clima_hoy}')