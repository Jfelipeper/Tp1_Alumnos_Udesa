from tp1_funciones_DeElizalde import rachas, full_pronostico    # Aca importeo las dos funciones que necesito

pronostico = full_pronostico()      # De nuevo necesito un pronostico asi que sigo usando esta funcion

racha_max, clima_max, rachas_3 = rachas(pronostico)     # Aca inputeo el pronostico en la siguiente funcion que revisa las rachas posibles

print ("\nRacha mas larga:", racha_max, "dias de", clima_max)       # Y esto solo printea la informaicon calculada
print ("\nRachas de mas de 3 dias:", rachas_3, "\n")