class Animal:
  def __init__(self, nombre):
    self.nombre = nombre
  
  def hacer_sonido(self):
    pass

class Perro(Animal):
  def hacer_sonido(self):
    return "Guau guau"

class Gato(Animal):
  def hacer_sonido(self):
    return "Miau miau"
  

# Instanciamos 2 objetos
gato1 = Gato("Níquel")
perro1 = Perro("Apolo")

# Ejecutamos los métodos de cada instancia
print(f"Hola, soy un perro me llamo {perro1.nombre} y digo", perro1.hacer_sonido())
print()
print(f"Hola, soy un gato me llamo {gato1.nombre} y digo", gato1.hacer_sonido())
print()
