# Lista para almacenar distintos nombres de productos (strings)
#1 Mostrar todos los productos registrados.
productos = ["Camarón", "Salmón", "Merluza", "Atún"]

print("Cantidad de productos:",len(productos))

elimina = input("Ingrese un  producto a eliminar: ")

#productos.remove(elimina)

print("Producto eliminado")

nueva = input("Ingrese un nuevo producto: ")

productos.append(nueva)

print(productos)

#elimina = input("Ingrese un  producto a eliminar: ")

productos.remove(elimina)

print(productos)

print(productos[0])


