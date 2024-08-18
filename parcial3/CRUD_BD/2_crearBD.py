import mysql.connector

#conectarse con la base de datos de mysql
conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_python"
)

#verificar la conexion con la  BD
if conexion.is_connected():
    print("Se creo la conexion con la base de datos")
else:
    print("No fue posible conectar la base de datos .. verifique..")
    #