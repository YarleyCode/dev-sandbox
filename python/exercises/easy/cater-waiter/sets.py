"""Funciones para compilar platos e ingredientes para una empresa de catering."""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Elimina duplicados de los ingredientes.

    Args:
        dish_name (str): Nombre del plato.
        dish_ingredients (list): Ingredientes del plato.

    Returns:
        tuple: (nombre del plato, conjunto de ingredientes sin duplicados).
    """
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    """Agrega 'Cocktail' o 'Mocktail' al nombre según contenga alcohol.

    Args:
        drink_name (str): Nombre de la bebida.
        drink_ingredients (list): Ingredientes de la bebida.

    Returns:
        str: Nombre de la bebida con 'Cocktail' o 'Mocktail'.
    """
    if ALCOHOLS.intersection(set(drink_ingredients)):
        return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    """Categoriza un plato según sus ingredientes.

    Args:
        dish_name (str): El plato a categorizar.
        dish_ingredients (set): Los ingredientes del plato.

    Returns:
        str: Nombre del plato seguido de ": <CATEGORÍA>".
    """
    ingredients = set(dish_ingredients)

    if ingredients.issubset(VEGAN):
        return f"{dish_name}: VEGAN"
    elif ingredients.issubset(VEGETARIAN):
        return f"{dish_name}: VEGETARIAN"
    elif ingredients.issubset(PALEO):
        return f"{dish_name}: PALEO"
    elif ingredients.issubset(KETO):
        return f"{dish_name}: KETO"
    else:
        return f"{dish_name}: OMNIVORE"


def tag_special_ingredients(dish):
    """Compara los ingredientes del plato con SPECIAL_INGREDIENTS.

    Args:
        dish (tuple): (nombre del plato, lista de ingredientes).

    Returns:
        tuple: (nombre del plato, conjunto de ingredientes especiales).
    """
    dish_name, ingredients = dish
    return (dish_name, SPECIAL_INGREDIENTS.intersection(set(ingredients)))


def compile_ingredients(dishes):
    """Crea una lista maestra de ingredientes.

    Args:
        dishes (list): Conjuntos de ingredientes por plato.

    Returns:
        set: Todos los ingredientes combinados.
    """
    all_ingredients = set()
    for dish in dishes:
        all_ingredients.update(dish)
    return all_ingredients


def separate_appetizers(dishes, appetizers):
    """Elimina los appetizers de la lista de platos.

    Args:
        dishes (list): Grupo de nombres de platos.
        appetizers (list): Grupo de nombres de appetizers.

    Returns:
        list: Platos que no están en la lista de appetizers.
    """
    appetizers_set = set(appetizers)
    return [dish for dish in dishes if dish not in appetizers_set]


def singleton_ingredients(dishes, intersection):
    """Encuentra ingredientes singleton (que aparecen en un solo plato).

    Args:
        dishes (list): Grupo de conjuntos de ingredientes.
        intersection (set): Intersección de todos los platos de la categoría.

    Returns:
        set: Ingredientes que solo aparecen en un plato.
    """
    all_ingredients = set()
    ingredient_count = {}

    for dish in dishes:
        for ingredient in dish:
            ingredient_count[ingredient] = ingredient_count.get(ingredient, 0) + 1
            all_ingredients.add(ingredient)

    return {ing for ing in all_ingredients if ingredient_count[ing] == 1}
