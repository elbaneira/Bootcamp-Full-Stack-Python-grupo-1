# 1. Pedir la cantidad (4)
cantidad = int(input("¿Cuántas veces quiere repetir el mensaje?: "))

# 2. Creamos nuestro CONTADOR manual y lo iniciamos en 1 (contador = 1)

# 3. Creamos una lista manual para que el FOR tenga de dónde sacar vueltas.
# Si el usuario quiere 4 repeticiones, necesitamos una lista con 3 elementos.
lista_vueltas = [1, 2, 3,4] 

# 4. El ciclo FOR recorre la lista elemento por elemento
for vuelta in lista_vueltas:
    
    # Mostramos el mensaje usando nuestro contador manual
    print(f"{contador}. - Aprendiendo Python")
    
    # ¡LA LÍNEA CLAVE! Le sumamos 1 al contador para la próxima vuelta
    contador = contador + 1