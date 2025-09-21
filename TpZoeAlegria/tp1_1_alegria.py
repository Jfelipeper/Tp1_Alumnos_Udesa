climas=('soleado', 'nublado', 'lluvioso', 'tormenta', 'nevado')

from tp1_funciones_alegria import pronostico, indice
    
clima_actual=input('\ningrese el clima actual: ').lower()

if clima_actual in climas: #se valida el clima ingresado 
     dias=(input('ingrese la cantidad de dias que quiere predecir el clima: '))
     print('\n', '*'*30, '\n')

     if dias.isdecimal() and int(dias) >0:  #se validan la cantidad de dias ingresada
        dias=int(dias)
        for dia in range (dias+1): #se ejecuta la simulacion por la cantidad de dias ingresada por el usuario
            proximo=pronostico(clima_actual) #se utiliza la funcion para simular el proximo dia en base a las probabilidades del dia ingresado
            clima_actual=proximo #se cambia el clima actual por el simulado
            print(f"Dia {dia}: {clima_actual}")
     else: 
         print('la cantidad de días debe ser un entero positivo!')
     print('\n', '*'*30, '\n')
else: 
    print('\n', '*'*30, '\n')
    print('el estado inicial debe ser uno de: soleado, nublado, lluvioso, tormenta, nevado')
    print('\n', '*'*30, '\n')
