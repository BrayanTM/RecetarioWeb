# Migración de Almacenamiento Local a Cloudinary

## Resumen de Cambios

Se ha migrado el sistema de almacenamiento de imágenes de recetas desde el almacenamiento local (FileSystemStorage) a Cloudinary para resolver el problema de almacenamiento efímero en Render.

## Cambios Realizados

### 1. Dependencias (`requirements.txt`)
- ✅ Agregado: `cloudinary==1.41.0`

### 2. Configuración (`backend/settings.py`)
- ✅ Importación de librerías de Cloudinary
- ✅ Configuración de Cloudinary usando `CLOUDINARY_URL` del archivo `.env`

```python
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Cloudinary Configuration
cloudinary.config(
    cloudinary_url=os.getenv('CLOUDINARY_URL')
)
```

### 3. Vistas (`recipes/views.py`)

#### Método POST (Crear Receta)
- ❌ Eliminado: `FileSystemStorage` para guardar archivos localmente
- ✅ Agregado: `cloudinary.uploader.upload()` para subir imágenes a Cloudinary
- ✅ Se guarda el `public_id` de Cloudinary en el campo `picture` del modelo
- ✅ Manejo de errores mejorado con try-except

#### Método PUT (Actualizar Receta)
- ❌ Eliminado: Eliminación de archivos locales con `os.remove()`
- ✅ Agregado: `cloudinary.uploader.upload()` para subir nuevas imágenes
- ✅ Agregado: `cloudinary.uploader.destroy()` para eliminar imágenes antiguas
- ✅ Manejo de errores mejorado

#### Método DELETE (Eliminar Receta)
- ❌ Eliminado: Eliminación de archivos locales con `os.remove()`
- ✅ Agregado: `cloudinary.uploader.destroy()` para eliminar imágenes de Cloudinary

### 4. Serializador (`recipes/serializers.py`)
- ❌ Eliminado: Generación de URL local concatenando `BASE_URL` + ruta del archivo
- ✅ Agregado: Generación de URL usando `cloudinary.utils.cloudinary_url()`
- ✅ Las URLs ahora apuntan directamente a Cloudinary

```python
def get_picture_url(self, obj):
    if obj.picture:
        # Generar URL segura desde Cloudinary
        return cloudinary.utils.cloudinary_url(obj.picture)[0]
    return None
```

## Estructura de Almacenamiento en Cloudinary

Las imágenes se almacenan con la siguiente estructura:
- **Carpeta**: `recipes/`
- **Nombre de archivo**: `{timestamp}` (sin extensión, Cloudinary lo maneja automáticamente)
- **Public ID completo**: `recipes/{timestamp}`

Ejemplo: `recipes/1729872345`

## Variables de Entorno Requeridas

Asegúrate de tener configurada la variable `CLOUDINARY_URL` en tu archivo `.env`:

```bash
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name
```

## Ventajas de Cloudinary

1. ✅ **Persistencia**: Las imágenes no se pierden al reiniciar el servidor en Render
2. ✅ **CDN Global**: Entrega rápida de imágenes desde servidores cercanos al usuario
3. ✅ **Optimización**: Cloudinary optimiza automáticamente las imágenes
4. ✅ **Transformaciones**: Posibilidad de redimensionar, recortar, aplicar efectos en tiempo real
5. ✅ **Escalabilidad**: No hay límites de almacenamiento (según tu plan)
6. ✅ **Backup**: Cloudinary mantiene backups de tus imágenes

## Migración de Datos Existentes (Opcional)

Si tienes recetas con imágenes en almacenamiento local, necesitarás migrarlas manualmente:

1. Subir cada imagen a Cloudinary
2. Actualizar el campo `picture` en la base de datos con el nuevo `public_id`
3. Eliminar las imágenes locales (opcional)

Script de ejemplo para migración (crear en `recipes/management/commands/migrate_to_cloudinary.py`):

```python
from django.core.management.base import BaseCommand
from recipes.models import Recipe
import cloudinary.uploader
import os

class Command(BaseCommand):
    help = 'Migrate recipe images from local storage to Cloudinary'

    def handle(self, *args, **options):
        recipes = Recipe.objects.exclude(picture__isnull=True).exclude(picture='')
        
        for recipe in recipes:
            if recipe.picture and not recipe.picture.startswith('recipes/'):
                # La imagen está en almacenamiento local
                local_path = f"uploads/recipes/{recipe.picture}"
                
                if os.path.exists(local_path):
                    try:
                        # Subir a Cloudinary
                        result = cloudinary.uploader.upload(
                            local_path,
                            folder="recipes",
                            resource_type="image"
                        )
                        
                        # Actualizar el registro
                        recipe.picture = result['public_id']
                        recipe.save()
                        
                        self.stdout.write(
                            self.style.SUCCESS(f'Migrated: {recipe.name}')
                        )
                    except Exception as e:
                        self.stdout.write(
                            self.style.ERROR(f'Error migrating {recipe.name}: {str(e)}')
                        )
```

## Testing

Para probar la integración:

1. **Crear una receta nueva**: Verificar que la imagen se suba correctamente
2. **Actualizar una receta**: Verificar que la imagen antigua se elimine y la nueva se suba
3. **Eliminar una receta**: Verificar que la imagen se elimine de Cloudinary
4. **Obtener recetas**: Verificar que las URLs de Cloudinary se generen correctamente

## Notas Importantes

- ⚠️ El campo `picture` ahora almacena el `public_id` de Cloudinary, no el nombre del archivo
- ⚠️ Las URLs son generadas dinámicamente por Cloudinary
- ⚠️ Asegúrate de tener configurado correctamente `CLOUDINARY_URL` en producción
- ⚠️ Cloudinary tiene límites según el plan (gratuito: 25 créditos/mes, ~25GB almacenamiento)

## Rollback (Volver al Sistema Anterior)

Si necesitas volver al almacenamiento local:

1. Revertir los cambios en `views.py`, `serializers.py` y `settings.py`
2. Restaurar `FileSystemStorage` en las vistas
3. Actualizar las URLs en el serializador
4. Desinstalar `cloudinary` de `requirements.txt`
