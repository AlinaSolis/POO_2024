#Una funcion es un conjunto de istruciones agrupadas bajo un nombre particular como programa mas pequeño
#que cumple una funcion especifica.la funcio se puede reutilizar con el simple hecho de invocarla,es ddecir,mandar a llamar.
# SINTAXIS
# def nombredeMifundacion(parametros):
#     bloque o conjunto de instruciones

#nombredeMifuncion(parametro)
#Las funciones puede ser 4 tipos
# 1-Funcion que no recibe parametros y no regresa Valor.
# 2-Funcion que no recibe parametros y regresaa Valor
# 3.Funciones que recibe parametrso y no regresa Valor
# 4-Funcion que recibe parametros y regrese valor

# Eje:
# 1.Funcion que no recibe parametros y no regresa Valor.
def solicitarNombre():
    nombre=input("Ingresa el nombre completo: ")
solicitarNombre()

def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

suma()

    # eje3 suma de dos numeros
    # solo regresa un valor y si se puede regresar mejor con una lista 
    # variables locales o globales

def suma():
    # locales propios de la funcionn1 y n2
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    return suma

resultad_suma=suma()
print(f"La suma es: {suma()}") 
# o print(f"La suma es: {resultad_suma}")

# 4-Funcion que recibe parametros y NO regrese valor .EJE4
# locales num1 y num2 son 2 variables diferentes y regresa en n1
def suma(num1,num2):
    # 
    
    suma=num1+num2
    return suma
    print(f"La suma es: {resultad_suma}")
# Funcion global n1 y n2 :Losacamos para enviar la informacion que queremos que reciba 
n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
suma(n1,n2)

#opcion 2 de ejemplo 4 
def suma(num1,num2):
   
    suma=num1+num2
    return suma
   
n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
resultad_suma=suma(n1,n2)
print(f"La sumaes: {resultad_suma}")

#Eje 6 crear un programa que solicite a traves de una funcion lo siguiente 
#nombre del paciente ,edad,estatura,tipo de sagre .utilizar una funcion que reciva parametros 
#4 tipos de funciones
#Metodo sse de lara en una funcion para crear objetos sin crear clases finciones es como un metodo la direncia es de como un objeto y se usa a traves de un objeto
#Se utiliza cuando regresa en algo particular  si puede recibir parametos y los imprime
def solicitarPaciente():
    nombrre

