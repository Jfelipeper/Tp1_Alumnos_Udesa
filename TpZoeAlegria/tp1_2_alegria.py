print('\nSIMULACIÓN POR 500 DIAS!')
climas=('soleado', 'nublado', 'lluvioso', 'tormenta', 'nevado')
dias=[0,0,0,0,0] #el indexado de esta lista es paralelo a la tupla climas, tal que funciona como contador

from tp1_funciones_alegria import pronostico, indice

clima_actual='soleado'
print('\n', '*'*30, '\n')

for dia in range (500+1): 
    clima_actual=pronostico('soleado') 
    INDICE=indice(clima_actual, climas) #se busca el indice del dia evaluado
    dias[INDICE]+=1 #se suma un dia al conteo del clima evaluado

#se imprime cada dia con su frecuencia 
INDICE=0 #recorre la lista de dias (frecuencia) a medida que avanzan los climas
for clima in climas: 
    print(f'Dias {clima}: {dias[INDICE]} ({dias[INDICE]/501*100:.2f}%)')
    INDICE+=1 

print('\n', '*'*30, '\n')

clima_frecuente=max(dias)
INDICE2=indice(clima_frecuente, dias) #se busca el indice del clima con mayor frecuencia
print(f'El clima mas frecuente fue: {climas[INDICE2]}')

print('\n', '*'*30, '\n')

