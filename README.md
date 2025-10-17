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

**Configuración adicional requerida:**

Asegúrate de configurar también en tu `.env`:
- `BASE_URL_FRONTEND`: URL de tu aplicación frontend (ej: `http://localhost:3000/`)
- `JWT_ALGORITHM`: Algoritmo para JWT, usa `HS256`

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

**Nota:** Si agregaste la app `security` después de la configuración inicial, asegúrate de crear las migraciones:

```bash
python manage.py makemigrations security
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

## � Configuración de Email (Mailtrap)

La aplicación utiliza SMTP para enviar correos electrónicos cuando un usuario envía un mensaje a través del formulario de contacto.

### Configuración para Desarrollo (Mailtrap)

1. Crea una cuenta gratuita en [Mailtrap.io](https://mailtrap.io/)
2. En tu inbox de Mailtrap, ve a **SMTP Settings**
3. Copia las credenciales y agrégalas a tu archivo `.env`:

```bash
SMTP_SERVER=sandbox.smtp.mailtrap.io
SMTP_PORT=2525
SMTP_USERNAME=tu_usuario_mailtrap
SMTP_PASSWORD=tu_contraseña_mailtrap
```

### Configuración para Producción

Para producción, puedes usar servicios como:
- **Gmail** (con contraseña de aplicación)
- **SendGrid**
- **AWS SES**
- **Mailgun**

Ejemplo con Gmail:
```bash
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=tu_email@gmail.com
SMTP_PASSWORD=tu_contraseña_de_aplicacion
```

**Nota:** Para Gmail, necesitas crear una [contraseña de aplicación](https://support.google.com/accounts/answer/185833).

## 🔒 Seguridad

- ✅ **NO** commitees el archivo `.env` a git
- ✅ Usa SECRET_KEY únicas para cada entorno
- ✅ Establece `DEBUG=False` en producción
- ✅ Configura correctamente `ALLOWED_HOSTS` en producción
- ✅ **Autenticación JWT**: Los endpoints críticos están protegidos con JSON Web Tokens
- ✅ **Verificación de email**: Los usuarios deben verificar su correo antes de acceder
- ✅ **Tokens de corta duración**: Los JWT expiran en 24 horas para mayor seguridad

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
│   ├── contact/                 # App de contacto
│   │   ├── models.py            # Modelo ContactMessage
│   │   ├── serializers.py       # Serializador REST
│   │   ├── views.py             # Vistas API
│   │   └── urls.py              # Rutas de contacto
│   ├── security/                # App de seguridad y autenticación
│   │   ├── models.py            # Modelo UsersMetadata
│   │   ├── views.py             # Vistas de registro, login y verificación
│   │   ├── decorators.py        # Decoradores JWT para proteger rutas
│   │   └── urls.py              # Rutas de seguridad
│   ├── utilities/               # Utilidades generales
│   │   └── utilities.py         # Funciones de utilidad (envío de emails)
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
- ✅ PUT - Actualizar categoría parcial
- ✅ DELETE - Eliminar categoría

**Recetas** (`/api/v1/recipes/`)
- ✅ GET - Listar todas las recetas
- ✅ POST - Crear nueva receta
- ✅ GET - Obtener receta por ID (`/api/v1/recipes/<id>/`)
- ✅ PUT - Actualizar receta parcial
- ✅ DELETE - Eliminar receta

**Contacto** (`/api/v1/contact/`)
- ✅ POST - Enviar mensaje de contacto (con notificación por email)

**Seguridad y Autenticación** (`/api/v1/security/`)
- ✅ POST - Registro de usuarios con verificación por email (`/api/v1/security/register/`)
- ✅ GET - Verificación de email mediante token (`/api/v1/security/verify/<token>/`)
- ✅ POST - Login de usuarios con generación de JWT (`/api/v1/security/login/`)
- ✅ Decorador JWT para proteger endpoints (aplicado en rutas de recetas)

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

**ContactMessage**
- `name`: Nombre del usuario (máx. 100 caracteres)
- `email`: Email del usuario
- `phone`: Teléfono del usuario (máx. 12 caracteres)
- `message`: Mensaje del usuario
- `created_at`: Fecha de creación (auto)

**UsersMetadata**
- `user`: Relación con User de Django (ForeignKey)
- `token`: Token de verificación de email (UUID)

### Variables de entorno

#### Django
- `SECRET_KEY`: Clave secreta de Django (obligatoria)
- `DEBUG`: Modo debug (True/False)
- `DJANGO_ALLOWED_HOSTS`: Hosts permitidos (separados por comas)
- `BASE_URL`: URL base de la aplicación
- `BASE_URL_FRONTEND`: URL del frontend (para redirección después de verificación de email)

#### JWT (Autenticación)
- `JWT_ALGORITHM`: Algoritmo para firmar tokens JWT (ej: HS256)

#### Base de Datos
- `DATABASE_URL`: URL de conexión a PostgreSQL
- `POSTGRES_DB`: Nombre de la base de datos
- `POSTGRES_USER`: Usuario de PostgreSQL
- `POSTGRES_PASSWORD`: Contraseña de PostgreSQL
- `POSTGRES_PORT`: Puerto de PostgreSQL (5433 por defecto)

#### Correo Electrónico (SMTP)
- `SMTP_SERVER`: Servidor SMTP (ej: sandbox.smtp.mailtrap.io)
- `SMTP_PORT`: Puerto del servidor SMTP (2525 o 587)
- `SMTP_USERNAME`: Usuario de autenticación SMTP
- `SMTP_PASSWORD`: Contraseña de autenticación SMTP

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
- **python-jose 3.5.0** - Manejo de tokens JWT (JSON Web Tokens)
- **ecdsa 0.19.1** - Algoritmos de firma digital para JWT
- **rsa 4.9.1** - Criptografía RSA para JWT
- **pyasn1 0.6.1** - Soporte ASN.1 para criptografía

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

### Contacto
```bash
# Enviar mensaje de contacto
POST /api/v1/contact/
{
  "name": "Juan Pérez",
  "email": "juan@example.com",
  "phone": "12345678",
  "message": "Hola, me gustaría más información sobre..."
}

# Nota: Este endpoint también envía un email de notificación
# al administrador configurado en las variables de entorno SMTP
```

### Seguridad y Autenticación

#### Registro de Usuario
```bash
POST /api/v1/security/register/
{
  "username": "juanperez",
  "password": "tu_contraseña_segura",
  "email": "juan@example.com",
  "first_name": "Juan",
  "last_name": "Pérez"
}

# Respuesta:
{
  "message": "User registered successfully. Please verify your email.",
  "verification_url": "http://localhost:8000/api/v1/security/verify/<token>/"
}

# Nota: Se enviará un email de verificación a la dirección proporcionada
```

#### Verificación de Email
```bash
GET /api/v1/security/verify/<token>/

# Este endpoint es llamado automáticamente cuando el usuario hace clic
# en el enlace del email de verificación. Redirige al frontend después
# de activar la cuenta.
```

#### Login
```bash
POST /api/v1/security/login/
{
  "email": "juan@example.com",
  "password": "tu_contraseña_segura"
}

# Respuesta exitosa:
{
  "user_id": "123",
  "name": "Juan",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}

# El token JWT debe ser incluido en las peticiones protegidas
# usando el header: Authorization: Bearer <token>
```

#### Uso del Token JWT

Para acceder a endpoints protegidos (como crear, actualizar o eliminar recetas):

```bash
# Ejemplo: Crear una receta (requiere autenticación)
POST /api/v1/recipes/
Headers:
  Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
  Content-Type: multipart/form-data

Body:
{
  "category": 1,
  "name": "Pastel de Chocolate",
  "time": "45 minutos",
  "file": <imagen>,
  "description": "Delicioso pastel..."
}
```

**Endpoints protegidos con JWT:**
- `POST /api/v1/recipes/` - Crear receta
- `PUT /api/v1/recipes/<id>/` - Actualizar receta
- `DELETE /api/v1/recipes/<id>/` - Eliminar receta

**Nota:** El token JWT expira después de 24 horas. El usuario deberá iniciar sesión nuevamente.

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

### Error de autenticación JWT

```bash
# Error: "Authorization header missing"
# Asegúrate de incluir el header Authorization en tus peticiones:
# Authorization: Bearer <tu_token_jwt>

# Error: "Token has expired"
# El token JWT expira en 24 horas. Inicia sesión nuevamente para obtener un nuevo token.

# Error: Token generation failed
# Verifica que JWT_ALGORITHM esté configurado correctamente en .env (usa HS256)
```

### Usuario no puede iniciar sesión

```bash
# Error: "Account is not active. Please verify your email."
# El usuario debe verificar su email haciendo clic en el enlace enviado.
# Verifica la configuración SMTP y revisa Mailtrap si estás en desarrollo.

# Error: "Invalid credentials"
# Verifica que el email y contraseña sean correctos.
```

## 📝 Licencia

Ver archivo [LICENSE](LICENSE)

## 👨‍💻 Autor

BrayanTM

---

**Nota:** Recuerda actualizar tu archivo `.env` con valores reales antes de ejecutar la aplicación.
