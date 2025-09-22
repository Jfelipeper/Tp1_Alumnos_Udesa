import random
def estado_clima(climas):
    '''Recive una lista llamada climas que contiene los climas requerídos.
    Pide al usuario ingresar un clima inicial y cantidad de días y controla 
    que sean validos. Mediante una seleccion probabilistica crea una lista con 
    los días y los climas.
    Devuelve una lista con los días pedidos y su respectivo clima.'''

    while True:
        primer_clima=input('Cual es el primer clima? ')
        if primer_clima in climas:
            break
        else:
            print('El estado inicial debe ser uno de: soleado, nublado, lluvioso, tormenta, nevado')

    while True:
        if primer_clima in climas:
            dia=float(input('Por cuantos dias quieres que se ejecute el programa: '))
            if dia % 1 !=0:
                print('El numero elegido carece de sentido')
            elif dia<=0:
                print('El numero carece de sentido')
            else:
                dia=int(dia)
                break
    
    dias=0
    resultado_total=[]
    resultado=f'Día {dias}: {primer_clima}'
    resultado_total+=[resultado]
    while dias<dia:
        if primer_clima=='soleado':
            dias+=1
            resultado=f'Día {dias}: {random.choices(climas, weights=[60,30,5,3,2])[0]}'
        elif primer_clima=='nublado':
            dias+=1
            resultado=f'Día {dias}: {random.choices(climas, weights=[40,30,20,5,5])[0]}'
        elif primer_clima=='lluvioso':
            dias+=1
            resultado=f'Día {dias}: {random.choices(climas, weights=[10,30,40,15,5])[0]}'
        elif primer_clima=='tormenta':
            dias+=1
            resultado=f'Día {dias}: {random.choices(climas, weights=[5,10,30,50,5])[0]}'
        else:
            dias+=1
            resultado=f'Día {dias}: {random.choices(climas, weights=[5,20,20,10,45])[0]}'
        resultado_total+=[resultado]
        
    return resultado_total

def clima_estable():
    '''No recive nada.
    Aumenta por 500 días el valor de una de los climas del diccionario
    de manera probabilistica empezando desde soleado. Posteriormente 
    agrega cada uno de los climas del diccionario a una lista que muestra
    el clima(key), su cantidad de días(value) y el % de este en los 
    500 días. Finalmente calcula cual de todos fue el que más salió y
    agrega un f'str' con la cantidad de días y el clima que más salió.
    Devuelve una lista con los climas y su cantidad de días, más el clima que más salió'''
    clima=['soleado','nublado', 'lluvioso', 'tormenta', 'nevado']
    climas={'soleado':0, 'nublado':0, 'lluvioso':0, 'tormenta':0, 'nevado':0}
    tope=500
    inicial='soleado'
    contador=0
    while contador<tope:
        if inicial=='soleado':
            inicial=random.choices(clima, weights=[60,30,5,3,2])[0]
            contador+=1
            climas['soleado']+=1
        elif inicial=='nublado':
            inicial=random.choices(clima, weights=[40,30,20,5,5])[0]
            contador+=1
            climas['nublado']+=1
        elif inicial=='lluvioso':
            inicial=random.choices(clima, weights=[10,30,40,15,5])[0]
            contador+=1
            climas['lluvioso']+=1
        elif inicial=='tormenta':
            inicial=random.choices(clima, weights=[5,10,30,50,5])[0]
            contador+=1
            climas['tormenta']+=1
        else:
            inicial=random.choices(clima, weights=[5,20,20,10,45])[0]
            contador+=1
            climas['nevado']+=1
    
    valores=list(climas.values())
    
    devolucion=[]
    
    maximo=max(valores)
        
    for elemento in climas:
        resultado=f'Día {elemento}: {climas[elemento]} ({(climas[elemento]/tope)*100:.2f})'
        devolucion.append(resultado)
        
    
    
    if maximo == valores[0]:
        mayor_clima=f'El clima más frecuente fue: soleado'
    elif maximo == valores[1]:
        mayor_clima=f'El clima más frecuente fue: nublado'
    elif maximo == valores[2]:
        mayor_clima=f'El clima más frecuente fue: lluvioso'
    elif maximo == valores[3]:
        mayor_clima=f'El clima más frecuente fue: tormenta'
    else:
        mayor_clima=f'El clima más frecuente fue: nevado'
        
    devolucion.append(mayor_clima)
        
    return devolucion

def racha_dias():
    '''No recive nada.
    Se encarga de reproducir 10000 días y buscar todas las rachas de 3 días 
    que hayan habido y cual fue la más larga.
    Devuelve un f'str' con la racha más larga, a que clima corresponde y cuantas
    rachas de más de 3 días hubo'''

    clima=['soleado','nublado', 'lluvioso', 'tormenta', 'nevado']
    contador=0
    inicial='soleado'
    orden_climas=[]
    orden_climas.append(inicial)
    while contador<10000:
        if inicial=='soleado':
            contador+=1
            inicial=random.choices(clima, weights=[60,30,5,3,2])[0]
            orden_climas.append(inicial)
        elif inicial=='nublado':
            contador+=1
            inicial=random.choices(clima, weights=[40,30,20,5,5])[0]
            orden_climas.append(inicial)
        elif inicial=='lluvioso':
            contador+=1
            inicial=random.choices(clima, weights=[10,30,40,15,5])[0]
            orden_climas.append(inicial)
        elif inicial=='tormenta':
            contador+=1
            inicial=random.choices(clima, weights=[5,10,30,50,5])[0]
            orden_climas.append(inicial)
        else:
            contador+=1
            inicial=random.choices(clima, weights=[5,20,20,10,45])[0]
            orden_climas.append(inicial)
    
    orden0=0
    orden1=1
    dias=0
    racha4=[]
    elemento4=[]
    
    while True:
        if orden_climas[orden0]==orden_climas[orden1]:
            orden0+=1
            orden1+=1
            dias+=1
            
        else:
            if dias>=3:
                racha4.append(dias)
                elemento4.append(orden_climas[orden0])
            dias=0
            orden0+=1
            orden1+=1
        
        if orden1==10000:
            break
        else:
            continue

    maximo=max(racha4)

    for elemento in range(len(racha4)):
        if racha4[elemento]==maximo:
            ubicacion=elemento
    
    for elemento in elemento4:
        if elemento in elemento4[ubicacion]:
            super_elemento=elemento

    super_racha=len(racha4)

    devolucion=f'Racha más larga: {maximo} en {super_elemento} \nRachas de más de 3 días: {super_racha}'
    return devolucion