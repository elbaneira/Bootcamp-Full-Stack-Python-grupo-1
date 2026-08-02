"""
Módulo de Validación de Entradas de Usuario.
Aplica bucles while, break y continue para garantizar datos correctos.
"""

def validar_rut(rut: str) -> bool:
    """Valida el formato básico del RUT chileno."""
    rut_limpio = rut.strip().replace(".", "").replace("-", "").upper()
    if len(rut_limpio) >= 8 and len(rut_limpio) <= 9:
        return True
    return False


def solicitar_texto_obligatorio(mensaje: str) -> str:
    """Garantiza que el usuario no ingrese campos vacíos usando break/continue."""
    while True:
        entrada = input(mensaje).strip()
        if not entrada:
            print("⚠️ El campo no puede estar vacío. Intente nuevamente.")
            continue  # Salta a la siguiente iteración del ciclo
        break  # Rompe el ciclo si la entrada es válida
    return entrada