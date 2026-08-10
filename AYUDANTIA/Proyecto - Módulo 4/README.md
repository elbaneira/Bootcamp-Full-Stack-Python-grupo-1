# 🚀 Gestor Inteligente de Clientes (GIC)

Sistema de gestión de clientes desarrollado en **Python** aplicando los principios fundamental de la **Programación Orientada a Objetos (POO)**, manejo de excepciones y persistencia de datos en archivos estructurados (**JSON** y **CSV**).

---

## 📌 Características del Proyecto

- **Modelo de Clientes con POO:**
  - **Superclase (`Cliente`):** Define los atributos base y encapsula la información mediante atributos privados.
  - **Subclases:** `ClienteRegular`, `ClientePremium` y `ClienteCorporativo`, implementando **Herencia** y **Polimorfismo**.
  - **Métodos dunder:** Uso de `__str__` para representación en formato texto y `__eq__` para comparación de instancias por identificador.
- **Validaciones Avanzadas:** Control estricto de datos de entrada que lanza excepciones `ValueError` si hay campos vacíos o formatos de correo inválidos.
- **Gestión CRUD:** Creación, búsqueda y eliminación de clientes asegurando que no existan identificadores duplicados.
- **Persistencia de Datos:** Exportación e importación masiva de clientes en formatos **JSON** y **CSV**.
- **Registro de Auditoría (Logs):** Guarda automáticamente un historial de las acciones realizadas con fecha y hora en `actividad.txt`.

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Módulos estándar:** `json`, `csv`, `datetime`
- **Paradigma:** Programación Orientada a Objetos (POO)

---

## 📁 Estructura del Repositorio

```text
├── clientes.py          # Definición de la superclase Cliente y sus subclases.
├── gestor_cliente.py    # Lógica de administración (CRUD), lectura/escritura de archivos y logs.
├── main.py              # Script principal de ejecución y demostración.
├── actividad.txt        # Archivo generado automáticamente con los logs del sistema.
├── clientes.json        # Archivo de exportación/importación en formato JSON.
├── clientes.csv         # Archivo de exportación en formato CSV.
└── README.md            # Documentación del proyecto.