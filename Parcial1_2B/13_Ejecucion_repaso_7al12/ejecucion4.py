#  4.-  Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#   y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones
# Definir las variables
mi_lista = [1, 2, 3]
mi_cadena = "Hola Gentee"
mi_entero = 42
mi_logico = True

# Función que retorna un mensaje según el tipo de dato
# isinstance es una funcion para comprobar el tipo de variable 
def obtener_mensaje(variable):
    if isinstance(variable, list):
        return "La variable es una lista."
    elif isinstance(variable, str):
        return "La variable es una cadena."
    elif isinstance(variable, int):
        return "La variable es un entero."
    elif isinstance(variable, bool):
        return "La variable es un lógico."
    else:
        return "Tipo de dato no existe"

# Lista de variables pque mete las variables que creo para meter las otras variables
variables = [mi_lista, mi_cadena, mi_entero, mi_logico]

# Imprimir mensajes para cada variable uno por uno
for i in variables:
    print(obtener_mensaje(i))
