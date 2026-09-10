# Ayuda

## Ejecutando las pruebas

Usamos [pytest][pytest: Getting Started Guide] como nuestro ejecutor de pruebas del sitio web.
Necesitarás instalar `pytest` en tu máquina de desarrollo si quieres ejecutar las pruebas del track de Python localmente.
También deberías instalar los siguientes plugins de `pytest`:

- [pytest-cache][pytest-cache]
- [pytest-subtests][pytest-subtests]

Puedes encontrar información extendida en nuestra [guía de pruebas de Python][Python track tests page] del sitio web.


### Ejecutando Pruebas

Para ejecutar las pruebas incluidas, navega a la carpeta donde está almacenado el ejercicio usando `cd` en tu terminal (_reemplaza `<exercise-folder-location>` abajo con tu ruta_).
Los archivos de prueba usualmente terminan en `_test.py`, y son las mismas pruebas que se ejecutan en el sitio web cuando se sube una solución.

Linux/MacOS
```bash
$ cd <path/to/exercise-folder-location>
```

Windows
```powershell
PS C:\Users\foobar> cd <path\to\exercise-folder-location>
```

<br>

A continuación, ejecuta el comando `pytest` en tu terminal, reemplazando `<exercise_test.py>` con el nombre del archivo de prueba:

Linux/MacOS
```bash
$ python3 -m pytest -o markers=task <exercise_test.py>
==================== 7 passed in 0.08s ====================
```

Windows
```powershell
PS C:\Users\foobar> py -m pytest -o markers=task <exercise_test.py>
==================== 7 passed in 0.08s ====================
```


### Opciones comunes
- `-o` : sobrescribe el `pytest.ini` por defecto (_puedes usar esto para evitar advertencias de marcadores_)
- `-v` : habilita salida detallada (verbose).
- `-x` : detiene la ejecución de pruebas al primer fallo.
- `--ff` : ejecuta los fallos de la prueba anterior antes de ejecutar otros casos de prueba.

Para opciones adicionales, usa `python3 -m pytest -h` o `py -m pytest -h`.


### Corrigiendo advertencias

Si no usas `pytest -o markers=task` al invocar `pytest`, podrías recibir un `PytestUnknownMarkWarning` para pruebas que usan nuestra nueva sintaxis:

```bash
PytestUnknownMarkWarning: Unknown pytest.mark.task - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/mark.html
```

Para evitar escribir `pytest -o markers=task` para cada prueba que ejecutes, puedes usar un archivo de configuración `pytest.ini`.
Hemos creado uno que puede descargarse desde el nivel superior del directorio del track de Python: [pytest.ini][pytest.ini].

También puedes crear tu propio archivo `pytest.ini` con el siguiente contenido:

```ini
[pytest]
markers =
    task: Una tarea de ejercicio de concepto.
```

Colocar el archivo `pytest.ini` en el directorio _raíz_ o _de trabajo_ para tus ejercicios del track de Python registrará los marcadores y detendrá las advertencias.
Más información sobre los marcadores de pytest se puede encontrar en la documentación de `pytest` sobre [marcado de funciones de prueba][pytest: marking test functions with attributes] y la documentación de `pytest` sobre [trabajar con marcadores personalizados][pytest: working with custom markers].

Información sobre personalización de configuraciones de pytest se puede encontrar en la documentación de `pytest` sobre [formatos de archivo de configuración][pytest: configuration file formats].


### Extendiendo tu IDE o Editor de Código

Muchos IDEs y editores de código tienen soporte integrado para usar `pytest` y otras herramientas de calidad de código.
Algunas opciones de origen comunitario se pueden encontrar en nuestra [página de herramientas del track de Python][Python track tools page].

[Pytest: Getting Started Guide]: https://docs.pytest.org/en/latest/getting-started.html
[Python track tools page]: https://exercism.org/docs/tracks/python/tools
[Python track tests page]: https://exercism.org/docs/tracks/python/tests
[pytest-cache]:http://pythonhosted.org/pytest-cache/
[pytest-subtests]:https://github.com/pytest-dev/pytest-subtests
[pytest.ini]: https://github.com/exercism/python/blob/main/pytest.ini
[pytest: configuration file formats]: https://docs.pytest.org/en/6.2.x/customize.html#configuration-file-formats
[pytest: marking test functions with attributes]: https://docs.pytest.org/en/6.2.x/mark.html#raising-errors-on-unknown-marks
[pytest: working with custom markers]: https://docs.pytest.org/en/6.2.x/example/markers.html#working-with-custom-markers

## Enviando tu solución

Puedes enviar tu solución usando el comando `exercism submit tuples.py`.
Este comando subirá tu solución al sitio web de Exercism e imprimirá la URL de la página de la solución.

Es posible enviar una solución incompleta lo que te permite:
- Ver cómo otros han completado el ejercicio
- Solicitar ayuda de un mentor

## ¿Necesitas obtener ayuda?

Si deseas ayuda para resolver el ejercicio, consulta las siguientes páginas:
- La [documentación del track de Python](https://exercism.org/docs/tracks/python)
- La [categoría de programación del track de Python en el foro](https://forum.exercism.org/c/programming/python)
- [Categoría de programación de Exercism en el foro](https://forum.exercism.org/c/programming/5)
- Las [Preguntas Frecuentes](https://exercism.org/docs/using/faqs)

Si esos recursos no son suficientes, podrías enviar tu solución (incompleta) para solicitar mentoría.

A continuación hay algunos recursos para obtener ayuda si tienes problemas:
- [La PSF](https://www.python.org) aloja descargas de Python, documentación y recursos de la comunidad.
- [Foros de la Comunidad Python](https://discuss.python.org/) ayuda, discusión de PEPs, committers del núcleo de Python y más.
- [La Comunidad Exercism en Discord](https://exercism.org/r/discord)
- [Los Foros de Discusión de la Comunidad Exercism](https://forum.exercsim.org)
- [Comunidad Python en Discord](https://pythondiscord.com/) es una comunidad muy útil y activa.
- [/r/learnpython/](https://www.reddit.com/r/learnpython/) es un subreddit diseñado para aprendices de Python.
- [#python en Libera.chat](https://www.python.org/community/irc/) aquí es donde los desarrolladores principales del lenguaje pasan el rato y trabajan.
- [Foros de la Comunidad Free Code Camp](https://forum.freecodecamp.org/)
- [Pythontutor](http://pythontutor.com/) para recorrer visualmente pequeños fragmentos de código paso a paso.

Adicionalmente, [StackOverflow](http://stackoverflow.com/questions/tagged/python) es un buen lugar para buscar tu problema/pregunta para ver si ya ha sido respondida.
 Si no - siempre puedes [preguntar](https://stackoverflow.com/help/how-to-ask) o [responder](https://stackoverflow.com/help/how-to-answer) la pregunta de otra persona.
