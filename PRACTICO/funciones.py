
import mysql.connector
from mysql.connector import Error


def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  # Asegúrate de que esto sea correcto para tu configuración
            database='agencia_autos_datos'
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos.")
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    return None

def cerrar_conexion(conexion):
    if conexion and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada.")

def registrar_cliente(correo, contrasena, nombre, direccion, ciudad, tel):
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "INSERT INTO clientes (correo, contrasena, nombre, direccion, ciudad, tel) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (correo, contrasena, nombre, direccion, ciudad, tel)
        cursor.execute(query, values)
        conexion.commit()
        print("Cliente registrado exitosamente.")
        cerrar_conexion(conexion)

def autenticar_cliente(correo, contrasena):
    """Autentica a un cliente con correo y contraseña."""
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "SELECT * FROM clientes WHERE correo = %s AND contrasena = %s"
        cursor.execute(query, (correo, contrasena))
        cliente = cursor.fetchone()
        cerrar_conexion(conexion)
        return cliente is not None
    return False

def agregar_auto(matricula, marca, modelo, color, nif):
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "INSERT INTO autos (matricula, marca, modelo, color, nif) VALUES (%s, %s, %s, %s, %s)"
        values = (matricula, marca, modelo, color, nif)
        cursor.execute(query, values)
        conexion.commit()
        print("Auto agregado exitosamente.")
        cerrar_conexion(conexion)

def actualizar_auto(matricula, marca=None, modelo=None, color=None, nif=None):
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "UPDATE autos SET marca = %s, modelo = %s, color = %s, nif = %s WHERE matricula = %s"
        values = (marca, modelo, color, nif, matricula)
        cursor.execute(query, values)
        conexion.commit()
        print("Auto actualizado exitosamente.")
        cerrar_conexion(conexion)

def eliminar_auto(matricula):
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "DELETE FROM autos WHERE matricula = %s"
        cursor.execute(query, (matricula,))
        conexion.commit()
        print("Auto eliminado exitosamente.")
        cerrar_conexion(conexion)

def consultar_auto():
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "SELECT * FROM autos"
        cursor.execute(query)
        autos = cursor.fetchall()
        for auto in autos:
            print(auto)
        cerrar_conexion(conexion)

def agregar_revision(no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula):
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "INSERT INTO revisiones (no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (no_revision, cambiofiltro, cambioaceite, cambiofrenos, otros, matricula)
        cursor.execute(query, values)
        conexion.commit()
        print("Revisión agregada exitosamente.")
        cerrar_conexion(conexion)

def actualizar_revision(no_revision, cambiofiltro=None, cambioaceite=None, cambiofrenos=None, otros=None, matricula=None):
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "UPDATE revisiones SET cambiofiltro = %s, cambioaceite = %s, cambiofrenos = %s, otros = %s, matricula = %s WHERE no_revision = %s"
        values = (cambiofiltro, cambioaceite, cambiofrenos, otros, matricula, no_revision)
        cursor.execute(query, values)
        conexion.commit()
        print("Revisión actualizada exitosamente.")
        cerrar_conexion(conexion)

def eliminar_revision(no_revision):
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "DELETE FROM revisiones WHERE no_revision = %s"
        cursor.execute(query, (no_revision,))
        conexion.commit()
        print("Revisión eliminada exitosamente.")
        cerrar_conexion(conexion)

def consultar_revision():
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "SELECT * FROM revisiones"
        cursor.execute(query)
        revisiones = cursor.fetchall()
        for revision in revisiones:
            print(revision)
        cerrar_conexion(conexion)

def agregar_cliente(nif, nombre, direccion, ciudad, tel):
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "INSERT INTO clientes (nif, nombre, direccion, ciudad, tel) VALUES (%s, %s, %s, %s, %s)"
        values = (nif, nombre, direccion, ciudad, tel)
        cursor.execute(query, values)
        conexion.commit()
        print("Cliente agregado exitosamente.")
        cerrar_conexion(conexion)

def actualizar_cliente(nif, nombre=None, direccion=None, ciudad=None, tel=None):
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "UPDATE clientes SET nombre = %s, direccion = %s, ciudad = %s, tel = %s WHERE nif = %s"
        values = (nombre, direccion, ciudad, tel, nif)
        cursor.execute(query, values)
        conexion.commit()
        print("Cliente actualizado exitosamente.")
        cerrar_conexion(conexion)

def eliminar_cliente(nif):
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "DELETE FROM clientes WHERE nif = %s"
        cursor.execute(query, (nif,))
        conexion.commit()
        print("Cliente eliminado exitosamente.")
        cerrar_conexion(conexion)

def consultar_clientes():
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "SELECT * FROM clientes"
        cursor.execute(query)
        clientes = cursor.fetchall()
        for cliente in clientes:
            print(cliente)
        cerrar_conexion(conexion)

def consultar_todas_las_tablas():
    conexion = crear_conexion()
    if conexion:
        cursor = conexion.cursor()
        
        print("\n--- Autos ---")
        cursor.execute("SELECT * FROM autos")
        autos = cursor.fetchall()
        for auto in autos:
            print(auto)
        
        print("\n--- Revisiones ---")
        cursor.execute("SELECT * FROM revisiones")
        revisiones = cursor.fetchall()
        for revision in revisiones:
            print(revision)
        
        print("\n--- Clientes ---")
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        for cliente in clientes:
            print(cliente)
        
        cerrar_conexion(conexion)
