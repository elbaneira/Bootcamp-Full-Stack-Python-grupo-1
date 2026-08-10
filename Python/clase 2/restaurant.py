# Pedir las 3 entradas (personas es número entero, el resto texto)
cantidad_personas = int(input("¿Cuántas personas son?: "))
tiene_reserva = input("¿Tiene reserva previa? (si/no): ")
llega_a_tiempo = input("¿Llegará antes de las 22:00 horas? (si/no): ")

# ---------------------------------------------------------------------
# ENTRADA 1: Validar el tamaño del grupo
# ---------------------------------------------------------------------
if cantidad_personas <= 6:
    
    # -----------------------------------------------------------------
    # ENTRADA 2: Si caben en la mesa, revisamos si tienen reserva
    # -----------------------------------------------------------------
    if tiene_reserva == "si":
        
        # -------------------------------------------------------------
        # ENTRADA 3: Si tienen reserva, revisamos la hora
        # -------------------------------------------------------------
        if llega_a_tiempo == "si":
            print("Reserva aceptada")
        else:
            print("Reserva cancelada por atraso")
        # -------------------------------------------------------------
        
    else:
        # Este else responde a: ¿Qué pasa si NO tenía reserva?
        print("Debe esperar disponibilidad")
    # -----------------------------------------------------------------

else:
    # Este else está alineado con el PRIMER 'if'.
    # Responde a: ¿Qué pasa si eran más de 6 personas?
    print("No hay mesas disponibles para grupos grandes")