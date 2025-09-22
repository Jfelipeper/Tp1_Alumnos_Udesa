from tp1_funciones_Taussig import simular_dias_cantidad

dias = 500
totales, porcentajes, clima_mas_frecuente, max_dias = simular_dias_cantidad(dias)

climas_ya_impresos = []

for i in range(len(totales)): # range(len(totales)) = 5
        for clima in totales: # agarro un valor inicial
            if clima not in climas_ya_impresos:
                clima_max = clima
                dias_max = totales[clima]
                break # salgo porque solo necesito uno
        for clima in totales: # compara todos los climas y se queda con la mayor cantidad de días.
            if clima not in climas_ya_impresos and totales[clima] > dias_max:
                clima_max = clima
                dias_max = totales[clima]
        print(f"Días {clima_max}: {dias_max} ({porcentajes[clima_max]:.2f}%)")
        climas_ya_impresos.append(clima_max) # Guarda en lista

print(f'El clima más frecuente fue: {clima_mas_frecuente.capitalize()} con {max_dias} días')