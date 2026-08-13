# 🚀 Gestor Inteligente de Clientes (GIC)

### Proyecto Módulo 4 — Programación Orientada a Objetos en Python

**Autora:** Elba Neira Arévalo  
**Formación:** Bootcamp Full Stack Python

 Sistema de gestión de clientes desarrollado en Python para registrar, consultar, eliminar y administrar información de distintos tipos de clientes.

El proyecto fue desarrollado aplicando los principios fundamentales de la Programación Orientada a Objetos (POO), manejo de excepciones y persistencia de datos mediante archivos JSON y CSV.

La solución permite trabajar con diferentes tipos de clientes mediante una estructura basada en una clase principal y clases especializadas, incorporando validaciones, operaciones CRUD, exportación de información y registro de actividades.

---

📌 Características del proyecto

El sistema incorpora las siguientes funcionalidades y conceptos de programación:

🧩 Programación Orientada a Objetos

Encapsulamiento
Herencia
Polimorfismo
__str__
__eq__

👥 Gestión de clientes

Crear
Buscar
Editar
Eliminar

💾 Gestión de datos

Persistencia en JSON
Exportación CSV

⚙️ Validaciones y excepciones

Uso de excepciones para controlar situaciones inesperadas.
Validación de entradas para evitar datos incorrectos.
Mensajes informativos para orientar al usuario durante la ejecución.

📝 Registro de actividades

Generación de un archivo de auditoría (actividad.txt) para mantener un registro de las principales operaciones realizadas en el sistema.
El sistema permite almacenar la información de los clientes en formato JSON y exportarla a CSV.

---

## 📽️ Presentación en Video

* **Duración:** ~3 minutos aprox.
* **Contenido:** Explicación del diagrama UML, pilares de POO (Encapsulamiento, Herencia, Polimorfismo, Composición), ejecución del CRUD y exportación a JSON/CSV.

[![Ver Video en YouTube](https://img.youtube.com/vi/iDbT40OkKc4/maxresdefault.jpg)](https://youtu.be/iDbT40OkKc4)

👉 **[Haz clic aquí si la imagen no abre el video](https://youtu.be/iDbT40OkKc4)**

---

## 🛠️ Tecnologías y conceptos utilizados

### Lenguaje

* 🐍 **Python**

### Programación

* Programación Orientada a Objetos (POO)
* Encapsulamiento
* Herencia
* Polimorfismo
* Métodos especiales `__str__` y `__eq__`
* Validación de atributos
* Manejo de excepciones

### Gestión y almacenamiento de datos

* **JSON** para almacenar la información de los clientes.
* **CSV** para exportar los datos en formato tabular.
* Archivo de texto para el registro de actividades.

### Control de versiones

* **Git / GitHub** para gestionar y documentar el proyecto.

---

## 📁 Estructura del proyecto

```text
Proyecto - Módulo 4/
│
├── docsGIC/                # Documentación complementaria del proyecto
├── img/                    # Recursos gráficos y material visual
│
├── src/                    # Código fuente de la aplicación
│   ├── Clientes.py         # Clases y modelos de clientes
│   ├── gestor_Clientes.py  # Gestión de clientes y operaciones CRUD
│   └── main.py             # Ejecución y demostración del sistema
│
├── .gitignore              # Archivos excluidos del control de versiones
└── README.md               # Documentación principal del proyecto
```


### Componentes principales

* **`Clientes.py`**: contiene la clase base `Cliente` y sus clases especializadas, aplicando encapsulamiento, herencia y polimorfismo.
* **`gestor_Clientes.py`**: concentra la gestión de clientes, incluyendo las operaciones CRUD, validaciones, almacenamiento en JSON, exportación a CSV y registro de actividades.
* **`main.py`**: punto de entrada utilizado para crear clientes y demostrar las principales funcionalidades del sistema.
* **`docsGIC/`**: contiene documentación complementaria asociada al proyecto.
* **`img/`**: contiene recursos gráficos utilizados para la presentación y documentación.

---

### Control de versiones

* **Git / GitHub** para gestionar y documentar el proyecto.

---
© 2026 Elba Neira Arévalo
