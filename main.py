import csv

name_table = "Product"
# Abrir el archivo CSV y el archivo .sql para escritura
with open('ens-catalogs-data - products-prep.csv', 'r') as archivo_csv, open('sentencias.sql', 'w') as archivo_sql:
    lector_csv = csv.DictReader(archivo_csv)
    # Iterar sobre cada fila del archivo CSV
    for fila in lector_csv:
        name= fila['product_name'].replace("'", "")
        if not name:
            print ("Ya acabo")
            break
        # Crear la sentencia INSERT INTO
        sentencia = "INSERT INTO "+ name_table+" (`id`, `brandId`, `name`,`model`,`baseCost`,`measuringUnitId`,`isActive`,`isKit`) VALUES ({}, {}, `{}`, '{}', {}, {}, {}, {});\n".format(
            fila['id'], fila['brandId'],name,fila['model'],fila['baseCost'],fila['measuringUnitId'],fila['isActive'],fila['isKit'])
        # Escribir la sentencia en el archivo .sql
        archivo_sql.write(sentencia)
