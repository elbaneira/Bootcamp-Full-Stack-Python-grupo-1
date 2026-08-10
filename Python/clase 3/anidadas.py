#Estructuras anidadas
alumnos = [
    [("Juan", "11.111.111-1"), [5.0, 6.0, 6.6]],
    [("Ana", "22.222.222-2"), [7.0, 4.5, 6.6]],
    [("Pedro", "33.333.333-3"), [5.8, 5.7, 6.1]]
]

#print(alumnos)

for i in range(len(alumnos)):
    #print(alumnos[i])
    #print(f"Datos personales: {alumnos[i][0]}")
    #print(f"Notas: {alumnos[i][1]}")

    print(f"Nombre: {alumnos[i][0][0]}")
