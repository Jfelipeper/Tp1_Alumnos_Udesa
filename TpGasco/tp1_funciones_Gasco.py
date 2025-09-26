def simulador_de_clima(status,days):
    """
    Simula e imprime la evolución del clima durante 'days' días, partiendo de 'status'.

    Parámetros
    ----------
    status : str
        Estado inicial del clima. Debe ser uno de los valores en `climas`.
    days : int
        Cantidad de días a simular. Debe ser un entero positivo.
    """
    # Validación de la cantidad de días 
    if status not in climas:
        print("El estado inicial debe ser uno de: Soleado, Nublado, Lluvioso, Tormenta o Nevado")
    if isinstance(days,(int,float)) == False or days <=0:
        print("La cantidad de dias debe ser un entero positivo")
    else:  
        for i in range(days):  # Bucle principal de simulación (índice de día comienza en 0)

        
            if status == "Soleado":
                new_clima = random.choices(climas,weights=[60,30,5,3,2])
                print(f"Dia {i}:{emojis[new_clima[0]]}  {new_clima[0]}")    
                status = new_clima[0]
            elif status == "Nublado":
                new_clima = random.choices(climas,weights=[40,30,20,5,5])
                print(f"Dia {i}:{emojis[new_clima[0]]}  {new_clima[0]}")
                status = new_clima[0]
            elif status == "Lluvioso":
                new_clima = random.choices(climas,weights=[10,30,40,15,5])
                print(f"Dia {i}:{emojis[new_clima[0]]}  {new_clima[0]}")
                status = new_clima[0]
            elif status == "Tormenta":
                new_clima = random.choices(climas,weights=[5,10,30,10,45])
                print(f"Dia {i}:{emojis[new_clima[0]]}  {new_clima[0]}")
                status = new_clima[0]
            elif status == "Nevado":
                new_clima = random.choices(climas,weights=[5,20,20,10,45])
                print(f"Dia {i}:{emojis[new_clima[0]]}  {new_clima[0]}")
                status = new_clima[0]

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
    database = {
        "Soleado":0,
        "Nublado":0,
        "Lluvioso":0,
        "Tormenta":0,
        "Nevado":0,
    }
    status = "Soleado"
    climas = ["Soleado","Nublado","Lluvioso","Tormenta","Nevado"]  
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

def clima_estable(time):
    """
    Ejecuta la simulación y devuelve un diccionario con:
    - "racha_de_3": cantidad de rachas que alcanzaron al menos 3 días (se cuenta cuando llega a 3).
    - "mejor_racha": [estado, longitud] de la racha más larga observada.
    - "frequency_counter": [estado_actual, longitud_actual] de la racha en curso al momento de terminar.
    Las rachas se van actualizando a medida que el programa las esta generando. 
    """
    database ={
        "racha_de_3":0,
        "mejor_racha":["Soleado",1], # mejor racha vista hasta ahora
        "frequency_counter":["Soleado",1] # racha actual: (estado, longitud)
    }
    
    
    status = "Soleado"
    climas = ["Soleado","Nublado","Lluvioso","Tormenta","Nevado"]
    # Bucle principal de simulación 
    for i in range(time):
        
        if status == "Soleado":

            # Si el nuevo estado coincide con el de la racha actual, extendemos la racha    
            new_clima = random.choices(climas,weights=[60,30,5,3,2])
            if new_clima[0] == database["frequency_counter"][0]:
                database["frequency_counter"][1] += 1
                if database["frequency_counter"][1] == 3: # Si recién alcanzamos longitud 3, contamos una nueva racha de ≥3

                    database["racha_de_3"] += 1 
                # Si cambió el estado, antes de resetear, chequeamos si la racha actual fue la mejor
            elif new_clima[0] != database["frequency_counter"][0]:
                if database["frequency_counter"][1] > database["mejor_racha"][1]:
                    database["mejor_racha"][0] = database["frequency_counter"][0]   
                    database["mejor_racha"][1] = database["frequency_counter"][1]   

                # Reseteamos racha para el nuevo estado (se inicia desde 0 en tu lógica original)
                database["frequency_counter"][0] = new_clima[0]
                database["frequency_counter"][1] = 0 

            # Actualizamos estado para la próxima iteración
            status = new_clima[0]

        #Funciona de igual manera para el resto de climas.
        elif status == "Nublado":
            new_clima = random.choices(climas,weights=[40,30,20,5,5])
            if new_clima[0] == database["frequency_counter"][0]:
                database["frequency_counter"][1] += 1
                if database["frequency_counter"][1] == 3:
                    database["racha_de_3"] += 1 

            elif new_clima[0] != database["frequency_counter"][0]:

                if database["frequency_counter"][1] > database["mejor_racha"][1]:
                    database["mejor_racha"][0] = database["frequency_counter"][0]   
                    database["mejor_racha"][1] = database["frequency_counter"][1]     
                database["frequency_counter"][0] = new_clima[0]
                database["frequency_counter"][1] = 0 
            
            status = new_clima[0]

        elif status == "Lluvioso":
            new_clima = random.choices(climas,weights=[10,30,40,15,5])

            if new_clima[0] == database["frequency_counter"][0]:
                database["frequency_counter"][1] += 1
                if database["frequency_counter"][1] == 3:
                    database["racha_de_3"] += 1 

            elif new_clima[0] != database["frequency_counter"][0]:

                if database["frequency_counter"][1] > database["mejor_racha"][1]:
                    database["mejor_racha"][0] = database["frequency_counter"][0]   
                    database["mejor_racha"][1] = database["frequency_counter"][1]     
                database["frequency_counter"][0] = new_clima[0]
                database["frequency_counter"][1] = 0 
            status = new_clima[0]
        elif status == "Tormenta":

            new_clima = random.choices(climas,weights=[5,10,30,10,45])

            if new_clima[0] == database["frequency_counter"][0]:
                database["frequency_counter"][1] += 1
                if database["frequency_counter"][1] == 3:
                    database["racha_de_3"] += 1 

            elif new_clima[0] != database["frequency_counter"][0]:

                if database["frequency_counter"][1] > database["mejor_racha"][1]:

                    database["mejor_racha"][0] = database["frequency_counter"][0]   
                    database["mejor_racha"][1] = database["frequency_counter"][1]     
                database["frequency_counter"][0] = new_clima[0]
                database["frequency_counter"][1] = 0 
            status = new_clima[0]
        elif status == "Nevado":

            new_clima = random.choices(climas,weights=[5,20,20,10,45])

            if new_clima[0] == database["frequency_counter"][0]:
                database["frequency_counter"][1] += 1
                if database["frequency_counter"][1] == 3:
                    database["racha_de_3"] += 1 

            elif new_clima[0] != database["frequency_counter"][0]:

                if database["frequency_counter"][1] > database["mejor_racha"][1]:
                    database["mejor_racha"][0] = database["frequency_counter"][0]   
                    database["mejor_racha"][1] = database["frequency_counter"][1]     
                database["frequency_counter"][0] = new_clima[0]
                database["frequency_counter"][1] = 0 
            status = new_clima[0]

    return database