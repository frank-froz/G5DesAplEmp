# 🎬 SeriesApp

Aplicación web para gestionar series , permitiendo listar, crear, editar y eliminar series, con soporte de imágenes y categorización.

---

## 🚀 Tecnologías Usadas

### 🖥️ Frontend
- **React**
- **React Router DOM**
- **Axios**
- **Bootstrap**

### 🛠️ Backend
- **Django**
- **Django REST Framework**
- **CORS Headers**
- **Pillow** (para manejo de imágenes)

---

## ⚙️ Instalación

### 🛠 Backend (Django)

1. Clona el repositorio:
   ```bash
   git clone hhttps://github.com/frank-froz/G5DesAplEmp.git
   cd G5DesAplEmp/Semana12/django-series
   ```

2. Crea entorno virtual y actívalo:
   ```bash
   python -m venv venv
   source venv/bin/activate  # o .\venv\Scripts\activate en Windows
   ```

3. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplica migraciones:
   ```bash
   python manage.py migrate
   ```

5. Corre el servidor:
   ```bash
   python manage.py runserver
   ```

6. Asegúrate de que `MEDIA_URL` esté configurado en `settings.py`:

   ```python
   MEDIA_URL = '/media/'
   MEDIA_ROOT = BASE_DIR / 'media'
   ```

7. Activa `urls.py` para servir imágenes:

   ```python
   from django.conf import settings
   from django.conf.urls.static import static

   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

---

### 🎨 Frontend (React)

1. Navega al frontend:
   ```bash
   cd G5DesAplEmp/Semana12/lab12
   ```

2. Instala dependencias:
   ```bash
   npm install
   ```

3. Corre el proyecto:
   ```bash
   npm run dev
   ```

---

## 📡 Endpoints de la API

### 🔹 Categorías

| Método | Endpoint                          | Descripción              |
|--------|-----------------------------------|--------------------------|
| GET    | `/series/api/v1/categories/`      | Listar categorías        |
| POST   | `/series/api/v1/categories/`      | Crear categoría          |
| GET    | `/series/api/v1/categories/:id/`  | Obtener una categoría    |
| PUT    | `/series/api/v1/categories/:id/`  | Editar categoría         |
| DELETE | `/series/api/v1/categories/:id/`  | Eliminar categoría       |

---

### 🔸 Series

| Método | Endpoint                          | Descripción              |
|--------|-----------------------------------|--------------------------|
| GET    | `/series/api/v1/series/`          | Listar series            |
| POST   | `/series/api/v1/series/`          | Crear serie (con imagen) |
| GET    | `/series/api/v1/series/:id/`      | Ver detalle de serie     |
| PUT    | `/series/api/v1/series/:id/`      | Editar serie             |
| DELETE | `/series/api/v1/series/:id/`      | Eliminar serie           |

---

## 🖼️ Visualización de Imágenes

Las imágenes subidas a través del formulario se almacenan en la carpeta `/media/series/` del backend y se acceden desde React utilizando la URL completa:

```
http://localhost:8000/media/series/nombre-imagen.jpg
```

---

## 📝 Integrantes del Grupo 5

Castro Peñaloza, Hector Hanmer – hector.castro@tecsup.edu.pe

Huaytalla Rodriguez, Franklin Alvaro - franklin.huaytalla@tecsup.edu.pe

Ramos Huaman, Jeyson Kenedy – jeyson.ramos@tecsup.edu.pe

- **Repositorio:** (https://github.com/frank-froz/G5DesAplEmp/tree/main/Semana12)

---

## ✅ Estado del Proyecto

✔️ Funcionalidad de CRUD completa  
✔️ Manejo de imágenes  
✔️ Navegación con React Router  
✔️ Separación por componentes y rutas

---
