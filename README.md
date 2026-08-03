# 🏗️ SGMO - Sistema Automatizado de Gestión de Mano de Obra

**Autor:** Elba Neira Arévalo  
**Curso / Módulo:** Desarrollo de Aplicaciones Full Stack Python (Grupo 1)  

---

## 📋 Descripción del Proyecto
El **SGMO** es una aplicación desarrollada en consola (Python) diseñada para automatizar la carga, validación, clasificación y análisis de la nómina de mano de obra en proyectos de construcción e ingeniería (asociados a códigos SAFI). El sistema permite mantener un flujo centralizado de trabajadores mediante una lista maestra en memoria y exportar informes consolidados en formato CSV.

---

## 🚀 Funcionalidades Principales
1. **Carga Masiva (CSV):** Permite importar registros de trabajadores asociados a un Código SAFI o proyecto, clasificándolos automáticamente.
2. **Registro Manual:** Validación y alta en tiempo real de nuevos colaboradores ingresando RUT, Nombre, Cargo, Género y Título.
3. **Visualización Paginada:** Muestra una tabla estructurada de los trabajadores procesados en memoria (con paginación para evitar saturar la terminal).
4. **Resumen y Estadísticas (Recursión):** Calcula el conteo y los porcentajes cuantitativos de calificación (Calificada, Semi Calificada, No Calificada) utilizando funciones recursivas.
5. **Exportación de Informes:** Generación de un archivo `.csv` consolidado con toda la nómina procesada en el periodo.
6. **Manejo de Errores (Resiliencia):** Control de excepciones (como `FileNotFoundError`) para evitar caídas del sistema ante rutas de archivos inválidas.

---

## 🧩 Arquitectura y Modularidad (Estándar PEP 8)
El código fuente está estructurado de manera modular para separar responsabilidades y facilitar la mantenibilidad:
* `main.py`: Menú interactivo principal y control de flujo de la aplicación.
* `gestor_datos.py`: Lógica para la carga de archivos, almacenamiento en la Lista Maestra y exportación.
* `validador.py`: Reglas de validación de entradas y formatos (como RUT y normalización de textos con `.strip()` y `.upper()`).
* `clasificador.py`: Lógica de asignación de categorías según el cargo del trabajador.

---

## ⚙️ Requisitos y Ejecución

1. **Requisitos previos:** Tener instalado **Python 3.x** en tu equipo.
2. **Clonar o descargar el repositorio** en tu carpeta de trabajo.
3. **Ejecutar la aplicación** desde la terminal de tu entorno (VS Code o similar):
   ```bash
   python main.py
