print("string methods python")
#Nota: Todos los métodos de cadena devuelven nuevos valores.
# No cambian la cadena original.
### Estructura de control Metodo rindex()###
# Busca un valor especificado 
# en la cadena y devuelve la última posición en la que se encontró

# cadena = "Hola mundo hola"
# cadena = cadena.rindex("hola")
# print(cadena)

# # #Devuelve una versión justificada a la derecha de la cadena
# # ### Estructura de control Metodo rjust(width,fillchar)###
# cadena = "Hola"
# cadena = cadena.rjust(10, '-')
# print(cadena)^

# #Devuelve una tupla en la que la cadena se divide en tres partes
# ### Estructura de control Metodo rpartition()###
# cadena = "Hola mundo"
# cadena = cadena.rpartition(" ")
# print(cadena)

# #Divide la cadena en el separador especificado y devuelve una lista
# ### Estructura de control Metodo rsplit()###
# cadena = "Hola mundo"
# cadena = cadena.rsplit()
# print(cadena)

# #Divide la cadena en el separador especificado y devuelve una lista
# ### Estructura de control Metodo splitlines(keepends=False)###
# cadena = "hola\nmundo"
# cadena = cadena.splitlines()
# print(cadena)

# #Devuelve true si la cadena comienza con el valor especificado
# ### Estructura de control Metodo startswith()###
cadena = "hola mundo"
x = cadena.startswith("hola")
print(x)

# #Devuelve una versión recortada de la cadena
# ### Estructura de control Metodo strip()###
cadena = " Hola "
cadena = cadena.strip()
print(cadena)

# #Intercambia mayúsculas, las minúsculas se convierten 
#en mayúsculas y viceversa
# ### Estructura de control Metodo swapcase()###
cadena = " hola MUNDOO"
cadena = cadena.swapcase()
print(cadena)

# #Convierte el primer carácter de cada palabra en mayúsculas
# ### Estructura de control Metodo title()###
# cadena = " hola mundo"
# cadena = cadena.title()
# print(cadena)

# #	Devuelve una cadena traducida
# ### Estructura de control Metodo translate(table)###
# txt = "Hola Joven!"
# tabla = str.maketrans("S","X")
# print(txt.translate(tabla))

# #Convierte una cadena en mayúsculas
# ### Estructura de control Metodo upper()###
# cadena = "Hola"
# cadena = cadena.upper()
# print(cadena)

# #Rellena la cadena con un número especificado de valores 0 al principio
# cadena = "42"
# cadena = cadena.zfill(5)
# print(cadena)