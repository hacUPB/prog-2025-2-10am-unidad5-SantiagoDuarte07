import os, sys, csv

TIENE_MPL = True
try:
    import matplotlib.pyplot as plt
except Exception:
    TIENE_MPL = False

# ---------- Utilidades ----------
def limpiar(): 
    try: os.system("cls" if os.name=="nt" else "clear")
    except: pass

def pausa():
    try: input("\nEnter para continuar...")
    except: pass

def listar_archivos():
    print("\n1) Ruta actual\n2) Especificar ruta")
    op = input("Opción: ").strip()
    ruta = "." if op!="2" else input("Ruta: ").strip()
    try:
        print("\nContenido de:", os.path.abspath(ruta))
        for nombre in os.listdir(ruta): print(" -", nombre)
    except Exception as e: print("Error:", e)

# ---------- TXT ----------
def leer_txt(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f: return f.read()
    except Exception as e:
        print("No se pudo leer:", e); return None

def escribir_txt(ruta, texto):
    try:
        with open(ruta, "w", encoding="utf-8") as f: f.write(texto); return True
    except Exception as e:
        print("No se pudo escribir:", e); return False

def txt_contar(ruta):
    t = leer_txt(ruta); 
    if t is None: return
    # Palabras
    partes = t.split()
    n_pal = len(partes)
    # Caracteres
    con_esp = len(t)
    sin_esp = 0
    i = 0
    while i < len(t):
        if not t[i].isspace(): sin_esp += 1
        i += 1
    print("\nPalabras:", n_pal)
    print("Caracteres (con espacios):", con_esp)
    print("Caracteres (sin espacios):", sin_esp)

def txt_reemplazar(ruta):
    t = leer_txt(ruta)
    if t is None: return
    a = input("Palabra a buscar: ").strip()
    b = input("Reemplazar por: ").strip()
    if a=="": print("No puede ser vacía."); return
    if escribir_txt(ruta, t.replace(a, b)): print("Archivo actualizado.")

def txt_vocales(ruta):
    t = leer_txt(ruta)
    if t is None: return
    vocales = ["a","e","i","o","u"]; cont = [0,0,0,0,0]
    i = 0
    while i < len(t):
        c = t[i].lower()
        j = 0
        while j < 5:
            if c == vocales[j]: cont[j]+=1; break
            j += 1
        i += 1
    print("\nOcurrencias:")
    k = 0
    while k < 5: 
        print(" ", vocales[k], ":", cont[k]); k += 1
    if TIENE_MPL:
        plt.bar(vocales, cont); plt.title("Vocales"); plt.xlabel("Vocal"); plt.ylabel("Frecuencia"); plt.show()
    else:
        print("(Matplotlib no disponible, no se muestra gráfico)")

def submenu_txt():
    ruta = input("Ruta del .txt: ").strip()
    while True:
        print("\nTXT: 1) Contar  2) Reemplazar  3) Histograma vocales  4) Volver")
        op = input("Opción: ").strip()
        if op=="1": txt_contar(ruta); pausa()
        elif op=="2": txt_reemplazar(ruta); pausa()
        elif op=="3": txt_vocales(ruta); pausa()
        elif op=="4": break
        else: print("Opción inválida")

# ---------- CSV ----------
def abrir_csv(ruta):
    try:
        f = open(ruta, "r", newline="", encoding="utf-8")
        return f, csv.reader(f)
    except Exception as e: print("No se pudo abrir:", e); return None, None

def csv_head(ruta):
    f, r = abrir_csv(ruta)
    if r is None: return
    n = 0
    try:
        for fila in r:
            print(fila); n += 1
            if n>=15: break
    finally:
        try: f.close()
        except: pass

def leer_todo_csv(ruta):
    f, r = abrir_csv(ruta)
    if r is None: return None
    data = []
    try:
        for fila in r: data.append(fila)
    finally:
        try: f.close()
        except: pass
    return data

def idx_col(headers, entrada):
    if entrada.isdigit():
        i = int(entrada); 
        return i if 0 <= i < len(headers) else -1
    i = 0
    while i < len(headers):
        if headers[i] == entrada: return i
        i += 1
    return -1

def col_a_floats(filas, i):
    vals = []; k = 0
    while k < len(filas):
        fila = filas[k]
        if i < len(fila):
            s = fila[i].strip()
            if s != "":
                try: vals.append(float(s.replace(",", ".")))
                except: pass
        k += 1
    return vals

def stats_manuales(vals):
    n = len(vals)
    if n == 0:
        return (0, None, None, None, None, None)
    # promedio
    s = 0.0; i = 0
    while i < n: s += vals[i]; i += 1
    prom = s / n
    # mediana/min/max con sorted (builtin)
    ords = sorted(vals)
    mn, mx = ords[0], ords[-1]
    if n % 2 == 1: med = ords[n//2]
    else: med = (ords[n//2 - 1] + ords[n//2]) / 2.0
    # desviación (poblacional)
    sc = 0.0; i = 0
    while i < n:
        d = vals[i] - prom; sc += d*d; i += 1
    desv = (sc / n) ** 0.5
    return (n, prom, med, desv, mn, mx)

def csv_stats(ruta):
    datos = leer_todo_csv(ruta)
    if not datos: print("CSV vacío o no válido."); return
    headers = datos[0]; print("\nEncabezados:")
    i = 0
    while i < len(headers): 
        print("  [{}] {}".format(i, headers[i])); i += 1
    sel = input("Nombre o índice de columna: ").strip()
    i = idx_col(headers, sel)
    if i==-1: print("Columna no encontrada."); return
    filas = datos[1:]  # asume encabezado
    vals = col_a_floats(filas, i)
    n,prom,med,desv,mn,mx = stats_manuales(vals)
    print("\nCantidad:", n)
    print("Promedio:", prom)
    print("Mediana:", med)
    print("Desviación estándar (poblacional):", desv)
    print("Mínimo:", mn)
    print("Máximo:", mx)

def csv_graficar(ruta):
    if not TIENE_MPL:
        print("Matplotlib no disponible."); return
    datos = leer_todo_csv(ruta)
    if not datos: print("CSV vacío o no válido."); return
    headers = datos[0]; print("\nEncabezados:")
    i = 0
    while i < len(headers): 
        print("  [{}] {}".format(i, headers[i])); i += 1
    sel = input("Columna numérica (nombre o índice): ").strip()
    i = idx_col(headers, sel)
    if i==-1: print("Columna no encontrada."); return

    xs, ys = [], []
    filas = datos[1:]; idx = 0; k = 0
    while k < len(filas):
        fila = filas[k]
        if i < len(fila):
            s = fila[i].strip()
            if s != "":
                try:
                    y = float(s.replace(",", "."))
                    xs.append(idx); ys.append(y); idx += 1
                except: pass
        k += 1
    if len(ys)==0: print("No hay datos numéricos válidos."); return

    # Dispersión
    plt.figure(); plt.scatter(xs, ys)
    plt.title("Dispersión - {}".format(headers[i])); plt.xlabel("Índice"); plt.ylabel(headers[i]); plt.show()

    # Barras: frecuencias por 5 rangos
    mn, mx = min(ys), max(ys); bins = 5
    ancho = (mx - mn) / bins if bins>0 else 1
    etiquetas, cuentas = [], []
    b=0
    while b < bins:
        a = mn + b*ancho; c = mn + (b+1)*ancho if b<bins-1 else mx
        etiquetas.append("{:.2f}-{:.2f}".format(a, c)); cuentas.append(0); b += 1
    j = 0
    while j < len(ys):
        v = ys[j]; b = 0
        while b < bins:
            # parsea límites desde la etiqueta
            guion = etiquetas[b].find("-")
            li = float(etiquetas[b][:guion]); ls = float(etiquetas[b][guion+1:])
            if (v >= li and (v < ls or (b==bins-1 and v<=ls))):
                cuentas[b]+=1; break
            b += 1
        j += 1
    plt.figure(); plt.bar(etiquetas, cuentas)
    plt.title("Barras por rangos - {}".format(headers[i])); plt.xlabel("Rango"); plt.ylabel("Frecuencia")
    plt.xticks(rotation=45); plt.tight_layout(); plt.show()

def submenu_csv():
    ruta = input("Ruta del .csv: ").strip()
    while True:
        print("\nCSV: 1) Primeras 15  2) Estadísticas  3) Graficar  4) Volver")
        op = input("Opción: ").strip()
        if op=="1": csv_head(ruta); pausa()
        elif op=="2": csv_stats(ruta); pausa()
        elif op=="3": csv_graficar(ruta); pausa()
        elif op=="4": break
        else: print("Opción inválida")

# ---------- Menú principal ----------
def main():
    limpiar(); print("CLI Unidad 5 - Archivos y Visualización\n")
    if not TIENE_MPL:
        print("Aviso: matplotlib no está instalado; las opciones de gráficas mostrarán aviso.")
    while True:
        print("\n1) Listar archivos\n2) .TXT\n3) .CSV\n4) Salir")
        op = input("Opción: ").strip()
        if op=="1": listar_archivos(); pausa()
        elif op=="2": submenu_txt()
        elif op=="3": submenu_csv()
        elif op=="4": print("Adiós"); break
        else: print("Opción inválida")

if __name__=="__main__":
    try: main()
    except KeyboardInterrupt:
        print("\nInterrumpido."); sys.exit(0)
