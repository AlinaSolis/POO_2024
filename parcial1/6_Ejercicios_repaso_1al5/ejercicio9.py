#Hacer un programa que solicite numeros indefinidamente hasta que se introduzca el 111 y salir del programa
#Rope el ciclo el break
x = 0

while x != 111:
    x=float(input("Ingresa un numero"))
    print(x)
    if x == 111:
        print("Listo Terminaste")
        break
