# 1. Cree un programa en Python que solicite al usuario la cantidad de notas 
# que desea ingresar. Luego, usando un ciclo for con contador, el programa 
# debe pedir cada nota una por una.

# Al finalizar, el programa debe calcular y mostrar el promedio de las notas 
# ingresadas. Además, debe indicar si el estudiante aprueba o reprueba, 
# considerando que aprueba con promedio mayor o igual a 4.0.

cantidad = int(input("Ingrese la cantidad de notas: "))
suma = 0

for contador in range(1, cantidad + 1):
    nota = float(input(f"Ingrese la nota {contador}: "))

    suma = suma + nota

promedio = round(suma / cantidad, 1)

print(f"El promedio es: {promedio}")

if promedio >= 4.0:
    print("Aprobado(a)")
else:
    print("Reprobado(a)")

