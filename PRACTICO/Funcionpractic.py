a = 2
b = 6
#Suma hace haciones muestra y hace opereciones en una sola lines
#
print("Seleciona la operacion que prefieres: ")
def sumar(a,b):
    print("La suma es: ", a+b)

def restar(a,b):
    print("La resta es: ", a-b)

def restar(a,b):
    print("La resta es: ", a-b)   
#multiplicacion
def multiplicar(a,b):
    print("la multiplicacion: ", a*b)


# division
def division(a,b):
    print("la multiplicacion es: ", a/b)


j = int(input(("selecciona una opcion \nsuma(1) \n resta(2) \n multiplicacion(3) \n divicion(4)\n")))

if j == 1:
    sumar(a, b)

elif j ==2:
    restar(a, b)

elif j ==  3:
  multiplicar(a,b)
else:
  division(a, b)