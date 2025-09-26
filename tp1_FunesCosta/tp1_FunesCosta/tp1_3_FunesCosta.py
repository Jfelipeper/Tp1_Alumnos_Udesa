from tp1_funciones_FunesCosta import simulador_clima, analizar_rachas #Importamos las funciones que vamos a utilizar

emoji= {'soleado':'☀️ ', 'nublado':'☁️ ', 'lluvioso':'🌧️ ', 'tormenta':'⛈️ ', 'nevado':'❄️ '}
cantidad_dias= 10000
estado_inicial= 'soleado' #Le asignamos a las variables el valor que dice la consigna porque ya no hay que pedirselas al usuario y son necesarias para que luego sean utilizadas en las funciones
clima_simulado= simulador_clima(cantidad_dias, estado_inicial) #Simulamos el clima por 10000 días
racha_max, rachas_mayores_3= analizar_rachas(estado_inicial, clima_simulado) #Obtenemos la racha más larga y la cantidad de rachas de más de tres días

print(f'Racha más larga: {racha_max[1]} días de {emoji[racha_max[0]]} {racha_max[0].capitalize()}')
print('Rachas de más de 3 días:', rachas_mayores_3)
