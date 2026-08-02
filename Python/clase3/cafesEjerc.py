#  Ejercicio de métodos de lista
pedidos = ["Café americano", "Té verde", "Capuchino", "Chocolate caliente", "Café latte"]
# 1 Copia de la lista
respaldo_pedidos = pedidos.copy()

# 2. Agregar al final
pedidos.append("Espresso")

# 3. Insertar en posición específica (índice 1)
pedidos.insert(1, "Mocaccino urgente")

# 4. Eliminar por nombre
pedidos.remove("Té verde")

# 5. Eliminar el último de la lista
pedidos.pop()

# 6. Ordenar alfabéticamente
pedidos.sort()

# 7. Cantidad total de elementos
total = len(pedidos)
print(f"7. Cantidad total de pedidos: {total}")

# 8. Buscar posición de un elemento
posicion = pedidos.index("Capuchino")
print(f"8. El Capuchino está en el índice/posición: {posicion}")

# 9. Comprobación final
print("\n9. RESULTADO FINAL DE LAS LISTAS:")
print("-> Lista modificada actual:", pedidos)
print("-> Lista original (respaldo):", respaldo_pedidos)




#Métodos como append(), insert(), remove() y sort() 
#realizan un trabajo interno dentro de la computadora: alteran la 
#lista directamente en segundo plano.
#No generan una respuesta visual por sí mismos.
#"Si intentaras hacer un print() de esa acción, como por ejemplo: