archivo = open("datos.txt", "a", encoding="utf-8")
archivo.write("Cuarta línea agregada en modo append\n")
archivo.close()

archivo = open("datos.txt", "r", encoding="utf-8")
print("Contenido después de agregar una nueva línea:")
print(archivo.read())
archivo.close()