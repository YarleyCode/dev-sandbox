# Búsqueda del Tesoro de Tisbury

Bienvenido a Búsqueda del Tesoro de Tisbury en el Track de Python de Exercism.
Si necesitas ayuda para ejecutar las pruebas o enviar tu código, consulta `HELP.md`.
Si te atascas en el ejercicio, consulta `HINTS.md`, ¡pero intenta resolverlo sin usar esas pistas primero! :)

## Introducción

En Python, una [tupla][tuple] es una colección _inmutable_ de elementos en _secuencia_.
Como la mayoría de colecciones, las `tuplas` pueden contener cualquier tipo de dato (o múltiples) — incluyendo otras `tuplas`.
Las tuplas soportan todas las [operaciones comunes de secuencia][common sequence operations], pero **no** soportan [operaciones de secuencia mutable][mutable sequence operations].

Los elementos de una tupla se pueden iterar usando la construcción `for item in <tupla>`.
Si se necesitan tanto el índice como el valor, se puede usar `for index, item in enumerate(<tupla>)`.
Como cualquier secuencia, los elementos dentro de las `tuplas` pueden ser accedidos mediante _notación de corchetes_ usando un número de índice `basado en 0` desde la izquierda o un número de índice `basado en -1` desde la derecha.
Las tuplas también pueden ser copiadas total o parcialmente usando notación de rebanado (_`<tupla>[<inicio>:<fin>:<paso>]`_).


## Construcción de Tuplas

Las tuplas pueden formarse de múltiples maneras, usando el constructor de clase `tuple(<iterable>)` o la declaración literal de `tupla`.

### Usando el constructor `tuple()` vacío o con un _iterable_:

```python
>>> no_elements = tuple()
()

# El constructor *requiere* un iterable, por lo que elementos individuales deben pasarse en una lista u otra tupla.
>>> one_element = tuple([16])
(16,)
```

Los strings son iterables, por lo que usar un solo `str` como argumento del constructor `tuple()` puede tener resultados sorprendentes:

```python
# Los elementos del string (caracteres) se iteran y se añaden a la tupla
>>> multiple_elements_string = tuple("Timbuktu")
('T', 'i', 'm', 'b', 'u', 'k', 't', 'u')
```

Los iterables individuales tienen sus elementos añadidos uno por uno:

```python
>>> multiple_elements_list = tuple(["Parrot", "Bird", 334782])
("Parrot", "Bird", 334782)

>>> multiple_elements_set = tuple({2, 3, 5, 7, 11})
(2,3,5,7,11)
```

#### Declarando una tupla como _literal_ :

Debido a que el constructor `tuple(<iterable>)` solo toma _iterables_ (o nada) como argumentos, es mucho más fácil crear
 una tupla de un elemento mediante el método literal.

```python
>>> no_elements = ()
()

>>> one_element = ("Guava",)
("Guava",)
```

Las estructuras de datos anidadas pueden incluirse como elementos de `tupla`, incluyendo otras `tuplas`:

```python
>>> nested_data_structures = ({"fish": "gold", "monkey": "brown", "parrot" : "grey"}, ("fish", "mammal", "bird"))
({"fish": "gold", "monkey": "brown", "parrot" : "grey"}, ("fish", "mammal", "bird"))

>>> nested_data_structures_1 = (["fish", "gold", "monkey", "brown", "parrot", "grey"], ("fish", "mammal", "bird"))
(["fish", "gold", "monkey", "brown", "parrot", "grey"], ("fish", "mammal", "bird"))
```

## Concatenación de Tuplas

Las tuplas pueden concatenarse usando el operador `+`, que desempaqueta cada `tupla` creando una nueva `tupla` combinada.

```python
>>> new_via_concatenate = ("George", 5) + ("cat", "Tabby")
("George", 5, "cat", "Tabby")

# De igual forma, usar el operador de multiplicación * es equivalente a usar + n veces
>>> first_group = ("cat", "dog", "elephant")

>>> multiplied_group = first_group * 3
('cat', 'dog', 'elephant', 'cat', 'dog', 'elephant', 'cat', 'dog', 'elephant')
```

## Accediendo a Elementos Dentro de una Tupla

Los elementos dentro de una `tupla` pueden ser accedidos mediante _notación de corchetes_ usando un número de índice `basado en 0` desde la izquierda o un número de índice `basado en -1` desde la derecha.

```python
student_info = ("Alyssa", "grade 3", "female", 8 )

# el género está en el índice 2 o índice -2
>>> student_gender = student_info[2]
'female'

>>> student_gender = student_info[-2]
'female'

# el nombre está en el índice 0 o índice -4
>>> student_name = student_info[0]
Alyssa

>>> student_name = student_info[-4]
Alyssa
```

## Iterando Sobre los Elementos de una Tupla

Los elementos dentro de una `tupla` pueden ser _iterados_ en un bucle usando la sintaxis `for item in <tupla>`.
Si se necesitan tanto índices como valores, se puede usar `for index, item in enumerate(<tupla>)`.

```python
>>> student_info = ("Alyssa", "grade 3", "female", 8 )
>>> for item in student_info:
...   print(item)

...
Alyssa
grade 3
female
8

>>> for index, item in enumerate(student_info):
...  print("Index is: " + str(index) + ", value is: " + str(item) +".")

...
Index is: 0, value is: Alyssa.
Index is: 1, value is: grade 3.
Index is: 2, value is: female.
Index is: 3, value is: 8.
```

## Verificando Pertenencia en una Tupla

El operador `in` puede usarse para verificar pertenencia en una `tupla`.

```python
>>> multiple_elements_list = tuple(["Parrot", "Bird", 334782])
("Parrot", "Bird", 334782)

>>> "Parrot" in multiple_elements_list
True
```

[common sequence operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[mutable sequence operations]: https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
[tuple]: https://docs.python.org/3/library/stdtypes.html#tuple

## Instrucciones

Azara y Rui son compañeros de equipo que compiten en una búsqueda del tesoro con temática pirata.
Una tiene una lista de tesoros con coordenadas del mapa, el otro una lista de nombres de lugares con coordenadas del mapa.
También les han dado mapas en blanco con un lugar de inicio marcado como TÚ ESTÁS AQUÍ (YOU ARE HERE).

<br>
<table>
<tr><th>Lista de Azara</th><th></th><th>Lista de Rui</th></tr>
<tr><td>

| Tesoro                        | Coordenadas |
| --------------------------- | ----------- |
| Amethyst Octopus            | 1F          |
| Angry Monkey Figurine       | 5B          |
| Antique Glass Fishnet Float | 3D          |
| Brass Spyglass              | 4B          |
| Carved Wooden Elephant      | 8C          |
| Crystal Crab                | 6A          |
| Glass Starfish              | 6D          |
| Model Ship in Large Bottle  | 8A          |
| Pirate Flag                 | 7F          |
| Robot Parrot                | 1C          |
| Scrimshawed Whale Tooth     | 2A          |
| Silver Seahorse             | 4E          |
| Vintage Pirate Hat          | 7E          |

</td><td></td><td>

| Nombre del Lugar                     | Coordenadas | Cuadrante |
| ------------------------------------- | ----------- | --------- |
| Seaside Cottages                      | ("1", "C")  | Blue      |
| Aqua Lagoon (Island of Mystery)       | ("1", "F")  | Yellow    |
| Deserted Docks                        | ("2", "A")  | Blue      |
| Spiky Rocks                           | ("3", "D")  | Yellow    |
| Abandoned Lighthouse                  | ("4", "B")  | Blue      |
| Hidden Spring (Island of Mystery)     | ("4", "E")  | Yellow    |
| Stormy Breakwater                     | ("5", "B")  | Purple    |
| Old Schooner                          | ("6", "A")  | Purple    |
| Tangled Seaweed Patch                 | ("6", "D")  | Orange    |
| Quiet Inlet (Island of Mystery)       | ("7", "E")  | Orange    |
| Windswept Hilltop (Island of Mystery) | ("7", "F")  | Orange    |
| Harbor Managers Office                | ("8", "A")  | Purple    |
| Foggy Seacave                         | ("8", "C")  | Purple    |

</td></tr>
</table>

<br>

Pero las cosas están un poco desorganizadas: las coordenadas de Azara parecen estar formateadas y ordenadas de forma diferente a las de Rui, y tienen que estar mirando de una lista a otra para averiguar qué tesoros van con qué lugares.
Como son pythonistas en ciernes, han acudido a ti en busca de ayuda para escribir un pequeño programa (un conjunto de funciones, en realidad) para organizar mejor la información de su búsqueda.


## 1. Extraer coordenadas

Implementa la función `get_coordinate()` que toma un par `(tesoro, coordenada)` de la lista de Azara y devuelve solo la coordenada del mapa extraída.


```python
>>> get_coordinate(('Scrimshawed Whale Tooth', '2A'))
2A
```

## 2. Formatear coordenadas

Implementa la función `convert_coordinate()` que toma una coordenada en formato "2A" y devuelve una tupla en formato `("2", "A")`.


```python
>>> convert_coordinate("2A")
("2", "A")
```

## 3. Comparar coordenadas

Implementa la función `compare_records()` que toma un par `(tesoro, coordenada)` y un registro `(lugar, coordenada, cuadrante)` y compara las coordenadas de cada uno.
Devuelve **`True`** si las coordenadas "coinciden", y devuelve **`False`** si no coinciden.
Reformatea las coordenadas según sea necesario para una comparación precisa.


```python
>>> compare_records(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue'))
False

>>> compare_records(('Model Ship in Large Bottle', '8A'), ('Harbor Managers Office', ('8', 'A'), 'purple'))
True
```

## 4. Combinar registros coincidentes

Implementa la función `create_record()` que toma un par `(tesoro, coordenada)` de la lista de Azara y un registro `(lugar, coordenada, cuadrante)` de la lista de Rui y devuelve `(tesoro, coordenada, lugar, coordenada, cuadrante)` **si las coordenadas coinciden**.
Si las coordenadas _no_ coinciden, devuelve la cadena **"not a match"** (no coincide).
Reformatea la coordenada según sea necesario para una comparación precisa.


```python
>>> create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue'))
('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')

>>> create_record(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue'))
"not a match"
```

## 5. "Limpiar" y hacer un reporte de todos los registros

Limpia los registros combinados de Azara y Rui para que solo haya un conjunto de coordenadas por registro. Haz un reporte para que puedan ver una sola lista de todo lo que necesitan poner en sus mapas.
Implementa la función `clean_up()` que toma una tupla de tuplas (_todo de ambas listas_), iterando a través de la tupla _exterior_, descartando las coordenadas no deseadas de cada tupla _interior_ y añadiendo cada una a un 'reporte'.
Formatea y devuelve el 'reporte' para que haya un registro limpio en cada línea.


```python
>>> clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple')))

"""
('Brass Spyglass', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')\n
('Vintage Pirate Hat', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange')\n
('Crystal Crab', 'Old Schooner', ('6', 'A'), 'Purple')\n
"""
```

## Fuente

### Creado por

- @BethanyG
