# 3.- Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#  palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#  el contenido de la lista en mayusculas

lista=[]
#checa que la lista esta vacia 
if not lista:
    print("Lalista esta vacia")
    print("Vamos, vamos a llenarla: ")
    while True:
        entra = input("Introduce una palabra o una frase: ")
        print("Para salir ingresa la palabra Salir: ")
        #lower letras minusculas
        if entra.lower() == "salir":
            break
        #oper mayusculas
        lista.append(entra)
        print("Contenido de la lista en mayuscula:  ")

for item in lista:
    print(item.upper())