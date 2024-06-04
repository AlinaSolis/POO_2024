# List (Array)
# son coleciones o con conjuntos de datos/valores bajo un mismo nombre,para acceder a los valores se hacen con un indice numerico
# nota:sus valores si son modificables
# la lista es una coleccion ordenada y modificable.
# permite miembros duplicados

#Eje 1:Crear una lista de numeros e imprimir el contenido
# numeros=23
# numeros=34 O la de abajo
numeros=[23,34]
print(numeros)
#para recorer lo de la lista
#recorer con un siclo for
#i va a tomar la posicion perimera y la otra la manda para abajo 

for i in numeros:
    print(i)

#recorer con un siclo While
#Longitud y ver de cuanto y los valores 
i=0
while i<=len(numeros)-1:
  print(numeros[i])
  #Contador
  i+=1;
#Eje2:Crear una lista de palabras y posterior mente buscar la coincidencia de palabras
# palabras=["Hola","saludos","america","azul","naranja"]
# palabras_buscar=input("Ingresa la palbra que quieres buscar fe: ")
# for i in palabras:
#  if i==palabras_buscar: 
#       print(f"Se encontro la palabra a buscar en la posicion: " posicion{palabras.index} )
      