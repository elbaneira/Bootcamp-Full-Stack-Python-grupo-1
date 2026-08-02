# =====================================================================
# EJERCICIO: PRESUPUESTO DE COMBUSTIBLE PARA VIAJE
# =====================================================================

# PASO 1: Solicitar los datos al usuario (usamos float para decimales)
distancia = float(input("Ingrese la distancia total del viaje (en km): "))
rendimiento = float(input("Ingrese el rendimiento del vehículo (km por litro): "))
precio_litro = float(input("Ingrese el precio actual del litro de combustible: "))

# PASO 2: Realizar los cálculos matemáticos
litros_necesarios = distancia / rendimiento
costo_total = litros_necesarios * precio_litro

# PASO 3: Mostrar los resultados de forma clara y ordenada
print("\n" + "="*40)
print("     PRESUPUESTO ESTIMADO DE VIAJE     ")
print("="*40)
print(f"- Combustible necesario: {litros_necesarios:.2f} litros")
print(f"- Costo total estimado:  ${costo_total:.2f}")
print("="*40)