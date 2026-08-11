import Clientes
import gestor_Clientes

def ejecutar_demostración():
    gestor = gestor_Clientes.GestorClientes()

    print("--- 1. Creando Clientes ---")
    try:
        # Instanciación de tipos de clientes
        c1 = Clientes.ClienteRegular("C001", "Elon Musk", "elon@email.com", "987654321", "Av. Central 123", 150)
        c2 = Clientes.ClientePremium("C002", "Jensen Huang", "jensen@email.com", "912345678", "Calle Alta 456", "Oro", 15)
        c3 = Clientes.ClienteCorporativo("C003", "Tech Corp", "contacto@tech.com", "955554444", "Parque Ind. 789", "Tech Solutions", 50000)

        # Agregar clientes al gestor
        gestor.crear_cliente(c1)
        gestor.crear_cliente(c2)
        gestor.crear_cliente(c3)
        print("¡Clientes creados e ingresados con éxito!")
    except Exception as e:
        print(f"Error al crear: {e}")

    print("\n--- 2. Exportando a JSON y CSV ---")
    gestor.guardar_json()
    gestor.guardar_csv()
    print("Archivos exportados correctamente.")

    print("\n--- 3. Probando Polimorfismo ---")
    for cliente in gestor.clientes:
        print(cliente.obtener_datos())

    print("\n--- 4. Probando Edición de Cliente ---")
    try:
        gestor.editar_cliente("C001", nuevo_nombre="Elon Musk Modificado", nuevo_email="elon.musk@x.com")
    except Exception as e:
        print(f"Error al editar: {e}")

if __name__ == "__main__":
    ejecutar_demostración()