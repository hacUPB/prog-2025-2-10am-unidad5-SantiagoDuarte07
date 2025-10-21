nombre_archivo = "./Archivos/texto.txt"
ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivo"
with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    lista = archivo.readlines()

for c in lista:
    print(c)