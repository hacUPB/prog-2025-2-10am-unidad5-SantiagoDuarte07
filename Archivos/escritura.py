ubicacion = "C:\\Users\\B09S202est\\Desktop\\Archivo"
# \ se usa para comandos de texto
nombre_archivo = "Frutas3.txt"
modo = "x" #solo escritura - sobreescribe
fp = open(ubicacion+"\\"+nombre_archivo, modo, encoding="utf-8")
frase = input("por favor ingresa una frase: ")
#solicitar una variable entera y una float al usuario y la escriben en el archivo
edad = int(input("Ingrese su edad: "))
estatura = float(input("Ingrese su estatura: "))
fp.write(frase + "\n")                
fp.write(str(edad))
fp.write("\n")
fp.write(str(estatura))

fp.close()