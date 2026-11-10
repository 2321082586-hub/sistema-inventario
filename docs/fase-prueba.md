# Fase de prueba (TEST)

Herramienta: **unittest** (incluida en Python). Archivo: `tests/test_producto.py`.
Ejecutar: `python -m unittest discover -s tests -v`

## Casos de prueba

| ID | Caso de prueba | Datos de entrada | Resultado esperado | Resultado |
| --- | --- | --- | --- | --- |
| CP01 | Crear un producto | P001, Teclado, 350, 10 | Se crea con esos datos | CORRECTO |
| CP02 | Mostrar el código | P001 | Se muestra P001 | CORRECTO |
| CP03 | Mostrar el nombre | Teclado | Se muestra Teclado | CORRECTO |
| CP04 | Mostrar el precio | 350 | Se muestra 350.00 | CORRECTO |
| CP05 | Mostrar la existencia | 10 | Se muestra 10 | CORRECTO |
| CP06 | Mostrar información completa | Todos los anteriores | Se muestran los 4 datos | CORRECTO |
| CP07 | Crear otro producto | P002, Mouse, 180, 5 | No se confunde con el primero | CORRECTO |

**Resultado: 7 de 7 pruebas satisfactorias.** Salidas reales en la carpeta `evidencias/`.

## Error provocado

Se cambió `mostrar_informacion` para imprimir `self.precio + 1` (ver `evidencias/2_cambio_con_error.txt`).
Las pruebas **CP04 (precio)** y **CP06 (información completa)** fallaron porque se mostraba 351.00 en lugar de 350.00 (`evidencias/3_pruebas_con_error.txt`).
Se restauró el código original y las 7 pruebas volvieron a pasar (`evidencias/4_pruebas_corregidas.txt`).

## Automatización

`.github/workflows/tests.yml` ejecuta las pruebas en GitHub Actions en cada push y Pull Request a `main`:
descarga el código (`actions/checkout`), prepara Python 3.12 (`actions/setup-python`) y corre `python -m unittest discover -s tests -v`.
Si alguna prueba falla, el comando termina con error y Actions marca ❌.

## Preguntas

- **¿Por qué probar antes de incorporar a la versión principal?** Para que los errores se detecten en la rama de trabajo y no lleguen a `main`, de donde todo el equipo toma el código.
- **¿Diferencia entre caso de prueba y prueba automatizada?** El caso de prueba es el diseño: datos de entrada y resultado esperado. La prueba automatizada es el código que ejecuta ese caso y compara el resultado sin intervención humana.
- **¿Diferencia entre resultado esperado y obtenido?** El esperado es lo que debería pasar según el requisito; el obtenido es lo que realmente hizo el programa. Si no coinciden, la prueba falla.
- **¿Qué ocurrió al modificar el código intencionalmente?** CP04 y CP06 fallaron e indicaron que se esperaba 350.00 y se obtuvo 351.00, lo que permitió ubicar el error en el precio.
- **¿Ventajas de ejecutar las pruebas en GitHub Actions?** Se ejecutan solas en cada cambio, en un entorno limpio, el resultado queda visible en el Pull Request y nadie tiene que acordarse de correrlas.
- **¿Por qué ejecutar las pruebas después de cada modificación?** Porque un cambio en una parte puede romper otra que ya funcionaba (regresión); probar siempre lo detecta al momento.

## Fuentes

- Python Docs – unittest: https://docs.python.org/3/library/unittest.html
- GitHub Docs – Building and testing Python: https://docs.github.com/actions/use-cases-and-examples/building-and-testing/building-and-testing-python
