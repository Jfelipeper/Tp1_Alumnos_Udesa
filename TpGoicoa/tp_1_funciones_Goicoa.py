from random import choices
def simulacion(estado_inicial,periodo): 
    """Recibe el clima actual de Kokaua y la cantidad de dias a predecir, y retorna una lista con la simulacion con esa cantidad de dias"""
    estados = ['Soleado', 'Nublado', 'Lluvioso', 'Tormenta','Nevado']
    clima_llaves = {'Soleado': [60,30,5,3,2],'Nublado': [40,30,20,5,5],'Lluvioso': [10,30,40,15,5],'Tormenta': [5,10,30,30,5],'Nevado': [5,20,20,10,45]}
    predicciones = [] #Creo esta lista vacia en la que luego voy a ir agregando la condición de cada día 

    for numero_dia in range (1, periodo+1): #Mi variable estado_inicial toma el valor de los climas que van saliendo de aplicar 'choices()' a mi lista de condiciones posibles, llamada 'estados'
        if estado_inicial == 'Soleado':
                estado_inicial = choices(estados,weights= clima_llaves['Soleado']) [0]
        elif estado_inicial == 'Nublado':
                estado_inicial = choices(estados,weights= clima_llaves['Nublado']) [0]
        elif estado_inicial == 'Lluvioso':
                estado_inicial = choices(estados, weights= clima_llaves['Lluvioso']) [0]
        elif estado_inicial == 'Tormenta':
                estado_inicial = choices(estados, weights= clima_llaves['Tormenta']) [0]
        elif estado_inicial == 'Nevado':
                estado_inicial = choices(estados, weights= clima_llaves['Nevado']) [0]
        else:
                estado_inicial = 'El dato introducido no es valido'
        predicciones.append(estado_inicial)
           
    return predicciones