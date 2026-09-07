"""Funciones para calcular los pasos en el intercambio de divisas."""


def exchange_money(budget: float, exchange_rate: float) -> float:
    """Calcula el valor estimado en moneda extranjera después del intercambio.

    Parámetros:
        budget (float): La cantidad de dinero que planeas cambiar.
        exchange_rate (float): El tipo de cambio (moneda local por unidad de moneda extranjera).

    Retorna:
        float: El valor en moneda extranjera que recibes.
    """
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """Calcula el dinero restante del presupuesto después de tomar una parte para cambiar.

    Parámetros:
        budget (float): Tu presupuesto total inicial.
        exchanging_value (float): La cantidad que vas a cambiar ahora.

    Retorna:
        float: El dinero que te queda del presupuesto inicial.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Calcula el valor total que representan los billetes recibidos.

    Parámetros:
        denomination (int): El valor de un solo billete.
        number_of_bills (int): La cantidad total de billetes.

    Retorna:
        int: El valor total acumulado de esos billetes.
    """
    return int(denomination * number_of_bills)


def get_number_of_bills(amount: float, denomination: int) -> int:
    """Calcula la cantidad de billetes enteros que se pueden obtener del monto.

    Parámetros:
        amount (float): La cantidad total de dinero a convertir en billetes.
        denomination (int): El valor de un solo billete.

    Retorna:
        int: El número de billetes enteros obtenibles (redondeado hacia abajo).
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount: float, denomination: int) -> float:
    """Calcula el dinero sobrante que no se pudo entregar en billetes.

    Parámetros:
        amount (float): La cantidad total de dinero.
        denomination (int): El valor de un solo billete.

    Retorna:
        float: El dinero sobrante (residuo/módulo).
    """
    return amount % denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    """Calcula el valor máximo canjeable en billetes enteros considerando la comisión (spread).

    Parámetros:
        budget (float): Tu presupuesto en moneda local.
        exchange_rate (float): El tipo de cambio básico.
        spread (int): El porcentaje de comisión de la casa de cambio.
        denomination (int): El valor de un solo billete de la nueva moneda.

    Retorna:
        int: El valor total en la nueva moneda entregado en billetes enteros.
    """
    # 1. Tasa de cambio real incluyendo la comisión (% spread)
    actual_rate = exchange_rate * (1 + spread / 100)
    
    # 2. Monto total convertido en la nueva moneda
    exchanged_amount = budget / actual_rate
    
    # 3. Cantidad de billetes enteros obtenibles
    number_of_bills = int(exchanged_amount // denomination)
    
    # 4. Valor total entregado en billetes enteros
    return number_of_bills * denomination
