import os

print("=== INSPECTOR DE ARCHIVOS ===")

# 1. Solicitar al usuario el nombre o ruta del archivo
nombre_archivo = input("Ingresa el nombre del archivo a inspeccionar (ej: datos.txt): ")

try:
    # 2. Intentar abrir el archivo en modo lectura ("r") usando try/except
    # 3. Obtener el tamaño en bytes usando os.stat().st_size
    tamanio_bytes = os.stat(nombre_archivo).st_size
    
    # Abrimos el archivo
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    
    print("\n--- ATRIBUTOS BÁSICOS ---")
    print(f"Nombre (.name): {archivo.name}")
    print(f"Modo (.mode): {archivo.mode}")
    print(f"¿Está cerrado? (.closed): {archivo.closed}")
    print(f"Tamaño del archivo: {tamanio_bytes} bytes")
    
    print("\n--- CONTENIDO DEL ARCHIVO ---")
    # 4. Condición según el tamaño (< 500 bytes vs >= 500 bytes)
    if tamanio_bytes < 500:
        print("(El archivo es pequeño, se lee completo con read())\n")
        contenido = archivo.read()
        print(contenido)
    else:
        print("(El archivo es grande, se lee línea por línea con readline())\n")
        # Usamos un bucle para recorrer todo el archivo línea por línea
        for linea in archivo:
            print(linea.strip())
            
    # 5. Cerrar el archivo correctamente
    archivo.close()
    
    print("\n--- ESTADO FINAL ---")
    print(f"¿Fue cerrado correctamente? (.closed): {archivo.closed}")

except FileNotFoundError:
    # 6. Manejo de errores si el archivo no existe
    print(f"\n[ERROR]: El archivo '{nombre_archivo}' no fue encontrado. Por favor, verifica el nombre e intenta nuevamente.")