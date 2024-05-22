#Hacer un programa que muestre todos los numeros entre 2 numeros 
#que le diga al usuario

num=int(input("Ingresa el primer numero:  "))
num1=int(input("Ingresa el Segundo numero:  "))

if num < num1:
       print("Los números entre ", num, " y ", num1, " son: ")
for cont in range(num + 1, num1):
        print(cont)
else:
        print("Coloca un valor inicial menor al segundo")
    
