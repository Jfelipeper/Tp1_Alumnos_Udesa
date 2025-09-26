from tp1_funciones_FunesCosta import simulador_clima #Importamos las funciones que vamos a utilizar
import random

CLIMAS= ['soleado', 'nublado', 'lluvioso', 'tormenta', 'nevado']
emoji= {'soleado':'☀️ ', 'nublado':'☁️ ', 'lluvioso':'🌧️ ', 'tormenta':'⛈️ ', 'nevado':'❄️ '} #Para agregar un emoji dependiendo el tipo de clima, le agrego un espacio al lado para que no se superponga con el texto
estado_inicial= input('Ingrese el estado inicial del clima: ').lower() #Pedimos que el usuario ingrese el estado inicial del clima y usamos lower para que coincida con CLIMAS
cantidad_dias= int(input('Ingrese cantidad de días: ')) #Pedimos que el usuario ingrese la cantidad de días que quiere simular y usamos int() para que no sea un str y pueda usarse en las funciones

if estado_inicial not in CLIMAS and cantidad_dias<=0:
    print('El estado inicial debe ser uno de: soleado, nublado, lluvioso, tormenta, nevado')
    print('La cantidad de días debe ser un entero positivo')
elif estado_inicial not in CLIMAS:
    print('El estado inicial debe ser uno de: soleado, nublado, lluvioso, tormenta, nevado')
elif cantidad_dias<=0:
    print('La cantidad de días debe ser un entero positivo') #Verificamos que el usuario ingrese los datos correctamente
else:
    clima_simulado= simulador_clima(cantidad_dias, estado_inicial) #Obtenemos el clima simulado
    for tupla in clima_simulado:
        print(f'Día {tupla[0]}: {emoji[tupla[1]]} {tupla[1].capitalize()}') 



