# 1. Pedir las 3 notas al usuario (usamos float por los decimales)
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

# 2. Calcular el promedio
promedio = (nota1 + nota2 + nota3) / 3


# =====================================================================
# APUNTES DE ELBA: MANERAS DE MOSTRAR DECIMALES
# =====================================================================

# MANERA 1: Usando f-strings (La activa, borra la pantalla limpia)
print(f"El promedio de las notas es: {promedio:.2f}")

# MANERA 2: Usando round() (La dejo comentada con '#' para recordar)
# promedio_corto = round(promedio, 2)
# print("El promedio de las notas es:", promedio_corto)