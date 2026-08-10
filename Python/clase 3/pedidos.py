# Solicitar cantidad de pedidos
cantidad = int(input("¿Ingrese la cantidad de pedidos: "))

# Variables acumuladoras y contadoras
total_vendido = 0
entregados = 0
pendientes = 0

# Ciclo for
for i in range(cantidad):
    #completar ¿?
    nombre = input("Ingrese nombre del cliente: ")
    monto = float(input("Ingrese el monto del pedido: "))
    estado = input("¿Fue entregado correctamente? (S/N): ")
    #suma automática del monto
    total_vendido = total_vendido + monto
    #condiciones 
    if estado == "S" or estado == "s":
        entregados = entregados + 1
    else:
        pendientes = pendientes + 1

print("\nRESULTADOS")
print("Total vendido:", total_vendido)
print("Pedidos entregados:", entregados)
print("Pedidos pendientes:", pendientes)