# Juego de Arcade: Ghost Gobble (Pac-Man)

¡Bienvenido al ejercicio Ghost Gobble Arcade Game en la ruta de Python de Exercism!

## Introducción

Python representa valores de verdadero y falso con el tipo [`bool`][bools] (booleanos), que es una subclase de `int`.
Solo existen dos valores en este tipo: `True` (Verdadero) y `False` (Falso).

Podemos evaluar expresiones booleanas utilizando los operadores `and` (Y), `or` (O), y `not` (NO / Negación):

```python
>>> verdadero = True and True
>>> falso = True and False

>>> verdadero = False or True
>>> falso = False or False

>>> verdadero = not False
>>> falso = not True
```

[bools]: https://docs.python.org/3/library/stdtypes.html#typebool

---

## Instrucciones

En este ejercicio, debes implementar algunas reglas de **Pac-Man**, el clásico juego de arcade.

Tienes cuatro funciones por implementar relacionadas con los estados del juego:

---

### 1. Definir si Pac-Man se come a un fantasma (`eat_ghost`)

Define la función `eat_ghost()` que recibe dos parámetros:
- `power_pellet_active` (booleano): ¿Pac-Man tiene una superpíldora activa?
- `touching_ghost` (booleano): ¿Pac-Man está tocando a un fantasma?

La función debe retornar `True` **únicamente si** Pac-Man tiene una superpíldora activa **Y** está tocando a un fantasma.

```python
>>> eat_ghost(False, True)
False
```

---

### 2. Definir si Pac-Man suma puntos (`score`)

Define la función `score()` que recibe dos parámetros:
- `touching_power_pellet` (booleano): ¿Pac-Man está tocando una superpíldora?
- `touching_dot` (booleano): ¿Pac-Man está tocando un punto?

La función debe retornar `True` si Pac-Man está tocando una superpíldora **O** un punto.

```python
>>> score(True, True)
True
```

---

### 3. Definir si Pac-Man pierde (`lose`)

Define la función `lose()` que recibe dos parámetros:
- `power_pellet_active` (booleano): ¿Pac-Man tiene una superpíldora activa?
- `touching_ghost` (booleano): ¿Pac-Man está tocando a un fantasma?

La función debe retornar `True` si Pac-Man está tocando a un fantasma **Y NO** tiene una superpíldora activa.

```python
>>> lose(False, True)
True
```

---

### 4. Definir si Pac-Man gana (`win`)

Define la función `win()` que recibe tres parámetros:
- `has_eaten_all_dots` (booleano): ¿Pac-Man se ha comido todos los puntos?
- `power_pellet_active` (booleano): ¿Pac-Man tiene una superpíldora activa?
- `touching_ghost` (booleano): ¿Pac-Man está tocando a un fantasma?

La función debe retornar `True` si Pac-Man se ha comido todos los puntos **Y NO** ha perdido (puedes reutilizar la función `lose()`).

```python
>>> win(False, True, False)
False
```