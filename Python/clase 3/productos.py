# Ejercicio. Registro de productos en una compra

#Cree un programa en Python que solicite al usuario cuántos productos comprará. 
# Luego, usando un ciclo for con contador, el programa debe pedir el precio de cada producto.

#Al finalizar, el programa debe mostrar el total a pagar. Además, si el total es mayor o 
# igual a $50.000, debe aplicar un descuento del 10% y mostrar el total final con descuento.

productos = int(input("Ingrese la cantidad de productos: "))
suma = 0

for contador in range(1, productos + 1):
    precio = float(input(f"Ingrese el precio del producto {contador}: "))
    suma = suma + precio

total = round(suma, 1)

print(f"El total es: ${total}")

# Aquí corregimos el 50000 sin punto
if total >= 50000:
    dscto = total * 0.10
    total_con_dscto = total - dscto
    print(f"¡Se aplicó un 10% de descuento! El total final es: ${total_con_dscto}")