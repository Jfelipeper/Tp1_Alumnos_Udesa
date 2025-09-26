from data import climas, emojis_climas
from tp1_funciones_Bugna import simulador_climas

def ej_2 ():
    estado_inicial = "soleado"
    dias = int(input("Ingrese la cantidad de dias que quieras simular: "))
    while(dias <= 0 ):
        print("La cantidad de dias ingresado debe ser un entero positivo")
        if(dias <= 0):
            dias = int(input("Ingrese nuevamente la cantidad de dias que quieras simular: "))
    simulacion = simulador_climas(estado_inicial, dias)
    soleado = nublado = lluvioso = tormenta = nevado = 0
    porcentaje_lluvioso=porcentaje_nevado=porcentaje_nublado=porcentaje_soleado=porcentaje_tormenta=0
    #Recorre todos los climas que pasen en la simulacion y dependiendo el clima que pase le va sumando 1 al clima que aparezca y luego calculamos el porcentaje del total de dias de esos climas
    for clima in simulacion:
        if (clima == "soleado"):
            soleado +=1
            porcentaje_soleado = (soleado*100)/dias
        elif(clima == "nublado"):
            nublado +=1
            porcentaje_nublado = (nublado*100)/dias
        elif(clima == "lluvioso"):
            lluvioso +=1
            porcentaje_lluvioso = (lluvioso*100)/dias
        elif(clima == "tormenta"):
            tormenta +=1
            porcentaje_tormenta = (tormenta*100)/dias
        else:
            nevado +=1
            porcentaje_nevado = (nevado*100)/dias
    print(f"Dias Soleados {emojis_climas["soleado"]}  = {soleado} ({porcentaje_soleado}%) \nDias Nublados {emojis_climas["nublado"]}  = {nublado} ({porcentaje_nublado}%) \nDias Lluviosos {emojis_climas["lluvioso"]}  = {lluvioso} ({porcentaje_lluvioso}%) \nDias Tormentosos {emojis_climas["tormenta"]}  = {tormenta} ({porcentaje_tormenta}%) \nDias Nevados {emojis_climas["nevado"]}  = {nevado} ({porcentaje_nevado}%)") 
    if(soleado > (nublado and lluvioso and tormenta and nevado)):
        print(f"El climas mas frecuente fue: {climas[0]} {emojis_climas["soleado"]}")
    elif(nublado > (soleado and lluvioso and tormenta and nevado)):
        print(f"El climas mas frecuente fue: {climas[1]} {emojis_climas["nublado"]}")
    elif(lluvioso > (nublado and soleado and tormenta and nevado)):
        print(f"El climas mas frecuente fue: {climas[2]} {emojis_climas["lluvioso"]}")
    elif(tormenta > (nublado and lluvioso and soleado and nevado)):
        print(f"El climas mas frecuente fue: {climas[3]} {emojis_climas["tormenta"]}")
    else:
        print(f"El climas mas frecuente fue: {climas[4]} {emojis_climas["nevado"]}")
ej_2()
