from random import choices
from tp_1_funciones_Goicoa import simulacion
dias = 10000
condicion_inicial = 'Soleado' 
call_simulacion = simulacion(condicion_inicial,dias) #Ejecuto mi funcion simulacion con los datos que pide la consigna
clima_actual = call_simulacion[0] #Esta variable toma en principio el valor de la primer condicion que hubo, y en cada corte de racha se convierte en el siguiente
largo_racha = 1 #Esta variable va a guardar el valor de longitud de cada racha que hay sobre la lista 'call_simulacion()'
rachas = {
    'Soleado': [],
    'Nublado': [],
    'Lluvioso': [],
    'Tormenta': [],
    'Nevado': []} #En cada una de estas listas vacías del diccionario se va a guardar el valor de longitud de cada racha, pero ahora almacenado para el clima correspondiente
for dia in range(len(call_simulacion)-1):
    if clima_actual == call_simulacion[dia+1]: #Esto significa que la condicion del primer dia es igual a la del siguiente
        largo_racha += 1
    else:
        rachas[clima_actual].append(largo_racha) #El valor de racha se agrega a la lista que corresponde dentro del diccionario 'rachas'
        largo_racha = 1 #Reinicio el contador de longitud de racha
        clima_actual = call_simulacion[dia+1] #Restauro clima_actual para que ahora tome el valor del proximo dia que toca
rachas_mayores = [
    max(rachas['Soleado']),
    max(rachas['Nublado']),
    max(rachas['Lluvioso']),
    max(rachas['Tormenta']),
    max(rachas['Nevado'])] #Esta lista va a guardar de cada clima, su racha mas larga, por lo que si o si la racha mas larga se va a encontrar acá
if max(rachas_mayores) == rachas_mayores [0]:
    print(f'Racha mas larga: {rachas_mayores[0]} dias de Soleado')
elif max(rachas_mayores) == rachas_mayores [1]:
    print(f'Racha mas larga: {rachas_mayores[1]} dias de Nublado')
elif max(rachas_mayores) == rachas_mayores [2]:
    print(f'Racha mas larga: {rachas_mayores[2]} dias de Lluvioso')
elif max(rachas_mayores) == rachas_mayores [3]:
    print(f'Racha mas larga: {rachas_mayores[3]} dias de Tormenta')
elif max(rachas_mayores) == rachas_mayores [4]:
    print(f'Racha mas larga: {rachas_mayores[4]} dias de Nevado')    #Printea el resultado en función de cual sea el clima con la racha mas larga
rachas_mayores_a_4_soleado = sum(1 for x in rachas['Soleado'] if x > 4) 
rachas_mayores_a_4_nublado = sum(1 for x in rachas['Nublado'] if x > 4)
rachas_mayores_a_4_lluvioso = sum(1 for x in rachas['Lluvioso'] if x > 4) #Cuenta dentro de los valores de longitud de las rachas, aquellas mayores a 4
rachas_mayores_a_4_tormenta = sum(1 for x in rachas['Tormenta'] if x > 4)
rachas_mayores_a_4_nevado = sum(1 for x in rachas['Nevado'] if x > 4)
total_rachas_mayores_a_4 = rachas_mayores_a_4_soleado + rachas_mayores_a_4_nublado + rachas_mayores_a_4_lluvioso + rachas_mayores_a_4_tormenta + rachas_mayores_a_4_nevado
print(total_rachas_mayores_a_4) #Sumo todos los valores obtenidos anteriormente y obtengo el total de rachas mayores a 4 dias


#Agrego, en la parte en la que se calcula las rachas maximas por clima. La función max puede llegar a fallar en el caso de que ocurra que haya un clima que no registre rachas
#Es tan improbable que ocurra eso simulando 10000 dias que preferí dejarlo así