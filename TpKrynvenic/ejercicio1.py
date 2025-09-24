import random

estado = input("como esta el dia de hoy?")
dias = input("cuantos dias simularemos?")
i = 0

l = ["soleado", "nevado", "tormenta", "lluvioso", "nublado"]

while int(i) < int(dias):
    if estado == "soleado":
     next_dia = random.choices(l, weights=[60,2,3,5,30])
     estado = next_dia [0]
     i = i + 1
     print(f"estado del dia {i}: {estado}")

    elif estado == "nevado":
     next_dia = random.choices(l, weights=[5,45,10,20,20])
     estado = next_dia [0]
     i = i + 1
     print(f"estado del dia {i}: {estado}")

    elif estado == "tormenta":
     next_dia = random.choices(l, weights=[5,5,50,30,5])
     estado = next_dia [0]
     i = i + 1
     print(f"estado del dia {i}: {estado}")

    elif estado == "lluvioso":
     next_dia = random.choices(l, weights=[10,5,15,40,30])
     estado = next_dia [0]
     i = i + 1
     print(f"estado del dia {i}: {estado}")
    elif estado == "nublado":
     next_dia = random.choices(l, weights=[40,5,5,20,30])
     estado = next_dia [0]
     i = i + 1
     print(f"estado del dia {i}: {estado}")
    else:
      print("no pusiste un estado valido")
      i = i +1