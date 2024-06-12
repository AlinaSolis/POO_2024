# 2.- 
# Escribir un programa  que añada valores a una lista mientras que su longitud 
#  sea menor a 120, y luego mostrar la lista: Usar un while y for

nume=[]
i=1
while len(nume)<=120:
    nume.append(i)
    i += 1
print("::Lista de numeros::")
for x in nume:
    print(x,end=' ')
    