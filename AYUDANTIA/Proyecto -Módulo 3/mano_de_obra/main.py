"""
Módulo Principal (Punto de entrada de la aplicación).
Coordina la interacción con el usuario mediante f-strings, formateo y ciclos de control.
"""

from constantes import CATEGORIAS
from validador import validar_rut, solicitar_texto_obligatorio
from clasificador import contar_trabajadores_recursivo
from gestor_datos import crear_trabajador, cargar_desde_csv, guardar_en_csv


def mostrar_resumen(trabajadores: list):
    """Muestra estadísticas agrupadas usando diccionarios y f-strings."""
    if not trabajadores:
        print("⚠️ No hay trabajadores registrados.")
        return

    # Uso de recursividad para el conteo total
    total = contar_trabajadores_recursivo(trabajadores)
    
    # Diccionario para conteo por categoría
    conteo = {cat: 0 for cat in CATEGORIAS}
    
    for t in trabajadores:
        conteo[t["clasificacion"]] += 1

    print("\n" + "=" * 55)
    print("📊 RESUMEN DE NÓMINA DE MANO DE OBRA DE LA ASESORÍA")
    print("=" * 55)
    print(f"Total de personal evaluado (vía recursión): {total}")
    for cat, cantidad in conteo.items():
        porcentaje = (cantidad / total) * 100 if total > 0 else 0
        print(f"  • {cat:<16}: {cantidad:>3} persona(s) ({porcentaje:.1f}%)")
    print("=" * 55 + "\n")


def menu():
    trabajadores = []
    ruts_registrados = set()

    while True:
        print("\n--- SISTEMA AUTOMATIZADO DE MANO DE OBRA (SGMO) ---")
        print("1. Cargar nómina desde archivo CSV")
        print("2. Registrar nuevo trabajador manualmente")
        print("3. Visualizar todos los trabajadores procesados")
        print("4. Mostrar resumen y estadísticas de calificación")
        print("5. Exportar informe a CSV")
        print("6. Salir")
        
        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            archivo = input("Ingrese la ruta del archivo CSV (ej: nomina_prueba.csv): ").strip()
            trabajadores, ruts_registrados = cargar_desde_csv(archivo)

        elif opcion == "2":
            rut = solicitar_texto_obligatorio("Ingrese RUT del trabajador: ")
            if not validar_rut(rut):
                print("❌ RUT inválido. Intente nuevamente.")
                continue
            
            if rut in ruts_registrados:
                print("⚠️ Este RUT ya fue registrado anteriormente.")
                continue

            nombre = solicitar_texto_obligatorio("Nombre completo: ")
            cargo = solicitar_texto_obligatorio("Cargo en la obra (ej: Jornal, Ingeniero, Capataz): ")
            genero = solicitar_texto_obligatorio("Género (Hombre/Mujer): ").upper()
            titulo_input = input("¿Posee título profesional/técnico? (SI/NO): ").strip().upper()
            tiene_titulo = (titulo_input == "SI")

            t = crear_trabajador(rut, nombre, cargo, genero, tiene_titulo)
            trabajadores.append(t)
            ruts_registrados.add(rut)
            print(f"✅ Trabajador registrado como: {t['clasificacion']}")

        elif opcion == "3":
            if not trabajadores:
                print("⚠️ La lista está vacía.")
                continue
            print("\n" + "-" * 75)
            print(f"{'RUT':<12} | {'NOMBRE':<25} | {'CARGO':<18} | {'CLASIFICACIÓN'}")
            print("-" * 75)
            for t in trabajadores:
                print(f"{t['rut']:<12} | {t['nombre']:<25} | {t['cargo']:<18} | {t['clasificacion']}")
            print("-" * 75)

        elif opcion == "4":
            mostrar_resumen(trabajadores)

        elif opcion == "5":
            salida = input("Nombre del archivo de salida (ej: informe_resultado.csv): ").strip()
            guardar_en_csv(trabajadores, salida)

        elif opcion == "6":
            print("👋 Saliendo del sistema de gestión. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Ingrese un número de 1 a 6.")


if __name__ == "__main__":
    menu()