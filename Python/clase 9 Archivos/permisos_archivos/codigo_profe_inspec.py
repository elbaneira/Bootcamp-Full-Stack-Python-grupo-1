import os

# 2. Solicitar al usuario la ruta o nombre del archivo
nombre_archivo = input("Ingresa el nombre o ruta del archivo: ")

# 3. Intentar abrir el archivo en modo "r" usando try/except
try:
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    
    # 4. Mostrar atributos básicos del archivo
    print(f"Nombre del archivo: {archivo.name}")
    print(f"Modo de apertura: {archivo.mode}")
    print(f"Estado de cierre (antes): {archivo.closed}")
    
    # 5. Obtener el tamaño usando os.stat().st_size
    tamano = os.stat(nombre_archivo).st_size
    print(f"Tamaño en bytes: {tamano}")
    
    print("\n--- Contenido del archivo ---")
    # 6. Según el tamaño leer de forma distinta
    if tamano < 500:
        # a. Si es pequeño -> leer todo con read()
        contenido = archivo.read()
        print(contenido)
    else:
        # b. Si es grande -> usar readline() en un bucle
        linea = archivo.readline()
        while linea:
            print(linea, end="")  # end="" evita saltos de línea dobles
            linea = archivo.readline()
    print("\n-----------------------------")
    
    # 7. Cerrar el archivo
    archivo.close()
    
    # 8. Confirmar que el archivo está cerrado (.closed)
    print(f"Estado de cierre (después): {archivo.closed}")

# 9. En caso de error (archivo no encontrado), mostrar mensaje claro
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe. Verifica la  ruta.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")