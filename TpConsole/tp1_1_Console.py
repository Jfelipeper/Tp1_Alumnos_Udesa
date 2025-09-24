import random

print(" ="*30)
print("aqui vamos a ver cual es el estado del clima en base  al IMH")
print(" ="*30)
print("")
print("")
print("recorda que los unicos estados que reconoce mi programa son :soleado, nublado, lluvioso, tormenta, nevado")
print("cualquiero otro valor que pongas no va a ser valido\n")

clim_est = ["soleado", "nublado", "lluvioso", "tormenta", "nevado"]


porcentaje = {"soleado" : [60, 30, 5, 3, 2] ,       #armo mi lista
              "nublado" : [40, 30,20, 5, 5],           
              "lluvioso" : [10, 30, 40, 15, 5], 
              "tormenta" : [5, 10,30,50, 5], 
              "nevado" : [ 5,20,20,10,45]
}



clima = input("cual es el estado del clima inicial? : ").lower()
while True:
    az = (clima in clim_est)                                              #creo un while para la variable clima asi de esta manera al
    if az == True:                                                        #poner cualquier cosa que no este en la lista vuelve a pedirlo hasta que lo ponga bien
        break
    elif az == False:
        print("esta mal escrito el estado del clima, intentá de nuevo.\n")
        clima = input("cual es el estado del clima inicial? : ").lower()




    
simular = int(input("cuantos dias son los que queres simular? (entero > 0): "))

while simular <= 0 :
    print("no me diste bien el valor de los dias (debe ser un entero mayor a 0).")        #mismo pedido que con la variable clima pero para los dias
    simular = int(input("cuantos dias son los que queres simular? (entero > 0): "))       #mi programa termina al poner palabras en el input de simular
                                                                                          #pero si se ponen numeros negativos vuelve a pedir hasta que ponga
                                                                                          #un numero entero positivo


dias = 0                                                                                        
print("dia 0 :", clima)



while dias < simular:
    if clima == "soleado":
        clima = random.choices(clim_est, weights=[60, 30, 5, 3, 2])[0]                     #creo un while para la variable dias asi de esta manera la persona al poner de que dia quiere simular va tomando los valores, y el while se ejecuta hasta que pasen todos los dias pedidos para simular      
        dias += 1
        print(f"Día {dias}: {clima}")
    elif clima == "nublado":
        clima = random.choices(clim_est, weights=[40, 30, 20, 5, 5])[0]
        dias += 1
        print(f"Día {dias}: {clima}")
    elif clima == "lluvioso":
        clima = random.choices(clim_est, weights=[10, 30, 40, 15, 5])[0]
        dias += 1
        print(f"Día {dias}: {clima}")
    elif clima == "tormenta":
        clima = random.choices(clim_est, weights=[5, 10,30,50, 5])[0]
        dias += 1
        print(f"Día {dias}: {clima}")
    elif clima == "nevado":
        clima = random.choices(clim_est, weights= [ 5,20,20,10,45])[0]
        dias += 1
        print(f"Día {dias}: {clima}")











