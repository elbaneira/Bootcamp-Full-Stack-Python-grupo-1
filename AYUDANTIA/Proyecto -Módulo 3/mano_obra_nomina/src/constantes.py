"""
Módulo de Constantes del Sistema de Gestión de Mano de Obra.
Aplica el uso de Tuplas (datos inmutables) y Sets (para búsquedas eficientes).
"""

# Tupla inmutable con los niveles de calificación (en Mayúsculas)
CATEGORIAS = ("CALIFICADA", "SEMI CALIFICADA", "NO CALIFICADA")

# Tupla inmutable para géneros
GENEROS = ("HOMBRE", "MUJER")

# Sets de palabras clave para clasificación automática (Conjuntos)

# 1. PALABRAS CLAVE - CALIFICADA (Universitaria / Jefaturas / Profesionales)
PALABRAS_CALIFICADAS = {
    "INGENIERO", "PREVENCIONISTA", "PROFESIONAL", "RESIDENTE", 
    "JEFE", "ENCARGADO", "ARQUITECTO", "GEOMENSOR", "PAC", "COORDINADOR",
    "NIVELADOR", "CAPATAZ", "ADMINISTRATIVO", "PREV", "ING", "JEFE"
}

# 2. PALABRAS CLAVE - SEMI CALIFICADA (Técnicos / Mandos Medios / Operadores)
PALABRAS_SEMI_CALIFICADAS = {
    "TOPOGRAFO", "TOPÓGRAFO", "ADMINISTRATIVA", "LABORATORISTA", 
    "MOTOSIERRISTA", "OPERADOR", "SUPERVISOR", "CONDUCTOR",
    "SECRETARIA", "CHOFER", "MAESTRO", "CARCHECK", "TÉCNICO", "TECNICO"
}

# 3. PALABRAS CLAVE - NO CALIFICADA (Terreno / Operativos / Sin Título)
PALABRAS_NO_CALIFICADAS = {
    "ALARIFE", "BANDERERA", "BANDERERO", "ESTAQUERO", 
    "JORNAL", "PALETERO", "AYUDANTE"
}