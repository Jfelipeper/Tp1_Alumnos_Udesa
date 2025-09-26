from tp1_funciones_FunesCosta import simulador_clima, contar_dias_por_clima, buscar_porcentaje #Importamos las funciones que vamos a utilizar

emoji= {'soleado':'☀️ ', 'nublado':'☁️ ', 'lluvioso':'🌧️ ', 'tormenta':'⛈️ ', 'nevado':'❄️ '}
cantidad_dias= 500
estado_inicial= 'soleado' #Le asignamos a las variables el valor que dice la consigna porque ya no hay que pedirselas al usuario y son necesarias para que luego sean utilizadas en las funciones
clima_simulado= simulador_clima(cantidad_dias, estado_inicial) #Simulamos el clima por 500 días
dicc_frecuencia= contar_dias_por_clima(clima_simulado) #Contamos cuantos días hubo por clima
dicc_frecuencia_final, clima, dias, porcentaje= buscar_porcentaje(cantidad_dias, dicc_frecuencia) #Obtenemos el porcentaje por clima y además encontramos los datos del clima más frecuente

for i in dicc_frecuencia_final: 
    print(f'Días {i}s: {dicc_frecuencia_final[i][0]} ({dicc_frecuencia_final[i][1]}%)') #Usamos el for para que la cantidad de días y el porcentaje de cada clima se impriman por separado
    
print(f'\nEl clima más frecuente fue: {emoji[clima]} {clima.capitalize()}')