# La Fabulosa Lasaña de Guido (Guido's Gorgeous Lasagna)

¡Bienvenido al ejercicio de la Fabulosa Lasaña de Guido en la ruta de Python de Exercism!

## Introducción

Este primer ejercicio introduce 4 características principales del lenguaje Python:
1. **Asignación de Nombres** (*Variables y Constantes*).
2. **Funciones** (*Las palabras clave `def` y `return`*).
3. **Comentarios** (`#`).
4. **Docstrings** (Documentación de funciones usando triple comilla `"""`).

---

### Variables y Constantes
- **Variables:** En Python se escriben usando el estilo `snake_case` (por ejemplo: `mi_variable = 10`).
- **Constantes:** Son valores que no cambian a lo largo del programa. Por convención, se escriben en mayúsculas sostenidas usando `SCREAMING_SNAKE_CASE` (por ejemplo: `EXPECTED_BAKE_TIME = 40`).

---

### Funciones
Las funciones se definen con la palabra clave `def`, seguida del nombre de la función y los parámetros entre paréntesis `()`:

```python
def mi_funcion(parametro_uno):
    return parametro_uno * 2
```

---

## Instrucciones del Ejercicio

Vas a escribir código para ayudarte a cocinar una deliciosa lasaña. El ejercicio se divide en 5 tareas:

### 1. Definir el tiempo esperado de horneado como una constante
Define la constante `EXPECTED_BAKE_TIME` que representa cuántos minutos debe hornearse la lasaña.
Según la receta, la lasaña debe estar en el horno por **40 minutos**.

```python
>>> print(EXPECTED_BAKE_TIME)
40
```

---

### 2. Calcular el tiempo restante de horneado en minutos
Completa la función `bake_time_remaining(elapsed_bake_time)` que toma los minutos que la lasaña ya lleva en el horno como argumento (`elapsed_bake_time`) y retorna cuántos minutos le faltan por hornear basándose en la constante `EXPECTED_BAKE_TIME`.

```python
>>> bake_time_remaining(30)
10
```

---

### 3. Calcular el tiempo de preparación en minutos
Define la función `preparation_time_in_minutes(number_of_layers)` que toma la cantidad de capas que quieres agregar a la lasaña (`number_of_layers`) y retorna cuántos minutos te tomará prepararlas.
Asume que **cada capa toma 2 minutos** de preparación.

```python
>>> preparation_time_in_minutes(2)
4
```

---

### 4. Calcular el tiempo total transcurrido (preparación + horneado) en minutos
Define la función `elapsed_time_in_minutes(number_of_layers, elapsed_bake_time)` que toma dos parámetros:
- `number_of_layers`: el número de capas agregadas.
- `elapsed_bake_time`: el número de minutos que la lasaña ya lleva en el horno.

Esta función debe retornar el total de minutos que has estado cocinando en la cocina (tiempo de preparación + tiempo en el horno).

```python
>>> elapsed_time_in_minutes(3, 20)
26
```

---

### 5. Documentar el código con Docstrings
Asegúrate de agregar descripciones y notas a tus funciones usando **docstrings** (comentarios multilínea entre triple comilla `"""`) para explicar qué hace cada función y cuáles son sus parámetros y valor de retorno.

---