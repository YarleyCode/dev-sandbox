# Intercambio de Divisas (Currency Exchange)

¡Bienvenido al ejercicio de Intercambio de Divisas en la ruta de Python de Exercism!

## Introducción: Números y Operaciones Aritméticas

En Python existen dos tipos principales de números con los que trabajaremos en este ejercicio:
- **`int` (enteros):** Números sin decimales (ej. `1234`, `-10`, `5`).
- **`float` (decimales):** Números con punto decimal (ej. `3.14`, `12.5`, `0.0`).

### Operaciones clave en Python:
1. **División normal (`/`):** Siempre devuelve un `float` (ej. `6 / 2` es `3.0`).
2. **División entera / Truncada (`//`):** Redondea hacia abajo y devuelve un número entero sin los decimales (ej. `7 // 4` es `1`).
3. **Módulo / Residuo (`%`):** Devuelve el sobrante o residuo de una división (ej. `7 % 4` es `3`).
4. **Conversiones:** `int(3.8)` convierte a `3` (entero), y `float(5)` convierte a `5.0`.

---

## Instrucciones del Ejercicio

Tu amigo Chandler va a viajar por el mundo y quiere una calculadora para que no lo estafen en las casas de cambio. Debes implementar 6 funciones:

---

### 1. Estimar el valor después del intercambio (`exchange_money`)
Calcula cuánto dinero extranjero recibes al cambiar tu presupuesto.
- `budget`: Dinero que vas a cambiar.
- `exchange_rate`: Tipo de cambio (cuánta moneda local equivale a 1 unidad extranjera).

**Fórmula:** `budget / exchange_rate`

```python
>>> exchange_money(127.5, 1.2)
106.25
```

---

### 2. Calcular el cambio restante (`get_change`)
Calcula cuánto dinero te queda del presupuesto inicial después de tomar una parte para cambiar.
- `budget`: Presupuesto total inicial.
- `exchanging_value`: Cantidad de dinero que retiras para hacer el cambio.

**Fórmula:** `budget - exchanging_value`

```python
>>> get_change(127.5, 120)
7.5
```

---

### 3. Calcular el valor total de los billetes (`get_value_of_bills`)
Calcula el valor total que representan cierta cantidad de billetes de una misma denominación.
- `denomination`: El valor de un solo billete (ej. 5, 10, 20).
- `number_of_bills`: La cantidad total de billetes.

**Fórmula:** `int(denomination * number_of_bills)`

```python
>>> get_value_of_bills(5, 128)
640
```

---

### 4. Calcular la cantidad de billetes enteros (`get_number_of_bills`)
Calcula cuántos billetes enteros caben en una cantidad de dinero (redondeando hacia abajo).
- `amount`: Cantidad total de dinero.
- `denomination`: Valor del billete.

**Fórmula:** `int(amount // denomination)`

```python
>>> get_number_of_bills(127.5, 5)
25
```

---

### 5. Calcular el sobrante tras entregar billetes (`get_leftover_of_bills`)
Calcula la fracción de dinero que queda libre al repartir una cantidad en billetes de cierta denominación.
- `amount`: Cantidad inicial.
- `denomination`: Valor del billete.

**Fórmula:** `amount % denomination`

```python
>>> get_leftover_of_bills(127.5, 20)
7.5
```

---

### 6. Calcular el valor máximo canjeable con comisión (`exchangeable_value`)
Calcula el valor máximo en la nueva moneda que puedes recibir en billetes enteros, teniendo en cuenta la comisión (*spread*).
- `spread`: Porcentaje de comisión de la casa de cambio (ej. `10` significa `10%`).
- La tasa de cambio real con comisión es: `exchange_rate * (1 + spread / 100)`.
- Primero obtienes el dinero total convertido: `budget / tasa_con_comisión`.
- Luego calculas cuántos billetes enteros de la denominación caben (`// denomination`), y finalmente el valor total en billetes (`* denomination`).

```python
>>> exchangeable_value(127.25, 1.20, 10, 20)
80
```