#Operaadores Aritmeticos
#Arithmetic Operators
#Operador Name Example
#Se utiliza con un ctrl alt y aplastar la linea investida \
#TIPO DE NUMERO ENTERO "estan son las variables":
#cuando es Entero: int Cadena:str  Logico:bol Real:float
#Antes de un Impir va auna variable 
#nota
#Operator	Description	Try it
# ()	Parentheses	
# **	Exponentiation	
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
# *  /  //  %	Multiplication, division, floor division, and modulus	
# +  -	Addition and subtraction	
# <<  >>	Bitwise left and right shifts	
# &	Bitwise AND	
# ^	Bitwise XOR	
# |	Bitwise OR	
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
# not	Logical NOT	
# and	AND	
# or	OR

print("Operadores:Aritmeticos")
#print("+	Suma	x + y ")
#Ejemplo
x = 5
y = 3
print( "La suma es: ", x + y)

# Resta : -	Subtraction	x - y
num=0
num1=0
re=0

num=float(input("Coloca un numero: "))
num1=float(input("Coloca un numero: "))

re= num - num1 
print(re)

#Multiplicacion: *	Multiplication	x * y
num=float(input("Ingresa un numero: "))
num1=float(input("Ingresa un numero: "))

print( "El resultado es : ",num * num1)

#Divicion:/	Division	x / y
num=float(input("Ingresa un numero: "))
num1=float(input("Ingresa un numero: "))

print( "El resultado es : ",num / num1)

#Porcentaje : %	Modulus	x % y
num=float(input("Ingresa un numero: "))
num1=float(input("Ingresa un numero: "))

print( "El resultado es : ",num % num1)

#Elevacion/Potencia :que es ^ **	Exponentiation	x ** y
num=float(input("Ingresa un numero: "))
num1=float(input("Ingresa un numero: "))

print( "El resultado es : ",num ** num1)

#Div Solo puros numeros enteros : //	Floor division	x // y
num=float(input("Ingresa un numero: "))
num1=float(input("Ingresa un numero: "))

print( "El resultado es : ",num // num1)

##__Operadores de Asignacion_Assignment Operators##
#Operator	Example	Same As	Try it
#Igual
=	
x = 5	
x = 5	
#Asignando un nuevo valor a la variable 
+=	
x += 3	
x = x + 3	
#Igual
-=
x -= 3	
x = x - 3	
#Igual lo que realice en el ejercicio anterior
*=	
x *= 3
x = x * 3	
#Igual lo que realice en el ejercicio anterior
*=	
/=	
x /= 3	
x = x / 3	
%=	
x %= 3	
x = x % 3	
//=	x   //= 3	    x = x // 3	
**=	x   **= 3	    x = x ** 3	
&=	x   &= 3	    x = x & 3	
|=	x   |= 3	    x = x | 3	
^=	x   ^= 3	    x = x ^ 3	
>>=	x   >>= 3	    x = x >> 3	
<<=	x   <<= 3	    x = x << 3	
:=	
print(x := 3)	x = 3
print(x)

# Operadores de comparación #_Comparison Operators_#
== Igual a x == y	
!= No es igual a x != y	
> Mayor que x > y	
< Menor que x < y >= Mayor o igual que x >= y	
<= Menor o igual que x <= y

#_Operadores Logicos_#_Logical Operators_#
y Devuelve True si ambas instrucciones son verdaderas x < 5 y x < 10	
o Devuelve True si una de las instrucciones es verdadera x < 5 o x < 4	
not Reverse the result, devuelve False si el resultado es true not(x < 5 y x < 10)

#Operadores de identidad
is Devuelve True si ambas variables son el mismo objeto x es y	
is not Devuelve True si ambas variables no son el mismo objeto x no es y

#Operadoras de membresía Son para las tablas
in Devuelve True si una secuencia con el valor especificado está presente en el objeto x en y	
#Ejemplo:
x = ["manzana", "banana"]

print("banana" en x)

# SE devuelve Verdadero porque una secuencia con el valor "banana" está en la lista y por eso entra al ciclo

not in Devuelve True si una secuencia con el valor especificado no está presente en el objeto x no en y
x = ["manzana", "banana"]

print("piña" no está en x)

# SE devuelve Verdadero porque una secuencia con el valor "piña" no está en la lista Es como un si

#_Operadores bit a bit_#Bitwise Operators#
& AND Establece cada bit en 1 si ambos bits son 1 x & y	
#Ejemplo solo cambia el signo
print(6 & 3)
#El operador & compara cada bit y lo establece en 1 si ambos son 1, de lo contrario se establece en 0:

# 6 = 0000000000000110
# 3 = 0000000000000011
# --------------------
# 2 = 0000000000000010
# ====================

# Números decimales y sus valores binarios:
# 0 = 000000000000000000
# 1 = 0000000000000001
# 2 = 0000000000000010
# 3 = 0000000000000011
# 4 = 0000000000000100
# 5 = 0000000000000101
# 6 = 0000000000000110
# 7 = 0000000000000111
|	OR Establece cada bit en 1 si uno de los dos bits es 1 x | y

^ XOR Establece cada bit en 1 si solo uno de los dos bits es 1 x ^ y

~ NOT Invierte todos los bits ~x	

<< Relleno de ceros Desplazamiento a la izquierda Desplazamiento a la izquierda empujando ceros desde la derecha y dejando que los bits más a la izquierda caigan x << 2 >> Desplazamiento a la derecha con signo Desplazamiento a la derecha empujando copias del bit situado más a la izquierda desde la izquierda y dejando que los bits más a la derecha caigan x >> 2