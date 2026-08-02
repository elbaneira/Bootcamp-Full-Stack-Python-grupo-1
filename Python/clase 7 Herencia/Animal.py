class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
    
    def hacer_sonido(self):
        return 'El animal hace un sonido'
    
    def dormir(self):
        return f'{self.nombre} está durmiendo'

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre, 'Canino')
        self.raza = raza
    
    def hacer_sonido(self):
        return 'Guau guau'

# Crear instancias
mi_perro = Perro('Apolo', 'Labrador')
print(f'Nombre: {mi_perro.nombre}')
print(f'Especie: {mi_perro.especie}')
print(f'Raza: {mi_perro.raza}')
print(mi_perro.hacer_sonido())
print(mi_perro.dormir())