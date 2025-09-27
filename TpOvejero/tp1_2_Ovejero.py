from tp1_funciones_Ovejero import*

#recibe como argumento (estado,n) siendo n la cantidad de días a simular
total_estados = simular("soleado",500)

cantidad_dias = obtener_cantidades(total_estados)

estado_frecuente = calcular_frecuencia(cantidad_dias)

resultado = obtener_porcentaje(cantidad_dias)
for clima, racha in resultado.items():
    print(f'días {clima}s: {racha[0]} ({racha[1]}) ')

#como calcular_frecuencia me puede darme 2 estados empatados
#planteo dicha condición:
if len(estado_frecuente) == 2:
    print(f"El clima más frecuente fue: {estado_frecuente[0]} y {estado_frecuente[1]}")
else:
    print(f"\nEl clima más frecuente fue: {estado_frecuente}")