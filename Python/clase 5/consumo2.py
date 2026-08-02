
# Consumo de Agua

def convertir_a_mililitros(litros):
    return litros * 1000

def cumplio_meta(litros):
    return litros >= 2.0

def calcular_promedio(consumo):
    if not consumo:
        return 0.0
    return sum(consumo) / len(consumo)

def contar_dias_meta(consumo):
    dias_cumplidos = 0
    for litros in consumo:
        if cumplio_meta(litros):
            dias_cumplidos += 1
    return dias_cumplidos

def obtener_dia_mayor_consumo(consumo):
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    max_consumo = max(consumo)
    indice_max = consumo.index(max_consumo)
    return dias[indice_max]

def contar_dias_corte(consumo):
    """Cuenta cuántos días se registró 0 litros de consumo."""
    return consumo.count(0)

# PROGRAMA PRINCIPAL

def main():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    consumo = []

    print(" REGISTRO DE CONSUMO DE AGUA SEMANAL \n")

    # Lectura de datos
    for dia in dias:
        while True:
            try:
                litros = float(input(f"Ingrese los litros consumidos el {dia}: "))
                if litros < 0:
                    print(" Por favor, ingrese una cantidad válida (no negativa).")
                    continue
                consumo.append(litros)
                break
            except ValueError:
                print(" Entrada inválida. Debe ingresar un número.")

    # LLAMADAS A LAS FUNCIONES (Dentro de main)
    promedio = calcular_promedio(consumo)
    dias_cumplidos = contar_dias_meta(consumo)
    dia_maximo = obtener_dia_mayor_consumo(consumo)
    dias_sin_agua = contar_dias_sin_consumo_agua(consumo)  

    # Muestra de resultados
    print("\n" + "="*40)
    print("        RESULTADOS DE LA SEMANA")
    print("="*40)
    print(f"• Consumo promedio semanal: {promedio:.2f} litros ({convertir_a_mililitros(promedio):.0f} ml)")
    print(f"• Días que alcanzó la meta (≥ 2L): {dias_cumplidos} de 7 días")
    print(f"• Día con mayor consumo de agua: {dia_maximo}")
    
    # Advertencia de corte 
    if dias_sin_agua > 0:
        print(f"• Días con posible ausencia de agua (0L): {dias_sin_agua} día(s) ")
        
    print("="*40)

# Punto de entrada para ejecutar el programa
if __name__ == "__main__":
    main()