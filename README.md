# RecetarioWeb 🍳

[![CI (Django)](https://github.com/BrayanTM/RecetarioWeb/actions/workflows/django-ci.yml/badge.svg)](https://github.com/BrayanTM/RecetarioWeb/actions/workflows/django-ci.yml)

Aplicación web de recetas desarrollada con Django REST Framework y PostgreSQL. Sistema completo para gestionar recetas de cocina con categorías, imágenes y búsqueda avanzada.

## 📋 Requisitos

### Backend
- Python 3.12+
- Git
- pip (gestor de paquetes de Python)
- **Docker Desktop** (para PostgreSQL 18)
- virtualenv o venv (para entorno virtual)

### Frontend
- Node.js 20.19.0+ o 22.12.0+
- npm (incluido con Node.js)

## 📚 Documentación de la API

Este proyecto incluye documentación interactiva completa de la API utilizando **Swagger/OpenAPI**.

Una vez que el servidor esté corriendo, accede a:
- **Swagger UI** (interfaz interactiva): `http://localhost:8000/docs/`
- **ReDoc** (documentación alternativa): `http://localhost:8000/redoc/`
- **Schema JSON**: `http://localhost:8000/docs.json/`

Ver documentación detallada de endpoints en: [backend/docs/ENDPOINTS_DOCUMENTATION.md](backend/docs/ENDPOINTS_DOCUMENTATION.md)

## 🚀 Instalación y Configuración

### Backend

#### 1. Clonar el repositorio

```bash
git clone https://github.com/BrayanTM/RecetarioWeb.git
cd RecetarioWeb
```

#### 2. Crear entorno virtual

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. Instalar dependencias

```bash
cd backend
pip install -r requirements.txt
```

#### 4. Configurar variables de entorno

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
- `CORS_ORIGIN_WHITELIST`: Lista de orígenes permitidos para CORS (separados por comas)
- `CORS_ORIGIN_REGEX_WHITELIST`: Patrones regex para orígenes CORS dinámicos

#### 5. Iniciar PostgreSQL con Docker

```bash
# Asegúrate de que Docker Desktop esté corriendo

# Desde la raíz del proyecto
docker-compose up -d

# Verificar que esté corriendo
docker-compose ps
```

#### 6. Ejecutar migraciones

```bash
python manage.py migrate
```

**Nota:** Si agregaste la app `security` después de la configuración inicial, asegúrate de crear las migraciones:

```bash
python manage.py makemigrations security
python manage.py migrate
```

#### 7. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

#### 8. Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

La aplicación estará disponible en: `http://localhost:8000`

El panel de administración en: `http://localhost:8000/admin`

### Frontend

#### 1. Instalar dependencias

```bash
cd frontend
npm install
```

#### 2. Configurar variables de entorno (recomendado)

El frontend utiliza variables de entorno de Vite para conectarse al backend:

```bash
# Copiar el archivo de ejemplo
cp .env.example .env

# Editar .env si necesitas cambiar configuraciones
# En Windows: notepad .env
# En Linux/Mac: nano .env
```

**Configuración por defecto en `.env`:**
```bash
VITE_API_URL=http://localhost:8000/api/v1
VITE_APP_TITLE=RecetarioWeb - Cookbook
```

**Importante:**
- ✅ Todas las variables de Vite deben comenzar con `VITE_`
- ✅ Las variables se incrustan en tiempo de compilación
- ✅ Debes reiniciar el servidor de desarrollo después de cambiar variables
- ✅ La aplicación funcionará con valores predeterminados si no existe el archivo `.env`

#### 3. Ejecutar servidor de desarrollo

```bash
npm run dev
```

La aplicación frontend estará disponible en: `http://localhost:5173`

**Páginas disponibles:**
- 🏠 Home: `http://localhost:5173/`
- 👥 About Us: `http://localhost:5173/about-us`
- 📖 Recipe Detail: `http://localhost:5173/recipe/:slug` (ej: `/recipe/pastel-de-chocolate`)

#### 4. Compilar para producción

```bash
npm run build
```

Los archivos compilados estarán en: `frontend/dist/`

#### 5. Vista previa de la compilación de producción

```bash
npm run preview
```

Esto iniciará un servidor local para previsualizar la versión de producción.

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
# Ejecutar tests del backend
cd backend
python manage.py test

# Verificar configuración de despliegue
python manage.py check --deploy

# Frontend: Ejecutar linter
cd frontend
npm run lint
```

## 📸 Contenido de Ejemplo

El proyecto incluye **20 recetas de ejemplo** con imágenes en `backend/uploads/recipes/`:

- 🥑 Avocado Toast
- 🍫 Brownies
- 🍞 Bruschetta
- 🌯 Burrito Bowl
- 🥗 Caesar Salad
- 🧁 Cupcakes
- 🧀 Grilled Cheese
- 🍗 Grilled Chicken
- ☕ Iced Coffee
- 🍋 Lemon Smoothie
- 🧀 Mac and Cheese
- 🥞 Pancakes
- 🥗 Quinoa Salad
- 🐟 Salmon
- 🍳 Scrambled Eggs
- 🍝 Spaghetti Bolognese
- 🍄 Stuffed Mushrooms
- 🍣 Sushi
- 🌮 Tacos al Pastor
- 🥡 Tofu Stir-Fry

Estas imágenes se utilizan para **desarrollo y pruebas**. En producción, los usuarios subirán sus propias imágenes de recetas.

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
│   ├── recipe_helper/           # App auxiliar para endpoints del frontend
│   │   ├── views.py             # Vistas de panel de usuario, búsqueda y home
│   │   └── urls.py              # Rutas auxiliares de recetas
│   ├── utilities/               # Utilidades generales
│   │   └── utilities.py         # Funciones de utilidad (envío de emails)
│   ├── home/                    # App principal
│   ├── example/                 # App de ejemplo
│   ├── uploads/                 # Archivos subidos
│   │   ├── recipes/             # Imágenes de recetas (20+ imágenes)
│   │   └── example/
│   ├── assets/                  # Archivos estáticos
│   ├── docs/                    # Documentación adicional
│   │   └── ENDPOINTS_DOCUMENTATION.md
│   ├── manage.py
│   └── requirements.txt         # Dependencias Python
├── frontend/                    # Aplicación Vue.js 3
│   ├── public/                  # Archivos públicos estáticos
│   │   ├── css/                 # Hojas de estilo (Bootstrap, Animate, etc.)
│   │   ├── img/                 # Imágenes del sitio
│   │   ├── js/                  # JavaScript (jQuery, plugins, etc.)
│   │   ├── fonts/               # Fuentes personalizadas
│   │   ├── scss/                # Archivos SCSS (preprocesador CSS)
│   │   └── style.css            # Estilos principales
│   ├── src/
│   │   ├── components/          # Componentes reutilizables
│   │   │   ├── HeaderBase.vue   # Barra de navegación
│   │   │   └── FooterBase.vue   # Pie de página
│   │   ├── views/               # Vistas/Páginas principales
│   │   │   ├── HomePage.vue     # Página de inicio
│   │   │   ├── AboutUs.vue      # Página "Nosotros"
│   │   │   ├── RecipeDetail.vue # Detalle de receta
│   │   │   └── ErrorPage404.vue # Página de error 404
│   │   ├── services/            # Servicios de API
│   │   │   └── homeServices.js  # Servicios para home
│   │   ├── router/              # Configuración de rutas
│   │   │   └── index.js         # Rutas de Vue Router
│   │   ├── stores/              # Stores de Pinia (gestión de estado)
│   │   ├── App.vue              # Componente raíz de Vue
│   │   └── main.js              # Punto de entrada de la aplicación
│   ├── index.html               # HTML principal
│   ├── vite.config.js           # Configuración de Vite
│   ├── package.json             # Dependencias de Node.js
│   ├── eslint.config.js         # Configuración de ESLint
│   ├── jsconfig.json            # Configuración de JavaScript
│   ├── .env.example             # Plantilla de variables de entorno
│   └── README.md                # Documentación del frontend
├── docker-compose.yml           # Configuración PostgreSQL
├── .env.example                 # Plantilla de variables de entorno (backend)
├── .gitignore
├── LICENSE
└── README.md
```

## 🛠️ Desarrollo

### Características Implementadas

#### 🎨 Aplicación Frontend Vue.js 3
- ✅ **Componentes reutilizables**:
  - `HeaderBase.vue`: Barra de navegación con menú y enlaces
  - `FooterBase.vue`: Pie de página con información del desarrollador
- ✅ **Vistas principales**:
  - `HomePage.vue`: Página principal con recetas destacadas
  - `AboutUs.vue`: Información sobre el proyecto
  - `RecipeDetail.vue`: Detalle de cada receta (en desarrollo)
  - `ErrorPage404.vue`: Página de error personalizada
- ✅ **Servicios API**:
  - `homeServices.js`: Conexión con endpoints del backend
  - Integración con `VITE_API_URL` para consumo de API REST
- ✅ **Sistema de navegación**:
  - Vue Router configurado con rutas dinámicas
  - Navegación por slug para recetas
  - Redirección automática a página 404
- ✅ **Assets y recursos**:
  - CSS personalizado y responsive
  - Bootstrap 5 integrado
  - Imágenes y fuentes optimizadas
  - JavaScript para interactividad (menú, carruseles, etc.)

#### 📖 Documentación Automática con Swagger/OpenAPI
- ✅ **drf-yasg** integrado para documentación automática
- ✅ **Swagger UI** disponible en `/docs/`
- ✅ **ReDoc** disponible en `/redoc/`
- ✅ Todos los endpoints documentados con descripciones, parámetros y respuestas
- ✅ Soporte para multipart/form-data (subida de archivos)
- ✅ Documentación de autenticación JWT

#### 🌐 CORS (Cross-Origin Resource Sharing)
- ✅ **django-cors-headers** configurado
- ✅ Whitelist configurable de orígenes permitidos
- ✅ Soporte para patrones regex en orígenes
- ✅ Credentials habilitados para peticiones con cookies/auth

#### 🎯 API REST con Django REST Framework

**Categorías** (`/api/v1/categories/`)
- ✅ GET - Listar todas las categorías
- ✅ POST - Crear nueva categoría
- ✅ GET - Obtener categoría por ID (`/api/v1/categories/<id>/`)
- ✅ PUT - Actualizar categoría parcial
- ✅ DELETE - Eliminar categoría

**Recetas** (`/api/v1/recipes/`)
- ✅ GET - Listar todas las recetas
- ✅ POST - Crear nueva receta (requiere autenticación JWT)
- ✅ GET - Obtener receta por ID (`/api/v1/recipes/<id>/`)
- ✅ PUT - Actualizar receta parcial (requiere autenticación JWT)
- ✅ DELETE - Eliminar receta (requiere autenticación JWT)

**Recipe Helper** (`/api/v1/`)
- ✅ GET - Panel de recetas por usuario (`/api/v1/recipes-panel/<user_id>/`)
- ✅ GET - Detalle de receta por slug (`/api/v1/recipes/slug/<slug>/`)
- ✅ GET - Recetas aleatorias para home (`/api/v1/recipes/home/`)
- ✅ GET - Búsqueda de recetas por categoría (`/api/v1/recipes/search/?category_id=<id>&search=<query>`)

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
- `user`: Relación con User (ForeignKey) - Usuario propietario de la receta
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

#### CORS (Cross-Origin Resource Sharing)
- `CORS_ORIGIN_WHITELIST`: Lista de orígenes permitidos para peticiones CORS (separados por comas)
- `CORS_ORIGIN_REGEX_WHITELIST`: Patrones regex para orígenes CORS dinámicos (separados por comas)

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

- 🐘 **PostgreSQL 18** con Docker
- 📦 Puerto: `5433` (local) → `5432` (contenedor)
- 🔄 Gestión con docker-compose
- 💾 Volumen persistente: `pgdata`

### Frontend

- ⚡ **Vite 7.1.7** - Build tool y dev server ultrarrápido
- 🎨 **Vue 3.5.22** - Framework progresivo de JavaScript
- 🗂️ **Vue Router 4.5.1** - Enrutamiento oficial para Vue.js
- 📦 **Pinia 3.0.3** - Store oficial para Vue.js (gestión de estado)
- 🧹 **ESLint 9.33.0** - Linter para JavaScript/Vue
- 🛠️ **Vue DevTools** - Plugin de desarrollo integrado
- 🎯 **Node.js 20.19+** o **22.12+** requerido

### Tecnologías y Dependencias

- **Django 5.2.7** - Framework web
- **Django REST Framework 3.16.1** - API REST
- **drf-yasg 1.21.11** - Generación automática de documentación Swagger/OpenAPI
- **django-cors-headers 4.9.0** - Gestión de CORS (Cross-Origin Resource Sharing)
- **PostgreSQL 16** - Base de datos
- **psycopg2-binary 2.9.11** - Adaptador PostgreSQL
- **django-autoslug 1.9.9** - Generación automática de slugs
- **python-dotenv 1.1.1** - Gestión de variables de entorno
- **dj-database-url 3.0.1** - Configuración de base de datos mediante URL
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

### 📚 Documentación Completa

**¡IMPORTANTE!** Para ver la documentación completa e interactiva de todos los endpoints:

1. **Inicia el servidor**: `python manage.py runserver`
2. **Accede a Swagger UI**: `http://localhost:8000/docs/`
3. **O consulta**: [backend/docs/ENDPOINTS_DOCUMENTATION.md](backend/docs/ENDPOINTS_DOCUMENTATION.md)

La documentación Swagger incluye:
- ✅ Descripción detallada de cada endpoint
- ✅ Parámetros requeridos y opcionales
- ✅ Tipos de datos esperados
- ✅ Ejemplos de peticiones y respuestas
- ✅ Códigos de estado HTTP
- ✅ **Interfaz interactiva** para probar los endpoints directamente

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
# Listar todas las recetas (administración)
GET /api/v1/recipes/

# Crear nueva receta (requiere autenticación JWT)
POST /api/v1/recipes/
Headers:
  Authorization: Bearer <token>
  Content-Type: multipart/form-data
Body:
{
  "category": 1,
  "name": "Pastel de Chocolate",
  "time": "45 minutos",
  "file": <imagen>,
  "description": "Delicioso pastel..."
}
# Nota: El campo 'user' se asigna automáticamente desde el token JWT

# Obtener una receta por ID (administración)
GET /api/v1/recipes/<id>/

# Actualizar receta (requiere autenticación JWT)
PUT /api/v1/recipes/<id>/
Headers:
  Authorization: Bearer <token>
  Content-Type: multipart/form-data

# Eliminar receta (requiere autenticación JWT)
DELETE /api/v1/recipes/<id>/
Headers:
  Authorization: Bearer <token>
```

### Recipe Helper (Endpoints para Frontend)
```bash
# Panel de recetas del usuario
GET /api/v1/recipes-panel/<user_id>/
# Retorna todas las recetas creadas por un usuario específico

# Detalle de receta por slug (para URLs amigables)
GET /api/v1/recipes/slug/<slug>/
# Ejemplo: /api/v1/recipes/slug/pastel-de-chocolate/

# Recetas aleatorias para página de inicio
GET /api/v1/recipes/home/
# Retorna 3 recetas aleatorias

# Búsqueda de recetas por categoría
GET /api/v1/recipes/search/?category_id=<id>&search=<query>
# Parámetros:
#   - category_id: ID de la categoría (requerido)
#   - search: Término de búsqueda en el nombre (opcional, puede estar vacío)
# Ejemplo: /api/v1/recipes/search/?category_id=1&search=chocolate
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

# Nota: El campo 'user' se asigna automáticamente desde el token JWT
# No es necesario incluirlo en la petición
```

**Endpoints protegidos con JWT:**
- `POST /api/v1/recipes/` - Crear receta (el usuario se asigna automáticamente)
- `PUT /api/v1/recipes/<id>/` - Actualizar receta
- `DELETE /api/v1/recipes/<id>/` - Eliminar receta
- `GET /api/v1/recipes-panel/<user_id>/` - Ver recetas de un usuario (con logging)

**Endpoints públicos (Recipe Helper):**
- `GET /api/v1/recipes/slug/<slug>/` - Ver detalle de receta por slug
- `GET /api/v1/recipes/home/` - Obtener recetas aleatorias para home
- `GET /api/v1/recipes/search/` - Buscar recetas por categoría

**Nota:** El token JWT expira después de 24 horas. El usuario deberá iniciar sesión nuevamente.

## � Mejores Prácticas de Desarrollo

### Variables de Entorno

#### Backend (.env)
- ✅ **Nunca** commitees el archivo `.env` a git
- ✅ Genera una `SECRET_KEY` única para cada entorno
- ✅ Usa `DEBUG=False` en producción
- ✅ Configura correctamente `ALLOWED_HOSTS` para producción
- ✅ Actualiza `CORS_ORIGIN_WHITELIST` según tus dominios
- ✅ Usa contraseñas fuertes para la base de datos
- ✅ Configura SMTP con credenciales reales en producción

#### Frontend (.env)
- ✅ Incluye el slash final en `VITE_API_URL` (ej: `/api/v1/`)
- ✅ Todas las variables deben comenzar con `VITE_`
- ✅ Reinicia el servidor de desarrollo después de cambiar el `.env`
- ✅ Las variables se incrustan en tiempo de compilación, no en runtime

### Desarrollo Local

#### Orden de inicio recomendado:
1. **Docker** (PostgreSQL): `docker-compose up -d`
2. **Backend** (Django): `cd backend && python manage.py runserver`
3. **Frontend** (Vue): `cd frontend && npm run dev`

#### Antes de hacer commits:
```bash
# Backend: Ejecutar tests
cd backend
python manage.py test

# Frontend: Ejecutar linter
cd frontend
npm run lint

# Verificar estado de git
git status
```

### Integración Frontend-Backend

#### Comunicación entre capas:
- 🔗 Frontend consume la API REST del backend
- 🌐 CORS debe estar configurado correctamente
- 🔑 JWT se usa para autenticación en endpoints protegidos
- 📤 Las imágenes se suben al backend y se sirven desde `/uploads/`

#### URLs importantes:
- Backend API: `http://localhost:8000/api/v1/`
- Documentación Swagger: `http://localhost:8000/docs/`
- Frontend App: `http://localhost:5173/`
- Admin Django: `http://localhost:8000/admin/`

## �🐛 Solución de Problemas

### Backend

#### Error de conexión a PostgreSQL

```bash
# Verificar que Docker esté corriendo
docker ps

# Reiniciar el contenedor
docker-compose down
docker-compose up -d

# Ver logs del contenedor
docker-compose logs db
```

#### Error con SECRET_KEY

```bash
# Generar nueva SECRET_KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Actualizar .env con el valor generado
```

#### Reinstalar dependencias

```bash
# Activar entorno virtual
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Reinstalar
pip install -r requirements.txt --upgrade
```

#### Error de autenticación JWT

```bash
# Error: "Authorization header missing"
# Asegúrate de incluir el header Authorization en tus peticiones:
# Authorization: Bearer <tu_token_jwt>

# Error: "Token has expired"
# El token JWT expira en 24 horas. Inicia sesión nuevamente para obtener un nuevo token.

# Error: Token generation failed
# Verifica que JWT_ALGORITHM esté configurado correctamente en .env (usa HS256)
```

#### Usuario no puede iniciar sesión

```bash
# Error: "Account is not active. Please verify your email."
# El usuario debe verificar su email haciendo clic en el enlace enviado.
# Verifica la configuración SMTP y revisa Mailtrap si estás en desarrollo.

# Error: "Invalid credentials"
# Verifica que el email y contraseña sean correctos.
```

### Frontend

#### Error al instalar dependencias

```bash
# Limpiar caché de npm
npm cache clean --force

# Eliminar node_modules y reinstalar
rm -rf node_modules package-lock.json
npm install
```

#### Puerto 5173 ya está en uso

```bash
# Vite usa el puerto 5173 por defecto
# Si está ocupado, Vite automáticamente usará el siguiente disponible (5174, etc.)

# O puedes especificar un puerto diferente:
npm run dev -- --port 3000
```

#### Errores de ESLint

```bash
# Ejecutar el linter y corregir automáticamente
npm run lint

# Si persisten errores, revisa eslint.config.js
```

#### El frontend no se conecta al backend

```bash
# 1. Verifica que el backend esté corriendo en http://localhost:8000
python manage.py runserver  # En el directorio backend

# 2. Verifica la variable de entorno en frontend/.env
# Debe contener: VITE_API_URL=http://localhost:8000/api/v1

# 3. Verifica la configuración de CORS en el backend (.env):
# CORS_ORIGIN_WHITELIST debe incluir http://localhost:5173

# 4. Si usas un puerto diferente, actualiza ambas configuraciones
```

#### Error de hot-reload no funciona

```bash
# Reinicia el servidor de desarrollo
# Ctrl+C para detener
npm run dev

# En algunos sistemas, puede ser necesario configurar el watcher
# Agrega en vite.config.js:
# server: { watch: { usePolling: true } }
```

#### Las imágenes no se muestran correctamente

```bash
# Las imágenes deben estar en la carpeta public/ del frontend
# O en backend/uploads/ para las subidas desde la API

# Verifica que la URL de la imagen sea correcta:
# Frontend: /img/ruta/imagen.jpg (desde public/)
# Backend: http://localhost:8000/uploads/recipes/imagen.jpg
```

#### Error "VITE_API_URL is not defined"

```bash
# Asegúrate de que existe el archivo .env en la carpeta frontend
cd frontend
cp .env.example .env

# Verifica que la variable comience con VITE_
# Incorrecto: API_URL=...
# Correcto: VITE_API_URL=...

# Reinicia el servidor de desarrollo después de crear/modificar el .env
```

## 📝 Licencia

Ver archivo [LICENSE](LICENSE)

## 🆕 Historial de Cambios Recientes

### Octubre 2025 - v3.1
- ✅ **Frontend Vue.js 3 completamente funcional**
  - ✨ Componentes reutilizables: `HeaderBase` y `FooterBase`
  - 📄 Múltiples vistas: HomePage, AboutUs, RecipeDetail, ErrorPage404
  - 🔀 Sistema de rutas completo con Vue Router
  - 🎨 Integración de assets públicos (CSS, imágenes, JS, fonts)
  - 🔌 Servicio de API: `homeServices.js` conectado al backend
  - 📱 Diseño responsive con Bootstrap y CSS personalizado
  - 🌐 Navegación fluida entre páginas
  - 🔗 Enlaces dinámicos a recetas por slug
  - 🎭 Animaciones CSS con Animate.css
  - 🎯 Font Awesome para iconografía
- ✅ **Contenido dinámico de recetas**
  - 🖼️ 20 imágenes de ejemplo de recetas en `backend/uploads/recipes/`
  - 📊 Datos de prueba para desarrollo (tacos, sushi, pancakes, etc.)
  - 🎲 Recetas aleatorias en página de inicio
  - 🔍 Sistema de búsqueda por categoría implementado
- ✅ **Integración Frontend-Backend**
  - ⚡ Consumo de API REST desde Vue
  - 🔄 Variables de entorno con Vite (VITE_API_URL)
  - 🌍 CORS configurado correctamente
  - 📡 Servicio `homeServices.js` para comunicación con la API
- ✅ **Archivos de configuración actualizados**
  - 📝 `.env.example` sincronizado en backend y frontend
  - 📚 README mejorado con documentación completa
  - 🔧 Variables de entorno documentadas

### Octubre 2025 - v3.0
- ✅ **Frontend Vue.js 3 implementado**
  - Aplicación SPA con Vue 3.5.22
  - Vite 7.1.7 como build tool y dev server
  - Vue Router 4.5.1 para navegación
  - Pinia 3.0.3 para gestión de estado
  - ESLint configurado para código limpio
  - Vue DevTools integrado
- ✅ **PostgreSQL actualizado a versión 18**
  - Docker Compose actualizado con imagen postgres:18
  - Compatibilidad mejorada y mejor rendimiento
- ✅ **Estructura de proyecto full-stack**
  - Separación clara entre backend y frontend
  - Configuración independiente de cada capa
  - README actualizado con instrucciones para ambas partes

### Octubre 2025 - v2.0
- ✅ **Documentación Swagger/OpenAPI completa** con drf-yasg
  - Interfaz interactiva en `/docs/` y `/redoc/`
  - Todos los endpoints documentados con ejemplos
  - Soporte para multipart/form-data correctamente configurado
- ✅ **CORS configurado** con django-cors-headers
  - Whitelist configurable de orígenes
  - Soporte para patrones regex
- ✅ **Mejoras en seguridad**
  - Autenticación JWT mejorada
  - Decoradores para protección de endpoints
  - Validación de tokens optimizada
- ✅ **Nuevas dependencias**
  - drf-yasg 1.21.11 (documentación API)
  - django-cors-headers 4.9.0 (CORS)
  - inflection 0.5.1 (transformación de nombres)
  - packaging 25.0 (gestión de versiones)
  - pytz 2025.2 (zonas horarias)
  - PyYAML 6.0.3 (parsing YAML)
  - uritemplate 4.2.0 (templates de URI)
- ✅ **Documentación actualizada**
  - README mejorado con nuevas secciones
  - Documentación detallada de endpoints
  - Guías de solución de problemas

## � Estado del Proyecto

### Funcionalidades Completadas
- ✅ Backend Django REST Framework completamente funcional
- ✅ Frontend Vue.js 3 con múltiples vistas y componentes
- ✅ Sistema de autenticación JWT con verificación de email
- ✅ CRUD completo de recetas y categorías
- ✅ Sistema de contacto con notificaciones por email
- ✅ Documentación Swagger/OpenAPI interactiva
- ✅ PostgreSQL 18 con Docker Compose
- ✅ CORS configurado para desarrollo y producción
- ✅ 20 recetas de ejemplo con imágenes

### En Desarrollo
- 🚧 Vista de detalle de receta (RecipeDetail.vue)
- 🚧 Sistema de búsqueda avanzada de recetas
- 🚧 Panel de usuario para gestionar recetas propias
- 🚧 Sistema de registro y login en el frontend
- 🚧 Página de contacto en el frontend

### Próximas Características
- 📅 Sistema de favoritos
- 📅 Comentarios y valoraciones en recetas
- 📅 Compartir recetas en redes sociales
- 📅 Filtros avanzados de búsqueda
- 📅 Perfil de usuario completo

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

**Nota:** Recuerda actualizar tu archivo `.env` con valores reales antes de ejecutar la aplicación.

**Última actualización:** Octubre 2025 - v3.1
