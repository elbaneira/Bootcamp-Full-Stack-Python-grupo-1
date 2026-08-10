# 1. Pedir los datos iniciales al usuario
horas = int(input("Ingrese las horas: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))

# 1  hora tiene 3600 segundos (60 * 60)
# 1 minuto tiene 60 segundos
segundos_totales = (horas * 3600) + (minutos * 60) + segundos

print(f"Todo convertido a SEGUNDOS: {segundos_totales} seg.")

