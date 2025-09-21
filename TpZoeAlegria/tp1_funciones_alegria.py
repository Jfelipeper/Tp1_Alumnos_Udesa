
import random 

def pronostico (c_inicial):

    ''' La funcion pronstico recibe como argumento un string. En base a la entrada, 
    se condidera como clima inicial para calcular el clima siguiente en base a las probabilidades
    establecidas. 
    La funcion devuelve un str, que corresponde al clima siguiente simulado '''

    climas=('soleado', 'nublado', 'lluvioso', 'tormenta', 'nevado')
    if c_inicial=='soleado': 
        siguiente=random.choices(climas, weights=[60,30,5,3,2])
    elif c_inicial=='nublado': 
        siguiente=random.choices(climas, weights=[40,30,20,5,5])
    elif c_inicial=='lluvioso': 
        siguiente=random.choices(climas, weights=[10,30,40,15,5])
    elif c_inicial=='tormenta': 
        siguiente=random.choices(climas, weights=[5,10,30,50,5])
    elif c_inicial=='nevado': 
        siguiente=random.choices(climas, weights=[5,20,20,10,45])
    siguiente=siguiente[0]
    return siguiente

def indice (elemento, lista): 

    ''' La funcon indice recibe dos argumentos, un elemento (de cualquier tipo) y una lista. 
    Se busca el elemento ingresado en la lista dada. 
    La funcion retorna un entero, que corresponde al indice del elemento en la lista proporcionada. 
    Considera que el elemento existe, sino retorna NoneType '''

    for i in range (len(lista)):
        if lista[i] == elemento: 
            indice_encontrado=int(i)
            break
    return indice_encontrado

