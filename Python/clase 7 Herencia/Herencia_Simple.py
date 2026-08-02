class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

class Empleado(Persona):
    def __init__(self, nombre, edad, cargo):
        super().__init__(nombre, edad)   # Llamamos al constructor de Persona
        self.cargo = cargo

    def presentarse(self):  # Sobrescritura
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años y soy {self.cargo}.")

    def trabajar(self):
        print(f"Estoy trabajando como {self.cargo}.")

empleado1 = Empleado("Juan Pérez", 45, "Chef")

empleado1.presentarse()   # Método sobrescrito
empleado1.trabajar()      # Método propio