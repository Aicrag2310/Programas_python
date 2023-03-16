import csv

name_table = "Inventory"
# Abrir el archivo CSV y el archivo .sql para escritura
with open('CSV/beauty.csv', 'r') as archivo_csv, open('sentencias4.sql', 'w') as archivo_sql:
    lector_csv = csv.DictReader(archivo_csv)
    # Iterar sobre cada fila del archivo CSV
    for fila in lector_csv:
        name= fila['product_name'].replace("'", "")
        if not name:
            print ("Ya acabo")
            break
        # Crear la sentencia INSERT INTO
        sentencia = "INSERT INTO "+ name_table+" (`productId`, `quantity`, `minQuantity`,`maxQuantity`,`storeId`) VALUES ({}, {}, {}, {}, {});\n".format(
            fila['id'], 0,0,fila['quantity'],1)
        # Escribir la sentencia en el archivo .sql
        archivo_sql.write(sentencia)
