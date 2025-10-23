ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivo"
modo = "w"
nombre_archivo = "salida.csv"

Nombres = []
Edades = []
Ciudades = []

import csv

with open(ubicacion+"\\"+nombre_archivo, modo, newline='') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['Nombre', 'Edad', 'Ciudad'])  # Escribe la fila de encabezados
    escritor.writerow(['John', 25, 'Nueva York'])
    escritor.writerow(['Jane', 30, 'Los Ángeles'])
    
    
with open('C:\\Users\\B09S202est\\Desktop\\Archivo\\Salida.csv', 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile)
    encabezado = next(lector)   
    for fila in lector:
        nombre = fila[0]
        edad = fila[1]
        ciudad = fila[2]
        Nombres.append(nombre)
        Edades.append(edad)
        Ciudades.append(ciudad)


print(Nombres)
print(Edades)
print(Ciudades)