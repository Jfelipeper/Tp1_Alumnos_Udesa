from tp1_funciones_alegria import pronostico, indice

print('\nSIMULACION POR 10.000 DIAS!')
climas=('soleado', 'nublado', 'lluvioso', 'tormenta', 'nevado')

racha=[0,0,0,0,0] #se inician las rachas en 0; el indexado de las rachas es correspondiente al indexado de la tupla de climas 

seguidos=0 #esta variable sera un contador de la cantidad de dias seguidos del clima evaluado 
anterior='soleado' #se arranca considerando el estado soleado
mayor_4=0 #contador de las rachas mayores o iguales a 4 dias 

for x in range (10000):
    
    clima_actual=pronostico(anterior)
    
    #compruebo si el clima siguiente es igual al anterior 
    if clima_actual==anterior: 
        seguidos+=1 #se le suma uno a la racha del clima en cuestion
    
    #si se rompe la racha:
    else:  
        anterior=clima_actual #cambiamos el clima del que se evalua la racha

        #si la racha que se rompio era mayor o igual a 4, se suma al contador 
        if seguidos>=4: 
            mayor_4+=1  

            
        seguidos=0 #reiniciamos la racha evaluada 

    INDICE=indice(clima_actual, climas) #se busca el indice del clima evaludo 
    
    #solo se modifica la racha del clima cada vez que la actual es mayor a la establecida
    if racha[INDICE]<seguidos: 
        racha[INDICE]=seguidos 

print('\n', '*'*30, '\n')

#se busca el indice del clima con mayor racha
mayor_racha=max(racha) 
INDICE=indice(mayor_racha, racha) 
print(f'Racha más larga: {mayor_racha} días de {climas[INDICE]}')

print(f'Rachas de mas de 3 dias: {mayor_4}')
print('\n', '*'*30, '\n')


