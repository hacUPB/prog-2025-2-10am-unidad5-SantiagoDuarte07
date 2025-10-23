# Solicitamos al usuario el nombre del archivo a crear
nombre_archivo = input("Ingrese el nombre del archivo de texto: ")
ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivo"
# Usamos 'with' para crear el contexto y escribir datos en el archivo 
with open(ubicacion+"\\"+nombre_archivo, 'w') as archivo:
    # Solicitamos al usuario los datos a escribir en el archivo
    datos = input("Ingrese su nombre: ")
    Cancion = input("ingrese su cancion favorita: ")
    archivo.write(datos)
    archivo.write("\n")
    archivo.write(Cancion)

# Ahora usamos 'with' para crear el contexto donde leer los datos del archivo
with open(ubicacion+"\\"+nombre_archivo, 'r') as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)