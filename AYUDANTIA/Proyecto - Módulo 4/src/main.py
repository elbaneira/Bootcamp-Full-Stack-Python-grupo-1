from Clientes import ClienteRegular, ClientePremium, ClienteCorporativo
from gestor_Clientes import GestorClientes

def ejecutar_demostración():
    gestor = GestorClientes()

    print("--- 1. Creando Clientes ---")
    try:
        # Instanciación de tipos de clientes
        c1 = ClienteRegular("C001", "Elon Musk", "elon@email.com", "987654321", "Av. Central 123", 150)
        c2 = ClientePremium("C002", "Jensen Huang", "jensen@email.com", "912345678", "Calle Alta 456", "Oro", 15)
        c3 = ClienteCorporativo("C003", "Tech Corp", "contacto@tech.com", "955554444", "Parque Ind. 789", "Tech Solutions", 50000)
        print("¡Clientes creados con éxito!")
    except Exception as e:
        print(f"Error al crear: {e}")

        gestor.crear_cliente(c1)
        gestor.crear_cliente(c2)
        gestor.crear_cliente(c3)

    print("\n--- 2. Exportando a JSON y CSV ---")
    gestor.guardar_json()
    gestor.guardar_csv()
    print("Archivos exportados correctamente.")

    print("\n--- 3. Probando Polimorfismo y Método __str__ ---")
    for cliente in gestor.clientes:
        print(cliente)  # Esto llama automáticamente a __str__() y obtener_datos()

if __name__ == "__main__":
    ejecutar_demostración()