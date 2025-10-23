import csv

with open('C:\\Users\\B09S202est\\Desktop\\Archivo\\Variables.csv', 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile, delimiter=";") 
    encabezado = next(lector)
    print(encabezado[3])
    densidad = []                             #se utiliza el método reader
    for fila in lector:
        fila[3] = fila[3].replace(',', '.')
        dato = float(fila[3])
        densidad.append(dato)          #con el for se itera sobre el objeto para leer
         
print(densidad)
