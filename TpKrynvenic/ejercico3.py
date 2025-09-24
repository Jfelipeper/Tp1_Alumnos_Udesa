import random

estado = "soleado"

l = ["soleado", "nevado", "tormenta", "lluvioso", "nublado"]
lista_total = []
ultima_racha = 0
racha = 0
clima = estado
rachas_de_4 = 0

for i in range (0,10000):
    if estado == "soleado":
     next_dia = random.choices(l, weights=[60,2,3,5,30])
     estado = next_dia [0]
     lista_total.append(estado)
     
    elif estado == "nevado":
     next_dia = random.choices(l, weights=[5,45,10,20,20])
     estado = next_dia [0]
     lista_total.append(estado)
     
    elif estado == "tormenta":
     next_dia = random.choices(l, weights=[5,5,50,30,5])
     estado = next_dia [0]
     lista_total.append(estado)
     
    elif estado == "lluvioso":
     next_dia = random.choices(l, weights=[10,5,15,40,30])
     estado = next_dia [0]
     lista_total.append(estado)
     
    elif estado == "nublado":
     next_dia = random.choices(l, weights=[40,5,5,20,30])
     estado = next_dia [0]
     lista_total.append(estado)

for h in range(1, len(lista_total)):
  if lista_total[h] == lista_total[int(h-1)]:
    racha = racha + 1
  else:
    if racha > ultima_racha:
        ultima_racha = racha
        clima = lista_total [h]
        racha = 1
    elif racha > 3:
      rachas_de_4 += 1
      clima = estado
      racha = 1

print (f"la racha mas larga es {ultima_racha} siendo de {clima}")
print (f"rachas de 4 dias o mas {rachas_de_4}")