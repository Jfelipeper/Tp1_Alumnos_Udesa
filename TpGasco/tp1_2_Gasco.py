import random

# Cantidad de días a simular
time = 500
def clima_estable(time):
    '''Simula 'time' días de clima comenzando en 'Soleado' y cuenta cuántos
    días se pasa en cada estado.

    Parámetros
    ----------
    time : int
        Número de días a simular (debe ser entero positivo).

    Retorna
    -------
    
        Una tupla con los días en cada estado, en el orden:
        (Soleado, Nublado, Lluvioso, Tormenta, Nevado)
    '''
    #Guardamos los datos en un diccionario 
    database = {
        "Soleado":0,
        "Nublado":0,
        "Lluvioso":0,
        "Tormenta":0,
        "Nevado":0,
    }
    status = "Soleado"
    climas = ["Soleado","Nublado","Lluvioso","Tormenta","Nevado"]  
    #Bucle principal
    for i in range(time):
        if status == "Soleado":
            new_clima = random.choices(climas,weights=[60,30,5,3,2])
            database["Soleado"] += 1 
            status = new_clima[0]
        elif status == "Nublado":
            new_clima = random.choices(climas,weights=[40,30,20,5,5])
            database["Nublado"] += 1 
            status = new_clima[0]
        elif status == "Lluvioso":
            new_clima = random.choices(climas,weights=[10,30,40,15,5])
            database["Lluvioso"] += 1 
            status = new_clima[0]
        elif status == "Tormenta":
            new_clima = random.choices(climas,weights=[5,10,30,10,45])
            database["Tormenta"] += 1 
            status = new_clima[0]
        elif status == "Nevado":
            new_clima = random.choices(climas,weights=[5,20,20,10,45])
            database["Nevado"] += 1 
            status = new_clima[0]
    
    return database["Soleado"], database["Nublado"], database["Lluvioso"], database["Tormenta"],database["Nevado"]

dias_soleados,dias_nublados,dias_lluviosos,dias_tormenta,dias_nevados = clima_estable(time)

#Calculamos e imprimimos los promedios
print(f"Dias Soleados:{dias_soleados} ({round((dias_soleados/time)*100,2)}%)")
print(f"Dias Nublados:{dias_nublados} ({round((dias_nublados/time)*100,2)}%)")
print(f"Dias Lluviosos:{dias_lluviosos} ({round((dias_lluviosos/time)*100,2)}%)")
print(f"Dias Tormentas:{dias_tormenta} ({round((dias_tormenta/time)*100,2)}%)")
print(f"Dias Nevados:{dias_nevados} ({round((dias_nevados/time)*100,2)}%)")


