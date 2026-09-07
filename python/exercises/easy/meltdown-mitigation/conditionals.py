"""Funciones para prevenir un meltdown nuclear."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verifica si la criticalidad está balanceada.

    Un reactor está en criticalidad balanceada si cumple las 3 condiciones:
        - Temperatura menor a 800 K.
        - Neutrones emitidos por segundo mayor a 500.
        - El producto de temperatura * neutrones menor a 500000.

    Args:
        temperature (int or float): Temperatura en kelvin.
        neutrons_emitted (int or float): Neutrones emitidos por segundo.

    Returns:
        bool: True si está balanceada, False si no.
    """
    return temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Determina la banda de eficiencia del reactor.

    La eficiencia se calcula como (voltage * current / theoretical_max_power) * 100.
    Bandas:
        - green: 80% o más
        - orange: menos de 80% pero al menos 60%
        - red: menos de 60% pero al menos 30%
        - black: menos de 30%

    Args:
        voltage (int or float): Voltaje.
        current (int or float): Corriente.
        theoretical_max_power (int or float): Potencia máxima teórica (100%).

    Returns:
        str: Una de ('green', 'orange', 'red', 'black').
    """
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60:
        return 'orange'
    elif efficiency >= 30:
        return 'red'
    else:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Evalúa el estado del reactor y retorna un código de estado.

    Categorías según el producto temperatura * neutrones vs el threshold:
        - 'LOW':    el producto es menor al 90% del threshold (faltan varillas de control).
        - 'NORMAL': el producto está dentro del rango +/- 10% del threshold (óptimo).
        - 'DANGER': el producto está fuera de los rangos anteriores (meltdown inminente).

    Args:
        temperature (int or float): Temperatura en kelvin.
        neutrons_produced_per_second (int or float): Flujo de neutrones.
        threshold (int or float): Umbral de referencia.

    Returns:
        str: Una de ('LOW', 'NORMAL', 'DANGER').
    """
    reactor_value = temperature * neutrons_produced_per_second
    lower_bound = threshold * 0.9
    upper_bound = threshold * 1.1

    if reactor_value < lower_bound:
        return 'LOW'
    elif lower_bound <= reactor_value <= upper_bound:
        return 'NORMAL'
    else:
        return 'DANGER'
