 #Clase Persona
class Persona:
    # Método constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre # self.nombre es atributo | nombre = parámetro
        self.edad = edad # self.edad es atributo | edad = parámetro

    # Método
    def presentarse(self):
        print(f"Buenas tardes, soy {self.nombre}")

# Instanciamos dos objetos: persona1 y persona2
persona1 = Persona("Ana", 25)
persona2 = Persona("Pedro", 30)

# Se invoca el método presentarse() de cada onjeto <- Mensaje
persona1.presentarse()
persona2.presentarse()

# vemos los estados de ambos objetos
print(f"Nombre: {persona1.nombre} | Edad: {persona1.edad }")
print(f"Nombre: {persona2.nombre} | Edad: {persona2.edad }")# Clase Persona
class Persona:
    # Método constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre # self.nombre es atributo | nombre = parámetro
        self.edad = edad # self.edad es atributo | edad = parámetro

    # Método presentarse()
    def presentarse(self):
        print(f"Buenas tardes, soy {self.nombre}")

    # Método cumplir_año()
    def cumplir_año(self):
        self.edad += 1

# Instanciamos dos objetos: persona1 y persona2
persona1 = Persona("Ana", 25)
persona2 = Persona("Pedro", 30)

# Se invoca el método presentarse() de cada onjeto <- Mensaje
persona1.presentarse()
persona2.presentarse()

# vemos los estados de ambos objetos
print(f"Nombre: {persona1.nombre} | Edad: {persona1.edad }")
print(f"Nombre: {persona2.nombre} | Edad: {persona2.edad }")

persona2.cumplir_año()
print(f"Nombre: {persona2.nombre} | Edad: {persona2.edad }")