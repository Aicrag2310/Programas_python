import csv

name_table = "ProductSupplier"
# Abrir el archivo CSV y el archivo .sql para escritura
with open('CSV/beauty.csv', 'r') as archivo_csv, open('sentencias2.sql', 'w') as archivo_sql:
    lector_csv = csv.DictReader(archivo_csv)
    # Iterar sobre cada fila del archivo CSV
    for fila in lector_csv:
        name= fila['product_name'].replace("'", "")
        if not name:
            print ("Ya acabo")
            break
        # Crear la sentencia INSERT INTO
        sentencia = "INSERT INTO "+ name_table+" (`productId`, `priceCost`, `supplierId`) VALUES ({}, {}, {});\n".format(
            fila['id'],fila['baseCost'],fila['supplierId'])
        # Escribir la sentencia en el archivo .sql
        archivo_sql.write(sentencia)
