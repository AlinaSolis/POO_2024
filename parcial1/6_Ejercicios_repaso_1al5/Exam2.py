print("___::Indice de masa corporal::___")

calcular = 0
acc = input("Deseas ingresar a calcular tu IMC? (Si/No)")

def calcular_imc(peso, altura):
    return peso / (altura ** 2)
while True:
    acc = input("Quieres calcular tu IMC?(Si/No)")
    if acc == "Si":
        calcular += 1
        peso = float(input("Introduce tu peso en kg: "))
        altura = float(input("Introduce tu altura en metros: "))
        imc = calcular_imc(peso, altura)

        if imc < 18.5:
            print(f"Tu IMC es de: {imc}, estas bajo de peso")

        elif imc >= 18.5 and imc <= 24.9:
            print(f"Tu IMC es: {imc}, estas normal")
        elif imc >= 25 and imc <= 29.9:
            print(f"Tu IMC es: {imc}, estas con sobrepeso")

        elif imc >= 30:
            print(f"Tu IMC es: {imc}, estas con obesidad")

        print(f"El cálculo del IMC se ha realizado {calcular} vez/veces.")
    elif acc == "No":
        print("Gracias por usar el calculador de IMC.")
        print(f"se han realizado {calcular} calculos.")
        break
    elif acc == "No" and calcular == 0:
        print("No se han realizado calculos")
    else:
        print("Entrada no válida. Por favor, introduce 'Si' para sí o 'No' para no.")
