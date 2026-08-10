import csv
import json
from datetime import datetime
from Clientes import ClienteRegular, ClientePremium, ClienteCorporativo

class GestorClientes:
    def __init__(self):
        self.clientes = []

    # CRUD
    def crear_cliente(self, cliente):
        if self.buscar_cliente(cliente.get_identificador()):
            raise ValueError("El cliente ya existe")
        self.clientes.append(cliente)
        self.registrar_log(f"Agregado cliente ID {cliente.get_identificador()}")

    def buscar_cliente(self, identificador):
        for c in self.clientes:
            if str(c.get_identificador()) == str(identificador):
                return c
        return None

    def eliminar_cliente(self, identificador):
        cliente = self.buscar_cliente(identificador)
        if cliente:
            self.clientes.remove(cliente)
            self.registrar_log(f"Eliminado cliente ID {identificador}")

    # Persistencia en JSON y CSV
    def guardar_json(self, ruta="clientes.json"):
        datos = []
        for c in self.clientes:
            info = {
                "id": c.get_identificador(),
                "nombre": c.get_nombre(),
                "email": c.get_email(),
                "tipo": c.__class__.__name__
            }
            datos.append(info)
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)
        self.registrar_log("Guardado en JSON")

    def guardar_csv(self, ruta="clientes.csv"):
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f, delimiter=";")
            escritor.writerow(["ID", "Nombre", "Email", "Tipo"])
            for c in self.clientes:
                escritor.writerow([c.get_identificador(), c.get_nombre(), c.get_email(), c.__class__.__name__])
        self.registrar_log("Guardado en CSV")

    # Registro de actividad (Logs)
    def registrar_log(self, mensaje):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("actividad.txt", "a", encoding="utf-8") as f:
            f.write(f"[{fecha}] {mensaje}\n")