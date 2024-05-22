# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for
#Aliiiii

conta = 1
while conta<= 60:
    acu = conta * conta
    print("con while, el cuadrado de: ", conta, "es: ", acu)
    conta+=1

conta=1
acu=0

for conta in range (1,61):
    acu = conta * conta
    print("con for, el cuadrado de: ", conta, "es: ", acu)
   

