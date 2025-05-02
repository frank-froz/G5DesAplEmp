<h1 align="center">Laboratorio 06 - Plantillas y Administrador de Django</h1>

Este laboratorio corresponde a la **semana 06** del curso **Desarrollo de Aplicaciones Empresariales**. El objetivo fue comprender y aplicar el sistema de plantillas de Django, así como configurar el panel de administración para gestionar datos. En esta práctica se logró crear la aplicación principal del portal de noticias.

## 🎯 Objetivo

- Configurar una aplicación Django con sistema de plantillas reutilizables.
- Comprender el uso del administrador para gestionar modelos.
- Crear y registrar modelos básicos (`Article`, `Category`).
- Estructurar un proyecto Django modularmente.

## 🛠️ Tecnologías Utilizadas

- Python 3.10+  
- Django 4.x  
- SQLite3  
- HTML con sistema de plantillas  
- Admin de Django

## 📂 Estructura del Proyecto

```bash

news_portal/
├── news/ # Aplicación de noticias
│ ├── models.py # Modelos: Artículo y Categoría
│ ├── admin.py # Configuración del panel admin
│ ├── views.py # Vistas para artículos
│ ├── templates/ # Plantillas HTML
├── config/ # Configuración general del proyecto
├── static/ # Archivos estáticos
├── db.sqlite3 # Base de datos
└── manage.py
```

## ⚙️ Instalación y Ejecución

1. Crear entorno virtual e instalar dependencias:

```bash
python -m venv venv

source venv/bin/activate  # Windows: venv\\Scripts\\activate

pip install -r requirements.txt
```

Migrar la base de datos y ejecutar el servidor:

```bash
python manage.py makemigrations

python manage.py migrate

python manage.py runserver

```


Acceder a la aplicación:

- Portal de Noticias: http://127.0.0.1:8000/

- Admin: http://127.0.0.1:8000/admin/

### ✅ Funcionalidades Implementadas

- [✔️] Creación de aplicación principal news

- [✔️] Configuración del panel de administración

- [✔️] Definición de modelos Article y Category


#### 📝 Observaciones
No se logró completar la implementación de vistas ni plantillas. Solo se configuró el modelo de datos y la administración básica.

### 👨‍💻 Autores

Castro Peñaloza, Hector Hanmer – hector.castro@tecsup.edu.pe

Huaytalla Rodriguez, Franklin Alvaro - franklin.huaytalla@tecsup.edu.pe

Ramos Huaman, Jeyson Kenedy – jeyson.ramos@tecsup.edu.pe

--- 

<p align="center">Made with ❤️ by the KaiMaki team</p>
