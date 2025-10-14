# RecetarioWeb 🍳

[![CI (Django)](https://github.com/BrayanTM/RecetarioWeb/actions/workflows/django-ci.yml/badge.svg)](https://github.com/BrayanTM/RecetarioWeb/actions/workflows/django-ci.yml)

Aplicación web de recetas desarrollada con Django REST Framework y PostgreSQL. Sistema completo para gestionar recetas de cocina con categorías, imágenes y búsqueda avanzada.

## 📋 Requisitos

- Python 3.12+
- Git
- pip (gestor de paquetes de Python)
- **Docker Desktop** (para PostgreSQL 16)
- virtualenv o venv (para entorno virtual)

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/BrayanTM/RecetarioWeb.git
cd RecetarioWeb
```

### 2. Crear entorno virtual

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
cd backend
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

```bash
# Copiar el archivo de ejemplo
cp ../.env.example ../.env

# Editar .env y configurar tus valores
# En Windows: notepad ../.env
# En Linux/Mac: nano ../.env
```

**IMPORTANTE:** Genera una nueva SECRET_KEY ejecutando:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copia el resultado y pégalo en tu archivo `.env` en la variable `SECRET_KEY`.

### 5. Iniciar PostgreSQL con Docker

```bash
# Asegúrate de que Docker Desktop esté corriendo

# Desde la raíz del proyecto
docker-compose up -d

# Verificar que esté corriendo
docker-compose ps
```

### 6. Ejecutar migraciones

```bash
python manage.py migrate
```

### 7. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 8. Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://localhost:8000`

El panel de administración en: `http://localhost:8000/admin`

## 🔒 Seguridad

- ✅ **NO** commitees el archivo `.env` a git
- ✅ Usa SECRET_KEY únicas para cada entorno
- ✅ Establece `DEBUG=False` en producción
- ✅ Configura correctamente `ALLOWED_HOSTS` en producción

## 🧪 Pruebas

```bash
# Ejecutar tests
python manage.py test

# Verificar configuración de despliegue
python manage.py check --deploy
```

## 📦 Estructura del Proyecto

```
RecetarioWeb/
├── .github/
│   └── workflows/
│       └── django-ci.yml        # GitHub Actions CI/CD
├── backend/
│   ├── backend/                 # Configuración Django
│   │   ├── settings.py          # Configuración principal
│   │   ├── urls.py              # Rutas principales
│   │   └── wsgi.py
│   ├── categories/              # App de categorías
│   │   ├── models.py            # Modelo Category
│   │   ├── serializers.py       # Serializador REST
│   │   ├── views.py             # Vistas API
│   │   └── urls.py              # Rutas de categorías
│   ├── recipes/                 # App de recetas
│   │   ├── models.py            # Modelo Recipe
│   │   ├── serializers.py       # Serializador REST
│   │   ├── views.py             # Vistas API
│   │   └── urls.py              # Rutas de recetas
│   ├── home/                    # App principal
│   ├── example/                 # App de ejemplo
│   ├── uploads/                 # Archivos subidos
│   │   ├── recipes/             # Imágenes de recetas
│   │   └── example/
│   ├── assets/                  # Archivos estáticos
│   ├── manage.py
│   └── requirements.txt         # Dependencias Python
├── docker-compose.yml           # Configuración PostgreSQL
├── .env.example                 # Plantilla de variables de entorno
├── .gitignore
├── LICENSE
└── README.md
```

## 🛠️ Desarrollo

### Características Implementadas

#### 🎯 API REST con Django REST Framework

**Categorías** (`/api/v1/categories/`)
- ✅ GET - Listar todas las categorías
- ✅ POST - Crear nueva categoría
- ✅ GET - Obtener categoría por ID (`/api/v1/categories/<id>/`)
- ✅ PUT - Actualizar categoría completa
- ✅ PATCH - Actualizar categoría parcial
- ✅ DELETE - Eliminar categoría

**Recetas** (`/api/v1/recipes/`)
- ✅ GET - Listar todas las recetas
- ✅ POST - Crear nueva receta
- ✅ GET - Obtener receta por ID (`/api/v1/recipes/<id>/`)
- ✅ PUT - Actualizar receta completa
- ✅ PATCH - Actualizar receta parcial
- ✅ DELETE - Eliminar receta

#### 📊 Modelos de Base de Datos

**Category**
- `name`: Nombre de la categoría (único)
- `slug`: URL amigable (auto-generado)

**Recipe**
- `category`: Relación con Category (ForeignKey)
- `name`: Nombre de la receta (único)
- `slug`: URL amigable (auto-generado)
- `time`: Tiempo de preparación
- `picture`: Imagen de la receta
- `description`: Descripción detallada
- `created_at`: Fecha de creación (auto)

### Variables de entorno

- `SECRET_KEY`: Clave secreta de Django (obligatoria)
- `DEBUG`: Modo debug (True/False)
- `DJANGO_ALLOWED_HOSTS`: Hosts permitidos (separados por comas)
- `DATABASE_URL`: URL de conexión a PostgreSQL
- `POSTGRES_DB`: Nombre de la base de datos
- `POSTGRES_USER`: Usuario de PostgreSQL
- `POSTGRES_PASSWORD`: Contraseña de PostgreSQL
- `POSTGRES_PORT`: Puerto de PostgreSQL (5433 por defecto)

### Base de Datos

- 🐘 **PostgreSQL 16** con Docker
- 📦 Puerto: `5433` (local) → `5432` (contenedor)
- 🔄 Gestión con docker-compose
- 💾 Volumen persistente: `pgdata`

### Tecnologías y Dependencias

- **Django 5.2.7** - Framework web
- **Django REST Framework 3.16.1** - API REST
- **PostgreSQL 16** - Base de datos
- **psycopg2-binary 2.9.10** - Adaptador PostgreSQL
- **django-autoslug 1.9.9** - Generación automática de slugs
- **python-dotenv 1.1.1** - Gestión de variables de entorno
- **dj-database-url 2.3.0** - Configuración de base de datos

### GitHub Actions

El proyecto incluye CI/CD con GitHub Actions que:
- ✅ Verifica la configuración de Django
- ✅ Ejecuta migraciones
- ✅ Ejecuta tests (cuando estén configurados)
- ✅ Se ejecuta en cada push a `main` y en pull requests

## 🔗 Endpoints de la API

### Base URL
```
http://localhost:8000/api/v1/
```

### Categorías
```bash
# Listar todas las categorías
GET /api/v1/categories/

# Crear nueva categoría
POST /api/v1/categories/
{
  "name": "Postres"
}

# Obtener una categoría
GET /api/v1/categories/<id>/

# Actualizar categoría
PUT /api/v1/categories/<id>/
PATCH /api/v1/categories/<id>/

# Eliminar categoría
DELETE /api/v1/categories/<id>/
```

### Recetas
```bash
# Listar todas las recetas
GET /api/v1/recipes/

# Crear nueva receta
POST /api/v1/recipes/
{
  "category": 1,
  "name": "Pastel de Chocolate",
  "time": "45 minutos",
  "picture": "path/to/image.jpg",
  "description": "Delicioso pastel..."
}

# Obtener una receta
GET /api/v1/recipes/<id>/

# Actualizar receta
PUT /api/v1/recipes/<id>/
PATCH /api/v1/recipes/<id>/

# Eliminar receta
DELETE /api/v1/recipes/<id>/
```

## 🐛 Solución de Problemas

### Error de conexión a PostgreSQL

```bash
# Verificar que Docker esté corriendo
docker ps

# Reiniciar el contenedor
docker-compose down
docker-compose up -d

# Ver logs del contenedor
docker-compose logs db
```

### Error con SECRET_KEY

```bash
# Generar nueva SECRET_KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Actualizar .env con el valor generado
```

### Reinstalar dependencias

```bash
# Activar entorno virtual
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Reinstalar
pip install -r requirements.txt --upgrade
```

## 📝 Licencia

Ver archivo [LICENSE](LICENSE)

## 👨‍💻 Autor

BrayanTM

---

**Nota:** Recuerda actualizar tu archivo `.env` con valores reales antes de ejecutar la aplicación.
