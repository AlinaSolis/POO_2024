#Mostrar todas las tablas del 1 al 10.
#Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10

for nu in range(1, 11):
    print("")
    print(f"Tabla de multiplicar del numero {nu}")
    for j in range(1, 11):
        resultado = nu * j
        print(f"{nu} x {j} = {resultado}")
print("")

