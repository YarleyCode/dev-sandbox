def leap_year(year):
    """Determina si un año es bisiesto.

    Un año es bisiesto si:
        - Es divisible entre 4
        - PERO NO divisible entre 100, a menos que también sea divisible entre 400

    Args:
        year (int): El año a evaluar.

    Returns:
        bool: True si es bisiesto.
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
