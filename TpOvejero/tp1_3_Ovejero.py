from tp1_funciones_Ovejero import*

#recibe como argumento (estado,n) siendo n la cantidad de días a simular
total_estados = simular("soleado",10000)

#max_racha puede devolver una tupla que en su primer elemento contiene una tupla con 2 estados
#empatados, por lo tanto planteo el condicional que verifica que return obtuve:
if type(max_racha(total_estados)[0]) != tuple:
    print(f"Racha más larga: {max_racha(total_estados)[1]} días de {max_racha(total_estados)[0]}")
else:
    print(f"Rachas más largas: \n{max_racha(total_estados)[1]} días de {max_racha(total_estados)[0][0]}")
    print(f"{max_racha(total_estados)[1]} días de {max_racha(total_estados)[0][1]}")
print(f"La cantidad de rachas de más de 3 días es: {cantidad_rachas(total_estados)}")