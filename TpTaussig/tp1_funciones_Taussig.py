import random
clima = ['soleado', 'nublado', 'lluvioso', 'tormenta', 'nevado']

probabilidades = {'soleado': [60, 30, 5, 3, 2],
            'nublado': [40, 30, 20, 5, 5],
            'lluvioso': [10, 30, 40, 15, 5], 
            'tormenta': [5, 10, 30, 50, 5],
            'nevado': [5, 20, 20, 10, 45]}

# funciones usadas en tp1_1_Taussig

def siguiente_estado(actual):
    """
    Dado un clima actual, devuelve el siguiente estado según las probabilidades definidas en el diccionario 'probabilidades'.
    """
    pesos = probabilidades[actual]
    siguiente = random.choices(clima, weights=pesos, k=1)[0]
    return siguiente

def simulador_dias():
    """
    Dado un estado inicial y una cantidad de días ingresados por el usuario, devuelve una simulación de climas que comienza 
    en ese estado y dura la cantidad de días ingresados, siguiendo las probabilidades definidas en el diccionario 'probabilidades'.
    """
    estado_inicial = input('Ingrese el estado inicial: ').lower()
    dias = int(input('Ingrese cantidad de días a simular: '))
    
    if estado_inicial not in clima:
        print('El estado inicial debe ser uno de: soleado, nublado, lluvioso, tormenta, nevado.')
        return
    if dias <= 0:
        print('La cantidad de días debe ser un entero positivo')
        return
         
    print(f'Día 0: {estado_inicial.capitalize()}')
    estado_actual = estado_inicial
    for i in range(1, dias + 1):
        if dias > 0: 
            estado_actual = siguiente_estado(estado_actual)
            print(f'Día {i}: {estado_actual.capitalize()}')

# funciones usadas en tp1_2_Taussig

def simular_dias_cantidad(dias_simulacion):
    """
    Simula el clima durante un número de días determinados y devuelve porcentajes de aparición de cada estado
    y cual fué el clima mas frecuente. 
    """
    racha_soleado = 0
    racha_nublado = 0
    racha_lluvioso = 0
    racha_tormenta = 0
    racha_nevado = 0

    estado_actual = 'soleado' # Estado inicial

    for i in range(dias_simulacion):
        estado_siguiente = siguiente_estado(estado_actual)
        if estado_siguiente == 'soleado':
            racha_soleado += 1 
        elif estado_siguiente == 'nublado':
            racha_nublado += 1
        elif estado_siguiente == 'lluvioso':
            racha_lluvioso += 1
        elif estado_siguiente == 'tormenta':
            racha_tormenta += 1
        elif estado_siguiente == 'nevado':
            racha_nevado +=1

        estado_actual = estado_siguiente

    totales = {
        'soleado': racha_soleado,
        'nublado': racha_nublado,
        'lluvioso': racha_lluvioso,
        'tormenta': racha_tormenta,
        'nevado': racha_nevado
    }

    porcentaje_soleado = (racha_soleado / dias_simulacion) * 100
    porcentaje_nublado = (racha_nublado / dias_simulacion) * 100
    porcentaje_lluvioso = (racha_lluvioso / dias_simulacion) * 100
    porcentaje_tormenta = (racha_tormenta / dias_simulacion) * 100
    porcentaje_nevado = (racha_nevado / dias_simulacion) * 100

    porcentajes = {
        'soleado': porcentaje_soleado,
        'nublado': porcentaje_nublado,
        'lluvioso': porcentaje_lluvioso,
        'tormenta': porcentaje_tormenta,
        'nevado': porcentaje_nevado
    }

    clima_mas_frecuente = None # guarda que clima corresponde al nro mayor de días
    max_dias = 0
    for clima, dias in totales.items():
        if dias > max_dias:
            max_dias = dias # guardo el nuevo máximo
            clima_mas_frecuente = clima # guardo el nombre del clima

    return totales, porcentajes, clima_mas_frecuente, max_dias

# funciones usadas en tp1_3_Taussig

def simular_dias_new(dias_simulacion):
    """
    Genera una lista con la secuencia de climas simulados comenzando en 'soleado' y siguiendo las probabilidades definidas
    en el diccionario 'probabilidades'.
    """
    estado_actual = 'soleado'
    lista_estados = []
    for i in range(dias_simulacion):
        lista_estados.append(estado_actual)
        estado_actual = siguiente_estado(estado_actual)
    return lista_estados

def analizar_rachas(lista_estados):
    """
    Analiza una lista de climas y devuelve la racha mas larga, el clima correspondiente a esa racha 
    y la cantidad de rachas que duraron 4 o más días
    """
    racha_actual = 1
    racha_max = 1
    clima_racha_max = lista_estados[0] #asumo que la racha más larga empieza desde el 1er clima.
    contador_rachas_4 = 0

    for i in range(1, len(lista_estados)):
        if lista_estados[i] == lista_estados[i - 1]:
            racha_actual += 1 # si i y i-1 son iguales, sigo la racha.
        else: # es decir, lista_estados[i] != lista_estados[i - 1]
            if racha_actual > racha_max:
                racha_max = racha_actual
                clima_racha_max = lista_estados[i - 1]
            if racha_actual >= 4:
                contador_rachas_4 += 1
            racha_actual = 1 # reinicio para nueva racha
    return racha_max, clima_racha_max, contador_rachas_4
          
