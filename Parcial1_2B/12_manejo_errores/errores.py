#Los errores de ejecucion en un lenjuage de programacion se presenta cuadno
#existe una anomalia dentro de la ejecucion del codigo,lo cual provoca que se dentega la ejecucion del SW.Con el control u manejo de expreciones sera posible minimizar o enviar la interrupcion del programa del programa debido a una excepcion
# Ejemplo:1 cuando una variable no se genera

# nombre=input("Introdice el nombre completo de una persona")
# if len(nombre)>0:
#      nombre_usuario="El nombre completo del usuario es "+nombre

# print(nombre_usuario) 

try:

    nombre=input("Introdice el nombre completo de una persona: ")

    if len(nombre)>0:
       nombre_usuario="El nombre completo del usuario es "+nombre
    print(nombre_usuario) 
except:
    print("Es necesario introducir un nombre: ")

# x=3+7
# print("El valor es x es: "+str(x))
# #Manejo de exepciones 

##Ejemplo 2:Cuando se solicita un numero y se ingresa otra cosa
try:
    numero=int(input("Ingresa un numero entero: "))

    if numero>0:
        print("Soy un numero positivo: ")
    elif numero==0:
        print("Soy un numero neutro: ")
    else:
        print("Soy un numero entero nogativo: ")
except ValueError:
    print("Introduce un numero entero: ")

##Ejemplo 3.Genera multiples exepciones 
try:
    numero=int(input("Introduce un numero: "))

    print("El cuadrado del numero es: "+str(numero*numero))
except ValueError:
    print("Introdusca un numero entero bbis ")

except TypeError:
    print("Se bebe que comvertir el numero en entero")
else:
    print("No se encontro errores fe fa")
    #Siempre se va ejecutar. Finally aunqueb tenga errores:
finally:
    print("termine la ejecucion")