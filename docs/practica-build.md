# Práctica BUILD – Automatización de la construcción

## Actividad 1. Investigación

**¿Qué es un workflow en GitHub Actions y para qué sirve?**
Es un proceso automatizado definido en un archivo YAML dentro de `.github/workflows/`. Se ejecuta en servidores de GitHub cuando ocurre un evento (push, pull request, etc.) y sirve para construir, probar o desplegar el proyecto sin intervención manual.

**¿Qué estructura debe tener el archivo YAML?**
- `name`: nombre del workflow.
- `on`: eventos que lo activan.
- `jobs`: trabajos a ejecutar; cada uno con `runs-on` (sistema operativo) y `steps` (pasos).
- Cada paso usa `uses` (una acción ya hecha) o `run` (un comando).

**¿Qué eventos pueden activarlo?**
`push`, `pull_request`, `workflow_dispatch` (manual), `schedule` (horario), `release`, `issues`, entre otros. Usamos `push` y `pull_request` sobre `main`, más `workflow_dispatch`.

**¿Qué sistema operativo y herramientas necesita el proyecto?**
El proyecto está en Python, que funciona en cualquier sistema. Usamos `ubuntu-latest` (rápido y gratuito) y Python 3.12.

**¿Cómo se configura el entorno del lenguaje?**
Con la acción oficial `actions/setup-python@v5`, indicando `python-version: "3.12"`.

**¿Qué comando verifica o construye el proyecto?**
Python no genera un ejecutable, pero sí compila cada archivo a bytecode antes de ejecutarlo. `python -m compileall -q -f src` compila todo `src/` y termina con error si algún archivo tiene un error de sintaxis, que es el equivalente a un error de compilación.

**¿Qué archivos de configuración o dependencias necesita?**
Solo el código en `src/` y el archivo `build.yml`. El proyecto usa únicamente la biblioteca estándar de Python, por eso no hay `requirements.txt` ni paso de instalación de dependencias.

**¿Cómo se comprueba si terminó bien o con errores?**
En la pestaña **Actions** de GitHub: palomita verde ✅ = correcto, tache rojo ❌ = falló. Dentro de la ejecución se ve el registro de cada paso con el mensaje de error. También aparece el resultado en cada Pull Request.

## Actividad 2. Explicación del YAML

| Sección | Función |
| --- | --- |
| `name` | Identifica el workflow en la pestaña Actions. |
| `on.push.branches: [main]` | Se ejecuta cuando se integran cambios a la rama principal. |
| `on.pull_request.branches: [main]` | Revisa cada PR antes de integrarlo, para detectar errores antes del merge. |
| `on.workflow_dispatch` | Permite ejecutarlo manualmente. |
| `runs-on: ubuntu-latest` | Entorno donde se realizan las tareas. |
| `actions/checkout@v4` | Descarga el código del repositorio en la máquina virtual. |
| `actions/setup-python@v5` | Instala y configura Python 3.12. |
| `python --version` | Deja registro de la versión usada. |
| `python -m compileall -q -f src` | Construye el proyecto: compila todos los archivos de `src`. `-q` muestra solo errores y `-f` obliga a compilar todo de nuevo. Si hay un error devuelve código distinto de 0 y el workflow falla. |

No se agregó paso de dependencias porque el proyecto no las tiene.

## Actividad 4. Prueba del error

1. En la rama `build/prueba-error` se quitaron los dos puntos de `def mostrar_informacion(self):` en `src/producto.py`.
2. Al subir el cambio, el workflow falló en el paso **"Construir (compilar) el código fuente"** con un `SyntaxError`.
3. Se corrigió el archivo, se hizo un nuevo commit y el workflow volvió a pasar ✅.

## Reflexión

- **¿Qué problema evita la automatización?** Que se integren cambios que "funcionan en mi computadora" pero rompen el proyecto para los demás.
- **¿Diferencia entre ejecutar manualmente y usar GitHub Actions?** A mano depende de que alguien se acuerde y de la configuración de su computadora. Actions lo hace siempre, igual y en un entorno limpio, y deja registro visible para todo el equipo.
- **¿Qué ocurrió al introducir un error?** El workflow marcó ❌ en el Pull Request y en Actions, indicando el archivo, la línea y el tipo de error.
- **¿Por qué detectar el error inmediatamente?** Porque es más fácil y barato corregirlo cuando el cambio es reciente y pequeño, y evita que llegue a `main` y afecte a todo el equipo.

## Fuentes consultadas

- GitHub Docs – Understanding GitHub Actions: https://docs.github.com/actions/about-github-actions/understanding-github-actions
- GitHub Docs – Workflow syntax for GitHub Actions: https://docs.github.com/actions/writing-workflows/workflow-syntax-for-github-actions
- GitHub Docs – Events that trigger workflows: https://docs.github.com/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows
- GitHub Docs – Building and testing Python: https://docs.github.com/actions/use-cases-and-examples/building-and-testing/building-and-testing-python
- actions/checkout: https://github.com/actions/checkout
- actions/setup-python: https://github.com/actions/setup-python
- Python Docs – compileall: https://docs.python.org/3/library/compileall.html
