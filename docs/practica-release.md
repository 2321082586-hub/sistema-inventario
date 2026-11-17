# Práctica 5 – Fase RELEASE

Se configuró un workflow que, al publicar una etiqueta `v*`, ejecuta las pruebas, genera el paquete
`sistema-inventario-<versión>.zip` con la carpeta `src/` y lo publica en GitHub Releases.
Se liberaron **v1.0.0** y **v1.0.2**; **v1.0.1** no se publicó porque sus pruebas fallaron.

## Versión liberada

| Elemento | Descripción |
| --- | --- |
| Proyecto | Sistema de Inventario |
| Versión | v1.0.0 |
| Funcionalidad | Representación, registro, consulta y visualización de productos |
| Pruebas | 7 de 7 satisfactorias |
| Paquete | `sistema-inventario-v1.0.0.zip` (carpeta `src/`) |
| Estado | Publicada en GitHub Releases |

## Workflow `.github/workflows/release.yml`

| Elemento | Función |
| --- | --- |
| `name` | Identifica el proceso de liberación. |
| `on.push.tags: 'v*'` | Se ejecuta solo cuando se publica una etiqueta que empieza con `v`. |
| `permissions: contents: write` | Permite crear la liberación y adjuntar el paquete. |
| `runs-on: ubuntu-latest` | Entorno de ejecución. |
| `actions/checkout@v4` | Descarga el código de la etiqueta. |
| `actions/setup-python@v5` | Prepara Python 3.12. |
| Ejecutar pruebas | `python -m unittest discover -s tests -v`. Si falla, el workflow se detiene y no publica. |
| Crear paquete | `zip -r` de la carpeta `src/` (sin `__pycache__`). `tests/` no se incluye porque solo se usa para validar. |
| Publicar version | `softprops/action-gh-release@v2` crea la liberación, adjunta el ZIP y genera las notas de cambios. |

## Resultados

| Etiqueta | Qué contenía | Resultado del workflow | ¿Publicada? |
| --- | --- | --- | --- |
| v1.0.0 | Primera versión | Correcto | Sí |
| v1.0.1 | Error intencional en el precio (+1) | Falló en "Ejecutar pruebas" (CP04 y CP06) | **No** |
| v1.0.2 | Corrección del error | Correcto | Sí |

No se reutilizó v1.0.1 para el código corregido: las etiquetas identifican un punto fijo del historial.
Evidencias: carpeta `evidencias/` (archivos `release-*`).

## Conceptos

| Concepto | Significado |
| --- | --- |
| Release | Versión del software preparada para su distribución. |
| Tag | Identificador asociado a un punto del historial del repositorio. |
| Versionamiento | Mecanismo para identificar las distintas versiones (vMAYOR.MENOR.PARCHE). |
| Artifact | Archivo generado durante un proceso automatizado (el ZIP). |
| Package | Conjunto de archivos preparado para su distribución. |
| Changelog | Registro de los cambios de cada versión (`CHANGELOG.md`). |
| GitHub Actions | Herramienta para automatizar procesos del repositorio. |
| Pipeline | Secuencia de actividades automatizadas: pruebas → paquete → publicación. |

## Preguntas de reflexión

- **¿Por qué es importante identificar cada versión?** Para saber exactamente qué código se entregó, cuál pasó las pruebas y poder recuperar una versión anterior.
- **¿Diferencia entre commit, tag y release?** Un commit registra un cambio; un tag le pone un nombre fijo (v1.0.0) a un commit; un release es la publicación de ese tag en GitHub con notas y archivos para descargar.
- **¿Por qué se ejecutan las pruebas antes de publicar?** Para que solo se distribuyan versiones que funcionan.
- **¿Qué ocurre si las pruebas fallan?** El workflow se detiene en "Ejecutar pruebas" y no crea el paquete ni la liberación, como pasó con v1.0.1.
- **¿Ventajas de generar el paquete automáticamente?** Siempre contiene los mismos archivos, sale del código exacto de la etiqueta y nadie tiene que copiar archivos a mano.
- **¿Por qué conservar un historial de versiones?** Para saber qué cambió en cada versión, rastrear errores y regresar a una versión estable.
- **¿Diferencia entre liberar y desplegar?** Liberar es preparar y publicar una versión; desplegar es instalarla y ponerla a funcionar en el entorno donde se usará.
