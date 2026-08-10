# =====================================================================
# EJERCICIO: CONTROL DE ACCESO A LA PISCINA
# =====================================================================

# PASO 1: Solicitar la edad al usuario (usamos int para números enteros)
edad = int(input("Por favor, ingrese su edad: "))

# PASO 2: Evaluar la condición usando IF / ELSE
if edad >= 12:
    # Bloque que se ejecuta si tiene 12 años o más
    print("¡Acceso PERMITIDO! Puedes ingresar a la piscina de adultos.")
else:
    # Bloque que se ejecuta si es menor de 12 años
    print("Acceso DENEGADO. Eres menor de 12 años, debes usar la piscina infantil.")

# Esta línea está fuera del condicional y siempre se mostrará
print("Gracias por usar el sistema de control.")