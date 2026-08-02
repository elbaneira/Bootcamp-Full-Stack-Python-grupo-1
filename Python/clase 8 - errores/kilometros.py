try:
    # Pedir kilómetros y convertir a número decimal
    kilometros = float(input("Ingresa la distancia en kilómetros: "))
    
    # Calcular las millas
    millas = kilometros * 0.621371
    
    # Mostrar resultado formateado a 2 decimales
    print(f"{kilometros} km equivalen a {millas:.2f} millas.")

except ValueError:
    # Mostrar mensaje si la entrada no es un número
    print("Debe ingresar un número válido.")

finally:
    print("Fin del proceso")    