# Laboratorio 07 - Dominando el ORM de Django

Este laboratorio se enfoca en el manejo avanzado del **ORM de Django**, desarrollando una plataforma de blog que utiliza relaciones entre modelos, consultas personalizadas, y anotaciones básicas. Es parte del curso **Desarrollo de Aplicaciones Empresariales**.

## 🎯 Objetivo

Aprender a implementar relaciones entre modelos en Django, incluyendo:

- Relaciones uno a muchos (ForeignKey)
- Relaciones muchos a muchos (ManyToMany)
- Consultas personalizadas con managers (ORM)
- Filtros complejos y anotaciones

  
## 🛠️ Tecnologías Utilizadas

- Python 3.10+  
- Django 4.x  
- SQLite3 (por defecto)  
- HTML/CSS básico para plantillas  
- Bootstrap (opcional)

## 📂 Estructura del Proyecto

```
blog_platform/
├── src/
│ ├── config/               # Configuración del proyecto
│ ├── blog/                 # Aplicación principal del blog
│ │ ├── models.py           # Modelos de datos con relaciones
│ │ ├── views.py            # Vistas basadas en clases
│ │ ├── urls.py             # Rutas de la app
│ │ ├── admin.py            # Configuración del panel administrativo
│ │ └── managers.py         # Managers personalizados
│ ├── templates/            # Plantillas HTML
│ ├── static/               # Archivos estáticos (CSS, JS)
│ └── manage.py             # Script principal de Django
├── requirements.txt        # Dependencias del Proyecto
└── .gitignore
```


## ⚙️ Instalación y Ejecución

1. Crear entorno virtual e instalar dependencias:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```


## Migrar la base de datos
```
python manage.py makemigrations
python manage.py migrate
```
## Ejecutar el servidor
```
python manage.py runserver
```

Acceder a:

- Blog: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- Usuario admin de prueba:
- Usuario: admin
- Contraseña: admin123

## ✅ Funcionalidades Implementadas
- [✔️] Modelos con relaciones uno a muchos y muchos a muchos

- [✔️] Panel de administración personalizado

- [✔️] Creación de vistas con CBV (Class-Based Views)

- [✔️] Registro de nuevos usuarios

- [✔️] Inicio y cierre de sesión (login/logout)

### 👨‍💻 Autores

Castro Peñaloza, Hector Hanmer – hector.castro@tecsup.edu.pe

Huaytalla Rodriguez, Franklin Alvaro - franklin.huaytalla@tecsup.edu.pe

Ramos Huaman, Jeyson Kenedy – jeyson.ramos@tecsup.edu.pe

- Desarrollo de Aplicaciones Empresariales
- TECSUP - 2025-1

<p align="center">Made with ❤️ by the KaiMaki team</p>
