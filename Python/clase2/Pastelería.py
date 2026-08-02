# =====================================================================
# EJERCICIO: CÁLCULO DE INGREDIENTES PARA PASTELERÍA
# =====================================================================

# 1. Solicitar la cantidad de pasteles al usuario
cantidad_pasteles = int(input("¿Cuántos pasteles iguales deseas preparar?: "))

# 2. Definir las cantidades base para UN solo pastel
HUEVOS_POR_PASTEL = 3
HARINA_POR_PASTEL = 250      # en gramos
AZUCAR_POR_PASTEL = 200      # en gramos
MANTEQUILLA_POR_PASTEL = 150  # en gramos
LECHE_POR_PASTEL = 200       # en mililitros

# 3. Calcular el total multiplicando la base por la cantidad de pasteles
total_huevos = HUEVOS_POR_PASTEL * cantidad_pasteles
total_harina = HARINA_POR_PASTEL * cantidad_pasteles
total_azucar = AZUCAR_POR_PASTEL * cantidad_pasteles
total_mantequilla = MANTEQUILLA_POR_PASTEL * cantidad_pasteles
total_leche = LECHE_POR_PASTEL * cantidad_pasteles

# 4. Mostrar los resultados de forma clara y ordenada
print("\n" + "="*40)
print(f" REPORTE DE INGREDIENTES PARA {cantidad_pasteles} PASTELES")
print("="*40)
print(f"- Huevos:      {total_huevos} unidades")
print(f"- Harina:      {total_harina} gramos")
print(f"- Azúcar:      {total_azucar} gramos")
print(f"- Mantequilla: {total_mantequilla} gramos")
print(f"- Leche:       {total_leche} mililitros")
print("="*40)