"""
Módulo de Clasificación de Mano de Obra.
Aplica condicionales e identificación de títulos/cargos.
"""

from constantes import CATEGORIAS, PALABRAS_CALIFICADAS, PALABRAS_SEMI_CALIFICADAS, PALABRAS_NO_CALIFICADAS


def clasificar_trabajador(cargo: str, tipo_titulo: str = "") -> str:
    """
    Determina la calificación de un trabajador evaluando primero el Tipo de Título 
    (Universitario vs Técnico) y luego las palabras clave del Cargo.
    """
    cargo_upper = cargo.strip().upper()
    tipo_str = str(tipo_titulo).strip().upper()

    # ----------------------------------------------------
    # REGLA 1: PRIORIDAD POR TIPO DE TÍTULO REAL
    # ----------------------------------------------------
    # Si es Universitario / Profesional -> CALIFICADA
    if "UNIVERSITARI" in tipo_str or "PROFESIONAL" in tipo_str:
        return CATEGORIAS[0]  # CALIFICADA

    # Si es Técnico / Instituto / CFT -> SEMI CALIFICADA
    elif "TECNICO" in tipo_str or "TÉCNICO" in tipo_str or "INSTITUTO" in tipo_str or "CFT" in tipo_str:
        return CATEGORIAS[1]  # SEMI CALIFICADA

    # ----------------------------------------------------
    # REGLA 2: EVALUACIÓN POR PALABRAS CLAVE EN EL CARGO
    # (Para cuando no viene 'Tipo' o dice 'Sin Título' / 'NO')
    # ----------------------------------------------------
    palabras_cargo = set(cargo_upper.replace(".", " ").replace("-", " ").split())

    # Palabras de Calificados (Ingenieros, Jefes, Prevencionistas, etc.)
    if any(p in palabras_cargo for p in PALABRAS_CALIFICADAS) or any(p in cargo_upper for p in PALABRAS_CALIFICADAS):
        return CATEGORIAS[0]  # CALIFICADA

    # Palabras de Semi Calificados (Topógrafos, Choferes, Maestros, Operadores, etc.)
    elif any(p in palabras_cargo for p in PALABRAS_SEMI_CALIFICADAS) or any(p in cargo_upper for p in PALABRAS_SEMI_CALIFICADAS):
        return CATEGORIAS[1]  # SEMI CALIFICADA

    # Si no coincide con las anteriores -> NO CALIFICADA (Jornales, Bandereros, Ayudantes)
    else:
        return CATEGORIAS[2]  # NO CALIFICADA


def contar_trabajadores_recursivo(lista_trabajadores: list, indice: int = 0) -> int:
    """Calcula el total de trabajadores de forma recursiva."""
    if indice >= len(lista_trabajadores):
        return 0
    return 1 + contar_trabajadores_recursivo(lista_trabajadores, indice + 1)
