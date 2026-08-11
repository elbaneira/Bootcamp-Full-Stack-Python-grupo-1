import csv
import json
from datetime import datetime
from Clientes import ClienteRegular, ClientePremium, ClienteCorporativo

class GestorClientes:
    def __init__(self):
        self.clientes = []

    # CRUD
    def crear_cliente(self, cliente):
        if self.buscar_cliente(cliente.getIdentificador()):
            raise ValueError("El cliente ya existe")
        self.clientes.append(cliente)
        self.registrar_log(f"Agregado cliente ID {cliente.getIdentificador()}")

    def buscar_cliente(self, identificador):
        for c in self.clientes:
            if str(c.getIdentificador()) == str(identificador):
                return c
        return None

    def eliminar_cliente(self, identificador):
        cliente = self.buscar_cliente(identificador)
        if cliente:
            self.clientes.remove(cliente)
            self.registrar_log(f"Eliminado cliente ID {identificador}")

    def editar_cliente(self, identificador, nuevo_nombre=None, nuevo_email=None):
        """
        Busca un cliente por su ID y actualiza los campos proporcionados.
        """
        cliente = self.buscar_cliente(identificador)
        if not cliente:
            raise ValueError(f"No se encontró un cliente con el ID {identificador}")
        
        # Modificar campos si vienen con datos
        if nuevo_nombre:
            cliente._Cliente__nombre = nuevo_nombre
        if nuevo_email:
            if "@" not in nuevo_email:
                raise ValueError("El email no es válido")
            cliente._Cliente__email = nuevo_email

        self.registrar_log(f"Editado cliente ID {identificador}")
        print(f"✅ Cliente {identificador} actualizado con éxito.")

    # Persistencia en JSON y CSV
    def guardar_json(self, ruta="clientes.json"):
        datos = []
        for c in self.clientes:
            info = {
                "id": c.getIdentificador(),
                "nombre": c.getNombre(),
                "email": c.getEmail(),
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
                escritor.writerow([c.getIdentificador(), c.getNombre(), c.getEmail(), c.__class__.__name__])
        self.registrar_log("Guardado en CSV")

    # Registro de actividad (Logs)
    def registrar_log(self, mensaje):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("actividad.txt", "a", encoding="utf-8") as f:
            f.write(f"[{fecha}] {mensaje}\n")