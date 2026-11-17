# Historial de versiones

Todas las versiones se generan automáticamente con el workflow
`.github/workflows/release.yml` al publicar una etiqueta `v*`.

## v1.0.2 – Corrección

- Corrección del error en el precio detectado durante la liberación de v1.0.1.
- Las 7 pruebas automatizadas (CP01–CP07) vuelven a pasar.
- Paquete publicado: `sistema-inventario-v1.0.2.zip`.

## v1.0.1 – No publicada

- Contenía un error intencional: el precio se mostraba con 1 peso de más.
- El workflow de liberación falló en "Ejecutar pruebas" (CP04 y CP06) y no publicó la versión.

## v1.0.0 – Primera versión

- Primera versión del Sistema de Inventario.
- Funcionalidad Producto: código, nombre, precio y existencia.
- Programa principal `src/main.py`: registrar, consultar y mostrar productos.
- Búsqueda y consulta de productos.
- Pruebas automatizadas (unittest) y workflows de BUILD y TEST.
- Paquete publicado: `sistema-inventario-v1.0.0.zip`.
