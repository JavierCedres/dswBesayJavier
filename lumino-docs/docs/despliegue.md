# Despliegue

## Entorno de Producción

- Se haria un servidor en local en Nginx, en el que habría que implementar DJango redireccionando al servidor

## Proceso de Despliegue

- Instalar Nginx, en la configuracion de este redireccionar a la ruta del entorno virtual y por último hacer que el servidor escuche en todos los puertos

## Planes de Recuperación

- Para manejar errores se tendrían las migraciones guardadas en caso de tener que revertir cualquier dato

- También se usaría un script en bash para prevenir errores

## Sostenibilidad

- El sistema se despliega en un entorno virtualizado, permitiendo un uso eficiente y reduciendo el consumo energético.

- El uso de Django favorece la
  sostenibilidad gracias a su estabilidad y facilidad de mantenimiento a largo plazo.

- La arquitectura modular facilita la reutilización de componentes y futuras mejoras.

- La base de datos se gestiona de forma eficiente mediante consultas optimizadas.
