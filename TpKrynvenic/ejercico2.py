import random

estado = "soleado"
l = ["soleado", "nevado", "tormenta", "lluvioso", "nublado"]
lista_total = []
dict1 = {}

for i in range (0,500):
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

for l in lista_total:
    if l in dict1:
      dict1[l] += 1
    else:
      dict1[l] = 1
sol = dict1.get("soleado")
nub = dict1.get("nublado")
tor = dict1.get("tormenta")
lluv= dict1.get("lluvioso")
nev = dict1.get("nevado")

def promedio(a):
  res = (a*100)/500
  return res

print(f"dias soleados: {dict1.get("soleado")} ({promedio(sol)})")
print(f"dias soleados: {dict1.get("nublado")} ({promedio(nub)})")
print(f"dias soleados: {dict1.get("tormenta")} ({promedio(tor)})")
print(f"dias soleados: {dict1.get("lluvioso")} ({promedio(lluv)})")
print(f"dias soleados: {dict1.get("nevado")} ({promedio(nev)})")

if (promedio(sol) > promedio(nub)) and (promedio(sol) > promedio(tor)) and (promedio(sol) > promedio(lluv)) and (promedio(sol) > promedio(nev)):
  print("hubo mas dias soleados")
if (promedio(nub) > promedio(sol)) and (promedio(nub) > promedio(tor)) and (promedio(nub) > promedio(lluv)) and (promedio(nub) > promedio(nev)):
  print("hubo mas dias nublados")
if (promedio(tor) > promedio(nub)) and (promedio(tor) > promedio(sol)) and (promedio(tor) > promedio(lluv)) and (promedio(tor) > promedio(nev)):
  print("hubo mas dias tormentosos")
if (promedio(lluv) > promedio(nub)) and (promedio(lluv) > promedio(tor)) and (promedio(lluv) > promedio(sol)) and (promedio(lluv) > promedio(nev)):
  print("hubo mas dias lluviosos")
if (promedio(nev) > promedio(nub)) and (promedio(nev) > promedio(tor)) and (promedio(nev) > promedio(lluv)) and (promedio(nev) > promedio(sol)):
  print("hubo mas dias nevados")
     