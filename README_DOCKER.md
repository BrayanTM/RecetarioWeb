# 🐳 Configuración de Docker

Este proyecto utiliza Docker Compose para gestionar la base de datos PostgreSQL.

## 📋 Requisitos previos

- Docker Desktop instalado
- Docker Compose (incluido con Docker Desktop)

## 🚀 Configuración inicial

### 1. Configurar variables de entorno

Copia el archivo de ejemplo y configura tus credenciales:

```bash
# PowerShell
Copy-Item .env.example .env
```

Luego edita el archivo `.env` con tus valores:

```env
# PostgreSQL Docker Configuration
POSTGRES_DB=development
POSTGRES_USER=tu_usuario
POSTGRES_PASSWORD=tu_contraseña_segura
POSTGRES_PORT=5433
```

### 2. Iniciar los servicios

```bash
# Iniciar PostgreSQL en segundo plano
docker-compose up -d

# Ver los logs
docker-compose logs -f

# Detener los servicios
docker-compose down

# Detener y eliminar volúmenes (¡cuidado, esto borra los datos!)
docker-compose down -v
```

## 🔧 Comandos útiles

```bash
# Ver estado de los contenedores
docker-compose ps

# Acceder a la consola de PostgreSQL
docker-compose exec db psql -U brayan -d development

# Reiniciar los servicios
docker-compose restart

# Ver logs en tiempo real
docker-compose logs -f db
```

## 🔒 Seguridad

- ✅ El archivo `.env` está en `.gitignore` y **NO** se sube a Git
- ✅ El archivo `docker-compose.yml` usa variables de entorno seguras
- ✅ El archivo `.env.example` es la plantilla pública (sin credenciales reales)

## 📝 Notas importantes

1. **NUNCA** subas el archivo `.env` a Git
2. Cambia las contraseñas por defecto en producción
3. El volumen `pgdata` persiste los datos incluso si detienes el contenedor
4. El puerto por defecto es `5433` para evitar conflictos con PostgreSQL local

## 🐛 Solución de problemas

### Puerto ya en uso
```bash
# Cambiar POSTGRES_PORT en .env a otro puerto disponible
POSTGRES_PORT=5434
```

### Resetear la base de datos
```bash
# Advertencia: Esto borrará todos los datos
docker-compose down -v
docker-compose up -d
```

### Ver errores del contenedor
```bash
docker-compose logs db
```
