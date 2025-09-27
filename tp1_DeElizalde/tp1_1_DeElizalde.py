from tp1_funciones_DeElizalde import full_pronostico     # Necesito esta linea para poder acceder a la fucnion requerida


pronostico = full_pronostico()                # Aca llamo a la funcion que hice para generar un diccionario con todos los pronosticos deseados


for i in range(len(pronostico)):            # Este ciclo hace que se impriman todos los climas con sus respectivos numeros de dias
    print(f"Día {i}: {pronostico[i]}")      
                                            # Uso el range combinada con len para hacer que la variable i sea un numero correspondiente al orden en el diccionario,
                                            # y despues accedo al diccionario usando i para poder sacar el clima