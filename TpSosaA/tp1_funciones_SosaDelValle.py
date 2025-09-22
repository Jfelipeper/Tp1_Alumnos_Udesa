import random

#-----------------------------------------------------------------

# TP 1

def sistema(dias, estados=("☀️  Soleado", "☁️  Nublado", "🌧️  Lluvioso", "⛈️  Tormenta", "❄️  Nevado")):
    """Imprime Día 1 en adelante."""
    dia = 1
    while dia <= dias:
        estado = random.choices(estados, weights=(60, 30, 5, 3, 2))[0]
        print(f"Dia {dia}: {estado}")
        dia += 1
    return estado

#-----------------------------------------------------------------

# TP 2

def sistema2(dias):
    """Sistema de simulación de (dias)(en este caso 500) días de clima."""
    estados = ("soleado", "nublado", "lluvioso", "tormenta", "nevado")

    # Cantidad de veces de los estados cuando empieza (soleado siempre es el primero y por eso empieza en 1)

    cantidad_sol = 1
    cantidad_nub = 0
    cantidad_llu = 0
    cantidad_tor = 0
    cantidad_nev = 0

    # Días 1 en adelante hasta 500 

    for i in range(dias - 1):
        estado = random.choices(estados, weights=(60, 30, 5, 3, 2))[0]
        if estado == "soleado":
            cantidad_sol += 1
        elif estado == "nublado":
            cantidad_nub += 1
        elif estado == "lluvioso":
            cantidad_llu += 1
        elif estado == "tormenta":
            cantidad_tor += 1
        elif estado=="nevado":
            cantidad_nev += 1

    # Devuelve  las cantidades de cada uno de los estados 
    return cantidad_sol, cantidad_nub, cantidad_llu, cantidad_tor, cantidad_nev

#-----------------------------------------------------------------

# TP 3 

def sistema3(dias):
    """Usamos este sistema para encontrar las rachas para una simulacion que dura 10000 dias"""

    # Definimos estados posibles

    estados = ("soleado", "nublado", "lluvioso", "tormenta", "nevado")

    # Condiciones actuales en las que el dia 0 es soleado y entonces hay una racha de un dia de soleado y ninguna de mas de 4 mismos estados seguidos

    # En el dia 0, el estado actual es soleado 

    actual = "soleado"

    # El largo de la racha desde el dia 0 que es soleado, que sabemos que dura 1 dia y por ende la actual = 1

    lengtitud_actual = 1

    #La racha mas larga 

    max_largo = 1

    # A que estado le pertenece la racha maxima
    racha_maxima = "soleado"

    # Cantidad de rachas mayores a 4 
    rachas = 0

    # Esto es lo mismo que el sistema 2, pero despues analizamos los largos de las cadenas
    for i in range(dias - 1):
        r = random.choices(estados, weights=[60, 30, 5, 3, 2])[0]
        if r == actual:
            # Como es soleado, se le suma 1 de largo a la legntitud de la racha actual
            lengtitud_actual += 1
        else:
            # Esto es si pasa la racha mas larga
            if lengtitud_actual > max_largo:
                max_largo = lengtitud_actual
                racha_maxima = actual
            # Si la racha es mayor o igual a 4 estados seguidos, se le suma 1 al contador de rachas (mayores o iguales a 4)
            if lengtitud_actual >= 4:
                rachas += 1
            # Se arranca nueva racha y puede ser de cualquiera de las opciones ya que se usa actual = r y r es la variable que genera cualquiera de los estados
            actual = r 
            lengtitud_actual = 1

    # Se cierra la ultima racha 
    
    if lengtitud_actual > max_largo:
        max_largo = lengtitud_actual
        racha_maxima = actual
    if lengtitud_actual >= 4:
        rachas += 1

    return max_largo, racha_maxima, rachas










