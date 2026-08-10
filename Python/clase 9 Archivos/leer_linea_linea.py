print("=== LEER LÍNEA POR LÍNEA ===")
archivo = open("prueba.txt", "r", encoding="utf-8")

primera_linea = archivo.readline()
print("Primera línea:")
print(primera_linea)

print("Resto del archivo:")
for linea in archivo:
    print(linea, end="")

archivo.close()
print("\n")