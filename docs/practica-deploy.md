# Práctica 7 – Fase DEPLOY

La versión **v1.0.2** se desplegó desde GitHub Releases en dos entornos: esta computadora (manual) y un
servidor Linux con acceso SSH (automático con GitHub Actions). La versión **v1.1.0** falló al ejecutarse y
se recuperó v1.0.2 en ambos entornos.

## 1. Versión desplegada

| Dato | Valor |
| --- | --- |
| Versión | v1.0.2 |
| Archivo | `sistema-inventario-v1.0.2.zip` (descargado de GitHub Releases, no se volvió a generar) |
| Despliegue manual | `~/Downloads/despliegue-inventario/` en macOS |
| Despliegue automático | `~/sistema-inventario/` en el servidor Linux, vía SSH |

Fecha de publicación: ver `evidencias/deploy-local-v1.0.2-version.txt`.

## 2. Requisitos del entorno

| Requisito | Detalle |
| --- | --- |
| Sistema operativo | Linux, macOS o Windows |
| Python | 3.8 o superior (`python3 --version`) |
| Herramienta para descomprimir | `unzip` o el explorador de archivos |
| Dependencias | Ninguna: solo biblioteca estándar de Python |
| Espacio | Menos de 1 MB |
| Para el despliegue automático | Servidor con SSH y Python, y los secretos `DEPLOY_HOST`, `DEPLOY_USER`, `DEPLOY_KEY`, `DEPLOY_PORT` |

## 3. Procedimiento de despliegue manual

1. Entrar a **GitHub → sistema-inventario → Releases** y abrir la versión a instalar (por ejemplo, v1.0.2).
2. Descargar `sistema-inventario-v1.0.2.zip` (o `gh release download v1.0.2 --repo 2321082586-hub/sistema-inventario`).
3. Crear la carpeta de despliegue y guardar ahí el ZIP:
   ```
   mkdir -p ~/despliegue-inventario && cd ~/despliegue-inventario
   ```
4. Extraer cada versión en su propia carpeta y marcar la activa:
   ```
   unzip -oq sistema-inventario-v1.0.2.zip -d version-v1.0.2
   ln -sfn version-v1.0.2 actual
   ```
   En Windows: extraer en `version-v1.0.2` con el explorador y trabajar desde esa carpeta.
5. Ejecutar el sistema desde la carpeta de la versión:
   ```
   cd actual
   python3 src/main.py          # menú interactivo
   python3 src/main.py --demo   # verificación rápida
   ```
6. Comprobar que funciona: el modo `--demo` debe registrar P001 y P002, consultar P001, mostrar el inventario
   y terminar con "Sistema funcionando correctamente."

No requiere configuración adicional.

## 4. Despliegue automático (`.github/workflows/deploy.yml`)

Se ejecuta a mano desde **Actions → Despliegue del Sistema de Inventario → Run workflow**, indicando la versión.

| Paso | Qué hace |
| --- | --- |
| Servidor de destino | Máquina Linux con SSH (contenedor `linuxserver/openssh-server`), usuario `deploy`, puerto 2222. |
| Descargar versión liberada | `gh release download` del ZIP publicado en Releases. |
| Configurar conexión SSH | Usa los secretos `DEPLOY_KEY`, `DEPLOY_HOST`, `DEPLOY_USER` y `DEPLOY_PORT`; ninguna llave va escrita en el YAML. |
| Preparar el servidor | Instala Python 3 y `unzip`, y crea `~/sistema-inventario`. |
| Transferir y preparar | `scp` del ZIP al servidor, extracción en `version-<versión>` y enlace `actual` a esa versión. |
| Ejecutar y verificar | `python3 src/main.py --demo` en el servidor. |
| Recuperar la versión anterior | Si la verificación falla y se indicó `version_anterior`, el enlace `actual` regresa a esa versión. |
| Resultado | Resumen en la ejecución; queda en rojo si la versión solicitada no pasó la verificación. |

**Sobre el servidor:** GitHub no puede conectarse por SSH a una computadora de casa detrás de un módem,
así que el servidor de destino es un contenedor Linux con SSH que el workflow levanta junto al job.
Para usar una máquina virtual o servidor real solo se cambian los valores de los secretos y se quita la
sección `services`; los pasos de SSH son los mismos.

## 5. Resultados de las verificaciones

| Comprobación | Mac (v1.0.2) | Servidor (v1.0.2) |
| --- | --- | --- |
| ¿El programa inicia? | Sí | Sí |
| ¿Se registran productos? | Sí (P001, P002) | Sí |
| ¿Se consultan productos? | Sí (P001) | Sí |
| ¿Se muestran correctamente los datos? | Sí | Sí |
| ¿Errores durante la ejecución? | No | No |

Evidencias: `evidencias/deploy-local-*.txt` y `evidencias/deploy-github-*.txt`.

## 6. Problema simulado y recuperación

1. Se desplegó y verificó **v1.0.2**.
2. Se liberó **v1.1.0**, que agrega el valor total del inventario. Las pruebas pasaron porque no cubren `main.py`.
3. Al ejecutarla, el sistema falló con `AttributeError: 'Producto' object has no attribute 'cantidad'`.
4. Recuperación en la Mac: `ln -sfn version-v1.0.2 actual` y el sistema volvió a funcionar.
5. Recuperación en el servidor: el workflow detectó la falla y regresó `actual` a `version-v1.0.2` automáticamente.
6. Se corrigió el error en `main` y la liberación v1.1.0 quedó marcada como "con error".

La recuperación es inmediata porque cada versión se conserva en su propia carpeta y solo se cambia el
enlace `actual`; no se borra ni se descarga nada de nuevo.

## 7. Problemas posibles y solución

| Problema | Causa | Solución |
| --- | --- | --- |
| `python3: command not found` | Python no instalado | Instalar Python 3.8+ y abrir una terminal nueva. |
| `ModuleNotFoundError: producto` | Se ejecutó desde otra carpeta | Ejecutar `python3 src/main.py` dentro de la carpeta de la versión. |
| `release not found` | Etiqueta mal escrita | Revisar el nombre exacto en Releases (por ejemplo, `v1.0.2`). |
| `Permission denied (publickey)` | Llave SSH incorrecta | Revisar el secreto `DEPLOY_KEY` y que la llave pública esté en el servidor. |
| `Host key verification failed` | Servidor desconocido | Agregarlo a `known_hosts` con `ssh-keyscan`. |
| `unzip: command not found` | Falta la herramienta | `sudo apt install unzip` / `sudo apk add unzip`. |
| La nueva versión falla | Error en el código | Regresar el enlace `actual` a la versión anterior. |

## Preguntas de reflexión

- **¿Diferencia entre liberar y desplegar?** Liberar es publicar una versión identificada con su paquete; desplegar es instalarla y ejecutarla en el entorno donde se usará.
- **¿Por qué se usa el paquete de la fase RELEASE?** Porque es exactamente el código que pasó las pruebas; generarlo de nuevo podría incluir otros cambios.
- **¿Qué función tiene el entorno de destino?** Es donde el sistema funciona para sus usuarios, separado de las computadoras de los desarrolladores.
- **¿Qué información se necesita para SSH?** Dirección del servidor, usuario, puerto y una credencial (llave privada).
- **¿Por qué usar secretos de GitHub?** Para no escribir llaves ni datos de acceso en el repositorio; GitHub los guarda cifrados y los oculta en los registros.
- **¿Ventajas de automatizar el despliegue?** Siempre se hacen los mismos pasos, sin olvidos, con registro de cada ejecución y recuperación automática si falla.
- **¿Problemas si el destino no cumple requisitos?** El sistema no inicia o falla (por ejemplo, sin Python o sin `unzip`); por eso el workflow prepara el servidor antes de desplegar.
- **¿Por qué un procedimiento de recuperación?** Porque una versión puede fallar en producción aunque pase las pruebas, como v1.1.0; regresar rápido a la anterior evita dejar a los usuarios sin sistema.
