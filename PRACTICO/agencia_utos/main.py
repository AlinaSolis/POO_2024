from dorador import *
from autos import autos 
import getpass
from usuarios import usuarios

def menu_principal():
    while True:    
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Registro
          2.- Login
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ").upper()

        if opcion == '1' or opcion=="REGISTRO":
            borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ")
            apellidos=input("\t ¿Cuales son tus apellidos?: ")
            email=input("\t Ingresa tu email: ")
            password=getpass.getpass("\t Ingresa tu contraseña: ")
            #Agregar codigo
            obj_usurio=usuarios.Usuario(nombre,apellidos,email,password)
            resultado=obj_usurio.registrar()
            if resultado:
                print(f"\n\t {nombre} {apellidos}, se registro correctamente, con el email: {email}")
            else:
                print(f"\n\t ** Por favor intentelo de nuevo, no fue posible insertar el registro ** ...")  
            esperarTecla()      
        elif opcion == '2' or opcion=="LOGIN":
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ")
            password=getpass.getpass("\t Ingresa tu Contraseña: ")
            #Agregar codigo 
            registro=usuario.Usuario.iniciar_sesion(email,password)
            if registro:
                menu_principal(registro[0],registro[1],registro[2])
            else:
                print(f"\n\t Email y/o contraseña incorrectas... vuelva a intentarlo ...")
                esperarTecla()    
        elif opcion == '3' or opcion=="SALIR":
            print("\n\t.. ¡Gracias Bye! ...")
            #opc=False
            break
            #exit()
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_inicial():
    while True:
        print("""
.:: Menu principal::.
              1.- Clientes
              2.- Autos
              3.- Revisiones
              4.- Salir""")
        opcion_inicial=input("Selecciona una de las opciones anteriores:").upper()
        if opcion_inicial=="1" or opcion_inicial=="CLIENTES":
            print("Clientes")
        elif opcion_inicial=="2" or opcion_inicial=="AUTOS":
            menu_autos()
        elif opcion_inicial =="3" or opcion_inicial=="REVISIONES":
            print("Revisiones")
        elif opcion_inicial=="4" or opcion_inicial=="SALIR":
            print("Salir")


def menu_autos():
    while True:
        
        print("""
    .::Menu de autos::.
            1.- Crear
            2.- mostrar
            3.- actualizar
            4.- eliminar
            5.- Salir""")
        opcion= input("Selecciona una de las opciones anteriores").upper()
        
        if opcion=='1' or opcion=="CREAR":
            borrarPantalla()
            print(f"\n \t .:: Crear Auto ::. ")
            matricula=input("\t 1Matricula: ")
            marca=input("\t Marca: ")
            modelo=input("\t modelo:")
            color=input("\t Color:")
            nif=input("\t Nif:")
            #Agregar codigo
            obj_nota=autos.Auto(matricula,marca,modelo,color,nif)
            resultado=obj_nota.crear()
            if resultado:
                print(f"\n \t \t.::El Auto se creo Correctamente ::.")
            else:
                print(f"\n \t \t No fue posible crear el auto... vuelva a intentarlo...") 
            esperarTecla()
            
        elif opcion=='2' or opcion =="MOSTRAR":
            borrarPantalla()
            #Agregar codigo  
            registros=autos.Auto.mostrar()
            if len(registros)>0:
                num_notas=1
                for fila in registros:
                   print(f"\nMatricula: {fila[0]}   .- marca: {fila[1]}         Modelo: {fila[2]} \tColor: {fila[3]}") 
                   num_notas+=1    
            else:
                print(f"\n \t \t** No existen notas para el usuario ... vuelva a intentarlo **...")
            esperarTecla()
            
        elif opcion=='3' or opcion=="ACTUALIZAR":
             borrarPantalla()
             marca= input("\t \t Marca: ")
             modelo= input("\t Nuevo modelo: ")
             color = input("\t Nuevo Color: ")
             nif=input("\t Nuevo Nif:")
             #Agregar codigo
             resultado=autos.Auto.actualizar(marca, modelo, color,nif)
             if resultado:
                 print(f"\n \t \t.::Nota Actualizada Correctamente ::.")
             else:
                print(f"\n \t \t** No fue posible actualizar la nota ... vuelva a intentarlo **...")  
             esperarTecla()
            
        elif opcion=='4' or opcion=="ELIMINAR":
            matricula= input("\t \t ID de la nota a eliminar: ")
            #Agregar codigo
            resultado=autos.Auto.eliminar(matricula)
        elif opcion=='5' or opcion=="SALIR":
            print("\t !!Gracias por usar nuestro software¡¡")

            break
        else:
            print("Asegurate que la opcion sea la correcta")

if __name__ == "__main__":
  menu_inicial()