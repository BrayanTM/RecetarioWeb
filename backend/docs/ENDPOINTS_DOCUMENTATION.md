# Documentación de Endpoints - RecetarioWeb API

Este documento resume todos los endpoints disponibles en la API de RecetarioWeb con su documentación Swagger.

## Acceso a la Documentación Interactiva

Una vez que el servidor esté corriendo, puedes acceder a la documentación interactiva en:

- **Swagger UI**: `http://localhost:8000/docs/`
- **ReDoc**: `http://localhost:8000/redoc/`
- **Schema JSON**: `http://localhost:8000/docs.json/`

## Resumen de Endpoints

### 🔐 Security (Autenticación y Registro)

#### 1. **POST** `/api/v1/security/register/`
- **Descripción**: Registrar un nuevo usuario
- **Body**: `username`, `password`, `email`, `first_name`, `last_name`
- **Respuesta**: Envía un correo de verificación
- **Estado**: 201 Created / 400 Bad Request

#### 2. **GET** `/api/v1/security/verify/{token}/`
- **Descripción**: Verificar el correo electrónico del usuario
- **Parámetros**: `token` (URL)
- **Respuesta**: Redirige al frontend
- **Estado**: 302 Redirect / 400 Bad Request

#### 3. **POST** `/api/v1/security/login/`
- **Descripción**: Iniciar sesión
- **Body**: `email`, `password`
- **Respuesta**: Retorna `user_id`, `name`, `token` (JWT)
- **Estado**: 200 OK / 401 Unauthorized

---

### 🍳 Recipes (Gestión de Recetas - Admin)

#### 4. **GET** `/api/v1/recipes/`
- **Descripción**: Obtener todas las recetas (orden descendente por ID)
- **Respuesta**: Lista de recetas
- **Estado**: 200 OK

#### 5. **POST** `/api/v1/recipes/`
- **Descripción**: Crear una nueva receta con imagen
- **Headers**: `Authorization: Bearer <token>` (requerido)
- **Form Data**: `file`, `name`, `time`, `description`, `category`
- **Respuesta**: Datos de la receta creada
- **Estado**: 201 Created / 400 Bad Request / 401 Unauthorized

#### 6. **GET** `/api/v1/recipes/{id}/`
- **Descripción**: Obtener una receta específica por ID
- **Parámetros**: `id` (URL)
- **Respuesta**: Detalles de la receta
- **Estado**: 200 OK / 404 Not Found

#### 7. **PUT** `/api/v1/recipes/{id}/`
- **Descripción**: Actualizar una receta (parcial o completa)
- **Headers**: `Authorization: Bearer <token>` (requerido)
- **Parámetros**: `id` (URL)
- **Form Data**: `file` (opcional), `name`, `time`, `description`, `category`
- **Respuesta**: Datos actualizados de la receta
- **Estado**: 200 OK / 400 Bad Request / 404 Not Found

#### 8. **DELETE** `/api/v1/recipes/{id}/`
- **Descripción**: Eliminar una receta y su imagen asociada
- **Headers**: `Authorization: Bearer <token>` (requerido)
- **Parámetros**: `id` (URL)
- **Respuesta**: Mensaje de confirmación
- **Estado**: 200 OK / 404 Not Found

---

### 📁 Categories (Gestión de Categorías)

#### 9. **GET** `/api/v1/categories/`
- **Descripción**: Obtener todas las categorías
- **Respuesta**: Lista de categorías
- **Estado**: 200 OK

#### 10. **POST** `/api/v1/categories/`
- **Descripción**: Crear una nueva categoría
- **Body**: `name`
- **Respuesta**: Datos de la categoría creada
- **Estado**: 201 Created / 400 Bad Request

#### 11. **GET** `/api/v1/categories/{id}/`
- **Descripción**: Obtener una categoría específica
- **Parámetros**: `id` (URL)
- **Respuesta**: Detalles de la categoría
- **Estado**: 200 OK / 404 Not Found

#### 12. **PUT** `/api/v1/categories/{id}/`
- **Descripción**: Actualizar una categoría
- **Parámetros**: `id` (URL)
- **Body**: `name`
- **Respuesta**: Datos actualizados de la categoría
- **Estado**: 200 OK / 400 Bad Request / 404 Not Found

#### 13. **DELETE** `/api/v1/categories/{id}/`
- **Descripción**: Eliminar una categoría (no permitido si tiene recetas asociadas)
- **Parámetros**: `id` (URL)
- **Respuesta**: Mensaje de confirmación
- **Estado**: 200 OK / 400 Bad Request / 404 Not Found

---

### 🍽️ Recipe Helper (Endpoints Públicos de Recetas)

#### 14. **GET** `/api/v1/recipe-helper/user/{pk}/`
- **Descripción**: Obtener todas las recetas de un usuario específico
- **Headers**: `Authorization: Bearer <token>` (requerido)
- **Parámetros**: `pk` (user ID en URL)
- **Respuesta**: Lista de recetas del usuario
- **Estado**: 200 OK / 404 Not Found

#### 15. **GET** `/api/v1/recipe-helper/recipe/{slug}/`
- **Descripción**: Obtener detalles de una receta por slug
- **Parámetros**: `slug` (URL)
- **Respuesta**: Detalles de la receta
- **Estado**: 200 OK / 404 Not Found

#### 16. **GET** `/api/v1/recipe-helper/recipes/`
- **Descripción**: Obtener 3 recetas aleatorias
- **Respuesta**: Lista de 3 recetas aleatorias
- **Estado**: 200 OK

#### 17. **GET** `/api/v1/recipe-helper/search/`
- **Descripción**: Buscar recetas por categoría y nombre
- **Query Params**: `category_id` (requerido), `search` (opcional)
- **Respuesta**: Lista de recetas filtradas
- **Estado**: 200 OK / 400 Bad Request / 404 Not Found

---

### 📧 Contact (Formulario de Contacto)

#### 18. **POST** `/api/v1/contact/`
- **Descripción**: Enviar un mensaje de contacto
- **Body**: `name`, `email`, `phone`, `message`
- **Respuesta**: Datos del mensaje enviado (también envía email)
- **Estado**: 201 Created / 400 Bad Request

---

### 🧪 Example (Endpoints de Ejemplo)

#### 19. **GET** `/api/v1/example/`
- **Descripción**: Endpoint de ejemplo con query params
- **Query Params**: `id` (opcional), `slug` (opcional)
- **Respuesta**: Mensaje de ejemplo
- **Estado**: 200 OK

#### 20. **POST** `/api/v1/example/`
- **Descripción**: Endpoint de ejemplo POST
- **Body**: `email`, `password`
- **Respuesta**: Mensaje de confirmación
- **Estado**: 201 Created / 404 Not Found

#### 21. **GET** `/api/v1/example/{id}/`
- **Descripción**: Endpoint de ejemplo con parámetro en URL
- **Parámetros**: `id` (URL)
- **Respuesta**: Mensaje con ID
- **Estado**: 200 OK

#### 22. **PUT** `/api/v1/example/{id}/`
- **Descripción**: Endpoint de ejemplo PUT
- **Parámetros**: `id` (URL)
- **Respuesta**: Mensaje de confirmación
- **Estado**: 200 OK

#### 23. **DELETE** `/api/v1/example/{id}/`
- **Descripción**: Endpoint de ejemplo DELETE
- **Parámetros**: `id` (URL)
- **Respuesta**: Mensaje de confirmación
- **Estado**: 200 OK

#### 24. **POST** `/api/v1/example/upload/`
- **Descripción**: Endpoint de ejemplo para subir archivos
- **Form Data**: `file`
- **Respuesta**: Mensaje de confirmación
- **Estado**: 201 Created

---

## Notas Importantes

### Autenticación
Los endpoints que requieren autenticación necesitan un token JWT en el header:
```
Authorization: Bearer <your_jwt_token>
```

### Subida de Archivos
Para los endpoints que aceptan archivos:
- Content-Type: `multipart/form-data`
- Solo se aceptan imágenes JPEG y PNG
- Los archivos deben tener contenido válido

### Validaciones
- Los campos requeridos están marcados en cada endpoint
- Las categorías no se pueden eliminar si tienen recetas asociadas
- Las recetas solo pueden ser creadas/modificadas por usuarios autenticados

### Variables de Entorno Requeridas
Asegúrate de tener configuradas las siguientes variables en tu archivo `.env`:
- `SECRET_KEY`: Clave secreta de Django
- `JWT_ALGORITHM`: Algoritmo para JWT (ej: HS256)
- `BASE_URL`: URL base del backend
- `BASE_URL_FRONTEND`: URL del frontend para redirecciones

## Estructura de Respuesta

Todas las respuestas siguen un formato JSON consistente:
- **Éxito**: `{ "data_key": data }`
- **Error**: `{ "error": "mensaje de error" }` o `{ "errors": {...} }`

## Códigos de Estado HTTP

- **200 OK**: Operación exitosa
- **201 Created**: Recurso creado exitosamente
- **400 Bad Request**: Datos inválidos o faltantes
- **401 Unauthorized**: Token inválido o faltante
- **404 Not Found**: Recurso no encontrado
- **500 Internal Server Error**: Error del servidor

---

## Cómo Probar los Endpoints

1. Inicia el servidor Django:
   ```bash
   cd backend
   python manage.py runserver
   ```

2. Accede a la documentación Swagger en tu navegador:
   ```
   http://localhost:8000/docs/
   ```

3. Usa la interfaz interactiva para probar los endpoints directamente desde el navegador.

---

**Última actualización**: 18 de octubre de 2025
