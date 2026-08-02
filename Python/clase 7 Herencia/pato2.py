class Volador:
  def volar(self):
    print("Estoy volando!")
  
class Nadador:
  def nadar(self):
    print("Estoy nadando!")

class Pato(Nadador, Volador):
    def __init__(self, nombre):
        self.nombre = nombre
    def hacer_sonido(self):
      print("Cuac cuac!")
      
# Instanciamos un objeto
pato1 = Pato("Patroclo")

# Ejecutamos los métodos de la instancia
print(f"Hola, soy un pato me llamo {pato1.nombre}")
print()

pato1.volar()
pato1.nadar()
pato1.hacer_sonido()

print(Pato.__mro__)