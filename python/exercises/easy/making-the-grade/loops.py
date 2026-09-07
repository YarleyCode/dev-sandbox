"""Funciones para organizar y calcular calificaciones de exámenes."""


def round_scores(student_scores):
    """Redondea todas las calificaciones al entero más cercano.

    Args:
        student_scores (list[float]): Calificaciones de los estudiantes.

    Returns:
        list[int]: Calificaciones redondeadas.
    """
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    """Cuenta la cantidad de estudiantes reprobados (calificación <= 40).

    Args:
        student_scores (list[int]): Calificaciones como enteros.

    Returns:
        int: La cantidad de estudiantes reprobados.
    """
    return sum(1 for score in student_scores if score <= 40)


def above_threshold(student_scores, threshold):
    """Determina qué calificaciones están por encima o en el umbral dado.

    Args:
        student_scores (list[int]): Calificaciones enteras.
        threshold (int): El umbral a superar.

    Returns:
        list[int]: Las calificaciones que están en o por encima del umbral.
    """
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """Crea una lista de umbrales de calificación basándose en la calificación más alta.

    Args:
        highest (int): El valor de la calificación más alta.

    Returns:
        list[int]: Umbrales inferiores para cada intervalo D-A.

    Ejemplo: Si highest=100, retorna [41, 56, 71, 86]
    """
    failing = 40
    range_size = (highest - failing) // 4
    return [failing + 1, failing + 1 + range_size, failing + 1 + range_size * 2, failing + 1 + range_size * 3]


def student_ranking(student_scores, student_names):
    """Organiza la información de ranking, nombre y calificación en orden descendente.

    Args:
        student_scores (list): Calificaciones en orden descendente.
        student_names (list[str]): Nombres de estudiantes por calificación.

    Returns:
        list[str]: Strings en formato "<rank>. <student name>: <score>".
    """
    return [f"{i+1}. {name}: {score}" for i, (name, score) in enumerate(zip(student_names, student_scores))]


def perfect_score(student_info):
    """Retorna el primer estudiante con calificación perfecta (100).

    Args:
        student_info (list[list[str, int]]): Lista de [nombre, calificación].

    Returns:
        list: El primer [nombre, 100] encontrado, o [] si ninguno tiene 100.
    """
    for name, score in student_info:
        if score == 100:
            return [name, score]
    return []
