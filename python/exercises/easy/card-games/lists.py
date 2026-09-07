"""Funciones para gestionar manos de póker y tareas de cartas."""


def get_rounds(number):
    """Crea una lista con el número de ronda actual y las dos siguientes.

    Args:
        number (int): Número de ronda actual.

    Returns:
        list: [number, number+1, number+2]
    """
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatena dos listas de rondas.

    Args:
        rounds_1 (list): Primera lista de rondas.
        rounds_2 (list): Segunda lista de rondas.

    Returns:
        list: Todas las rondas combinadas.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Verifica si una lista de rondas contiene un número específico.

    Args:
        rounds (list): Las rondas jugadas.
        number (int): El número de ronda a buscar.

    Returns:
        bool: True si la ronda está en la lista.
    """
    return number in rounds


def card_average(hand):
    """Calcula el valor promedio de las cartas en la mano.

    Args:
        hand (list): Lista de valores de cartas.

    Returns:
        float: El promedio de las cartas.
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Verifica si el promedio aproximado (primera + última carta) o la carta del medio
    son iguales al promedio real.

    Args:
        hand (list): Lista de valores de cartas.

    Returns:
        bool: True si alguno de los promedios aproximados coincide con el real.
    """
    real_average = card_average(hand)
    approx_avg = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]

    return approx_avg == real_average or middle_card == real_average


def average_even_is_average_odd(hand):
    """Verifica si el promedio de las cartas en posiciones pares es igual
    al promedio de las cartas en posiciones impares.

    Args:
        hand (list): Lista de valores de cartas.

    Returns:
        bool: True si ambos promedios son iguales.
    """
    even_cards = [hand[i] for i in range(0, len(hand), 2)]
    odd_cards = [hand[i] for i in range(1, len(hand), 2)]

    if not even_cards or not odd_cards:
        return False

    return sum(even_cards) / len(even_cards) == sum(odd_cards) / len(odd_cards)


def maybe_double_last(hand):
    """Si la última carta es un J (valor 11), duplica su valor.

    Args:
        hand (list): Lista de valores de cartas.

    Returns:
        list: La mano con el último valor duplicado si era J.
    """
    if hand[-1] == 11:
        hand[-1] = 22
    return hand
