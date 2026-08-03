"""
Módulo de Gestión de Datos.
Administra Listas, Diccionarios y la interacción con archivos CSV.
"""

import csv
import os
from clasificador import clasificar_trabajador


def crear_trabajador(rut: str, nombre: str, cargo: str, genero: str = "HOMBRE", tipo_titulo: str = "", safi: str = "") -> dict:
    clasificacion = clasificar_trabajador(cargo, tipo_titulo)
    return {
        "safi": safi,
        "rut": rut,
        "nombre": nombre,
        "cargo": cargo,
        "genero": genero,
        "tipo_titulo": tipo_titulo,
        "clasificacion": clasificacion
    }


def cargar_desde_csv(ruta_archivo: str, codigo_safi: str = ""):
    trabajadores = []
    ruts_procesados = set()

    # Buscador de ruta
    if not os.path.isabs(ruta_archivo) and not os.path.exists(ruta_archivo):
        carpeta_script = os.path.dirname(os.path.abspath(__file__))
        ruta_alternativa = os.path.join(carpeta_script, ruta_archivo)
        if os.path.exists(ruta_alternativa):
            ruta_archivo = ruta_alternativa

    try:
        with open(ruta_archivo, mode="r", encoding="utf-8-sig") as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                fila_limpia = {k.strip(): v.strip() for k, v in fila.items() if k}
                
                rut = fila_limpia.get("RUT", fila_limpia.get("rut", ""))
                nombre = fila_limpia.get("NOMBRE", fila_limpia.get("nombre", ""))
                cargo = fila_limpia.get("CARGO", fila_limpia.get("cargo", ""))
                
                # OJO AQUÍ: Priorizar la columna 'Tipo' (Universitario/Técnico) antes que 'TÍTULO' (SI/NO)
                tipo_titulo = fila_limpia.get("Tipo", fila_limpia.get("tipo", fila_limpia.get("TÍTULO", "")))
                
                genero = fila_limpia.get("GENERO", fila_limpia.get("genero", "HOMBRE"))
                safi_csv = fila_limpia.get("SAFI", fila_limpia.get("safi", ""))
                safi_final = safi_csv if safi_csv else codigo_safi

                if rut and rut not in ruts_procesados:
                    trabajador = crear_trabajador(
                        rut=rut,
                        nombre=nombre,
                        cargo=cargo,
                        genero=genero,
                        tipo_titulo=tipo_titulo,
                        safi=safi_final
                    )
                    trabajadores.append(trabajador)
                    ruts_procesados.add(rut)
                    
        print(f"📊 Procesadas {len(trabajadores)} filas desde el archivo.")

    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo en la ruta '{ruta_archivo}'.")
    except Exception as e:
        print(f"❌ Error inesperado al leer el CSV: {e}")

    return trabajadores, ruts_procesados


def guardar_en_csv(trabajadores: list, ruta_salida: str):
    if not trabajadores:
        print("⚠️ No hay datos para exportar.")
        return

    campos = ["safi", "rut", "nombre", "cargo", "genero", "tipo_titulo", "clasificacion"]
    
    try:
        if not os.path.isabs(ruta_salida):
            carpeta_script = os.path.dirname(os.path.abspath(__file__))
            ruta_salida = os.path.join(carpeta_script, ruta_salida)

        with open(ruta_salida, mode="w", newline="", encoding="utf-8-sig") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(trabajadores)
        print(f"✅ Archivo exportado exitosamente como '{ruta_salida}'.")
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")