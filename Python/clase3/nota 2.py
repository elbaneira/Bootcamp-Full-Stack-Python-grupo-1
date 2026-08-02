


cantidad = int(input("Ingrese la cantidad de notas: "))

# 1. Creamos los contadores en 0
aprobados = 0
reprobados = 0

# 2. El ciclo for se mantiene igual para pedir las notas
for contador in range(1, cantidad + 1):
    nota = float(input(f"Ingrese la nota {contador}: "))

    # 3. Evaluamos CADA nota dentro del ciclo
    if nota >= 4.0:
        aprobados = aprobados + 1  # Si es 4.0 o más, sumamos a aprobados
    else:
        reprobados = reprobados + 1  # Si es menor, sumamos a reprobados

# --- Fuera del ciclo (al final del programa) ---

# 4. Mostramos los resultados totales
print(f"Cantidad de notas aprobadas: {aprobados}")
print(f"Cantidad de notas reprobadas: {reprobados}")