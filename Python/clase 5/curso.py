#Lista de cursos
cursos= [
    {
        "nombre": "Python",
        "duracion": 40,
        "estudiantes": 25,
        "estado": "Disponible"
    },
    {
        "nombre": "JavaScript",
        "duracion": 40,
        "estudiantes": 30,
        "estado": "Completo"
    },
    {
        "nombre": "Diseño Web",
        "duracion": 25,
        "estudiantes": 20,
        "estado": "Disponible"
    },
    {
        "nombre": "Marketing Digital",
        "duracion": 20,
        "estudiantes": 35,
        "estado": "Completo"
    },
    {
        "nombre": "Bases de Datos",
        "duracion": 35,
        "estudiantes": 15,
        "estado": "Disponible"
    }
]   

#Saludo
print("=================================================")
print("   BIENVENIDO AL REGISTRO DE CURSOS")
print("=================================================")

# 1. Mostrar todos los cursos
print("\n=== Cursos registrados: ===\n")
for curso in cursos:
    print("Nombre:", curso["nombre"])
    print("Duración (horas):", curso["duracion"])
    print("Estudiantes inscritos:", curso["estudiantes"])
    print("Estado:", curso["estado"])
    print("----------------------------------------------")

# 2. Mostrar cursos disponibles
print("\n=== Cursos disponibles: ===\n")
for curso in cursos:
    if curso["estado"] == "Disponible":
       print("* Nombre Curso:", curso["nombre"])

# 3. Agregar un nuevo curso
nuevo_curso = {
    "nombre": "Inteligencia Artificial",
    "duracion": 50,
    "estudiantes": 10,
    "estado": "Disponible"
}
# Agregar el nuevo curso a la lista de cursos
cursos.append(nuevo_curso)
print("\n=== Nuevo curso agregado: ===\n")
print("Nombre:", nuevo_curso["nombre"])
print("Duración (horas):", nuevo_curso["duracion"])
print("Estudiantes inscritos:", nuevo_curso["estudiantes"])
print("Estado:", nuevo_curso["estado"])

# 4. Modificar cantidad de estudiantes de un curso
print("\n=== Actualización de estudiantes ===\n")
actualizar = input("¿Desea actualizar el número de estudiantes de un curso? (Si/No): ")

while actualizar != "Si" and actualizar != "No":
    actualizar = input("Respuesta inválida. Ingrese Si o No: ")

    for curso in cursos:
        if curso["nombre"] == nombre_curso:

            print("\nCurso encontrado:")
            print("* Nombre:", curso["nombre"])
            print("* Estudiantes actuales:", curso["estudiantes"])

            nuevos_estudiantes = int(input("Ingrese la nueva cantidad de estudiantes: "))

            curso["estudiantes"] = nuevos_estudiantes

            print("\n=== Curso actualizado correctamente ===\n")
            print("* Curso:", curso["nombre"])
            print("* Nueva cantidad de estudiantes:", curso["estudiantes"])
            break

    else:
        print("No se encontró el curso.")

else:
    print("No se realizaron cambios.")

# 5. Cambiar el estado de un curso
print("\n=== Cambio de estado de un curso ===\n")
nombre_curso = input("Ingrese el nombre del curso a modificar: ")

for curso in cursos:
    if curso["nombre"] == nombre_curso:

        print("\nCurso encontrado:")
        print("* Nombre:", curso["nombre"])
        print("* Estado actual:", curso["estado"])

        nuevo_estado = input("Ingrese el nuevo estado del curso (Disponible/Completo): ")

        if nuevo_estado in ["Disponible", "Completo"]:
            curso["estado"] = nuevo_estado
            print("\nEstado del curso actualizado correctamente.")
            print("* Curso:", curso["nombre"])
            print("* Nuevo estado:", curso["estado"])
        else:
            print("Estado inválido. No se realizaron cambios.")
        break

# 6. Eliminar un curso
print("\n=== Eliminación de un curso ===\n")
eliminar = input("¿Desea eliminar un curso? (Si/No): ")

if eliminar == "Si":
    nombre_curso = input("Ingrese el nombre del curso a eliminar: ")

    for curso in cursos:
        if curso["nombre"] == nombre_curso:
            cursos.remove(curso)
            print("\nCurso eliminado correctamente.")
            break
    else:
        print("No se encontró el curso.")

# 7. Contar cantidad de cursos dispònibles
cantidad_disponibles = 0
for curso in cursos:
    if curso["estado"] == "Disponible":
        cantidad_disponibles += 1

print("\n=== Cantidad de cursos disponibles ===\n")
print("Total de cursos disponibles:", cantidad_disponibles)

#8. Mostrar cursos que duren mas de 30 horas
print("\n=== Cursos con duración mayor a 30 horas ===\n")
for curso in cursos:
    if curso["duracion"] > 30:
        print("* Nombre Curso:", curso["nombre"])
        print("* Duración:", curso["duracion"], "horas")
        print("--------------------------------------------------")

# 9. Calcular total de estudiantes registrados
total_estudiantes = 0
for curso in cursos:
    total_estudiantes += curso["estudiantes"]

print("\n=== Total de estudiantes registrados ===\n")
print("Total de estudiantes:", total_estudiantes)

#10. Mostrar lista actualizada
print("\n=== Lista final de cursos===\n")
for curso in cursos:
    print("* Nombre:", curso["nombre"])
    print("* Duración:", curso["duracion"], "horas")
    print("* Estudiantes:", curso["estudiantes"])
    print("* Estado:", curso["estado"])
    print("------------------------------------------")


print("=================================================")
print("¡Gracias por utilizar el sistema! :)")
print("=================================================")
