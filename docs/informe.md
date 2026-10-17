```markdown
# Informe Técnico: Sistema Simulador de Disney+

**Asignatura:** Lenguaje de Programación II  
**Semestre:** 2026-2  
**Evaluación:** Evaluación Grupal 1  
---

## 1. Descripción del Escenario o Sistema
El sistema simula la gestión interna de la plataforma de streaming **Disney+**. Permite administrar el catálogo de contenidos (películas y series con sus atributos como título, duración, género y clasificación), gestionar los diferentes planes de suscripción disponibles (Estándar, Premium, etc.) y registrar usuarios que adquieren suscripciones y agregan títulos a sus listas de favoritos.

---

## 2. Arquitectura y Diseño Orientado a Objetos

El diseño del sistema se basa en 3 clases principales interconectadas mediante relaciones de asociación y composición:

```text
+-------------------+        +-------------------+        +--------------------+
|     Contenido     |        | PlanSuscripcion   |        |      Usuario       |
+-------------------+        +-------------------+        +--------------------+
| - titulo          |        | - nombre_plan     |        | - nombre           |
| - duracion_min    |        | - precio_mensual  |        | - email            |
| - genero          |        | - resolucion      |        | - plan_activo      |
+-------------------+        +-------------------+        | - mi_lista         |
| + mostrar_info()  |        | + mostrar_plan()  |        +--------------------+
+-------------------+        | + obtener_precio()|        | + contratar_plan() |                                                +-------------------+        | + agregar_a_lista()|
                                                          | + ver_mi_lista()   |
                                                          +--------------------+
---

## 3. Descripción de Clases, Atributos y Métodos

### A. Clase `Contenido` (`src/models.py`)
Representa una película o serie disponible en la plataforma.
- **Atributos Encapsulados (Privados):**
  - `_titulo` (str): Nombre de la película o serie.
  - `_duracion_min` (int): Duración total en minutos.
  - `_genero` (str): Género del contenido (Acción, Animación, Ciencia Ficción, etc.).
- **Métodos:**
  - `__init__(titulo, duracion_min, genero)`: Constructor de la clase.
  - `mostrar_info()`: Imprime los detalles del contenido formatetados.
  - *Getters y Setters* con encapsulamiento.

### B. Clase `PlanSuscripcion` (`src/plan.py`)
Representa el paquete o plan comercial que adquiere el cliente.
- **Atributos Encapsulados (Privados):**
  - `_nombre_plan` (str): Nombre del plan (ej. *Estándar*, *Premium*).
  - `_precio_mensual` (float): Costo mensual en moneda local.
  - `_resolucion` (str): Calidad de transmisión (ej. *1080p Full HD*, *4K UHD + HDR*).
- **Métodos:**
  - `__init__(nombre_plan, precio_mensual, resolucion)`: Constructor.
  - `mostrar_plan()`: Retorna un resumen visual del plan y su precio.

### C. Clase `Usuario` (`src/models.py`)
Representa al cliente registrado en la plataforma.
- **Atributos Encapsulados (Privados):**
  - `_nombre` (str): Nombre completo del usuario.
  - `_email` (str): Correo electrónico.
  - `_plan_activo` (PlanSuscripcion): Objeto de tipo `PlanSuscripcion` que tiene contratado.
  - `_mi_lista` (list): Estructura de datos (lista) que almacena los objetos de tipo `Contenido` favoritos del usuario.
- **Métodos:**
  - `__init__(nombre, email)`: Constructor inicializa la lista vacía de favoritos.
  - `contratar_plan(plan)`: Asigna una instancia de `PlanSuscripcion` al usuario.
  - `agregar_a_lista(contenido)`: Añade un objeto `Contenido` a la lista de reproducción.
  - `ver_mi_lista()`: Muestra todos los títulos guardados en la lista del usuario.

---

## 4. Requisitos Cumplidos
- **Uso de al menos 3 clases:** `Contenido`, `PlanSuscripcion`, `Usuario`.
- **POO:** Implementación de constructores, encapsulamiento de atributos (`_`) y métodos miembro.
- **Estructura de datos:** Uso de listas (`list`) de Python para almacenar el catálogo global y la lista de reproducción por usuario.
- **Interfaz Interactiva:** Menú en consola interactivo ejecutado desde `src/main.py`.
