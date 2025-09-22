# TP 2 - Agustin Sosa del Valle

from tp1_funciones_SosaDelValle import sistema2

# Cantidad de dias a simular

total=500

l= sistema2(total)

# Las variables siendo los estados, asignados un numero que es la cantidad de veces que hay ese estado en los 500 dias (dentro de la funcion).
# Lo que hace esto es a cada estado, asignarle un valor de conteo y como es por orden, se iguala al orden en el que se hizo el return.

soleado= l[0]
nublado= l[1]
lluvioso= l[2]
tormenta= l[3]
nevado= l[4]

# Ahora calculamos el % de dias para cada estado y lo hacemos una variable.

sol_pctj= ((soleado/total)*100)
nub_pctj= ((nublado/total)*100)
llu_pctj= ((lluvioso/total)*100)
tor_pctj= ((tormenta/total)*100)
nev_pctj= ((nevado/total)*100)

# Ahora hacemos el print de la cantidad de dias en los que ocurre cada estado durante los 500 simulados. Usamos :.2f para que nos quede con dos decimales.

print(f"Total soleados: {soleado} (%{sol_pctj:.2f}) ")
print(f"Total nublados: {nublado} (%{nub_pctj:.2f}) ")
print(f"Total lluviosos: {lluvioso} (%{llu_pctj:.2f}) ")
print(f"Total tormenta: {tormenta} (%{tor_pctj:.2f}) ")
print(f"Total nevados: {nevado} (%{nev_pctj:.2f}) ")

# Calculamos el que mas ocurrio durante la simulacion (asumimos soleado por default pero podria haber sido cualquiera).

estado_max = "soleado"
max = soleado

if nublado > max: 
    estado_max="nublado"
    max = nublado
if lluvioso > max: 
    estado_max= "lluvioso"
    max=lluvioso
if tormenta > max: 
    estado_max = "tormenta"
    max=tormenta
if nevado> max: 
    estado_max="nevado"
    max = nevado

# Esto lo usamos para printear el estado maximo final con el emoji correspondiente

if estado_max == "soleado":
    final= "☀️  Soleado"
elif estado_max == "nublado":
    final= "☁️  Nublado"
elif estado_max == "lluvioso":
    final= "🌧️  Lluvioso"
elif estado_max == "tormenta":
    final= "⛈️  Tormenta"
else:
    final= "❄️  Nevado"

print(f"El clima mas frecuente fue: {final}")