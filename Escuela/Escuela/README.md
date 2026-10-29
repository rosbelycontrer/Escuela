# Escuela – CRUD de Alumnos y Materias (Python + MySQL + Tkinter)

## Estructura de archivos
| Archivo | Qué hace |
|---|---|
| `escuela.sql` | Crea la base `escuela` con las tablas `alumno` y `materia` (5 campos cada una) y datos de ejemplo |
| `base_datos.py` | Clase **Base_datos** (gestor): conexión y métodos `tomar_info`, `buscar`, `guardar`, `actualizar`, `eliminar` |
| `alumnos.py` | Clase **Alumnos** con su constructor y métodos CRUD |
| `materias.py` | Clase **Materias** con su constructor y métodos CRUD |
| `interfaz.py` | Clase **Interfaz** (Tkinter) con pestañas Alumnos y Materias |
| `principal.py` | Código principal: crea los objetos y abre la ventana |

## Cómo ejecutarlo
1. Abrir XAMPP y encender **MySQL** (y Apache para phpMyAdmin).
2. En phpMyAdmin → pestaña **SQL** → pegar el contenido de `escuela.sql` → **Continuar**.
3. Instalar el conector:
   ```
   python -m pip install mysql-connector-python
   ```
4. Ejecutar:
   ```
   python principal.py
   ```

## CRUD en la interfaz
- **Guardar** → INSERT (Create)
- **Mostrar / Buscar** → SELECT (Read) – `fetchall()` devuelve un arreglo de duplas
- **Actualizar** → UPDATE (Update)
- **Eliminar** → DELETE (Delete)
- Clic en una fila de la tabla llena los campos automáticamente.
