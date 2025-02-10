# Se tiene instacia de prueba en RDS para esta prueba, la credenciales son de un usuario con permisos unicamente para la finalidad de este script.
# Inicialmente la base de datos ya tiene creada dos tablas
# La tabla "transactions" la cual almacena los datos de los archivos CSV (timestamp, price, user_id)
# La tabla "statistics" la cual almacena las estadisticas (total_rows, total_sum_price, min_price, max_price) que se actualizan en cada insercion de registros

import os
from decimal import Decimal
import pandas as pd
import pymysql

### Se definen las funciones a utilizar 

# Función para limpiar datos, algunos archivos vienen incompletos en algunos campos y con formato incorrecto
def clean_data(df):
    #Limpia los datos de un DataFrame antes de insertarlos en la BD
    df['price'] = df['price'].fillna(df['price'].median())  # Completar NaN con la mediana
    df['price'] = df['price'].apply(lambda x: Decimal(str(x)))  # Convertir a Decimal

    # Convertir timestamp de formato MM/DD/YYYY a YYYY-MM-DD
    df['timestamp'] = pd.to_datetime(df['timestamp'], format="%m/%d/%Y")
    df['timestamp'] = df['timestamp'].dt.strftime("%Y-%m-%d")

    return df

# Función para mostrar estadísticas actuales desde la base de datos
def print_statistics():
    cursor.execute("SELECT total_rows, total_sum_price/total_rows AS avg_price, min_price, max_price FROM statistics")
    stats = cursor.fetchone()
    print(f"Estadísticas actuales: {stats}\n")

# Función para actualizar estadísticas de manera incremental
def update_statistics(price):
    cursor.execute("SELECT total_rows, total_sum_price, min_price, max_price FROM statistics WHERE id = 1")
    stats = cursor.fetchone()

    # Se mantiene en una sola fila la actualizacion de estadisticas (id = 1)
    if stats is None:
        # Manejar el caso en el que no haya datos en statistics (cuando inicia el script)
        total_rows = 1
        total_sum_price = price
        min_price = price
        max_price = price

        cursor.execute("""
        INSERT INTO statistics (id, total_rows, total_sum_price, min_price, max_price)
        VALUES (1, %s, %s, %s, %s)
        """, (total_rows, total_sum_price, min_price, max_price))
    else:
        total_rows = stats['total_rows'] + 1
        total_sum_price = stats['total_sum_price'] + price
        min_price = min(stats['min_price'], price)
        max_price = max(stats['max_price'], price)

        cursor.execute("""
            UPDATE statistics
            SET total_rows = %s, total_sum_price = %s, min_price = %s, max_price = %s
            WHERE id = 1
        """, (total_rows, total_sum_price, min_price, max_price))

    conn.commit()

    # Imprimir estadísticas actualizadas después de cada fila insertada
    print(f"Estadísticas actualizadas: total_rows={total_rows}, avg_price={total_sum_price/total_rows:.2f}, min_price={min_price}, max_price={max_price}")




# Conectar a MySQL en RDS usando pymysql
conn = pymysql.connect(
    host="database-test-pragma.c14kkq4s62v9.us-east-1.rds.amazonaws.com",
    user="user_pragma",
    password="f!Nc$5JkuZ!enKmt",
    database="test_pragma",
    cursorclass=pymysql.cursors.DictCursor  # Para obtener los resultados como diccionarios
)
cursor = conn.cursor()

# Limpiar las tablas antes de procesar nuevos archivos , con la finalidad de correr el script sin acumular filas en las tablas
cursor.execute("DELETE FROM transactions")
cursor.execute("ALTER TABLE transactions AUTO_INCREMENT = 1")

cursor.execute("DELETE FROM statistics")
cursor.execute("ALTER TABLE statistics AUTO_INCREMENT = 1")
conn.commit()


## Agregar los archivos a la BD
# Procesar archivos en la carpeta "file"
for file in sorted(os.listdir("./file")):
    if file == "validation.csv":
        continue  # Ignorar validation.csv por ahora

    df = pd.read_csv(os.path.join("file", file))
    df = clean_data(df)  # Aplicar limpieza de datos

    for _, row in df.iterrows():
        cursor.execute("INSERT INTO transactions (timestamp, price, user_id) VALUES (%s, %s, %s)",
                       (row['timestamp'], row['price'], row['user_id']))
        update_statistics(row['price'])

    conn.commit()
    print(f"------------------------ Archivo {file} procesado. ------------------------ \n")



# Mostrar estadísticas después de cargar los archivos CSV
print("\nEstadísticas DESPUÉS de procesar todos los archivos CSV:")
print_statistics()


### Validacion
# Procesar validation.csv
print("\nProcesando validation.csv...")
df_val = pd.read_csv("file/validation.csv")
# Limpieza de datos
df_val = clean_data(df_val)

for _, row in df_val.iterrows():
    cursor.execute("INSERT INTO transactions (timestamp, price, user_id) VALUES (%s, %s, %s)",
                   (row['timestamp'], row['price'], row['user_id']))
    update_statistics(row['price'])

conn.commit()
print(f"------------------------ Archivo {file} procesado. ------------------------ \n")


# Mostrar estadísticas finales después de validation.csv
print("\nEstadísticas DESPUÉS de procesar validation.csv:")
print_statistics()

# Cerrar conexión
cursor.close()
conn.close()
        
