"""Funciones para ayudar a jugar y puntuar una partida de blackjack."""


def value_of_card(card):
    """Determina el valor de una carta.

    Args:
        card (str): La carta ('2'-'10', 'J', 'Q', 'K', 'A').

    Returns:
        int: El valor de la carta.
    """
    if card in ('J', 'Q', 'K'):
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determina qué carta tiene mayor valor.

    Args:
        card_one (str): Primera carta.
        card_two (str): Segunda carta.

    Returns:
        str or tuple: La carta de mayor valor, o ambas si son iguales.
    """
    val1 = value_of_card(card_one)
    val2 = value_of_card(card_two)

    if val1 > val2:
        return card_one
    elif val2 > val1:
        return card_two
    else:
        return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calcula el valor más ventajoso para un as que va a llegar.

    Si la suma de las cartas actuales + 11 no pasa de 21, el as vale 11.
    Si no, el as vale 1.

    Args:
        card_one (str): Primera carta.
        card_two (str): Segunda carta.

    Returns:
        int: 1 o 11.
    """
    if card_one == 'A' or card_two == 'A':
        return 1
    current_sum = value_of_card(card_one) + value_of_card(card_two)
    if current_sum + 11 <= 21:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    """Determina si la mano es un blackjack natural (21 exacto con 2 cartas).

    Args:
        card_one (str): Primera carta.
        card_two (str): Segunda carta.

    Returns:
        bool: True si es blackjack.
    """
    val1 = value_of_card(card_one)
    val2 = value_of_card(card_two)

    # Blackjack: As + carta de valor 10
    if (val1 == 1 and val2 == 10) or (val1 == 10 and val2 == 1):
        return True
    return False


def can_split_pairs(card_one, card_two):
    """Determina si se pueden separ en pares.

    Args:
        card_one (str): Primera carta.
        card_two (str): Segunda carta.

    Returns:
        bool: True si ambas cartas tienen el mismo valor.
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determina si el jugador puede duplicar la apuesta.

    Se puede duplicar si la suma de las cartas es 9, 10 u 11.

    Args:
        card_one (str): Primera carta.
        card_two (str): Segunda carta.

    Returns:
        bool: True si se puede duplicar.
    """
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in (9, 10, 11)
