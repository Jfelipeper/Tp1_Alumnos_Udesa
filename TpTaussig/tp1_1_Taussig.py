from tp1_funciones_Taussig import simulador_dias

clima = ['soleado', 'nublado', 'lluvioso', 'tormenta', 'nevado']

probabilidades = {'soleado': [60, 30, 5, 3, 2],
            'nublado': [40, 30, 20, 5, 5],
            'lluvioso': [10, 30, 40, 15, 5], 
            'tormenta': [5, 10, 30, 50, 5],
            'nevado': [5, 20, 20, 10, 45]}

simulador_dias()
