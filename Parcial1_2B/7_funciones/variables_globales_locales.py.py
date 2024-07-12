resultado_global = 0

def suma(a, b):
    resultado_local = a + b
    print(f"Suma (variable local): {resultado_local}")

def resta(a, b):
    resultado_local = a - b
    print(f"Resta (variable local): {resultado_local}")

suma(5, 3)
resta(5, 3)
print(f"Resultado global fuera de las funciones: {resultado_global}")