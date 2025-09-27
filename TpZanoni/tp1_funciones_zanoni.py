
import random

climas = ['soleado', 'nublado', 'lluvioso', 'tormenta', 'nevado']
probabilidades = {
    'soleado': [60, 30, 5, 3, 2],
    'nublado': [40, 30, 20, 5, 5],
    'lluvioso': [10,30,40,15,5],
    'tormenta': [5,10,30,50,5],
    'nevado': [5,20,20,10,45]
}
input_usuario = {
    'soleado': '☀ Soleado',
    'nublado': '🌤 Nublado',
    'lluvioso': '🌧 Lluvioso',
    'tormenta': '⛈ Tormenta',
    'nevado': '❄ Nevado'
}


#PARA EL EJERCICIO 1
def simulador_clima(e_inicial, d_inicial):
    """
    Simula el clima durante una cantidad definida de dias, a partir de lo que introduce el usuario.
    Parametros:
        e_inicial (str): Estado inicial del clima, debe ser uno de: 'soleado', 'nublado', 'lluvioso', 'tormenta', 'nevado'.
        d_inicial (int): Cantidad de días a simular, debe ser un entero positivo.
    Salida:
        Imprime en pantalla el estado del clima de cada día usando emojis representativos.
    """
    if d_inicial > 0:
        if e_inicial in climas:
            clima_act = e_inicial
            print(f'Día 0: {input_usuario[clima_act]}')
            for i in range(1, d_inicial +1):
                clima_act_us=random.choices(climas,weights=probabilidades[clima_act])[0]
                clima_act = clima_act_us
                print(f'Día {i}: {input_usuario[clima_act]}')
        else:
          print('El estado inicial debe ser uno de: soleado, nublado, lluvioso, tormenta, nevado.')  
    else:
        print('La cantidad de días debe ser un entero positivo.')



#PARA EL EJERCICIO 2
def cant_dias(dias_simular, clima_inicial):
    """ 
    Simula el clima durante una cantidad definida de dias.
    Parámetros:
        clima_inicial (str): Estado inicial del clima, debe ser uno de: 'soleado', 'nublado', 'lluvioso', 'tormenta', 'nevado'.
        dias_simular (int): Cantidad de días a simular, debe ser un entero positivo.
    Retorna:
        Diccionario con la cantidad de días de cada clima.
    """
    conteo = {
    'soleado': 0,
    'nublado': 0,
    'lluvioso': 0,
    'tormenta': 0,
    'nevado': 0
    }

    clima_sol = clima_inicial
    for i in range(dias_simular):
        conteo[clima_sol] += 1
        clima_sol = random.choices(climas, weights=probabilidades[clima_sol])[0]

    return conteo


def frec_ap(conteo, total_dias):
    """ 
    Calcula y muestra la frecuencia de cada clima a partir de un conteo de días.
    Parámetros:
        conteo (dict): Diccionario con la cantidad de días de cada clima.
        total_dias (int): Total de días simulados, usado para calcular porcentajes.
    Salida:
        Imprime en pantalla la cantidad de días, el porcentaje de cada clima y muestra cuál fue el clima más frecuente.
    """
    for clima in climas:
        cantidad = conteo[clima]
        porcentaje = (cantidad / total_dias) * 100
        print(f'Días {input_usuario[clima]}: {cantidad} ({"%.2f" % porcentaje}%)')

    clima_mas_frec = None
    max_cantidad = -1
    for clima in climas:
        if conteo[clima] > max_cantidad:
            max_cantidad = conteo[clima]
            clima_mas_frec = clima

    print(f'\nEl clima más frecuente fue: {input_usuario[clima_mas_frec]}')
    return clima_mas_frec



#PARA EL EJERCICIO 3
def simular_clima(dias_simular, clima_inicial):
    """
    Genera una lista con el clima durante una cantidad definida de días.
    Parámetros:
        clima_inicial (str): Estado inicial del clima, debe ser uno de: 'soleado', 'nublado', 'lluvioso', 'tormenta', 'nevado'.
        dias_simular (int): Cantidad de días a simular, debe ser un entero positivo.
    Retorna: 
        Lista con el clima de cada día, incluyendo el día inicial.
    """
    clima_act= clima_inicial
    lista_climas = [clima_act]
    for i in range(dias_simular):
        clima_act=random.choices(climas,weights=probabilidades[clima_act])[0]
        lista_climas.append(clima_act)
    return lista_climas


def racha_larga(dias_simular, clima_inicial):
    """
    Calcula y muestra la racha más larga de días consecutivos con el mismo clima.
    Parámetros: 
        clima_inicial (str): Estado inicial del clima, debe ser uno de: 'soleado', 'nublado', 'lluvioso', 'tormenta', 'nevado'.
        dias_simular (int): Cantidad de días a simular, debe ser un entero positivo.
    Salida:
        Imprime en pantalla la racha más larga indicando la cantidad de días y el clima.
    """
    racha = simular_clima(dias_simular, clima_inicial)
    contador = 1
    racha_max = 1
    clima_max = racha[0]

    for i in range(1, len(racha)):
        if racha[i] == racha[i-1]:
            contador +=1
        else:
            if contador > racha_max:
                racha_max = contador
                clima_max = racha[i-1]
            contador = 1
    if contador > racha_max:
        racha_max = contador
        clima_max = racha[-1]      
    
    print(f"Racha más larga: {racha_max} días de {input_usuario[clima_max]}")

def rachas_min4(dias_simular, clima_inicial):
    """
    Calcula y muestra la cantidad de rachas de al menos 4 días consecutivos del mismo clima.
    Parámetros:
        clima_inicial (str): Estado inicial del clima, debe ser uno de: 'soleado', 'nublado', 'lluvioso', 'tormenta', 'nevado'.
        dias_simular (int): Cantidad de días a simular, debe ser un entero positivo.
    Salida:
        Imprime en pantalla la cantidad de rachas que duraron 4 o más días.
    """
    racha = simular_clima(dias_simular, clima_inicial)
    contador = 1
    cant_rachas = 0
    for i in range(1, len(racha)):
        if racha[i] == racha[i-1]:
            contador +=1
        else:
            if contador >= 4:
                cant_rachas += 1
            contador = 1
    if contador >= 4:
        cant_rachas += 1
    
    print(f"Rachas de más de 3 días: {cant_rachas}")
