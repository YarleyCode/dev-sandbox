"""
GESTOR DE COMPRA DE MECHA MUNCH
===============================
Funciones para gestionar el carrito de compras de un usuario,
recetas, y la información de la tienda (pasillos, inventario).

Temas clave: Diccionarios, métodos de diccionarios (.get(), .update(), .items()),
             comprensión de diccionarios, OrderedDict.
"""


def add_item(current_cart, items_to_add):
    """
    Agrega items al carrito de compras.

    Si el item ya existe en el carrito, incrementa su cantidad en 1 por cada
    vez que aparece en items_to_add. Si no existe, lo agrega con cantidad 1.

    Parámetros:
        current_cart (dict): Diccionario del carrito actual donde las claves
                             son nombres de productos (str) y los valores son
                             cantidades (int).
        items_to_add (iterable): Iterable (tupla, lista, etc.) con los nombres
                                 de los items a agregar al carrito.

    Retorna:
        dict: El diccionario del carrito actualizado con los nuevos items.

    Ejemplo:
        >>> add_item({"Manzana": 1}, ("Manzana", "Plátano"))
        {"Manzana": 2, "Plátano": 1}
    """
    for item in items_to_add:
        # Si el item ya está en el carrito, sumar 1 a su cantidad
        if item in current_cart:
            current_cart[item] += 1
        # Si no está, agregarlo con cantidad 1
        else:
            current_cart[item] = 1
    return current_cart


def read_notes(notes):
    """
    Crea un carrito de compras a partir de un iterable de notas.

    Cada item del iterable se convierte en una entrada del diccionario
    con valor 1. Si un item aparece múltiples veces, se cuenta como
    un solo item con valor 1 (porque es un set de notas).

    Parámetros:
        notes (iterable): Iterable (tupla, lista, etc.) con los nombres
                          de los productos anotados por el usuario.

    Retorna:
        dict: Un diccionario donde cada clave es un nombre de producto
              y cada valor es 1.

    Ejemplo:
        >>> read_notes(("Manzana", "Plátano", "Manzana"))
        {"Manzana": 1, "Plátano": 1}
    """
    # Crear un diccionario vacío para el carrito
    cart = {}
    # Por cada item en las notas, asignarle valor 1
    # .setdefault() busca la clave; si no existe, la crea con el valor dado
    for item in notes:
        cart[item] = 1
    return cart


def update_recipes(ideas, recipe_updates):
    """
    Actualiza el diccionario de ideas de recetas.

    Si la receta ya existe en ideas, se reemplazan sus ingredientes
    completamente con los nuevos. Si la receta no existe, se agrega
    como una nueva entrada.

    Parámetros:
        ideas (dict): Diccionario de recetas existentes. Cada clave es el
                      nombre de la receta (str) y cada valor es un diccionario
                      de ingredientes {ingrediente: cantidad}.
        recipe_updates (iterable): Iterable de tuplas con formato
                                   (nombre_receta, {ingrediente: cantidad}).

    Retorna:
        dict: El diccionario de ideas actualizado con los cambios.

    Ejemplo:
        >>> ideas = {"Tarta": {"Harina": 1, "Huevos": 2}}
        >>> updates = [("Tarta", {"Harina": 2, "Mantequilla": 1})]
        >>> update_recipes(ideas, updates)
        {"Tarta": {"Harina": 2, "Mantequilla": 1}}
    """
    # Recorrer cada tupla de actualización (nombre_receta, ingredientes)
    for recipe_name, ingredients in recipe_updates:
        # .update() reemplaza completamente el valor de la clave existente
        # o crea una nueva entrada si la clave no existe
        ideas[recipe_name] = ingredients
    return ideas


def sort_entries(cart):
    """
    Ordena el carrito de compras en orden alfabético por nombre de item.

    Parámetros:
        cart (dict): Diccionario del carrito donde las claves son nombres
                     de productos (str) y los valores son cantidades (int).

    Retorna:
        dict: Un nuevo diccionario ordenado alfabéticamente por claves.

    Ejemplo:
        >>> sort_entries({"Plátano": 4, "Manzana": 2, "Naranja": 1})
        {"Manzana": 2, "Naranja": 1, "Plátano": 4}
    """
    # sorted() retorna una lista de claves ordenadas alfabéticamente
    # Luego creamos un diccionario nuevo usando comprensión de diccionario
    return {key: cart[key] for key in sorted(cart)}


def send_to_store(cart, aisle_mapping):
    """
    Combina el carrito del usuario con la información de pasillos y refrigeración.

    Crea un diccionario de cumplimiento (fulfillment) donde cada item tiene
    su cantidad, número de pasillo y si requiere refrigeración.

    Parámetros:
        cart (dict): Diccionario del carrito del usuario {producto: cantidad}.
        aisle_mapping (dict): Diccionario de mapeo de pasillos donde cada
                              entrada es {producto: [pasillo, bool_refrigeración]}.

    Retorna:
        dict: Diccionario de cumplimiento listo para enviar a la tienda.
              Formato: {producto: [cantidad, pasillo, refrigeración]}.

    Ejemplo:
        >>> cart = {"Leche": 2, "Pan": 3}
        >>> mapping = {"Leche": ["Pasillo 2", True], "Pan": ["Pasillo 5", False]}
        >>> send_to_store(cart, mapping)
        {"Leche": [2, "Pasillo 2", True], "Pan": [3, "Pasillo 5", False]}
    """
    fulfillment = {}
    # Recorrer el aisle_mapping en orden inverso, incluyendo solo items del carrito
    # reversed() invierte el orden de las claves del diccionario
    for product in reversed(list(aisle_mapping.keys())):
        # Solo incluir si el producto está en el carrito
        if product in cart:
            quantity = cart[product]
            aisle_info = aisle_mapping[product]
            fulfillment[product] = [quantity, aisle_info[0], aisle_info[1]]
    return fulfillment


def update_store_inventory(fulfillment_cart, store_inventory):
    """
    Actualiza el inventario de la tienda restando lo que el usuario pidió.

    Para cada item en el carrito de cumplimiento, se resta la cantidad
    solicitada del inventario. Si la cantidad llega a 0 o menos, se marca
    como "Out of Stock" (agotado).

    Parámetros:
        fulfillment_cart (dict): Carrito de cumplimiento con formato
                                 {producto: [cantidad, pasillo, refrigeración]}.
        store_inventory (dict): Inventario de la tienda con formato
                                {producto: [cantidad, pasillo, refrigeración]}.

    Retorna:
        dict: El inventario de la tienda actualizado.

    Ejemplo:
        >>> fulfillment = {"Manzana": [3, "Pasillo 1", False]}
        >>> inventory = {"Manzana": [10, "Pasillo 1", False]}
        >>> update_store_inventory(fulfillment, inventory)
        {"Manzana": [7, "Pasillo 1", False]}
    """
    # Recorrer cada item del carrito de cumplimiento
    for product, fulfillment_info in fulfillment_cart.items():
        # Cantidad solicitada por el usuario (primer elemento de la lista)
        requested_qty = fulfillment_info[0]

        # Verificar si el producto existe en el inventario
        if product in store_inventory:
            # Cantidad actual en inventario (primer elemento de la lista)
            current_qty = store_inventory[product][0]

            # Calcular la nueva cantidad después de restar lo solicitado
            new_qty = current_qty - requested_qty

            # Si la nueva cantidad es 0 o menor, marcar como agotado
            if new_qty <= 0:
                store_inventory[product][0] = "Out of Stock"
            else:
                # Si hay suficiente stock, actualizar la cantidad
                store_inventory[product][0] = new_qty
    return store_inventory
