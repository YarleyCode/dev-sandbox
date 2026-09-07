"""Funciones para editar tareas usando manipulación de strings."""


def capitalize_title(title):
    """Convierte la primera letra de cada palabra del título a mayúscula.

    Args:
        title (str): El título del ensayo.

    Returns:
        str: El título con cada palabra en title case.
    """
    return title.title()


def check_sentence_ending(sentence):
    """Verifica si la oración termina con un punto.

    Args:
        sentence (str): La oración a verificar.

    Returns:
        bool: True si termina con punto.
    """
    return sentence.endswith('.')


def clean_up_spacing(sentence):
    """Elimina espacios en blanco al inicio y final de la oración.

    Args:
        sentence (str): La oración a limpiar.

    Returns:
        str: La oración sin espacios extra.
    """
    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    """Reemplaza una palabra por otra en la oración.

    Args:
        sentence (str): La oración original.
        old_word (str): La palabra a reemplazar.
        new_word (str): La palabra nueva.

    Returns:
        str: La oración con la palabra reemplazada.
    """
    return sentence.replace(old_word, new_word)
