import csv

# Abrir el archivo CSV y el archivo .sql para escritura
with open('ens-catalogs-data - products-prep.csv', 'r') as archivo_csv, open('sentencias.sql', 'w') as archivo_sql:
    lector_csv = csv.DictReader(archivo_csv)
    # Iterar sobre cada fila del archivo CSV
    for fila in lector_csv:
        # Eliminar comillas simples de la columna de nombres
        nombre = fila['nombre'].replace("'", "")
        # Crear la sentencia INSERT INTO
        sentencia = "INSERT INTO tabla ('nombre', 'apellido', 'edad') VALUES ('{}', '{}', {});\n".format(
            nombre, fila['apellido'], fila['edad'])
        # Escribir la sentencia en el archivo .sql
        archivo_sql.write(sentencia)