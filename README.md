# sistema-inventario

Sistema web para la gestión de inventarios de un comercio electrónico.

Tablero: **DevOps - Sistema de Inventario** (GitHub Projects, vista Board).
Flujo: Backlog → Por hacer → En progreso → En revisión → Terminado.

---

## Práctica 1. Tablero DevOps

**¿Por qué un equipo de desarrollo necesita visualizar el estado de sus tareas?**
Porque todos ven en un solo lugar qué se está haciendo, quién lo hace y qué falta. Así se evita duplicar trabajo, se detectan cuellos de botella (por ejemplo, muchas tareas detenidas en revisión) y se pueden tomar decisiones sobre prioridades con información real.

**¿Qué diferencia existe entre Backlog y Por hacer?**
El Backlog guarda ideas y necesidades que todavía no están listas ni comprometidas. Por hacer contiene tareas ya definidas, priorizadas y listas para empezar en el corto plazo.

**¿Cuándo una tarea debe pasar de Por hacer a En progreso?**
Cuando un integrante se la asigna y comienza a trabajar en ella realmente, y el equipo tiene capacidad para atenderla sin dejar otras a medias.

**¿Por qué una tarea no debería pasar directamente de En progreso a Terminado?**
Porque antes debe revisarse y probarse. Saltar la revisión permite que lleguen errores a la rama principal o al usuario.

**¿Qué función cumple la columna En revisión?**
Es el punto de control de calidad: revisión de código (Pull Request), pruebas y validación de que la tarea cumple lo solicitado.

**¿Qué relación tiene este tablero con la entrega continua en DevOps?**
La entrega continua busca entregar valor en cambios pequeños y frecuentes. El tablero hace visible ese flujo, ayuda a mantener las tareas pequeñas, a que avancen sin atascarse y a que cada una pase por revisión antes de integrarse, que es la base para entregar de forma continua y confiable.

---

## Práctica 3. Campos personalizados

### Situación A
- Issue con mayor atención: **Implementar registro de productos**.
- Prioridad: **Alta** (el cliente lo necesita antes de la próxima revisión).
- Estimación: **5** (requiere capturar, validar y guardar varios datos).
- Fase DevOps: **CODE** (el trabajo principal es programarla).

### Situación B
Una vez terminada la programación, la tarea ya no está principalmente en CODE: su propósito actual es comprobar que funciona, por lo que se cambia a **TEST** y la tarjeta pasa a **En revisión**. El campo debe reflejar la fase en la que está la tarea ahora, no en la que empezó.

### Reto: Mejorar búsqueda de productos
- Prioridad: **Media**. Es una petición del cliente, pero no bloquea la próxima revisión; el registro de productos va primero.
- Fase DevOps: **CODE**. La necesidad ya está clara (buscar por nombre, código y categoría); el trabajo principal es implementarla.
- Estimación: **5**. Implica tres criterios de búsqueda y combinarlos, más complejo que una búsqueda simple (3) pero no tan grande como el control de existencias (8).

### Reflexión
- **¿Qué problema resuelve Prioridad?** Indica qué atender primero cuando hay más tareas que tiempo.
- **¿Para qué sirve identificar la Fase DevOps?** Para saber en qué parte del ciclo (planear, programar, probar, desplegar…) está cada tarea y ver si alguna fase concentra demasiado trabajo.
- **¿Por qué la estimación no son horas?** Porque es una medida relativa de esfuerzo y complejidad entre tareas; las horas varían según la persona y los imprevistos.
- **¿Qué pasa si todas las tareas son Alta?** La prioridad pierde sentido: nada se distingue, el equipo no sabe por dónde empezar y lo realmente urgente se retrasa.
- **¿Por qué estimar antes de desarrollar?** Para planear cuánto trabajo cabe en un periodo, detectar tareas demasiado grandes que conviene dividir y fijar expectativas realistas con el cliente.
- **¿Qué información adicional da ahora el tablero?** Además del estado de cada tarea, muestra su importancia, la fase DevOps y el esfuerzo estimado, lo que permite priorizar y planear, no solo dar seguimiento.

---

## Fase de codificación

| Concepto | Significado |
| --- | --- |
| Repository | Lugar donde se almacena el proyecto |
| Branch | Línea independiente de desarrollo |
| Commit | Registro de un cambio |
| Push | Enviar cambios al repositorio remoto |
| Pull Request | Solicitud para integrar cambios |
| Review | Revisión de los cambios |
| Merge | Integración de cambios |
| Conflict | Cambios incompatibles que requieren intervención |

Para ejecutar el ejemplo: `cd src && python producto.py`
