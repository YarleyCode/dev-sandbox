"""Funciones para crear, transformar y agregar prefijos a strings."""


def add_prefix_un(word):
    """Agrega el prefijo 'un' a una palabra.

    Args:
        word (str): La palabra raíz.

    Returns:
        str: La palabra con el prefijo 'un'.
    """
    return 'un' + word


def make_word_groups(vocab_words):
    """Transforma una lista con prefijo y palabras, aplicando el prefijo a cada una.

    Args:
        vocab_words (list[str]): Lista donde el primer elemento es el prefijo.

    Returns:
        str: Prefijo seguido de las palabras con prefijo aplicado, separados por ' :: '.
    """
    prefix = vocab_words[0]
    words_with_prefix = [prefix + word for word in vocab_words[1:]]
    return ' :: '.join([prefix] + words_with_prefix)


def remove_suffix_ness(word):
    """Elimina el sufijo 'ness' de una palabra y ajusta la ortografía.

    Si la palabra termina en 'iness', se convierte en 'y' (ej: heaviness -> heavy).
    Si termina en 'ness' directamente, solo se elimina el sufijo.

    Args:
        word (str): La palabra con sufijo 'ness'.

    Returns:
        str: La palabra sin el sufijo.
    """
    if word.endswith('iness'):
        return word[:-5] + 'y'
    return word[:-4]


def adjective_to_verb(sentence, index):
    """Extrae un adjetivo de la oración y lo convierte en verbo agregando 'en'.

    Args:
        sentence (str): La oración que contiene el adjetivo.
        index (int): El índice del adjetivo en la oración.

    Returns:
        str: El adjetivo transformado en verbo (con 'en' al final).
    """
    words = sentence.split()
    return words[index] + 'en'
