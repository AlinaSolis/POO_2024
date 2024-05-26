    #k
#Para la funcion .upper, necesitamos una variable, es decir en este caso, usamos "siono=siono.upper"
sueldo_mes=0
contador = 0
cap = 0
acumulador=0
while True:

   nomta = input("Intrudisca el Nombre del trabajador: ")
   hora = float(input("Intrudisca las Horas trabajadas: "))
   dias = float(input("Intrudisca dias trabajadas: "))
   suel = float(input("Intrudisca el sueldo por horas: "))
#LEa    
   sueldo_diari = hora *  suel
   sueldo_semana = sueldo_diari * dias
#LEb
   print(sueldo_semana)

   sueldo_mes=sueldo_semana * 4
   print(sueldo_mes)
   if sueldo_mes >= 10000:
      print("Obrero tipo A")

   elif sueldo_mes > 10000 and sueldo_mes < 15000:
      print("Obrero tipo B")
   else:
      print("Sin categoria")
#LEc
   contador=contador+1
   acumulador=sueldo_mes+acumulador
   siono=str(input("¿Deseas otra captura?: (SI/NO)"))
   siono=siono.upper()
   if siono=="NO":
      break
  
print(contador)
print("Sueldo de los trabajadores: ", acumulador)


