#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario
num=int(input("Ingresa el primer numero:  "))
num1=int(input("Ingresa el Segundo numero:  "))

for con in range(num,num1):
    if con % 2!=0:
        print(con)
