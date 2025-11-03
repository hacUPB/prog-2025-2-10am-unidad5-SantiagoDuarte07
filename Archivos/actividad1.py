
archivo = open("./Archivos/texto2.txt","r")
'''
for i in range(3):
    datos = archivo.readline()
print(datos[12:])
'''
archivo.seek()
datos = archivo.readline()
archivo.close()