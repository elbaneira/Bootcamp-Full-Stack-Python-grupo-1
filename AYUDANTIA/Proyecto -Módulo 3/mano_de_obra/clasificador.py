"""
Módulo de Clasificación de Mano de Obra.
Aplica condicionales if/elif/else y funciones recursivas.
"""

from constantes import CATEGORIAS, PALABRAS_CALIFICADAS, PALABRAS_SEMI_CALIFICADAS


def clasificar_trabajador(cargo: str, tiene_titulo: bool) -> str:
    """
    Determina la calificación de un trabajador según su cargo y si posee título profesional/técnico.
    Uso de estructuras condicionales (if / elif / else).
    """
    cargo_upper = cargo.upper()
    
    # Regla 1: Si posee título profesional o su cargo incluye palabras clave de profesionales
    if tiene_titulo or any(palabra in cargo_upper for palabra in PALABRAS_CALIFICADAS):
        return CATEGORIAS[0]  # CALIFICADA
    
    # Regla 2: Si su cargo es técnico/operativo especializado
    elif any(palabra in cargo_upper for palabra in PALABRAS_SEMI_CALIFICADAS):
        return CATEGORIAS[1]  # SEMI CALIFICADA
    
    # Regla 3: Oficios no calificados (Jornal, Banderero, Paletero, etc.)
    else:
        return CATEGORIAS[2]  # NO CALIFICADA


def contar_trabajadores_recursivo(lista_trabajadores: list, indice: int = 0) -> int:
    """
    Función RECURSIVA que calcula el total de trabajadores procesados en una lista.
    Cumple con el requisito de implementación de funciones recursivas.
    """
    # Caso base: cuando el índice llega al final de la lista
    if indice >= len(lista_trabajadores):
        return 0
    
    # Caso recursivo: 1 + llamada con el siguiente índice
    return 1 + contar_trabajadores_recursivo(lista_trabajadores, indice + 1)