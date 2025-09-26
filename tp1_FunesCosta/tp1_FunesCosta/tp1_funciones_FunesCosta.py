import random #Importamos random
CLIMAS= ['soleado', 'nublado', 'lluvioso', 'tormenta', 'nevado']
dicc_probabilidades={
    'soleado':[60, 30, 5, 3, 2], 
    'nublado':[40, 30, 20, 5, 5], 
    'lluvioso':[10, 30, 40, 15, 5], 
    'tormenta': [5, 10, 30, 50, 5], 
    'nevado': [5, 20, 20, 10, 45]
    }

#Definimos las funciones 
def simulador_clima(cantidad_dias:int, estado_inicial:str) -> list:
    '''Recibe el estado inicial del clima y simula el clima durante la cantidad de días dado.
    Argumentos: 
    cantidad_dias -- cantidad de días que se simularán
    estado_inicial -- estado inicial del clima 
    Retorna: una lista de tuplas (dia, clima) que tienen el número de día y el estado simulado(día 0 no es simulado, es el estado inicial).
    '''
    pronostico=[(0, estado_inicial),] #Creamos una lista con el estado inicial (día 0) a la que se le va a agregar la cantidad de días simulados que elija el usuario con sus respectivos climas
    estado= estado_inicial #Le asignamos a estado el estado_inicial para comenzar el for usando las probabilidades correctas
    for dia_a_simular in range(1,cantidad_dias+1): #Le sumamos uno porque comienza en 1 no en 0
        estado_aleatorio= random.choices(CLIMAS, weights=dicc_probabilidades[estado])[0] #Simulamos el clima teniendo en cuenta las probabilidades
        estado= estado_aleatorio #Cambiamos el estado al ultimo estado simulado para que cuando vuelva al for el random use las probabilidades de este clima
        pronostico+=[(dia_a_simular, estado),] #Sumamos el dia y clima simulado al pronostico
    return pronostico

def contar_dias_por_clima(clima_simulado:list) -> dict:
    '''Recibe una lista con el clima simulado y cuenta la cantidad de días de cada tipo de clima.
    Argumentos:
    clima_simulado -- lista con tuplas con el número de día y su clima (dia, clima)
    Retorna: un diccionario con los climas como keys y la cantidad de días de cada uno como values.
    '''
    dicc_frecuencia={ #Creamos un diccionario vacío al que se le van a agregar la cantidad de veces que aparece cada uno en el clima simulado
    'soleado': 0, 
    'nublado': 0, 
    'lluvioso': 0, 
    'tormenta': 0, 
    'nevado': 0
    }
    for dia in clima_simulado: #Vemos día por día y sumamos 1 al value del clima correspondiente
        dicc_frecuencia[dia[1]]+=1
    return dicc_frecuencia

def buscar_porcentaje(cantidad_dias:int, dicc_frecuencia:dict) -> tuple:
    '''Recibe un diccionario con la cantidad de días de cada clima, calcula el porcentaje de cada clima y busca el clima predominante.
    Argumentos:
    cantidad_dias -- la cantidad de días simulados en total, de todos los climas
    dicc_frecuencia -- diccionario con los climas como keys y la cantidad de días de cada uno como values
    Retorna: diccionario de climas con la cantidad de días y sus porcentajesel, el clima predominante, la cantidad de días 
    que tuvo este y su porcentaje equivalente.
    '''
    porcentaje_mas_alto= 0 #Creamos esta variable =0 para que a medida que se ejecute la función buscar_porcentaje esta variable guarde el porcentaje más alto
    clima_predominante= '' #Creamos esta variable vacía para que a medida que se ejecute la función buscar_porcentaje esta variable guarde el clima más frecuente
    for clima in dicc_frecuencia: #Analizamos los distintos climas
        porcentaje= (dicc_frecuencia[clima]*100)/(cantidad_dias+1) #Calculamos el porcentaje. Al dividir sumamos 1 porque tenemos en cuenta los días simulados + el estado inicial
        dicc_frecuencia[clima]= (dicc_frecuencia[clima], round(porcentaje,2)) #Agregamos el porcentaje (redondeado a dos decimales) al value del clima analizado
        if dicc_frecuencia[clima][1]> porcentaje_mas_alto: #Comparamos porcentajes, para que siempre se guarde el mayor
            porcentaje_mas_alto= dicc_frecuencia[clima][1]
            clima_predominante=clima #Como el porcentaje mayor cambió tambien debemos cambiar el clima al que corresponde el nuevo porcentaje más alto
    return dicc_frecuencia, clima_predominante, dicc_frecuencia[clima_predominante][0],dicc_frecuencia[clima_predominante][1]  

def analizar_rachas(estado_inicial:str, clima_simulado:list) -> tuple:
    '''Recibe el estado inicial del clima y una lista con el clima simulado de los próximos días, busca la racha más larga de un mismo clima y cuenta cuantas rachas de al menos 4 días hubo en total.
    Argumentos: 
    estado_inicial -- estado inicial del clima
    clima_simulado -- lista con tuplas con el número de día y su clima (dia, clima)
    Retorna: una tupla con una lista con la información de la racha más larga [clima, dias de racha] y la cantidad de rachas de al menos 4 días en total.
    '''
    clima= estado_inicial
    dias_racha=0 #Creamos esta variable =0 para que el conteo de la racha se vaya guardando
    racha_max=['', 0] #Creamos una lista vacía, donde se va a guardar el clima con la racha máxima y los dias de racha
    rachas_mayores_3=0 # Creamos esta variable para que cada vez que se encuentre una racha mayor a 3 días se guarde
    for tupla in clima_simulado: #Analizamos cada día (tupla por tupla)
        if tupla[1] == clima: #Verificamos que el clima del día analizado sea igual que el anterior porque sí lo es la racha se agranda
            dias_racha+=1
            clima= tupla[1]
        else:
            if dias_racha > racha_max[1]: #Como el clima cambió, comparamos la nueva racha con la racha más larga
                racha_max= [clima, dias_racha] #Si es mayor, guardamos la nueva racha como la racha mas larga
            if dias_racha >= 4: #Vemos si tuvo al menos cuatro días
                rachas_mayores_3+=1
            dias_racha=1 #Reiniciamos el contador de racha (a 1 porque ya comenzó)
            clima= tupla[1]
    if dias_racha > racha_max[1]: #Para asegurarnos de que la ultima racha sea comparada con la racha más larga (Si el anteultimo día y el último son del mismo clima el for termina sin entrar al else por lo tanto la última racha no se compararía con la más larga si no fuera por este if)
        racha_max= [clima, dias_racha]
    if dias_racha >= 4: #Chequeamos si la ultima racha tuvo al menos cuatro días
        rachas_mayores_3+=1
    return racha_max, rachas_mayores_3
