# RecetarioWeb 🍳

[![CI (Django)](https://github.com/BrayanTM/RecetarioWeb/actions/workflows/django-ci.yml/badge.svg)](https://github.com/BrayanTM/RecetarioWeb/actions/workflows/django-ci.yml)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.7-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.5.22-4FC08D?style=flat&logo=vue.js&logoColor=white)](https://vuejs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📖 Descripción del Proyecto

**RecetarioWeb** es una aplicación web full-stack moderna y robusta diseñada para **gestionar, compartir y descubrir recetas de cocina**. El proyecto combina un backend potente desarrollado con **Django REST Framework** y un frontend interactivo construido con **Vue.js 3**, ofreciendo una experiencia de usuario fluida y profesional.

> Tomar en consideración que el backend tarda al rededor de 30 segundos en iniciar debido a que este se encuentra alojado en la capa gratuita de Render. Luego de 30 segundos refresca la página para poder visualizar las recetas, registrarte, iniciar sesión...

[Cookbook](https://cookbook-bice-eight.vercel.app/)

### ✨ Características Principales

- 🔐 **Sistema de autenticación completo** con JWT (JSON Web Tokens)
- ✉️ **Verificación de email** mediante Mailtrap API para activación de cuentas
- 📝 **CRUD completo de recetas** con soporte para imágenes
- 🎨 **Panel de usuario personalizado** para gestionar recetas propias
- 🔍 **Búsqueda avanzada** por categorías y términos
- 📧 **Formulario de contacto** con notificaciones por email
- 📚 **Documentación interactiva** de la API con Swagger/OpenAPI
- 🖼️ **Galería de imágenes** con Fancybox (zoom y navegación)
- 📱 **Diseño responsive** compatible con todos los dispositivos
- 🚀 **Desplegado en producción** (Vercel + Render + Neon)

### 🏗️ Arquitectura

El proyecto sigue una arquitectura **cliente-servidor** desacoplada:

- **Backend (API REST)**: Django 5.2.7 + Django REST Framework 3.16.1 + PostgreSQL 16
- **Frontend (SPA)**: Vue.js 3.5.22 + Vite 7.1.7 + Vue Router + Pinia
- **Autenticación**: JWT con tokens de 24 horas
- **Base de Datos**: PostgreSQL (local con Docker, producción en Neon)
- **Emails**: Mailtrap API para envíos transaccionales
- **Documentación**: Swagger/OpenAPI con drf-yasg

### 🎯 Casos de Uso

- **Usuarios**: Registrarse, crear y compartir recetas personales
- **Búsqueda**: Encontrar recetas por categoría (postres, bebidas, platos principales, etc.)
- **Gestión**: Editar y eliminar recetas propias desde el panel de usuario
- **Contacto**: Enviar mensajes al administrador del sitio
- **Exploración**: Navegar por recetas destacadas y aleatorias

## 🛠️ Stack Tecnológico

### Backend
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/DRF-ff1709?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)
![Cloudinary](https://img.shields.io/badge/Cloudinary-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white)

### Frontend
![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

### DevOps & Herramientas
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![Neon](https://img.shields.io/badge/Neon-00E699?style=for-the-badge&logo=neon&logoColor=white)
![Cloudinary](https://img.shields.io/badge/Cloudinary-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![ESLint](https://img.shields.io/badge/ESLint-4B32C3?style=for-the-badge&logo=eslint&logoColor=white)

## 🌐 Proyecto en Producción

Este proyecto está **desplegado y en funcionamiento** en producción:

- **Frontend**: Desplegado en [Vercel](https://vercel.com) 🚀
- **Backend**: Desplegado en [Render](https://render.com) 🌟
- **Base de Datos**: PostgreSQL en [Neon](https://neon.tech) 🐘
- **Almacenamiento de Imágenes**: [Cloudinary](https://cloudinary.com) 🖼️
- **Emails**: Envío mediante [Mailtrap API](https://mailtrap.io) 📧

## 📋 Requisitos

### Backend
- Python 3.12+
- Git
- pip (gestor de paquetes de Python)
- **Docker Desktop** (para PostgreSQL local, opcional en desarrollo)
- virtualenv o venv (para entorno virtual)
- **Cuenta de Cloudinary** (para almacenamiento de imágenes, gratuita disponible)

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
- `CLOUDINARY_URL`: URL de configuración de Cloudinary (ver siguiente sección)

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
- 📖 Recipes List: `http://localhost:5173/recipes`
- 🔍 Recipe Search: `http://localhost:5173/recipes/search`
- 📖 Recipe Detail: `http://localhost:5173/recipe/:slug` (ej: `/recipe/pastel-de-chocolate`)
- 📧 Contact: `http://localhost:5173/contact`
- 📝 Register: `http://localhost:5173/register`
- 🔐 Login: `http://localhost:5173/login`
- ✉️ Verify Email: `http://localhost:5173/verify-email?token=<uuid>` (desde email)
- 👤 Panel: `http://localhost:5173/panel` (requiere autenticación)

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

### Configuración para Desarrollo

1. Crea una cuenta gratuita en [Mailtrap.io](https://mailtrap.io/)
2. Ve a tu inbox de Mailtrap
3. Copia tu **API Token** desde la sección de configuración
4. Agrega las credenciales a tu archivo `.env`:

```bash
# Mailtrap API Configuration
MAILTRAP_API_TOKEN=tu_token_api_de_mailtrap
DOMAIN=example.com
```

**Nota**: En desarrollo, usa `DOMAIN=example.com` o tu dominio local. En producción, usa tu dominio real.

### Configuración para Producción

Para producción, Mailtrap ofrece una API robusta para envío transaccional de emails:

```bash
# Production Mailtrap Configuration
MAILTRAP_API_TOKEN=tu_token_api_produccion
DOMAIN=tudominio.com
```

### Variables de Entorno Requeridas

- `MAILTRAP_API_TOKEN`: Token de API de Mailtrap (requerido)
- `DOMAIN`: Dominio desde el que se envían los emails (opcional, por defecto: example.com)

### Migración desde SMTP

**Cambios importantes**: El proyecto migró de SMTP tradicional a la API de Mailtrap para mayor confiabilidad y simplicidad.

**Antes (SMTP - deprecado)**:
```python
# Configuración SMTP antigua (ya no se usa)
SMTP_SERVER=sandbox.smtp.mailtrap.io
SMTP_PORT=2525
SMTP_USERNAME=usuario
SMTP_PASSWORD=contraseña
```

**Ahora (Mailtrap API)**:
```python
# Nueva configuración con API
import mailtrap as mt
client = mt.MailtrapClient(token=os.getenv('MAILTRAP_API_TOKEN'))
client.send(mail)
```

**Ventajas de la API**:
- ✅ Más confiable y rápido
- ✅ Mejor entregabilidad de emails
- ✅ Configuración más simple (solo token)
- ✅ Métricas y seguimiento mejorados
- ✅ Sin necesidad de configurar SMTP
- ✅ Soporte nativo para templates HTML

## � Despliegue en Producción

El proyecto está actualmente desplegado en producción usando las siguientes plataformas:

### Frontend - Vercel

**Plataforma**: [Vercel](https://vercel.com)

**Características**:
- ✅ Despliegue automático desde Git
- ✅ CDN global para rendimiento óptimo
- ✅ HTTPS automático
- ✅ Preview deployments para cada PR

**Variables de entorno en Vercel**:
```bash
VITE_API_URL=https://tu-backend.onrender.com/api/v1/
VITE_APP_TITLE=RecetarioWeb - Cookbook
```

**Pasos de despliegue**:
1. Conecta tu repositorio a Vercel
2. Configura el directorio raíz: `frontend`
3. Framework preset: Vite
4. Build command: `npm run build`
5. Output directory: `dist`
6. Agrega las variables de entorno

### Backend - Render

**Plataforma**: [Render](https://render.com)

**Características**:
- ✅ Despliegue automático desde Git
- ✅ SSL/TLS gratuito
- ✅ Health checks automáticos
- ✅ Escalado automático

**Variables de entorno en Render**:
```bash
SECRET_KEY=tu-secret-key-produccion
DEBUG=False
DJANGO_ALLOWED_HOSTS=tu-backend.onrender.com
BASE_URL=https://tu-backend.onrender.com/
BASE_URL_FRONTEND=https://tu-frontend.vercel.app/
JWT_ALGORITHM=HS256
CORS_ORIGIN_WHITELIST=https://tu-frontend.vercel.app
DATABASE_URL=tu-url-de-neon-postgres
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name
MAILTRAP_API_TOKEN=tu-token-api-produccion
DOMAIN=tudominio.com
PYTHON_VERSION=3.12.0
```

**Pasos de despliegue**:
1. Crea un nuevo Web Service en Render
2. Conecta tu repositorio
3. Root directory: `backend`
4. Build command: `pip install -r requirements.txt`
5. Start command: `gunicorn backend.wsgi:application`
6. Agrega todas las variables de entorno
7. Crea un servicio de tipo "Web Service"

**Archivos adicionales requeridos**:
- `requirements.txt`: Ya incluido con todas las dependencias
- Considera agregar `gunicorn` a `requirements.txt` para producción

### Base de Datos - Neon

**Plataforma**: [Neon](https://neon.tech)

**Características**:
- ✅ PostgreSQL serverless
- ✅ Escalado automático
- ✅ Backups automáticos
- ✅ Tier gratuito generoso

**Configuración**:
1. Crea un proyecto en Neon
2. Crea una base de datos
3. Copia la connection string (DATABASE_URL)
4. Agrega la URL a las variables de entorno de Render

**Formato de la URL**:
```bash
postgres://usuario:password@host.region.neon.tech/database?sslmode=require
```

### Almacenamiento de Imágenes - Cloudinary

**Plataforma**: [Cloudinary](https://cloudinary.com)

**Configuración en Producción**:
1. Crea una cuenta en Cloudinary
2. Ve a Dashboard > Settings > API Keys
3. Copia tu Cloudinary URL
4. Agrega la URL a las variables de entorno de Render:
   - `CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name`

**Características**:
- ✅ Almacenamiento persistente en la nube
- ✅ CDN global para entrega rápida
- ✅ Optimización automática de imágenes
- ✅ Transformaciones en tiempo real
- ✅ Backup automático de imágenes
- ✅ Plan gratuito generoso (25 créditos/mes)

### Emails - Mailtrap

**Plataforma**: [Mailtrap](https://mailtrap.io)

**Configuración en Producción**:
1. Crea una cuenta en Mailtrap
2. Configura tu dominio de envío (opcional pero recomendado)
3. Obtén tu API Token desde la sección "API Tokens"
4. Agrega el token a las variables de entorno:
   - `MAILTRAP_API_TOKEN=tu-token-produccion`
   - `DOMAIN=tudominio.com`

**Características**:
- ✅ API confiable para envío transaccional
- ✅ Métricas y analytics de emails
- ✅ Testing de emails en sandbox
- ✅ Sin configuración SMTP compleja

### Checklist de Despliegue

Antes de desplegar a producción, asegúrate de:

**Backend**:
- [ ] `DEBUG=False` en variables de entorno
- [ ] `SECRET_KEY` única y segura generada
- [ ] `ALLOWED_HOSTS` configurado con dominio de Render
- [ ] `CORS_ORIGIN_WHITELIST` con dominio de Vercel
- [ ] `DATABASE_URL` apuntando a Neon
- [ ] `CLOUDINARY_URL` configurado con credenciales de producción
- [ ] `MAILTRAP_API_TOKEN` configurado
- [ ] Ejecutar migraciones: `python manage.py migrate`
- [ ] Recopilar archivos estáticos si es necesario
- [ ] Verificar logs de despliegue en Render

**Frontend**:
- [ ] `VITE_API_URL` apuntando al backend de Render
- [ ] Build exitoso en Vercel
- [ ] **vercel.json** configurado para SPA routing
- [ ] CORS funcionando correctamente
- [ ] Probar autenticación JWT
- [ ] Verificar carga de imágenes desde Cloudinary
- [ ] Probar flujo completo de verificación de email

**Base de Datos**:
- [ ] Migraciones aplicadas
- [ ] Conexión SSL habilitada
- [ ] Backups configurados
- [ ] Datos de prueba cargados (opcional)

**Cloudinary**:
- [ ] CLOUDINARY_URL configurado
- [ ] Probar subida de imágenes
- [ ] Verificar generación de URLs de imágenes
- [ ] Probar eliminación de imágenes
- [ ] Monitorear uso de créditos en dashboard

**Emails**:
- [ ] Token de Mailtrap configurado
- [ ] Dominio verificado (producción)
- [ ] Probar envío de emails de verificación
- [ ] Probar envío de emails de contacto

### Monitoreo y Mantenimiento

**Render**:
- Revisa los logs regularmente
- Configura alertas de salud
- Monitorea uso de recursos

**Vercel**:
- Revisa analytics de visitas
- Monitorea tiempos de carga
- Configura alertas de build fallidos

**Neon**:
- Monitorea uso de almacenamiento
- Revisa conexiones activas
- Configura backups programados

**Cloudinary**:
- Monitorea uso de créditos y almacenamiento
- Revisa analytics de transformaciones
- Verifica rendimiento de CDN

**Mailtrap**:
- Revisa métricas de entrega
- Monitorea bounce rate
- Verifica logs de envío

## �🔒 Seguridad

- ✅ **NO** commitees el archivo `.env` a git
- ✅ Usa SECRET_KEY únicas para cada entorno
- ✅ Establece `DEBUG=False` en producción
- ✅ Configura correctamente `ALLOWED_HOSTS` en producción
- ✅ **Autenticación JWT**: Los endpoints críticos están protegidos con JSON Web Tokens
- ✅ **Verificación de email**: Los usuarios deben verificar su correo antes de acceder
- ✅ **Tokens de corta duración**: Los JWT expiran en 24 horas para mayor seguridad
- ✅ **SSL/TLS**: Todo el tráfico en producción usa HTTPS
- ✅ **Variables de entorno**: Todas las credenciales están en variables de entorno
- ✅ **CORS configurado**: Solo orígenes autorizados pueden acceder a la API

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
│       ├── django-ci.yml        # GitHub Actions CI/CD Backend
│       └── frontend-ci.yml      # GitHub Actions CI/CD Frontend
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
│   │   │   ├── RecipeList.vue   # Listado de recetas con búsqueda
│   │   │   ├── RecipeSearch.vue # Búsqueda avanzada de recetas
│   │   │   ├── RecipeDetail.vue # Detalle completo de receta
│   │   │   ├── ContactPage.vue  # Formulario de contacto
│   │   │   ├── RegisterPage.vue # Registro de usuarios
│   │   │   ├── LoginPage.vue    # Inicio de sesión
│   │   │   ├── VerifyEmail.vue  # Verificación de email (nuevo en v4.2)
│   │   │   ├── PanelPage.vue    # Panel de usuario (requiere auth)
│   │   │   └── ErrorPage404.vue # Página de error 404
│   │   ├── composables/         # Composables de Vue 3
│   │   │   ├── recipeComposable.js       # Lógica para lista y búsqueda de recetas
│   │   │   ├── recipeDetailComposable.js # Lógica para detalle de recetas
│   │   │   ├── useContactComposable.js   # Lógica para envío de mensajes de contacto
│   │   │   └── useSecurityComposable.js  # Lógica para registro, login y verificación
│   │   ├── schemas/             # Esquemas de validación con Yup
│   │   │   └── validationScheme.js # Esquemas: contact, register, login, recipe
│   │   ├── services/            # Servicios de API (deprecated, usar composables)
│   │   │   └── homeServices.js  # Servicios para home
│   │   ├── router/              # Configuración de rutas
│   │   │   └── index.js         # Rutas de Vue Router
│   │   ├── stores/              # Stores de Pinia (gestión de estado)
│   │   │   └── authStore.js    # Store de autenticación con JWT
│   │   ├── App.vue              # Componente raíz de Vue
│   │   └── main.js              # Punto de entrada de la aplicación
│   ├── index.html               # HTML principal
│   ├── vite.config.js           # Configuración de Vite
│   ├── package.json             # Dependencias de Node.js
│   ├── eslint.config.js         # Configuración de ESLint
│   ├── jsconfig.json            # Configuración de JavaScript
│   ├── vercel.json              # Configuración de Vercel (SPA routing)
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
  - `HeaderBase.vue`: Barra de navegación con menú y enlaces (integrado con authStore)
  - `FooterBase.vue`: Pie de página con información del desarrollador
- ✅ **Vistas principales**:
  - `HomePage.vue`: Página principal con recetas destacadas
  - `AboutUs.vue`: Información sobre el proyecto
  - `RecipeList.vue`: Listado completo de recetas con búsqueda y filtrado por categoría
  - `RecipeSearch.vue`: Vista dedicada de búsqueda avanzada de recetas
  - `RecipeDetail.vue`: Detalle completo de cada receta con toda la información
  - `ContactPage.vue`: Formulario de contacto con validación y envío de emails
  - `RegisterPage.vue`: Registro de usuarios con verificación de email
  - `LoginPage.vue`: Inicio de sesión con JWT
  - `PanelPage.vue`: Panel de usuario con CRUD completo de recetas propias
  - `ErrorPage404.vue`: Página de error personalizada
- ✅ **Composables (Composition API)**:
  - `recipeComposable.js`: Manejo de lista de recetas y categorías
  - `useCreateRecipe`: Crear recetas con autenticación JWT
  - `useUpdateRecipe`: Actualizar recetas existentes
  - `useDeleteRecipe`: Eliminar recetas con confirmación
  - `recipeDetailComposable.js`: Obtención de detalle de recetas por slug
  - `useContactComposable.js`: Envío de mensajes de contacto al backend
  - `useSecurityComposable.js`: Lógica de registro y login con axios
  - Integración con `VITE_API_URL` para consumo de API REST
  - Manejo de estados reactivos con Vue 3 Composition API
- ✅ **Gestión de Estado con Pinia**:
  - `authStore.js`: Store de autenticación con JWT
  - Gestión de authId, authName, authToken en localStorage
  - Funciones: login(), logOut(), isLogin(), cerrarSesion()
  - Persistencia de sesión entre recargas de página
- ✅ **Validación de formularios**:
  - Integración de VeeValidate para validación de formularios
  - Soporte para esquemas de validación con Yup
  - Componentes Form, Field y ErrorMessage para formularios reactivos
  - Esquemas: `contactValidationSchema`, `registerValidationSchema`, `loginValidationSchema`, `recipeValidationSchema`, `recipeUpdateValidationSchema`
- ✅ **Sistema de navegación**:
  - Vue Router configurado con rutas dinámicas
  - Navegación por slug para recetas
  - **Guardas de navegación** (router.beforeEach) para proteger rutas
  - Rutas protegidas con meta: { requiresAuth: true }
  - Redirección automática según estado de autenticación
- ✅ **Cliente HTTP**:
  - Axios 1.12.2 para peticiones HTTP
  - Configurado para trabajar con VITE_API_URL
  - Manejo de errores y estados de carga
- ✅ **Assets y recursos**:
  - CSS personalizado y responsive
  - Bootstrap 5 integrado
  - Imágenes y fuentes optimizadas
  - JavaScript para interactividad (menú, carruseles, etc.)
  - Fancybox para galerías de imágenes con zoom y navegación

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
- ✅ GET - Verificación de email mediante token query parameter (`/api/v1/security/verify/?uid=<token>`)
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
- 📡 **Axios 1.12.2** - Cliente HTTP basado en promesas para el navegador y Node.js
- ✅ **VeeValidate 4.15.1** - Validación de formularios para Vue 3
- 📋 **@vee-validate/yup 4.15.1** - Integración de Yup con VeeValidate para esquemas de validación
- 🔍 **Yup 1.7.1** - Schema builder para validación de valores (incluido con @vee-validate/yup)
- 🖼️ **@fancyapps/ui 6.1.0** - Librería moderna para lightbox/galería de imágenes con zoom y navegación
- 🧹 **ESLint 9.33.0** - Linter para JavaScript/Vue
- 🛠️ **Vue DevTools** - Plugin de desarrollo integrado
- 🎯 **Node.js 20.19+** o **22.12+** requerido

### Tecnologías y Dependencias

- **Django 5.2.7** - Framework web
- **Django REST Framework 3.16.1** - API REST
- **drf-yasg 1.21.11** - Generación automática de documentación Swagger/OpenAPI
- **django-cors-headers 4.9.0** - Gestión de CORS (Cross-Origin Resource Sharing)
- **PostgreSQL 16** - Base de datos (Neon en producción)
- **psycopg2-binary 2.9.11** - Adaptador PostgreSQL
- **django-autoslug 1.9.9** - Generación automática de slugs
- **python-dotenv 1.1.1** - Gestión de variables de entorno
- **dj-database-url 3.0.1** - Configuración de base de datos mediante URL
- **python-jose 3.5.0** - Manejo de tokens JWT (JSON Web Tokens)
- **ecdsa 0.19.1** - Algoritmos de firma digital para JWT
- **rsa 4.9.1** - Criptografía RSA para JWT
- **pyasn1 0.6.1** - Soporte ASN.1 para criptografía
- **cloudinary 1.41.0** - SDK de Cloudinary para almacenamiento de imágenes en la nube
- **mailtrap 2.3.0** - Cliente API de Mailtrap para envío de emails transaccionales

### GitHub Actions

El proyecto incluye CI/CD con GitHub Actions para ambos, backend y frontend:

**Backend (Django CI)**:
- ✅ Verifica la configuración de Django con `--deploy`
- ✅ Ejecuta migraciones de la base de datos
- ✅ Ejecuta tests unitarios
- ✅ Se ejecuta en cada push a `main` y en pull requests

**Frontend (Vue.js CI)**:
- ✅ Instala dependencias con npm
- ✅ Ejecuta linter (ESLint) para verificar calidad de código
- ✅ Compila el proyecto con Vite
- ✅ Verifica que la compilación sea exitosa
- ✅ Se ejecuta en Node.js 20.x y 22.x (matrix strategy)
- ✅ Se ejecuta en cada push a `main`, `dev` y en pull requests

[![CI (Django)](https://github.com/BrayanTM/RecetarioWeb/actions/workflows/django-ci.yml/badge.svg)](https://github.com/BrayanTM/RecetarioWeb/actions/workflows/django-ci.yml)
[![CI (Frontend)](https://github.com/BrayanTM/RecetarioWeb/actions/workflows/frontend-ci.yml/badge.svg)](https://github.com/BrayanTM/RecetarioWeb/actions/workflows/frontend-ci.yml)

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
GET /api/v1/security/verify/?uid=<token>

# Este endpoint es llamado cuando el usuario hace clic en el enlace
# del email de verificación. Devuelve una respuesta JSON.

# Respuesta exitosa:
{
  "success": true,
  "message": "Email verified successfully! You can now log in to your account.",
  "user": {
    "id": "123",
    "username": "juanperez",
    "email": "juan@example.com"
  }
}

# Respuesta de error:
{
  "success": false,
  "error": "Invalid or expired verification token. Please request a new verification email."
}

# Nota: El frontend muestra estos mensajes en la vista VerifyEmail.vue
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

### Octubre 2025 - v4.2.1 🔄 CI/CD FRONTEND
- ✅ **GitHub Actions para Frontend**
  - 🔧 **frontend-ci.yml**: Nuevo workflow para CI/CD del frontend
  - 🧪 **Matrix strategy**: Testing en Node.js 20.x y 22.x
  - 📦 **Install dependencies**: Instalación con npm ci
  - 🔍 **ESLint**: Verificación de calidad de código
  - 🏗️ **Build verification**: Compilación con Vite y verificación de dist/
  - ✅ **Triggers**: Se ejecuta en push a `main`, `dev` y en pull requests
- ✅ **Documentación actualizada**
  - 📊 **Badges**: Agregados badges de CI para backend y frontend
  - 📝 **README**: Sección de GitHub Actions ampliada con detalles de ambos workflows
  - 🗂️ **Estructura**: Actualizada la estructura del proyecto con frontend-ci.yml

### Octubre 2025 - v4.2 ✉️ VERIFICACIÓN DE EMAIL
- ✅ **Sistema de Verificación de Email Mejorado**
  - 📧 **VerifyEmail.vue**: Nueva vista dedicada para verificación de email
  - 🔄 **Endpoint actualizado**: Cambio de path parameter a query parameter (`?token=uid`)
  - 📝 **Respuesta JSON estructurada**: El endpoint ahora devuelve JSON con `success`, `message` y `user`
  - 🎯 **URL amigable al frontend**: `/verify-email?token={uuid}` en lugar de `/api/v1/security/verify/{uuid}/`
  - ✨ **UX mejorada**: Mensajes claros de éxito/error con estados de carga
  - 🔗 **Integración completa**: Composable `useVerifyEmailComposable` consume el nuevo formato
- ✅ **Mejoras en Breadcrumbs**
  - 🖼️ **Rutas absolutas**: Corrección de rutas de imágenes de fondo en breadcrumbs
  - 📝 Afectó: RegisterPage, LoginPage, PanelPage, VerifyEmail, RecipeSearch, RecipeList, HomePage
  - 🎨 Cambio de `url(img/bg-img/...)` a `url(/img/bg-img/...)` para correcta visualización
  - ✅ Breadcrumbs ahora cargan correctamente en todas las páginas
- ✅ **Configuración de Vercel**
  - 📄 **vercel.json**: Archivo de configuración para despliegue en Vercel
  - 🔄 Rewrite rules para SPA: Todas las rutas redirigen a `index.html`
  - 🌐 Soporte completo para Vue Router en producción
- ✅ **Mejoras en Seguridad**
  - 🔒 **Query parameters**: Tokens de verificación ahora en query string (más estándar)
  - 📊 **Respuestas estructuradas**: Formato consistente con campo `success` para validación rápida
  - ⚠️ **Mensajes descriptivos**: Errores más informativos para mejor debugging

### Octubre 2025 - v4.1 🖼️ CLOUDINARY
- ✅ **Migración a Cloudinary para Almacenamiento de Imágenes**
  - 🖼️ **Cloudinary 1.41.0**: Nueva dependencia para almacenamiento en la nube
  - 🔄 **Migración completa**: De `FileSystemStorage` local a Cloudinary
  - 🗑️ Eliminado uso de `django.core.files.storage.FileSystemStorage`
  - 📝 **settings.py actualizado**: Configuración de Cloudinary con `CLOUDINARY_URL`
  - 🔧 **recipes/views.py refactorizado**: 
    - POST: `cloudinary.uploader.upload()` para subir imágenes
    - PUT: Actualización de imágenes con eliminación de la anterior
    - DELETE: `cloudinary.uploader.destroy()` para eliminar imágenes
  - 🔗 **recipes/serializers.py actualizado**: Generación de URLs con `cloudinary.utils.cloudinary_url()`
  - 📚 **Documentación completa**: [CLOUDINARY_MIGRATION.md](backend/docs/CLOUDINARY_MIGRATION.md)
- ✅ **Beneficios de la Migración**
  - 💾 **Persistencia**: Las imágenes no se pierden en Render (almacenamiento efímero resuelto)
  - 🌍 **CDN Global**: Entrega rápida desde servidores cercanos al usuario
  - ⚡ **Optimización**: Compresión y transformaciones automáticas
  - 🔄 **Escalabilidad**: Sin límites de almacenamiento según plan
  - 🔒 **Backup**: Cloudinary mantiene backups automáticos
- ✅ **Configuración Actualizada**
  - 🆕 Nueva variable de entorno: `CLOUDINARY_URL`
  - 📝 `.env.example` actualizado con instrucciones de Cloudinary
  - 📖 README ampliado con sección completa de Cloudinary
  - ✅ Checklist de despliegue actualizado
- ✅ **Estructura de Almacenamiento**
  - 📁 Carpeta en Cloudinary: `recipes/`
  - 🏷️ Public IDs: `recipes/{timestamp}`
  - 🔗 URLs generadas dinámicamente por Cloudinary

### Octubre 2025 - v4.0 🚀 PRODUCCIÓN
- ✅ **Despliegue en Producción Completo**
  - 🌐 **Frontend desplegado en Vercel**: Despliegue automático desde Git con CDN global
  - 🖥️ **Backend desplegado en Render**: Web service con SSL/TLS y health checks
  - 🐘 **Base de datos en Neon**: PostgreSQL serverless con backups automáticos
  - 📧 **Emails con Mailtrap API**: Migración de SMTP a API para mayor confiabilidad
- ✅ **Migración de SMTP a Mailtrap API**
  - 📦 **mailtrap 2.3.0**: Nueva dependencia para envío de emails
  - 🔄 **utilities.py actualizado**: Implementación completa con Mailtrap API
  - 🗑️ Eliminadas variables SMTP deprecadas (SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD)
  - 🆕 Nuevas variables: `MAILTRAP_API_TOKEN` y `DOMAIN`
  - ✨ Ventajas: Mayor confiabilidad, configuración simplificada, métricas mejoradas
- ✅ **Configuración de Producción**
  - 📝 **.env.example actualizado**: Variables para despliegue en Vercel, Render y Neon
  - 📚 **README actualizado**: Guía completa de despliegue con checklist
  - 🔒 Configuración de seguridad mejorada (CORS, ALLOWED_HOSTS, SSL/TLS)
  - 🌍 Variables de entorno específicas para producción documentadas
- ✅ **Documentación de Despliegue**
  - 📖 Sección completa sobre despliegue en producción
  - ✅ Checklist de verificación pre-despliegue
  - 🛠️ Guías paso a paso para Vercel, Render, Neon y Mailtrap
  - 📊 Sección de monitoreo y mantenimiento

### Octubre 2025 - v3.5
- ✅ **Panel de Usuario Completo (CRUD de Recetas)**
  - 📋 **PanelPage.vue**: Panel completamente funcional para gestionar recetas del usuario
  - ✏️ Crear, editar y eliminar recetas propias
  - 📊 Tabla con todas las recetas del usuario
  - 🖼️ Galería de imágenes con Fancybox para vista previa
  - 🔒 Integración completa con JWT para operaciones protegidas
- ✅ **Nuevos Composables de Recetas**
  - 🆕 **useCreateRecipe**: Crear recetas con autenticación JWT
  - ✏️ **useUpdateRecipe**: Actualizar recetas existentes
  - 🗑️ **useDeleteRecipe**: Eliminar recetas con confirmación
  - 📡 Todos con manejo de errores y mensajes de éxito
  - 🔄 Sistema de mensajes (clearMessages) para limpiar estados
- ✅ **Validación de Formularios de Recetas**
  - 📝 **recipeValidationSchema**: Validación completa para crear recetas
    - Name (3-200 caracteres)
    - Category (selección válida requerida)
    - Time (requerido)
    - Description (mínimo 10 caracteres)
  - ✏️ **recipeUpdateValidationSchema**: Validación para actualizar
    - Picture es opcional en edición (mantiene imagen actual)
- ✅ **Fancybox Integration**
  - 📦 **@fancyapps/ui 6.1.0**: Librería para galería de imágenes
  - 🖼️ Vista previa elegante de imágenes de recetas
  - 🔍 Zoom y navegación entre imágenes
  - 📱 Responsive y touch-friendly
- ✅ **Mejoras en la Experiencia de Usuario**
  - ⏳ Indicadores de carga durante operaciones
  - ✅ Mensajes de éxito/error con cierre manual
  - 🔄 Recarga automática de datos después de CRUD
  - 🎨 Modal personalizado para crear/editar recetas
  - 🖼️ Vista previa de imagen actual al editar
  - ⚠️ Confirmación antes de eliminar recetas

### Octubre 2025 - v3.4
- ✅ **Sistema de Autenticación Completo Frontend**
  - 🔐 **LoginPage.vue**: Página de inicio de sesión con validación
  - 📝 **RegisterPage.vue**: Página de registro de usuarios con verificación de email
  - ✉️ **VerifyEmail.vue**: Vista de verificación de email (añadida en v4.2)
  - 👤 **PanelPage.vue**: Panel de usuario (base para futuras funcionalidades)
  - 🏪 **authStore.js**: Store de Pinia para gestión de estado de autenticación
  - 🔑 Gestión de tokens JWT en localStorage
  - 🚪 Funciones login(), logOut(), isLogin(), cerrarSesion()
- ✅ **Composables de Seguridad**
  - 🔐 **useLoginComposable.js**: Lógica de autenticación de usuarios
  - 📝 **useRegisterComposable.js**: Lógica de registro de usuarios
  - 📡 Integración con endpoints `/api/v1/security/login/` y `/api/v1/security/register/`
  - ⚡ Manejo de estados de carga y errores
  - 🔄 Redirección automática después de login exitoso
- ✅ **Axios 1.12.2 integrado**
  - 📡 Cliente HTTP para comunicación con API REST
  - 🌐 Reemplaza fetch nativo para mejor manejo de peticiones
  - 🔧 Configurado para trabajar con VITE_API_URL
- ✅ **Validación de Autenticación**
  - 📋 **loginValidationSchema**: Validación de email y contraseña
  - 📋 **registerValidationSchema**: Validación completa de registro
    - Username (3-150 caracteres, solo letras, números y @/./+/-/_)
    - First Name y Last Name (2-150 caracteres)
    - Email (formato válido, máx. 254 caracteres)
    - Password (6-128 caracteres)
    - Password confirmation (debe coincidir)
- ✅ **Protección de Rutas con Vue Router**
  - 🛡️ **router.beforeEach**: Guard de navegación para proteger rutas
  - 🔒 Rutas protegidas: `/panel` (requiere autenticación)
  - 🚫 Rutas públicas: `/login`, `/register` (solo para usuarios no autenticados)
  - 🔄 Redirección automática según estado de autenticación
- ✅ **Mejoras en HeaderBase**
  - 🔗 Enlaces de Login, Register y Panel integrados
  - 👤 Saludo personalizado: "Hi [nombre]" cuando está autenticado
  - 🚪 Botón de logout con confirmación
  - 🎯 Navegación condicional según authToken

### Octubre 2025 - v3.3
- ✅ **Página de Contacto completa implementada**
  - 📧 **ContactPage.vue**: Formulario de contacto completamente funcional
  - ✅ **useContactComposable.js**: Composable para envío de mensajes de contacto
  - 📋 **validationScheme.js**: Esquemas de validación con Yup para formularios
  - 🎨 Integración completa con VeeValidate (Form, Field, ErrorMessage)
  - 🔄 Estados de carga con preloader visual durante envío
  - ✉️ Envío automático de emails mediante API del backend
  - 🌐 Conectado a endpoint `/api/v1/contact/` con `VITE_API_URL`
- ✅ **Mejoras en navegación y recursos**
  - 🗺️ Ruta `/contact` agregada al router con lazy loading
  - 🔗 Enlace de contacto actualizado en `HeaderBase.vue`
  - 🎨 Imágenes actualizadas: favicon y logo optimizados
  - 📬 Email de contacto genérico para ejemplo: `yourmail@gmail.com`
- ✅ **Validación de formularios robusta**
  - ✅ Validación de contacto (nombre, email, teléfono, mensaje)
  - ✅ Validación de registro (username, nombres, email, contraseñas)
  - ✅ Validación de login (email, contraseña)
  - ✅ Validación de recetas (nombre, categoría, tiempo, descripción)
  - ✅ Validación de actualización de recetas (imagen opcional)
  - 🔴 Mensajes de error contextuales con `ErrorMessage`

### Octubre 2025 - v3.2
- ✅ **Mejoras en el Frontend Vue.js 3**
  - 📋 **VeeValidate 4.15.1** integrado para validación de formularios
  - 🔧 **@vee-validate/yup 4.15.1** para esquemas de validación declarativos
  - 📝 Componentes `Form` y `Field` de VeeValidate en uso
  - 🎨 Formularios reactivos con validación en tiempo real
- ✅ **Nuevas vistas completadas**
  - 📖 **RecipeList.vue**: Listado completo de recetas con búsqueda por categoría
  - 🔍 **RecipeSearch.vue**: Vista dedicada de búsqueda avanzada de recetas
  - 📄 **RecipeDetail.vue**: Vista completa de detalle de receta con toda la información
- ✅ **Composables Vue 3 implementados**
  - 🔄 **recipeComposable.js**: Lógica reutilizable para listar recetas y categorías
  - 🆕 **useCreateRecipe**: Composable para crear recetas con JWT
  - ✏️ **useUpdateRecipe**: Composable para actualizar recetas existentes
  - 🗑️ **useDeleteRecipe**: Composable para eliminar recetas
  - 📊 **recipeDetailComposable.js**: Manejo de datos de recetas individuales por slug
  - 🔐 **useLoginComposable.js**: Lógica de autenticación de usuarios
  - 📝 **useRegisterComposable.js**: Lógica de registro de usuarios
  - 📧 **useContactComposable.js**: Envío de mensajes de contacto
  - ⚡ Uso de Composition API con `ref`, `readonly`, `watchEffect`
  - 🌐 Integración con endpoints del backend mediante `VITE_API_URL`
- ✅ **Mejoras en rutas y navegación**
  - 🔀 Rutas actualizadas en `HeaderBase.vue`: `/recipes`, `/contact`
  - 🗺️ Nuevas rutas en router: `/recipes`, `/recipes/search`
  - 🔗 Enlaces dinámicos a recetas por slug funcionando correctamente
- ✅ **Experiencia de usuario mejorada**
  - 🎯 Búsqueda por categoría y término de búsqueda
  - 📱 Diseño responsive mantenido en todas las vistas
  - ⚠️ Manejo de errores con redirección automática
  - 🖼️ Visualización de imágenes de recetas optimizada

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
  - 🖼️ Fancybox para galerías de imágenes interactivas
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
- ✅ Sistema de autenticación JWT con verificación de email (backend + frontend)
- ✅ **Sistema completo de Login y Registro en frontend**
  - ✅ Formularios con validación robusta (VeeValidate + Yup)
  - ✅ Integración con authStore (Pinia) para gestión de sesión
  - ✅ Composables useLoginComposable y useRegisterComposable
  - ✅ Guardas de navegación para proteger rutas
  - ✅ Persistencia de sesión con localStorage
- ✅ CRUD completo de recetas y categorías
- ✅ Sistema de contacto con notificaciones por email
- ✅ **Página de contacto completamente funcional en frontend**
- ✅ **Axios 1.12.2** integrado como cliente HTTP
- ✅ Documentación Swagger/OpenAPI interactiva
- ✅ PostgreSQL 18 con Docker Compose
- ✅ CORS configurado para desarrollo y producción
- ✅ 20 recetas de ejemplo con imágenes
- ✅ Vista de listado de recetas con filtros
- ✅ Vista de búsqueda avanzada de recetas por categoría
- ✅ Vista de detalle de receta completa
  - ✅ Composables para manejo de datos reactivos (recipes, contact, security)
  - ✅ Integración de VeeValidate para validación de formularios
  - ✅ Esquemas de validación con Yup implementados (contact, login, register, recipe)
  - ✅ Panel de usuario completo con CRUD de recetas (crear, editar, eliminar)
  - ✅ Fancybox integrado para galería de imágenes interactiva### En Desarrollo
- 🚧 Mejoras en la UI/UX del panel de usuario
- 🚧 Notificaciones toast/snackbar más sofisticadas
- 🚧 Paginación para lista de recetas
- 🚧 Filtros adicionales de búsqueda

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

**Nota:** Recuerda actualizar tu archivo `.env` con valores reales antes de ejecutar la aplicación.

**🚀 Estado del proyecto**: En producción activa
- Frontend: Desplegado en Vercel
- Backend: Desplegado en Render
- Base de datos: PostgreSQL en Neon
- Almacenamiento de Imágenes: Cloudinary
- Emails: Mailtrap API

**Última actualización:** Octubre 2025 - v4.2 (Sistema de Verificación de Email Mejorado)
