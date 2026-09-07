"""Funciones para gestionar colas en la montaña rusa de Chaitana."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Agrega una persona a la cola express o normal según el tipo de ticket.

    Args:
        express_queue (list): Cola express.
        normal_queue (list): Cola normal.
        ticket_type (int): 1 = express, 0 = normal.
        person_name (str): Nombre de la persona.

    Returns:
        list: La cola actualizada.
    """
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    else:
        normal_queue.append(person_name)
        return normal_queue


def find_my_friend(queue, friend_name):
    """Busca un nombre en la cola y retorna su posición (índice).

    Args:
        queue (list): La cola de nombres.
        friend_name (str): Nombre a buscar.

    Returns:
        int: El índice donde se encontró el nombre.
    """
    return queue.index(friend_name)


def add_me_with_my_friends(queue, index, person_name):
    """Inserta el nombre de una persona en un índice específico de la cola.

    Args:
        queue (list): La cola de nombres.
        index (int): El índice donde insertar.
        person_name (str): Nombre a agregar.

    Returns:
        list: La cola actualizada.
    """
    queue.insert(index, person_name)
    return queue


def remove_the_mean_person(queue, person_name):
    """Elimina una persona de la cola por su nombre.

    Args:
        queue (list): La cola de nombres.
        person_name (str): Nombre a eliminar.

    Returns:
        list: La cola actualizada.
    """
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue, person_name):
    """Cuenta cuántas veces aparece un nombre en la cola.

    Args:
        queue (list): La cola de nombres.
        person_name (str): Nombre a contar.

    Returns:
        int: El número de veces que aparece el nombre.
    """
    return queue.count(person_name)


def remove_the_last_person(queue):
    """Elimina y retorna la persona en el último índice de la cola.

    Args:
        queue (list): La cola de nombres.

    Returns:
        str: El nombre eliminado.
    """
    return queue.pop()


def sorted_names(queue):
    """Ordena los nombres de la cola en orden alfabético.

    Args:
        queue (list): La cola de nombres.

    Returns:
        list: Una copia de la cola ordenada alfabéticamente.
    """
    return sorted(queue)
