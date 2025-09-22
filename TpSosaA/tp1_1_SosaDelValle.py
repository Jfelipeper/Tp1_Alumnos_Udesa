# TP 1 - Agustin Sosa del Valle

from tp1_funciones_SosaDelValle import sistema

print("Bienvenido querido ciudadando de Kokua, espero que el simulador lo ayude a planificar sus actividades a futuro")

# Inputs iniciales 
estado_inicial= input("Ingrese estado inicial: ").lower()
dias_inicial= int(input("Ingrese cantidad de dias: "))

# Estados válidos y diccionario para posibles "respuestas" a los estados
ESTADOS = ("soleado", "nublado", "lluvioso", "tormenta", "nevado")
Respuesta_estado= {
    "soleado":  "☀️  Soleado",
    "nublado":  "☁️  Nublado",
    "lluvioso": "🌧️  Lluvioso",
    "tormenta": "⛈️  Tormenta",
    "nevado":   "❄️  Nevado",
}

# Dos posibilidades cuando usuario no pone input indicado

if estado_inicial not in ESTADOS:
    print(f"El estado inicial debe ser uno de: {ESTADOS}")
    estado_inicial = input("Ingrese estado inicial: ").lower()

if dias_inicial < 1:
    print("La cantidad de días debe ser un entero positivo")
    dias_inicial = int(input("Ingrese cantidad de dias: "))

# Printear espacio 
print("")

# Dia 0 y su print
print(f"Dia 0: {Respuesta_estado[estado_inicial]}")

#Dia 1 incluido, en adelante con el sistema definido
sistema(dias_inicial)