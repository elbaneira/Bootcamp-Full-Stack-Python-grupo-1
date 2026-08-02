"""
Módulo de Gestión de Datos.
Administra Listas, Diccionarios y la interacción con archivos CSV.
"""

import csv
import os
from clasificador import clasificar_trabajador


def crear_trabajador(rut: str, nombre: str, cargo: str, genero: str, tiene_titulo: bool) -> dict:
    """Crea y retorna un Diccionario con la estructura de un trabajador."""
    clasificacion = clasificar_trabajador(cargo, tiene_titulo)
    return {
        "rut": rut,
        "nombre": nombre,
        "cargo": cargo,
        "genero": genero,
        "tiene_titulo": "SI" if tiene_titulo else "NO",
        "clasificacion": clasificacion
    }


def obtener_ruta_absoluta(nombre_archivo: str) -> str:
    """
    Si la ruta dada es relativa, la une con la carpeta del script actual 
    para encontrar siempre el archivo sin importar desde dónde se ejecute la terminal.
    """
    if not os.path.isabs(nombre_archivo):
        directorio_script = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(directorio_script, nombre_archivo)
    return nombre_archivo


def cargar_desde_csv(ruta_archivo: str) -> tuple[list, set]:
    """
    Lee un archivo CSV con datos de la nómina y los clasifica automáticamente al importar.
    Usa un Conjunto (set) para garantizar que los RUTs no se dupliquen.
    """
    trabajadores = []
    ruts_procesados = set()
    
    # Busca la ruta exacta dentro del proyecto
    ruta_completa = obtener_ruta_absoluta(ruta_archivo)
    
    try:
        with open(ruta_completa, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Normalizamos las claves del diccionario (por si tienen espacios)
                fila_norm = {k.strip().upper(): v.strip() for k, v in fila.items() if k}
                
                rut = fila_norm.get("RUT", "")
                
                # Evitar registros vacíos o duplicados
                if not rut or rut in ruts_procesados:
                    continue
                
                nombre = fila_norm.get("NOMBRE", "")
                cargo = fila_norm.get("CARGO", "")
                genero = fila_norm.get("GENERO", "HOMBRE").upper()
                tiene_titulo_str = fila_norm.get("TIENE_TITULO", "NO").upper()
                tiene_titulo = (tiene_titulo_str == "SI")
                
                # Clasificación automática al cargar
                trabajador = crear_trabajador(rut, nombre, cargo, genero, tiene_titulo)
                trabajadores.append(trabajador)
                ruts_procesados.add(rut)
                
        print(f"\n✅ Se cargaron y clasificaron exitosamente {len(trabajadores)} registros desde '{os.path.basename(ruta_completa)}'.")
    
    except FileNotFoundError:
        print(f"\n❌ Error: No se encontró el archivo '{ruta_archivo}'.")
        print(f"📍 Python lo está buscando en esta ruta exacta:\n   {ruta_completa}")
        print("💡 Asegúrate de que el archivo .csv tenga ese mismo nombre y esté en esa carpeta.")
    except Exception as e:
        print(f"\n❌ Ocurrió un error inesperado al leer el archivo: {e}")
    
    return trabajadores, ruts_procesados


def guardar_en_csv(trabajadores: list, ruta_salida: str):
    """Guarda la lista de diccionarios de trabajadores en un archivo CSV."""
    if not trabajadores:
        print("\n⚠️ No hay datos para exportar.")
        return
    
    ruta_completa = obtener_ruta_absoluta(ruta_salida)
    columnas = ["rut", "nombre", "cargo", "genero", "tiene_titulo", "clasificacion"]
    
    try:
        with open(ruta_completa, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(trabajadores)
            
        print(f"\n💾 Informe exportado correctamente a '{os.path.basename(ruta_completa)}'.")
    except Exception as e:
        print(f"\n❌ Error al guardar el archivo: {e}")