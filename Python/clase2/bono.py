# Si vende más de $1.000.000, recibirá $75.000. 
# Si vende entre $400.000 y $1.000.000, recibirá $50.000. 
# En cualquier otro caso, recibirá $0.



# 1. Qué monto total de ventas tiene el vendedor?
ventas = int(input("Ingrese el monto total de sus ventas: $"))

# 2. Tramos de bonos
if ventas > 1000000:
    bono = 75000

elif ventas >= 400000:
    # este ELIF cubre  el tramo entre 400.000 y 1.000.000.
    bono = 50000

else:
    # Cualquier otro caso (ventas menores a 400.000)
    bono = 0

# 3. Mostrar el resultado final
print(f"Su comisión final es de: ${bono}")