#TUPLAS
tupla = ("Galletas", 3000)
tupla2 = ("Harina", 2000)

# muestra la tupla
print(tupla)

print(tupla2)

# muestra un elemento de la tupla, dada su posición 
#print(tupla[0])

# muestra la cantidad de elementos de la tupla
#print(len(tupla))

# esto da error. las tuplas son inmutables
#tupla[0] = "Harina"

tupla3 = tupla + tupla2

print(tupla3)

lista = ["ejemplo"]

# agregamos a la lista los elemento de la tupla 
lista.extend(tupla2)

print(lista)
