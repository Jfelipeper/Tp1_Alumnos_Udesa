# TP 3 - Agustin Sosa del Valle

from tp1_funciones_SosaDelValle import sistema3

# Dias totales que se van a simular.

total=10000

# Creamos una variable que sea la funcion definida sistema3(total).

l=sistema3(total)

# Hacemos lo mismo que en el ejercico 2.

max_largo= l[0]
racha_maxima= l[1]
rachas= l[2]

# Ahora solo queda imprimir la racha maxima dependiendo que estado sea.

if racha_maxima=="soleado":
    x="☀️  Soleado"
elif racha_maxima=="nublado":
    x="☁️  Nublado"
elif racha_maxima=="lluvioso":
    x="🌧️  Lluvioso"
elif racha_maxima=="tormenta":
    x="⛈️  Tormenta"
elif racha_maxima=="nevado":
    x="❄️  Nevado"

# Por ultimo, printeamos lo unico que queremos que aparezca en el programa. 

print(f"Racha mas larga: {max_largo} dias de {x}")
print(f"Racha de mas de 3 dias: {rachas}")




