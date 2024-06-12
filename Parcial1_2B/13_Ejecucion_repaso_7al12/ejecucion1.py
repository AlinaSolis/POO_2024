# Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 
#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado
#

nume=[3,4,7,6,8,9,10,5]
#a
print(nume)
#b
for i in nume:
    print(i)
    #Se trasformo a texto "Stri"
lista_como_string = ", " .join(map(str, nume))
print(lista_como_string)
#Para acomodar la lista md
numeros_ordenados = sorted(nume)
print(numeros_ordenados)
#Para la cantidad de numeros de una lista  y empieza en 1
print(len(nume))
# E.Buscar algún elemento que el usuario pida por teclado

elemento_buscado = int(input("\nIntroduce el número a buscar: "))
if elemento_buscado in nume:
    print(f"El número {elemento_buscado} está en la lista: ")
else:
    print(f"El número {elemento_buscado} no está en la lista")

elemento_buscado = int(input("introduce el numero a busacar: "))
if elemento_buscado in nume:

 print(f"el numiero {elemento_buscado} esta en la lista: ")
