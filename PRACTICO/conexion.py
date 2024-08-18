import mysql.connector
from mysql.connector import Error

def crear_conexion():

    try:
        conexion = mysql.connector.connect(
            host='localhost',              
            user='root',                   
            password='',                   
            database='bd_a'
        )
        if conexion.is_connected():
            print("Se a conectado exitosamente")
            return conexion
    except Error as e:
        print(f"Intenta mas tarde o verifica tu conexion con la base de datos{e}")
        return None
