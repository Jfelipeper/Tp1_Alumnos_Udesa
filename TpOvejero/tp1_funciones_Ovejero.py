import random
def simular(estado:str,n:int)-> list | str:
    '''
    Simula el clima, partiendo de un estado inicial según una matriz  
    probabilistica, la cantidad de días que el usuario indica
    
    Args:
    -estado: Estado inicial de ejecución. (Posibles estados: ["soleado","nublado","lluvioso",
    "tormenta","nevado"])        
    -n: cantidad de simulaciones a realizar. (Entero mayor a 0)
    
    Returns: 
    -total_estados: Lista que contiene cada día simulado concatenado y ordenados
    de izquierda a derecha por simulación
    -str: string que indica que el input 'estado' no forma parte de los posibles
    valores a usar
    
    Ejemplos:
    simular("nevado",3)
    [nevado,tormenta,nevado]
    '''
    #Creo un diccionario que contendrá como claves los posibles estados, y cada clave tendrá
    #asociada a su valor una lista con los respectivos 'weights' probabilísticos que usaré
    #más adelante con random.choices
    matriz_estados = {"soleado": [60,30,5,3,2], 
                "nublado":   [40,30,20,5,5],
                "lluvioso":  [10,30,40,15,5],
                "tormenta":  [5,10,30,50,5],
                "nevado":    [5,20,20,10,45]}
    if estado in list(matriz_estados.keys()):
        total_estados = [estado]
        dias = 0
        while dias < n:
            #redefino mi variable estado con el while, el random.choices seleccionará
            #un posible estado en base a una lista de estados generadas con las claves 
            #de mi diccionario, el orden se respeta para que también correspondan sus
            #weights 
            estado = random.choices(list(matriz_estados.keys()),weights = matriz_estados[estado])[0]
            total_estados.append(estado)
            dias += 1
        return total_estados
    else: 
        return "El estado inicial debe ser uno de: soleado, nublado, lluvioso, tormenta, nevado"
#-------------------------------------------------------------------------------------------------------

def obtener_cantidades(total_estados:list[str])-> dict[str:int]:
    '''
    Cuenta la cantidad de 5 tipos de estados, almacenados en una lista, y 
    la añade en un diccionario con su estado correspondiente
    
    Args:
    -total_estados: Lista con estados, cada uno como elemento adicional
    
    Returns:
    -cantidad_dias: Diccionario con estados y su cantidad correspondiente 
    de repeticiones
    '''
    cantidad_dias = {"soleado": 0,
                    "nublado": 0,
                    "lluvioso": 0,
                    "tormenta": 0,
                    "nevado": 0}
    for dia in total_estados:
        if dia in cantidad_dias:
            cantidad_dias[dia] += 1
    return cantidad_dias
#-----------------------------------------------------------------------------------------------

def calcular_frecuencia(cantidad_dias:dict[str:int])-> str | tuple:
    '''
    Calcula el estado con mayor frecuencia en base a los valores de un diccionario,

    Args:
    -cantidad_dias: diccionario que contiene estados y su cantidad respectiva de repeticiones

    Returns:
    -Devuelve un string del estado más frecuente.
    en caso de haber 2 estados empatados en frecuencia devuelve ambos en tipo tuple.
    '''
    frecuencia = 0
    estado_frecuente = [[]]
    for estado in cantidad_dias.keys():
        if cantidad_dias[estado] > frecuencia: #reescribo en función del tamaño del valor
            frecuencia = cantidad_dias[estado]
            estado_frecuente[0] = [estado, frecuencia]
        elif cantidad_dias[estado] == frecuencia: #en caso de que 2 estados empaten en frecuencia
            estado_frecuente.append([estado, frecuencia])
    if len(estado_frecuente) == 2:
        return estado_frecuente[0][0],estado_frecuente[1][0]
    else:
        return estado_frecuente[0][0]    
#-----------------------------------------------------------------------------------------------

def obtener_porcentaje(cantidad_dias:dict[str:int])-> dict[str:list]:
    '''
    Calcula y devuelve el porcentaje de la cantidad de días de cada estado, en proporción 
    a la suma de valores de un diccionario

    Args: 
    cantidad_dias: diccionario que almacena estados climáticos y la 
    cantidad de días correspondiente a cada uno

    Return:
    -cantidad_dias: diccionario de entrada reescrito con el porcentaje del valor
    en proporcion a la suma total de valores del input
    '''
    total_dias = sum(cantidad_dias.values())
    for d in cantidad_dias:
        dias = cantidad_dias[d]
        porcentaje = (f"{round(((cantidad_dias[d]/total_dias) * 100),2)} %")
        cantidad_dias[d] = [dias, porcentaje]
    return cantidad_dias
#---------------------------------------------------------------------------------------------

def max_racha(total_estados:list[str])-> tuple[str,int] | tuple[tuple:int]:
    '''
    Calcula la racha más larga de estados

    Args:
    -total_estados: Lista que contiene estados como elementos de la misma

    Returns:
    -tuple que contiene el estado y la longitud de la racha, dicha tupla puede almacenar
    otra tupla con 2 frecuencias empatadas, y un entero de su longitud
    '''
    conteo_rachas = {"soleado": 0,
                    "nublado": 0,
                    "lluvioso": 0,
                    "tormenta": 0,
                    "nevado": 0}
    racha_actual = 1
    for i,estado in enumerate(total_estados[:-1]):
        if total_estados[i] == total_estados[i+1]:
            racha_actual += 1
        else:
            racha_actual = 1 
        if racha_actual > conteo_rachas[estado]:
            conteo_rachas[estado] = racha_actual
    racha_estado = calcular_frecuencia(conteo_rachas)
    #reutilizo la función calcular_frecuencias ya que me permite encontrar la clave de
    #un máximo del diccionario "conteo_rachas"
    racha_longitud = max(list(conteo_rachas.values()))
    return racha_estado,racha_longitud 
#-----------------------------------------------------------------------------------------------

def cantidad_rachas(total_estado:list)-> int:
    ''' 
    Cuenta la cantidad de rachas de 4 o más días en que se repite un estado,
    según una lista con los mismos

    Args:
    -total_estados: Lista que contiene estados como elementos de la misma

    Returns:
    -conteo_rachas: entero que describe la cantidad de rachas de 4 o más días
    '''
    racha_actual = 1
    conteo_rachas = 0
    for i,estado in enumerate(total_estado[:-1]): #desenpaqueto para indexar
        if estado == total_estado[i+1]:
            racha_actual += 1
        else:
            if racha_actual > 3: #ante de reiniciar el contador de rachas verifico si es mayor a 3
                conteo_rachas += 1 
            racha_actual = 1
    if racha_actual > 3: 
        conteo_rachas += 1
        #utilizo esta condicion en caso de que mi lista termine en racha, ya que no existirá
        #iteración "i+1" 
    return conteo_rachas
