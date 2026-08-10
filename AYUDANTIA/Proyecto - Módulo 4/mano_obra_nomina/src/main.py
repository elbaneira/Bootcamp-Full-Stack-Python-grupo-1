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
        if t["clasificacion"] in conteo:
            conteo[t["clasificacion"]] += 1

    print("\n" + "=" * 60)
    print("📊 RESUMEN DE NÓMINA DE MANO DE OBRA ")
    print("=" * 60)
    print(f"Total de personal evaluado (vía recursión): {total}")
    for cat, cantidad in conteo.items():
        porcentaje = (cantidad / total) * 100 if total > 0 else 0
        print(f"  • {cat:<16}: {cantidad:>3} persona(s) ({porcentaje:.1f}%)")
    print("=" * 60 + "\n")


def menu():
    trabajadores = []
    ruts_registrados = set()

    while True:
        print("\n--- SISTEMA AUTOMATIZADO DE MANO DE OBRA (SGMO) ---")
        print("1. Cargar nómina desde archivo CSV (por SAFI/Proyecto)")
        print("2. Registrar nuevo trabajador manualmente")
        print("3. Visualizar todos los trabajadores procesados")
        print("4. Mostrar resumen y estadísticas de calificación")
        print("5. Exportar informe a CSV")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción (1-6): ").strip()

        # ----------------------------------------------------
        # OPCIÓN 1: CARGAR DESDE CSV
        # ----------------------------------------------------
        if opcion == "1":
            safi = input("Ingrese el Código SAFI o Proyecto (ej: 370806 / Presione Enter si viene en el CSV): ").strip()
            ruta = input("Ingrese la ruta del archivo CSV (ej: prueba_nomina.csv): ").strip()
            
            nuevos_trabajadores, ruts_procesados = cargar_desde_csv(ruta, codigo_safi=safi)
            
            if nuevos_trabajadores:
                trabajadores.extend(nuevos_trabajadores)
                ruts_registrados.update(ruts_procesados)
                print(f"✅ Se cargaron exitosamente {len(nuevos_trabajadores)} trabajadores.")

        # ----------------------------------------------------
        # OPCIÓN 2: REGISTRO MANUAL
        # ----------------------------------------------------
        elif opcion == "2":
            safi = solicitar_texto_obligatorio("Ingrese Código SAFI / Proyecto: ")
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
            tipo_titulo = input("Tipo de Título (Universitario / Técnico / Sin Título): ").strip()

            t = crear_trabajador(
                rut=rut, 
                nombre=nombre, 
                cargo=cargo, 
                genero=genero, 
                tipo_titulo=tipo_titulo,
                safi=safi
            )
            trabajadores.append(t)
            ruts_registrados.add(rut)
            print(f"✅ Trabajador registrado como: {t['clasificacion']}")

        # ----------------------------------------------------
        # OPCIÓN 3: VISUALIZAR
        # ----------------------------------------------------
        elif opcion == "3":
            if not trabajadores:
                print("⚠️ La lista está vacía.")
                continue
            
            print("\n" + "-" * 85)
            print(f"{'SAFI':<8} | {'RUT':<12} | {'NOMBRE':<25} | {'CARGO':<18} | {'CLASIFICACIÓN'}")
            print("-" * 85)
            for t in trabajadores:
                safi_val = t.get('safi', 'N/A')
                print(f"{safi_val:<8} | {t['rut']:<12} | {t['nombre']:<25} | {t['cargo']:<18} | {t['clasificacion']}")
            print("-" * 85)

        # ----------------------------------------------------
        # OPCIÓN 4: RESUMEN
        # ----------------------------------------------------
        elif opcion == "4":
            mostrar_resumen(trabajadores)

        # ----------------------------------------------------
        # OPCIÓN 5: EXPORTAR
        # ----------------------------------------------------
        elif opcion == "5":
            salida = input("Nombre del archivo de salida (ej: informe_resultado.csv): ").strip()
            guardar_en_csv(trabajadores, salida)

        # ----------------------------------------------------
        # OPCIÓN 6: SALIR
        # ----------------------------------------------------
        elif opcion == "6":
            print("👋 Saliendo del sistema de gestión. ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Ingrese un número de 1 a 6.")


if __name__ == "__main__":
    menu()