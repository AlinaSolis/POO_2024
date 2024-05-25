#Como se utliza la funcion While 
#Un ciclo while se utiliza mientras la expresión que le sigue (condición de salida) sea evaluada como verdadera
#Podemos "traducirlo" por:
#mientras la <expresión> sea verdadera, entra al sistema:
#eje
i = 0
while i <= 4:
    print("Se ejecuto el bucle")
    i += 1
#en este caso la condición de salida es que la variable i sea mayor o igual de 4
#mientras esta condición no se cumpla el ciclo seguira engtando

#funciona While True
#En el caso de while True la expresión siempre va a ser evaluada como verdadera por definición
#volviendo a nuestra traducción equivaldría a:
#Bucle infinito 
#Para no depender de ninguna expresio y siempre se ejecuta hasta cuando 
#le digamos break
#El in funciona como unn SI
#== Es igual Y con un igual es = caracter  
#Eje
#float :Numeros decimales
#int para todos los numeros enteros 
#sty:Es cadena o caracteres
#bool:Logocos verdaero o falso 
while True:
    siono=str(input("Deseas repetir la pregunta  (si/NO)"))
    if siono == "NO":

        break
   
   