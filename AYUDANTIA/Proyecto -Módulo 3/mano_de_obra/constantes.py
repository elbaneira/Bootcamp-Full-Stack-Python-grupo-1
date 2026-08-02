"""
Módulo de Constantes del Sistema de Gestión de Mano de Obra.
Aplica el uso de Tuplas (datos inmutables) y Sets (para búsquedas eficientes).
"""

# Tupla inmutable con los niveles de calificación
CATEGORIAS = ("CALIFICADA", "SEMI CALIFICADA", "NO CALIFICADA")

# Tupla inmutable para géneros
GENEROS = ("HOMBRE", "MUJER")

# Sets de palabras clave para clasificación automática (Conjuntos)
PALABRAS_CALIFICADAS = {
    "INGENIERO", "PREVENCIONISTA", "PROFESIONAL", "RESIDENTE", 
    "JEFE", "ENCARGADO", "ARQUITECTO", "GEOMENSOR"
}

PALABRAS_SEMI_CALIFICADAS = {
    "TOPOGRAFO", "ADMINISTRATIVA", "LABORATORISTA", "CAPATAZ", 
    "MOTOSIERRISTA", "OPERADOR", "SUPERVISOR", "CONDUCTOR"
}