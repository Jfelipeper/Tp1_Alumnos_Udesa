from tp1_funciones_Taussig import simular_dias_new, analizar_rachas
import random

clima = ['soleado', 'nublado', 'lluvioso', 'tormenta', 'nevado']

probabilidades = {'soleado': [60, 30, 5, 3, 2],
            'nublado': [40, 30, 20, 5, 5],
            'lluvioso': [10, 30, 40, 15, 5], 
            'tormenta': [5, 10, 30, 50, 5],
            'nevado': [5, 20, 20, 10, 45]}

dias_simulacion = 10000

lista_climas = simular_dias_new(dias_simulacion)
racha_mas_larga, racha_clima, cantidad_rachas_4 = analizar_rachas(lista_climas)
        
print(f'Racha más larga: {racha_mas_larga} días de {racha_clima}\nRachas de más de 3 días: {cantidad_rachas_4}')

    
        


