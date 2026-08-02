class Celular:
    # 1. Constructor con los 3 atributos requeridos
    def __init__(self, marca, modelo, almacenamiento):
        self.marca = marca
        self.modelo = modelo
        self.almacenamiento = almacenamiento

    # 2. Método encender()
    def encender(self):
        print(f"Encendiendo {self.marca} {self.modelo}...")

    # 3. Método mostrar_info()
    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Almacenamiento: {self.almacenamiento} GB")


# --- Ejemplo  ---
mi_cel = Celular("Samsung", "Galaxy S23", 256)

mi_cel.encender()
# Salida: Encendiendo Samsung Galaxy S23...

mi_cel.mostrar_info()
# Salida:
# Marca: Samsung
# Modelo: Galaxy S23
# Almacenamiento: 256 GB