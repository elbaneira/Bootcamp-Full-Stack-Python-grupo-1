# Lista para almacenar distintos nombres de frutas (strings)
frutas = ["Naranja", "Pera", "Manzana", "Frambuesa", "Uva", "Melón", "Mandarina", "Piña", "Plátano"]

print(frutas)

# crea una nueva lista independiente a partir de la original
nueva_lista = frutas.copy()

print(nueva_lista)

frutas.append("Mora")
nueva_lista.append("Frutilla")

print(frutas)
print(nueva_lista)

# consulto si determinada fruta se encuentra en la lista
#if frutas.count("Arándano") > 0:
#    print("El arándano sí se encuentra en la lista")
#else:
#    print("El arándano no se encuentra en la lista")

# nueva = input("Ingrese una nueva fruta: ")

# agrega un elemento al final de la lista
#frutas.append(nueva)

# agrega un elemento en la posici+on indicada
#frutas.insert(3, nueva)

#print(frutas)

# elimina el elemento de la posición indicada
#frutas.pop(5)

# elimina todos los elementos. La lista queda vacía
#frutas.clear()

# entrega el índice del elemento indicado
#print(frutas.index("Plátano"))

# devuelve la cantidad de veces en que se encuentra el valor dentro de la lista
#print(frutas.count("Piña"))

# ordena ascendentemente los elementos de la lista
#frutas.sort()

#print(frutas)

# ordena descendentemente los elementos de la lista
#frutas.reverse()

#print(frutas)

# agrega otra lista al final de la original
#frutas.extend(["Sandía", "Mango", "Níspero", "Membrillo", "Mora"])

#print(frutas)

#elimina = input("Ingrese una fruta a eliminar: ")

# elimina el primer elemento con el valor indicado
#frutas.remove(elimina)

#print(frutas)

# accede al elemento de la posición indicada
#print(frutas[0])

# muestra la cantidad de elementos de la lista
#print(len(frutas))

#print(frutas[100]) # Esto da error

#for i in range(9):
#    print(frutas[i])

#for i in range(len(frutas)):
#    print(frutas[i])

#i = 0
#while i < len(frutas):
#    print(frutas[i])
#
#    i += 1


