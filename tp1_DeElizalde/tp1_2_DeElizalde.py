from tp1_funciones_DeElizalde import full_pronostico    # De nuevo necesito esto para poder usar la funcion que pronostico

pronostico = full_pronostico()    # Aca de nuevo saco el pronostico y los dias necesarios

total = len(pronostico)     # Con esta linea puedo saber el total de pronosticos en la lista y por lo tanto el 100% por el cual divido

tot_sol = 0    
tot_nub = 0
tot_llu = 0     # En esta columna establezco unas variables con valores arbitrarios para despues poder operar sobre ellas
tot_tor = 0
tot_nev = 0

for i in pronostico:                # Este ciclo va por toda la lista del pronostico y va sumando cada clima individual a cada variable respectiva
    if i == "☀️  Soleado":
        tot_sol += 1
    elif i == "☁️  Nublado":
        tot_nub += 1
    elif i == "🌧️  Lluvioso":
        tot_llu += 1
    elif i == "⛈️  Tormenta":
        tot_tor += 1
    elif i == "❄️  Nevado":
        tot_nev += 1

por_sol = tot_sol / total * 100
por_nub = tot_nub / total * 100
por_llu = tot_llu / total * 100     # Esta columna calcula cada procentaje de cada clima sobre el total sacado previamente
por_tor = tot_tor / total * 100
por_nev = tot_nev / total * 100

print(f"\nDias Soleados: {tot_sol} ({round(por_sol, 2)}%)\n"    # Aca printeo toda la informacion previamente calculada, asegurandome que 
    f"Dias Nublados: {tot_nub} ({round(por_nub, 2)}%)\n"        # los porcentajes esten bien redondeados a 2 digitos
    f"Dias Lluviosos: {tot_llu} ({round(por_llu, 2)}%)\n"
    f"Dias Tormentas: {tot_tor} ({round(por_tor, 2)}%)\n"
    f"Dias Nevados: {tot_nev} ({round(por_nev, 2)}%)")

totales = {                               
    tot_sol:"☀️  Soleado",
    tot_nub:"☁️  Nublado" ,
    tot_llu:"🌧️  Lluvioso",             # Este diccionario chiquito es para poder ejecutar la linea de abajo mas facilmente
    tot_tor:"⛈️  Tormenta",
    tot_nev:"❄️  Nevado"
}

print ("\nEl clima mas frencuente fue: ", totales[max(tot_sol, tot_nub, tot_llu, tot_tor, tot_nev)], "\n")      # Al elegir el clima que mas veces aparecio lo printeo como 
                                                                                                                # para que elija el valor del diccionairo de encima