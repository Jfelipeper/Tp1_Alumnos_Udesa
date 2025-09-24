import random 

climas = ["soleado", "nublado", "lluvioso", "tormenta", "nevado"]

primer_estado = "soleado"

#Esta función devuelve devuelve 10000 dependiendo de las probabilidades y arrancando siempre por soleado
from Tp1_Funciones_Gramajo import pronostico2

fin_bucle = pronostico2(primer_estado)

clima_inicial= "soleado"
racha=0
clima= ""
racha_mas_larga = 0
clima_racha_mas_larga = ""
racha_4_dias = 0 
racha_4_dias = 0

#A medida que da vueltas el for, se va viendo si el siguiente clima es igual al anterior para ver las rachas
for clima_racha in fin_bucle:
    if clima_racha == clima_inicial:
        racha += 1
    else:
        if racha > 3:
            racha_4_dias +=1 #Se fija si las rachas son de más de 4 días y las va sumando 
        if racha > racha_mas_larga: #Si la racha es mayor, la racha más larga pasa a ser la racha 
            racha_mas_larga = racha
            clima_racha_mas_larga = clima_inicial #El clima de la racha mas larga pasa a ser el clima inicial, para que empiece el bucle desde ahí
        racha=1
        clima_inicial = clima_racha 
#Devuelve la racha ma´s larga y cuantas rachas de más de 4 días hay

print(f"La racha más larga es: {racha_mas_larga} días de clima {clima_racha_mas_larga}")
print(f"Hay {racha_4_dias} rachas de más de tres días")