# Sistema de Gestión de Tareas por Consola (CLI)

Este proyecto es un **sistema de gestión de tareas en modo consola (CLI)** desarrollado en Python.  
Su objetivo principal es **reforzar y practicar conocimientos fundamentales de Python**, especialmente:

- Programación Orientada a Objetos (clases, herencia, encapsulamiento).
- Manejo de errores con `try/except`.
- Validación de datos de entrada (por ejemplo, emails).
- Diseño de una interfaz de línea de comandos (CLI) con menús interactivos.
- Organización del código en módulos (`main.py`, `user.py`, `tareas.py`, `utils.py`).
- Uso básico de Git y creación de commits descriptivos.

---

## Funcionalidades principales

- **Creación de usuario** desde consola:
  - Solicita nombre y email.
  - Valida el formato del email mediante funciones reutilizables en `utils.py`.

- **Gestión de tareas por usuario**:
  - Agregar tareas simples.
  - Agregar tareas con fecha límite (`TareaConFecha`).
  - Listar todas las tareas del usuario.
  - Listar solo tareas pendientes.
  - Listar solo tareas completadas.

- **Manejo de errores y validaciones**:
  - Uso de `try/except` para capturar errores y cancelaciones del usuario (por ejemplo, `KeyboardInterrupt`).
  - Mensajes de consola más claros y amigables para guiar al usuario.

---

## Estructura del proyecto

- `main.py`:  
  Punto de entrada del programa. Implementa el **CLI** con un menú interactivo para:
  - Crear el usuario.
  - Agregar tareas.
  - Listar tareas (todas, pendientes, completadas).
  - Salir del sistema.

- `user.py`:  
  Contiene la clase `Usuario`, responsable de administrar las tareas de un usuario:
  - Guarda internamente una lista de tareas.
  - Métodos para agregar tareas, listar todas, ver pendientes y ver completadas.
  - Usa las clases definidas en `tareas.py`.

- `tareas.py`:  
  Define el modelo de las tareas:
  - `Tarea`: título, descripción y estado de completada.
  - `TareaConFecha`: hereda de `Tarea` y agrega una fecha límite.
  - Implementa `__str__` para mostrar las tareas de forma legible en consola.

- `utils.py`:  
  Funciones de utilidad reutilizables:
  - `validar_email(email)`: valida el formato de un email.
  - `pedir_email_valido(...)`: pide un email por consola hasta que sea válido.
  - `pedir_campo_no_vacio(...)`: pide textos no vacíos.
  - Incluye manejo de errores con `try/except` y mensajes claros.

---

## Requisitos

- Python 3.x instalado en el sistema.

No se utilizan librerías externas, solo la biblioteca estándar de Python (`re` para expresiones regulares).

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio o descargar los archivos.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar:

   python main.py
   
