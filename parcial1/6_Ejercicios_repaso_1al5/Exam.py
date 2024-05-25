    #k
siono ="SI"
siono.upper()
contador = 0
cap = 0

while True:
 if siono == "SI":
     nomta = input("Intrudisca el Nombre del trabajador: ")
     hora = float(input("Intrudisca las Horas trabajadas: "))
     dias = float(input("Intrudisca dias trabajadas: "))
     suel = float(input("Intrudisca el sueldo por horas: "))
#LEa    
     sueldo_diari = hora *  suel
     sueldo_semana = sueldo_diari * dias
#LEb
     print(sueldo_semana)

     sueldo_mes = sueldo_semana * 4
     if sueldo_mes >= 10000:
        print("Obrero tipo A")

     elif sueldo_mes > 10000 or sueldo_mes < 15000:
        print("Obrero tipo B")
     else:
        print("Sin categoria")
#LEc
     cap=float(print("Impresion de todas las capturas: "))
     
     siono=str(input("¿Deseas otra captura?: (SI/NO)"))
     siono=siono.upper()

     break
  


