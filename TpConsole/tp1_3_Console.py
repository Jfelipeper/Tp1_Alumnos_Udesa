import random

clim_est = ["soleado", "nublado", "lluvioso", "tormenta", "nevado"]

porcentaje = {
    "soleado":  [60, 30, 5, 3, 2],
    "nublado":  [40, 30, 20, 5, 5],
    "lluvioso": [10, 30, 40, 15, 5],
    "tormenta": [5, 10, 30, 50, 5],
    "nevado":   [5, 20, 20, 10, 45],
}

DIAS = 10000
estado_inicial = "soleado"
registro_climas = [estado_inicial] #hacemos una lista
contador_dias = 1


while contador_dias < DIAS:
    clima_dia_anterior = registro_climas[-1] #toma el clima de dia anterior que saco(nos da el dia mas reciente)
    clima_siguiente = random.choices(clim_est, weights=porcentaje[clima_dia_anterior], k=1)[0] #con el k lo que hacemos es pedir solo una eleccion
    registro_climas = registro_climas + [clima_siguiente] #agrego el nuevo dia a la lista
    contador_dias += 1



duracion_racha_mas_larga = 1
clima_racha_mas_larga = registro_climas[0]
cantidad_rachas_mayores_4 = 0

clima_en_racha = registro_climas[0]
duracion_racha_actual = 1



posicion_dia = 1


while posicion_dia < len(registro_climas): #ver cuantos dias pasaron, usamos  len para ver la cantidad de dias simulados con la lista
    if registro_climas[posicion_dia] == clima_en_racha:
        duracion_racha_actual += 1
    else:
        if clima_en_racha == "soleado":
            if duracion_racha_actual > duracion_racha_mas_larga:
                duracion_racha_mas_larga = duracion_racha_actual
                clima_racha_mas_larga = "soleado"
            if duracion_racha_actual >= 4:
                cantidad_rachas_mayores_4 += 1

        elif clima_en_racha == "nublado":
            if duracion_racha_actual > duracion_racha_mas_larga:
                duracion_racha_mas_larga = duracion_racha_actual
                clima_racha_mas_larga = "nublado"
            if duracion_racha_actual >= 4:
                cantidad_rachas_mayores_4 += 1

        elif clima_en_racha == "lluvioso":
            if duracion_racha_actual > duracion_racha_mas_larga:
                duracion_racha_mas_larga = duracion_racha_actual
                clima_racha_mas_larga = "lluvioso"
            if duracion_racha_actual >= 4:
                cantidad_rachas_mayores_4 += 1

        elif clima_en_racha == "tormenta":
            if duracion_racha_actual > duracion_racha_mas_larga:
                duracion_racha_mas_larga = duracion_racha_actual
                clima_racha_mas_larga = "tormenta"
            if duracion_racha_actual >= 4:
                cantidad_rachas_mayores_4 += 1

        elif clima_en_racha == "nevado":
            if duracion_racha_actual > duracion_racha_mas_larga:
                duracion_racha_mas_larga = duracion_racha_actual
                clima_racha_mas_larga = "nevado"
            if duracion_racha_actual >= 4:
                cantidad_rachas_mayores_4 += 1

        clima_en_racha = registro_climas[posicion_dia]
        duracion_racha_actual = 1

    posicion_dia += 1



#copio lo mismo que esta dentro del whiele
#creamos un nuevo bloque igual que el anterior con ifs para cerrar el bucle
#porque cuando llegamos al final de la lista no hay un proxio dia
#eso hace que la racha quede abierta y con estos ifs hacemos el ultimo pasado y cerrado


if clima_en_racha == "soleado":
    if duracion_racha_actual > duracion_racha_mas_larga:
        duracion_racha_mas_larga = duracion_racha_actual
        clima_racha_mas_larga = "soleado"
    if duracion_racha_actual >= 4:
        cantidad_rachas_mayores_4 += 1

elif clima_en_racha == "nublado":
    if duracion_racha_actual > duracion_racha_mas_larga:
        duracion_racha_mas_larga = duracion_racha_actual
        clima_racha_mas_larga = "nublado"
    if duracion_racha_actual >= 4:
        cantidad_rachas_mayores_4 += 1

elif clima_en_racha == "lluvioso":
    if duracion_racha_actual > duracion_racha_mas_larga:
        duracion_racha_mas_larga = duracion_racha_actual
        clima_racha_mas_larga = "lluvioso"
    if duracion_racha_actual >= 4:
        cantidad_rachas_mayores_4 += 1

elif clima_en_racha == "tormenta":
    if duracion_racha_actual > duracion_racha_mas_larga:
        duracion_racha_mas_larga = duracion_racha_actual
        clima_racha_mas_larga = "tormenta"
    if duracion_racha_actual >= 4:
        cantidad_rachas_mayores_4 += 1

elif clima_en_racha == "nevado":
    if duracion_racha_actual > duracion_racha_mas_larga:
        duracion_racha_mas_larga = duracion_racha_actual
        clima_racha_mas_larga = "nevado"
    if duracion_racha_actual >= 4:
        cantidad_rachas_mayores_4 += 1

print(f"Racha más larga: {duracion_racha_mas_larga} días de {clima_racha_mas_larga} ")
print(f"Rachas de más de 3 días: {cantidad_rachas_mayores_4}")


#se que esta manera de hacer el ejercicio es muy cuentosa pero es la manera la cual mas entiendo y se hacer




































