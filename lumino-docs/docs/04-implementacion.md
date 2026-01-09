# Implementación

## Estructura del Código

- El proyecto esta organizado por apps, cada una con sus respectivos archivos de modelos, vistas y rutas
- Las convenciones empleadas fueron 'snake_case' para las variables y funciones, y 'camel_case' para las clases. Se han hecho uso de conversores para las rutas y de 'URL canónica', también se han usado migraciones par el proyecto

## Tecnologías y Herramientas

- Se ha usado DJango con Python usando atajos de comando con Justfile, bootstrap, Sort Thumbnail y SQLite

## Instrucciones de Configuración

- Para empezar hay que instalar Python, para luego poder crear un entorno virtual con UV

??? info "UV"

    UV es una version mejorada de PIP solo que este maneja las dependencias necesiarias para que funcionen entre sí

- Cuando tengamos el entorno virtual procedemos a instalar las dependencias necesarias con UV

```bash title="Django"
uv add django
```

```bash title="Bootstrap"
uv add crispy-bootstrap5
```

```bash title="Sorl-Thumbnail"
uv add sorl-thumbnail
```

```bash title="Django-rq"
uv add django-rq
```

```bash title="Django-Markdownify"
uv add django-markdownify
```

??? info "Otras formas"

    También se puede utilizar Pip para instalar las dependencias

- Al cargar los datos en la base de datos hay que realizar las migraciones necesarias

```bash title="Migraciones"
uv run manage.py migrate
```
