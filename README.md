# RecetarioWeb 🍳

[![CI (Django)](https://github.com/BrayanTM/RecetarioWeb/actions/workflows/django-ci.yml/badge.svg)](https://github.com/BrayanTM/RecetarioWeb/actions/workflows/django-ci.yml)

Aplicación web de recetas desarrollada con Django.

## 📋 Requisitos

- Python 3.12+
- Git
- pip (gestor de paquetes de Python)

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

### 5. Ejecutar migraciones

```bash
python manage.py migrate
```

### 6. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 7. Ejecutar servidor de desarrollo

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
│       └── CI_Django_Vue.yml    # GitHub Actions CI/CD
├── backend/
│   ├── backend/                 # Configuración Django
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── home/                    # App principal
│   ├── manage.py
│   └── requirements.txt         # Dependencias Python
├── .env.example                 # Plantilla de variables de entorno
├── .gitignore
└── LICENSE
```

## 🛠️ Desarrollo

### Variables de entorno

- `SECRET_KEY`: Clave secreta de Django (obligatoria)
- `DEBUG`: Modo debug (True/False)
- `DJANGO_ALLOWED_HOSTS`: Hosts permitidos (separados por comas)

### GitHub Actions

El proyecto incluye CI/CD con GitHub Actions que:
- ✅ Verifica la configuración de Django
- ✅ Ejecuta migraciones
- ✅ Ejecuta tests (cuando estén configurados)
- ✅ Se ejecuta en cada push a `main` y en pull requests

## 📝 Licencia

Ver archivo [LICENSE](LICENSE)

## 👨‍💻 Autor

BrayanTM

---

**Nota:** Recuerda actualizar tu archivo `.env` con valores reales antes de ejecutar la aplicación.
