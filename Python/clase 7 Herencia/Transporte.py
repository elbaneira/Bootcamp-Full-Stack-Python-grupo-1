# 1. Definición de las clases de transporte
class Auto:
    def desplazarse(self):
        return "El auto avanza por la carretera"


class Bicicleta:
    def desplazarse(self):
        return "La bicicleta avanza por la ciclovía"


# 2. Función que aplica polimorfismo
def iniciar_desplazamiento(vehiculo):
    print(vehiculo.desplazarse())


# 3. Creación de instancias (objetos)
mi_auto = Auto()
mi_bici = Bicicleta()

# 4. Pruebas llamando a la función
iniciar_desplazamiento(mi_auto)   # Imprime: El auto avanza por la carretera
iniciar_desplazamiento(mi_bici)   # Imprime: La bicicleta avanza por el ciclopaseo