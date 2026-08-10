# ==========================================
# 1. Escribir en un archivo (modo 'w')
# ==========================================
print("--- 1. Escribiendo en el archivo ---")

# 'w' crea el archivo (o lo sobrescribe si ya existe)
archivo = open("datos.txt", "w", encoding="utf-8")

archivo.write("Línea 1: Bienvenidos al manejo de archivos en Python.\n")
archivo.write("Línea 2: Estamos aprendiendo a programar en el Bootcamp.\n")
archivo.write("Línea 3: Este archivo fue creado automáticamente.\n")

archivo.close()
print("¡Archivo 'datos.txt' creado y escrito con éxito!\n")


# ==========================================
# 2. Leer el archivo completo (modo 'r' con read())
# ==========================================
print("--- 2. Leyendo el archivo completo con read() ---")

archivo = open("datos.txt", "r", encoding="utf-8")
contenido_completo = archivo.read()
print(contenido_completo)
archivo.close()


# ==========================================
# 3. Leer línea por línea
# ==========================================
print("--- 3. Leyendo línea por línea ---")

archivo = open("datos.txt", "r", encoding="utf-8")

# Leer solo la primera línea con readline()
primera_linea = archivo.readline()
print("Primera línea leída:", primera_linea.strip())

print("\nResto del archivo leído con ciclo for:")
# El ciclo for continúa leyendo las líneas que quedan
for linea in archivo:
    print(linea.strip())

archivo.close()
print()


# ==========================================
# 4. Añadir contenido (modo 'append' / 'a')
# ==========================================
print("--- 4. Añadiendo contenido con modo append ('a') ---")

# 'a' abre el archivo sin borrar lo anterior, agregando al final
archivo = open("datos.txt", "a", encoding="utf-8")
archivo.write("Línea 4: Esta línea fue agregada usando el modo append.\n")
archivo.close()

# Comprobamos abriéndolo nuevamente en modo lectura ('r')
print("Comprobando el contenido actualizado:")
archivo = open("datos.txt", "r", encoding="utf-8")
print(archivo.read())
archivo.close()

# ==========================================
# 5. Atributos y cierre del archivo
# ==========================================
print("--- 5. Atributos y estado del archivo ---")

# Abrimos el archivo nuevamente solo para consultar sus propiedades
archivo = open("datos.txt", "r", encoding="utf-8")

# Mostrar nombre, estado y modo
print(f"Nombre del archivo: {archivo.name}")
print(f"¿Está cerrado?: {archivo.closed}")
print(f"Modo de apertura: {archivo.mode}")

# Cerramos el archivo correctamente con .close()
archivo.close()