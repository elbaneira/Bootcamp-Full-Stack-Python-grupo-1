# 🚀 Gestor Inteligente de Clientes (GIC)

 Sistema de gestión de clientes desarrollado en Python para registrar, consultar, eliminar y administrar información de distintos tipos de clientes.

El proyecto fue desarrollado aplicando los principios fundamentales de la Programación Orientada a Objetos (POO), manejo de excepciones y persistencia de datos mediante archivos JSON y CSV.

La solución permite trabajar con diferentes tipos de clientes mediante una estructura basada en una clase principal y clases especializadas, incorporando validaciones, operaciones CRUD, exportación de información y registro de actividades.

---

📌 Características del proyecto

El sistema incorpora las siguientes funcionalidades y conceptos de programación:

🧩 Programación Orientada a Objetos
Encapsulamiento: protección y control del acceso a los atributos de las clases.
Herencia: utilización de una clase base Cliente y clases especializadas para los distintos tipos de clientes.
Polimorfismo: implementación de comportamientos específicos según el tipo de cliente.
Métodos especiales: utilización de __str__ y __eq__ para representar y comparar objetos.

👥 Gestión de clientes
Registro de nuevos clientes.
Consulta de información.
Modificación y eliminación de registros.
Gestión diferenciada de clientes según su tipo.
Validación de los datos ingresados.

💾 Persistencia de datos
Almacenamiento de información mediante archivos JSON.
Exportación de información a formato CSV.
Recuperación de los datos almacenados al ejecutar nuevamente el sistema.

⚙️ Manejo de errores
Uso de excepciones para controlar situaciones inesperadas.
Validación de entradas para evitar datos incorrectos.
Mensajes informativos para orientar al usuario durante la ejecución.

📝 Registro de actividades
Generación de un archivo de auditoría para registrar las principales acciones realizadas en el sistema.
Seguimiento de las operaciones efectuadas durante la ejecución.

---

## 📽️ Presentación en Video

* **Duración:** ~3 minutos aprox.
* **Contenido:** Explicación del diagrama UML, pilares de POO (Encapsulamiento, Herencia, Polimorfismo, Composición), ejecución del CRUD y exportación a JSON/CSV.

[![Ver Video en YouTube](https://img.youtube.com/vi/iDbT40OkKc4/maxresdefault.jpg)](https://youtu.be/iDbT40OkKc4)

👉 **[Haz clic aquí si la imagen no abre el video](https://youtu.be/iDbT40OkKc4)**

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

---

**Autor:** Elba Neira Arévalo  
**Curso / Módulo:** Desarrollo de Aplicaciones Full Stack Python (Grupo 1) 