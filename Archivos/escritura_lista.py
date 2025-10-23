Lista = ["Orion","Hacia falta yo", "Korazong", "noche de arreboles", "lo dudo"]
ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivo"
modo = "w"
nombre_archivo = "canciones.txt"
fp = open(ubicacion+"\\"+nombre_archivo, modo, encoding="utf-8")
for cancion in Lista:
    fp.write(cancion+"\n")
fp.close()