import random
status = input(f"Ingrese el estado inicial: ")
days = int(input(f"Ingrese la cantidad de dias: "))
emojis = {
    'Soleado':  '☀️',
    'Nublado':  '☁️',
    'Lluvioso': '🌧️',
    'Tormenta': '⛈️',
    'Nevado':   '❄️',
}

climas = ["Soleado","Nublado","Lluvioso","Tormenta","Nevado"]
def simulador_de_clima(status,days):
    """
    Simula e imprime la evolución del clima durante 'days' días, partiendo de 'status'.

    Parámetros
    ----------
    status : str
        Estado inicial del clima. Debe ser uno de los valores en `climas`.
    days : int
        Cantidad de días a simular. Debe ser un entero positivo.
    """
    # Validación de la cantidad de días
    if status not in climas:
        print("El estado inicial debe ser uno de: Soleado, Nublado, Lluvioso, Tormenta o Nevado")
    if isinstance(days,(int,float)) == False or days <=0:
        print("La cantidad de dias debe ser un entero positivo")
    else:  
        for i in range(days):  # Bucle principal de simulación (índice de día comienza en 0)

        
            if status == "Soleado":
                new_clima = random.choices(climas,weights=[60,30,5,3,2])
                print(f"Dia {i}:{emojis[new_clima[0]]}  {new_clima[0]}")    
                status = new_clima[0]
            elif status == "Nublado":
                new_clima = random.choices(climas,weights=[40,30,20,5,5])
                print(f"Dia {i}:{emojis[new_clima[0]]}  {new_clima[0]}")
                status = new_clima[0]
            elif status == "Lluvioso":
                new_clima = random.choices(climas,weights=[10,30,40,15,5])
                print(f"Dia {i}:{emojis[new_clima[0]]}  {new_clima[0]}")
                status = new_clima[0]
            elif status == "Tormenta":
                new_clima = random.choices(climas,weights=[5,10,30,10,45])
                print(f"Dia {i}:{emojis[new_clima[0]]}  {new_clima[0]}")
                status = new_clima[0]
            elif status == "Nevado":
                new_clima = random.choices(climas,weights=[5,20,20,10,45])
                print(f"Dia {i}:{emojis[new_clima[0]]}  {new_clima[0]}")
                status = new_clima[0]


                
simulador_de_clima(status,days)