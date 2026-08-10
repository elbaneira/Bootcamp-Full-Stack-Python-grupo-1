print("=== LEER CON READLINES ===")
archivo = open("prueba.txt", "r", encoding="utf-8")

# Guarda cada línea como un elemento de una lista
lineas = archivo.readlines() 

# Imprime la lista completa para ver su estructura
print(lineas) 

archivo.close()