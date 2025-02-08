import os
import pymysql

# Obtener credenciales desde las variables de entorno
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

try:
    connection = pymysql.connect(host=db_host,user=db_user,password=db_password,database=db_name)
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
connection.close()
        
