# Pedir las notas al estudiante
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

# 2. Calcular el promedio usando paréntesis para la suma y dividiendo por 3
promedio = (nota1 + nota2 + nota3) / 3

# 3. Mostrar el resultado final
# Redondea el promedio a solo 2 decimales
promedio_corto = round(promedio, 2)

print("El promedio de las notas es:", promedio_corto)

# 2f hace la magia de cortar al segundo decimal automáticamente al imprimir
print(f"El promedio de las notas es: {promedio:.2f}")