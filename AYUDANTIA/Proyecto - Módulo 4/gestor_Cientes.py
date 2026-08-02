import csv
from datetime import datetime

from Cliente import ClienteRegular
from Cliente import ClientePremium
from Cliente import ClienteCorporativo

class GestorClientes:

    def __init__(self):
        self.clientes = []

    def crearCliente(self, tipo, identificador, nombre, email, telefono, direccion, dato1, dato2=""):
        if tipo == "Regular":
            cliente = ClienteRegular(identificador, nombre, email, telefono, direccion, dato1)
        elif tipo == "Premium":
            cliente = ClientePremium(identificador, nombre, email, telefono, direccion, dato1, dato2)
        elif tipo == "Corporativo":
            cliente = ClienteCorporativo(identificador, nombre, email, telefono, direccion, dato1, dato2)
        else:
            raise ValueError("El tipo no existe")

        self.clientes.append(cliente)
        self.guardar_actividad("Agregó cliente")

    def editar_cliente(self, identificador, tipo, nombre, email, telefono, direccion, dato1, dato2=""):
        cliente = self.buscar_cliente(identificador)

        if cliente == None:
            raise ValueError("No se encontró el cliente")

        posicion = self.clientes.index(cliente)

        if tipo == "Regular":
            cliente_editado = ClienteRegular(identificador, nombre, email, telefono, direccion, dato1)
        elif tipo == "Premium":
            cliente_editado = ClientePremium(identificador, nombre, email, telefono, direccion, dato1, dato2)
        elif tipo == "Corporativo":
            cliente_editado = ClienteCorporativo(identificador, nombre, email, telefono, direccion, dato1, dato2)
        else:
            raise ValueError("El tipo indicado no existe")

        self.clientes[posicion] = cliente_editado
        self.guardar_actividad("Editó cliente")

    def eliminar_cliente(self, identificador):
        cliente = self.buscar_cliente(identificador)
        
        if cliente == None:
            raise ValueError("No se encontró el cliente")

        self.clientes.remove(cliente)
        self.guardar_actividad("Eliminó cliente")
    
    def buscar_cliente(self, identificador):
        for cliente in self.clientes:
            if cliente.getIdentificador() == identificador:
                self.guardar_actividad("Cliente encontrado")
                return cliente

        return None

    def guardar_clientes_txt(self):
        with open("clientes.txt", "w", encoding="utf-8") as archivo:
            for cliente in self.clientes:
                archivo.write(cliente.obtener_datos() + "\n")

        self.guardar_actividad("Generó archivo .txt")

    def guardar_clientes_csv(self):
        with open("clientes.csv", "w", newline="", encoding="utf-8") as archivo:

            escritor = csv.writer(archivo, delimiter=";")

            escritor.writerow([
                "Identificador",
                "Nombre",
                "Email",
                "Teléfono",
                "Dirección"
            ])

            for cliente in self.clientes:
                escritor.writerow([
                    cliente.getIdentificador(),
                    cliente.getNombre(),
                    cliente.getEmail(),
                    cliente.getTelefono(),
                    cliente.getDireccion()
                ])
        self.guardar_actividad("Generó archivo .csv")

    def guardar_actividad(self, mensaje):
        fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        with open("actividad.txt", "a", encoding="utf-8") as archivo:

            archivo.write(f"Fecha: {fecha} | Acción: {mensaje}\n")



    

















gestor1 = GestorClientes()

gestor1.crearCliente("Regular", 1, "Juan", "juan@gmail.com", "987654321", "Calle 1 S/N", 0)
gestor1.crearCliente("Premium", 2, "Ana", "ana@gmail.com", "987654322", "Calle 2 S/N", "Platinum", 10)
gestor1.crearCliente("Corporativo", 3, "Luis", "luis@gmail.com", "987654323", "calle 3 S/N", "CCU", 10000000)

for cliente in gestor1.clientes:
    print(cliente.obtener_datos())

print("")

gestor1.editar_cliente(1, "Premium", "Juan", "juan@gmail.com", "987654321", "Calle 1 S/N", "Gold", 5)

for cliente in gestor1.clientes:
    print(cliente.obtener_datos())

print("")

gestor1.eliminar_cliente(1)

for cliente in gestor1.clientes:
    print(cliente.obtener_datos())

gestor1.guardar_clientes_txt()
gestor1.guardar_clientes_csv()
