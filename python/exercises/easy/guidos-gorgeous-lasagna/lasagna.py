"""Módulo lasagna - Funciones para calcular tiempos de cocción de una lasaña.

Este módulo contiene constantes y funciones de utilidad para el ejercicio
'Guido's Gorgeous Lasagna' de Exercism. Permite calcular el tiempo restante
de horneado, el tiempo de preparación según capas y el tiempo total transcurrido.
"""

# TAREA 1: Constantes
EXPECTED_BAKE_TIME = 40
"""int: Tiempo esperado de horneado de la lasaña en minutos."""

PREPARATION_TIME = 2
"""int: Tiempo de preparación por capa de lasaña en minutos."""


# TAREA 2: Calcular el tiempo restante de horneado
def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calcula el tiempo restante de horneado de la lasaña.

    Resta el tiempo ya transcurrido en el horno al tiempo total esperado
    (EXPECTED_BAKE_TIME).

    Args:
        elapsed_bake_time: Minutos que la lasaña lleva en el horno.

    Returns:
        Minutos restantes para que la lasaña termine de hornearse.

    Example:
        >>> bake_time_remaining(30)
        10
    """
    time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return time_remaining


# TAREA 3: Calcular el tiempo de preparación en minutos
def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calcula el tiempo de preparación según el número de capas.

    Cada capa toma PREPARATION_TIME (2) minutos en prepararse.

    Args:
        number_of_layers: Número de capas añadidas a la lasaña.

    Returns:
        Tiempo total de preparación en minutos.

    Example:
        >>> preparation_time_in_minutes(2)
        4
    """
    time = PREPARATION_TIME * number_of_layers
    return time


# TAREA 4: Calcular el tiempo total transcurrido (preparación + horneado)
def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calcula el tiempo total transcurrido de elaboración.

    Suma el tiempo de preparación (según capas) más el tiempo que
    la lasaña lleva en el horno.

    Args:
        number_of_layers: Número de capas de la lasaña.
        elapsed_bake_time: Minutos que la lasaña lleva horneándose.

    Returns:
        Tiempo total transcurrido en minutos (preparación + horneado).

    Example:
        >>> elapsed_time_in_minutes(3, 20)
        26
    """
    time_layers = preparation_time_in_minutes(number_of_layers)
    total_time = time_layers + elapsed_bake_time
    return total_time

def total_calories(number_of_layers: int):
    return number_of_layers * 150

    