import random 

climas = ["soleado", "nublado", "lluvioso", "tormenta", "nevado"]

primer_estado = "soleado"

#Esta función devuelve devuelve 500 dependiendo de las probabilidades y arrancando siempre por soleado
from Tp1_Funciones_Gramajo import pronostico

fin_bucle = pronostico(primer_estado)

contar_climas = {} #diccionario vacío

#Si no esta el clima en el diccionario vacío, lo agrega, si ya está le suma uno
for clima in fin_bucle:   #para la cantidad de dias que pedí (500)
    if clima in contar_climas: 
        contar_climas[clima] += 1 #si hay uno además del que contó, ir sumando con el bucle
    else:
        contar_climas[clima] = 1 

#Del diccionario vacío, devuelve el clima y la cantidad de ese clima que se haya guardado en el dicc y luego saca el porcentaje de cada uno
for clima in climas: 
    cantidad  = contar_climas.get(clima, 0) #Si encuentra el clima, devuelve el valor, si no lo encuentra devuelve 0
    porcentaje = round(cantidad*100/500)
    print(f"{clima}: {cantidad} días, es decir, ({porcentaje:.2f}%) del total") 
    
mas_frecuente = max(contar_climas, key=contar_climas.get) #Devuelve el clima más frecuente
print(f"El clima más frecuente es {mas_frecuente}")