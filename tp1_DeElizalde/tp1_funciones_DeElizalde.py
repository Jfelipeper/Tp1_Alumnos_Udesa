import random       # Necesito esta libreria para poder hacer el uso de las funciones random

def full_pronostico():  # Esta funcion cumple el proposito de generar un pronostico dado el clima incial y la cantidad de dias que se necesita calcular
    '''
    Esta funcion genera un diccionario en el que se encuentra un pronostico de los dias que se simulan con su condicion correspondiente

    La funcion solicita dos inputs del usuario:
        - La condicion de clima inicial, que solo puede ser una predeterminada
        - La cantidad de dias a simular, que tiene que ser un numero entero positivo
    
    A partir de esto, se usa la funcion "clima_random" para ir generando un clima nuevo con sus respectivas probabilidades y las mete a un diccionario

    Esta funcion devuelve:
        - Una lista de strings que comienza con la condicion inicial y sifue con los climas pornosticados

    '''
    climas_validos = ["soleado", "nublado", "lluvioso", "tormenta", "nevado"]   # Esta es una tupla de inputs que el usuario deberia ingresar

    presente = input("Ingrese el clima inicial: ").lower()      # Esta seccion revisa que el input del usuario del clima inicial sea una condicion valida par asignarlo como el clima inicial
    while presente not in climas_validos:
        print("El estado inicial debe ser uno de: soleado, nublado, lluvioso, tormenta, nevado")
        presente = input("Ingrese el clima inicial: ").lower()

    dias = int(input("Ingrese la cantidad de dias a predecir: "))   # Esta seccion hace lo mismo pero con la cantidad de dias, fijandose que la canatidad de dias sea un numero entero positivo
    while dias < 1:
        print("La cantidad de días debe ser un número entero positivo.")
        dias = int(input("Ingrese la cantidad de dias a predecir: "))

    if presente == "soleado":           
        presente = "☀️  Soleado"
    elif presente == "nublado":
        presente = "☁️  Nublado"
    elif presente == "lluvioso":        # Esta columna simplemente cambia el nombre de la variable para poder acomodar el uso de emojis
        presente = "🌧️  Lluvioso"
    elif presente == "tormenta":
        presente = "⛈️  Tormenta"
    elif presente == "nevado":
        presente = "❄️  Nevado"

    inicial = presente         # Esta varibable esta aca para simplemente anotar cual es la condicion inicial

    pronostico = [inicial]     # Aca se crea el diccionario de climas calculados, con el primer valor siendo la condicion inicial para tener el "Dia 0"

    for i in range(dias):       
        presente = clima_random(presente)       # Este ciclo va ejecutando la funcion que calcula el clima random dadas las probabilidades y lo va agregando al diccionario de climas
        pronostico.append(presente)

    return pronostico           # Aca devuelvo el diccionario que se pide compuesto por todos los climas

def clima_random(presente):    # Esta funcion cumple el proposito de ir cambiando el clima dependiendo de las probabilidades, usando la variable de presente que inputea el usuario
    '''
    Esta funcion calcula en base de probabilidades el siguiente clima pronosticado

    Toma como input:
        - La variable presente, que es la condicion de clima actual del for de la funcion anterior

    Despues calcula en base a las probabilidades de esa condicion dada el siguiente clima

    Luego devuelve:
        - La variable return que toma el valor del clima nuevo pronosticado en formato str
    '''
    probabilidades = {
    "☀️  Soleado": [60, 30, 5, 3, 2],
    "☁️  Nublado":[40, 30, 20, 5, 5],
    "🌧️  Lluvioso":[10, 30, 40, 15, 5],     # Este diccionario contiene las probabilidades (guardadas en tuplas) de cambios para cada condicion respectiva
    "⛈️  Tormenta":[5, 10, 30, 50, 5],
    "❄️  Nevado":[5, 20, 20, 10, 45]
}

    clima = {1:"☀️  Soleado",
        2:"☁️  Nublado", 
        3:"🌧️  Lluvioso",           # Este diccionario cumple el proposito de asignar los 5 numeros posibles del random a cada clima respectivo
        4:"⛈️  Tormenta", 
        5:"❄️  Nevado"}



    l = [1, 2, 3, 4, 5] # Esta tupla guarda 5 numeros para poder usar en el random, que tambien representan las probabilidades del diccionario de encima
    resultado = clima[random.choices(l, weights=probabilidades[presente])[0]]   # Esta linea toma el valor presente (el clima establecido) y saca los pesos respectivos al meterlo en el diccionario
                                                                                # despues selecciona un numero random dentro de l en base a esos pesos. Y finalmente le asgina a la variable resultado el clima
                                                                                # respectivo al numero seleccionado. El [0] al final es necesario para tomar los numeros de las probabilidades sin otro caracter 
                                                                                # que interfiera con la operacion
    
    return resultado    # La funcion devuelve este resultado que despues se le asigna a presente y por lo tanto poder repetir esta funcion las veces necesarias

def rachas(pronostico):     # Esta funcion calcula las rachas de dias pedidas por el ejercicio
    '''
    Esta funcion calcula todas las rachas que se buscan, la mas larga y las que son mayores a 3

    Toma como input:
        - La lista de climas ya pronosticados, generada por la funcion full_pronostico

    Despues calcula la racha actual, que lo hace al comparar el valor actual de la lista con el anterior y fijandose si son iguales, y si es verdad sumar uno a la racha actual
    Va comparando la raacha actual con la racha maxima y si esta es mayor le asigna el valor de la racha actual a la racha maxima, y tambien  guarda la condicion de este clima como clima_max
    Al mismo tiempo revisa si la racha actual es igual a 4, para ver si esta es mayor a 3 (No uso un > 3 porque podria contar la misma racha varias veces)
    Y si los valores de la lista de pronosticos no son iguales resetea la racha actual a 1

    Luego devuelve:
        - racha_max: Un valor numerico de la racha maxima
        - clima_max: La condicion climatica de la racha maxima
        - rachas_3: La cantidad de rachas que superaron 3 de longitud

    '''

    racha_max = 1
    racha_act = 1       # Esta columna establece valores arbitrarios para las variables que voy a usar
    rachas_3 = 0
    clima_max = pronostico[0]

    for i in range(1, len(pronostico)):         # Este ciclo va a pasar por todos los items del diccionario de climas para calcular las rachas
        if pronostico[i] == pronostico[i-1]:    
            racha_act += 1                      # Este if va revisando si el item de la lista es igual al anterior y si si va sumando 1 a la reacha actual

            if racha_act > racha_max:           # Al mismo tiemmpo, dentro del if, se va revisando si la racha actual es mayor que otra racha calculada, y si se logra esto s eguarda el numeor de la racha y el clima en el momento
                racha_max = racha_act
                clima_max = pronostico[i]

            if racha_act == 4:                  # Tambien vamos viendo cuando la racha supera a 3, es importante notar que solo tomamos que sea igual a 4 y no mayor a 3 porque sino contaria la misma racha varias veces
                rachas_3 += 1
        else:
            racha_act = 1                       # Y este else hace que cuando dos items del diccionario consecutivos no sean iguales, resetee la racha
    
    return racha_max, clima_max, rachas_3       # Aca devolvemos los valores de las rachas que necesitamos saber