# Pistas

## General


- Las [tuplas][tuples] son tipos de [secuencia][sequence types] inmutables que pueden contener cualquier tipo de dato.
- Las tuplas son [iterables][iterable]. Si necesitas índices además de valores, usa [`enumerate()`][enumerate]
- Los elementos dentro de las tuplas pueden ser accedidos mediante [notación de corchetes][bracket notation], usando un índice basado en cero desde la izquierda, o -1 desde la derecha. Otras [Operaciones Comunes de Secuencia][common sequence operations] también pueden usarse al trabajar con tuplas.

## 1. Extraer coordenadas

- Recuerda: las tuplas permiten acceso mediante _índice_, usando _corchetes_. Los índices comienzan desde la izquierda en cero.

## 2. Formatear coordenadas

- Consulta [`class tuple`][class tuple] para más detalles sobre tuplas.
- Consulta [`class str`][class str] para más detalles sobre strings.

## 3. Comparar coordenadas

- ¿Qué métodos podrían usarse aquí para [probar pertenencia][testing membership]?.
- Consulta [`class tuple`][class tuple] para más detalles sobre tuplas.
- ¿Podrías reutilizar tu función `convert_coordinate()`?

## 4. Combinar registros coincidentes

- Recuerda que las tuplas soportan todas las [operaciones comunes de secuencia][common sequence operations].
- ¿Podrías reutilizar tu función `compare_records()` aquí?

## 5. "Limpiar" y hacer un reporte de todos los registros

- Recuerda: las tuplas son _inmutables_, pero el contenido puede ser accedido mediante _índice_ usando _notación de corchetes_.
- Las tuplas no tienen que usar paréntesis a menos que haya _ambigüedad_.
- Python tiene múltiples métodos de formateo de strings. [`str.format()`][str.format] y [`f-strings`][f-strings] son dos muy comunes.
- Hay múltiples opciones de formateo textual disponibles a través del [`mini-lenguaje de especificación de formato`][format specification mini-language] de Python.


[bracket notation]: https://stackoverflow.com/questions/30250282/whats-the-difference-between-the-square-bracket-and-dot-notations-in-python
[class str]: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
[class tuple]: https://docs.python.org/3/library/stdtypes.html#tuple
[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[enumerate]: https://docs.python.org/3/library/functions.html#enumerate
[f-strings]: https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
[format specification mini-language]: https://docs.python.org/3/library/string.html#format-specification-mini-language
[iterable]: https://docs.python.org/3/glossary.html#term-iterable
[sequence types]: https://docs.python.org/3/library/stdtypes.html#typesseq
[str.format]: https://docs.python.org/3/library/stdtypes.html#str.format
[testing membership]: https://docs.python.org/3/reference/expressions.html#membership-test-operations
[tuples]: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
