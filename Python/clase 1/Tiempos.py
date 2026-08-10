# =====================================================================
# EJERCICIO: CONVERSIONES DE TIEMPO (Horas, Minutos y Segundos)
# =====================================================================

# 1. Pedir los datos iniciales al usuario
horas = int(input("Ingrese las horas: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))

print("-" * 40) # Una línea decorativa para ordenar la consola

# ---------------------------------------------------------------------
# PARTE A: CONVERTIR TODO A SEGUNDOS (Multiplicamos)
# ---------------------------------------------------------------------
# 1 hora tiene 3600 segundos (60 * 60)
# 1 minuto tiene 60 segundos
segundos_totales = (horas * 3600) + (minutos * 60) + segundos

print(f"Todo convertido a SEGUNDOS: {segundos_totales} seg.")


# ---------------------------------------------------------------------
# PARTE B: CONVERTIR TODO A MINUTOS (Dividimos y multiplicamos)
# ---------------------------------------------------------------------
# Las horas se multiplican por 60 para ser minutos.
# Los segundos se dividen por 60 para ser minutos.
minutos_totales = (horas * 60) + minutos + (segundos / 60)

print(f"Todo convertido a MINUTOS: {minutos_totales:.2f} min.")


# ---------------------------------------------------------------------
# PARTE C: CONVERTIR TODO A HORAS (Dividimos)
# ---------------------------------------------------------------------
# Los minutos se dividen por 60.
# Los segundos se dividen por 3600.
horas_totales = horas + (minutos / 60) + (segundos / 3600)

print(f"Todo convertido a HORAS: {horas_totales:.4f} hrs.")
# ---------------------------------------------------------------------