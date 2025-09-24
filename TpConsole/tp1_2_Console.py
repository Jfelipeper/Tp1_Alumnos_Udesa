import random

print(" ="*30)
print("aqui vamos a ver cual es el estado del clima en base  al IMH")
print(" ="*30)
print("")
print("")


clim_est = ["soleado", "nublado", "lluvioso", "tormenta", "nevado"]


porcentaje = {"soleado" : [60, 30, 5, 3, 2] , 
              "nublado" : [40, 30,20, 5, 5], 
              "lluvioso" : [10, 30, 40, 15, 5], 
              "tormenta" : [5, 10,30,50, 5], 
              "nevado" : [ 5,20,20,10,45]
}


conteo ={                                # Contador de cuántos días pasa cada estado
    "soleado": 0,
    "nublado": 0,
    "lluvioso": 0,
    "tormenta": 0,
    "nevado": 0
}

clima = ("soleado")


simular = 500

dia_clima = 0

while dia_clima < simular:  
    clima = random.choices(clim_est, weights=porcentaje[clima])[0]
    conteo[clima] += 1
    dia_clima += 1



for estado in clim_est:                                # Muestro el resultado final que seria la cantidad y porcentaje de días por estado
    dia_diario = conteo[estado]
    pct = (dia_diario * 100) / simular
    print(f"Días {estado}s: {dia_diario} ({pct:.2f}%)")





maximo = max(conteo["soleado"], conteo["nublado"], conteo["lluvioso"], conteo["tormenta"], conteo["nevado"])        # Determino el clima más frecuente

if conteo["soleado"] == maximo:
    mas_frecuente = "soleado"
elif conteo["nublado"] == maximo:
    mas_frecuente = "nublado"
elif conteo["lluvioso"] == maximo:
    mas_frecuente = "lluvioso"
elif conteo["tormenta"] == maximo:
    mas_frecuente = "tormenta"
elif conteo["nevado"] == maximo:
    mas_frecuente = "nevado"

print("\n")

print(f"El clima más frecuente fue: {mas_frecuente}")

  









