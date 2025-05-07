<h1 align="center">📚 Laboratorio 4 - Relaciones entre modelos en Django 📘</h1> 

Este laboratorio se enfoca en la implementación de relaciones entre modelos en Django, utilizando una aplicación de gestión bibliotecaria como caso de estudio. El desarrollo incluyó relaciones `OneToOne`, `ForeignKey`, `ManyToMany` y relaciones `ManyToMany` con tabla intermedia.

## ✅ Funcionalidades Implementadas

- Aplicación principal: `library`
- Relaciones entre modelos implementadas:
  - OneToOne (`Author` - `AuthorProfile`)
  - OneToMany (`Author` - `Book`)
  - ManyToMany (`Book` - `Category`)
  - ManyToMany con modelo intermedio (`Book` - `Publisher` con `Publication`)
- Panel de administración personalizado para todos los modelos.
- Plantillas usando Bootstrap 5 con íconos de `bootstrap-icons`.
- Vistas para listar y detallar libros, autores, categorías.
- Página de inicio con estadísticas y contenido dinámico.
- Seed automático de base de datos con datos ficticios mediante un comando personalizado `populate_db`.

## 🧩 Aplicaciones Adicionales Desarrolladas

- `users`: manejo de usuarios personalizados, listas de lectura, reviews.
- `analytics`: vistas y métricas para libros, autores y categorías.

## ⚠️ Estado del Desarrollo de la App `management`

- Iniciado pero incompleto.
- Se definieron modelos como `LibraryBranch`, `BookCopy`, `BookLoan` y `Reservation`.
- Faltó completar vistas, templates y rutas.

## 🚀 Cómo Ejecutar

1. Activar el entorno virtual:
    ```bash
    source venv/bin/activate  # Windows: venv\\Scripts\\activate
    ```
2. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3. Migraciones:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
4. Crear superusuario:
    ```bash
    python manage.py createsuperuser
    ```
5. Poblar base de datos:
    ```bash
    python manage.py populate_db
    ```
6. Ejecutar servidor:
    ```bash
    python manage.py runserver
    ```

## 📌 Rutas Principales

- Inicio: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`
- Libros: `/books/`
- Autores: `/authors/`
- Categorías: `/categories/`

## 📦 Estructura del Proyecto

```bash
library_project/
├── src/
│ ├── config/
│ ├── library/
│ ├── users/
│ ├── analytics/
│ └── management/ # (en progreso)
└── requirements.txt
```

### 👨‍💻 Autor

Huaytalla Rodriguez, Franklin Alvaro - franklin.huaytalla@tecsup.edu.pe

---
<p align="center">Made with ❤️ by the KaiMaki team</p>
