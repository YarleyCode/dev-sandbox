"""Funciones para ayudar a Azara y Rui a localizar el tesoro pirata."""


from os import truncate
def get_coordinate(record):
    """Devuelve el valor de la coordenada de una tupla que contiene el nombre del tesoro y la coordenada del tesoro.

    Parámetros:
        record (tuple): Un par (tesoro, coordenada).

    Retorna:
        str: La coordenada del mapa extraída.
    """
    return record[1]


def convert_coordinate(coordinate):
    """Divide la coordenada dada en una tupla que contiene sus componentes individuales.

    Parámetros:
        coordinate (str): Una coordenada del mapa en formato string (ej. "2A").

    Retorna:
        tuple: La coordenada string dividida en sus componentes individuales.
    """
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compara dos tipos de registro y determina si sus coordenadas coinciden.

    Parámetros:
        azara_record (tuple): Un par (tesoro, coordenada).
        rui_record (tuple): Un trío (ubicación, tuple(coordenada_1, coordenada_2), cuadrante).

    Retorna:
        bool: ¿Coinciden las coordenadas?
    """

    coordenada_azara = azara_record[1]
    coor1, coor2 = rui_record[1]
    coordenada_rui = coor1 + coor2

    if coordenada_azara == coordenada_rui:
        return True
    else:
        return False


def create_record(azara_record, rui_record):
    """Combina los dos tipos de registro (si es posible) y crea un grupo de registros combinado.

    Parámetros:
        azara_record (tuple): Un par (tesoro, coordenada).
        rui_record (tuple): Un trío (ubicación, coordenada, cuadrante).

    Retorna:
        tuple o str: El registro combinado (si es compatible), o la cadena "not a match" (si es incompatible).
    """
    #si la reutilizacion de la fncio devuelve true o fals, uso directo
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    else:
        return "not a match"


def clean_up(combined_record_group):
    """Limpia un grupo de registros combinados en una cadena multilínea de registros individuales.

    Parámetros:
        combined_record_group (tuple): Todo lo de ambos participantes (tupla de tuplas).

    Retorna:
        str: Todo "limpio", se eliminan las coordenadas e información sobrantes.
    """
    # 1. Inicializamos una variable acumuladora de texto vacía.
    #    Aquí iremos sumando cada renglón del reporte final.
    reporte = ""

    # 2. Recorremos cada registro (tupla individual de 5 elementos) dentro de la tupla principal.
    for record in combined_record_group:
        
        # 3. Creamos la tupla limpia de 4 elementos mediante 'slicing' (rebanado):
        #    - record[:1] toma la posición 0: ('Tesoro',)
        #    - record[2:] toma las posiciones 2 en adelante: ('Lugar', ('Coord1', 'Coord2'), 'Cuadrante')
        #    - Concatenamos (+) ambas tuplas para descartar la posición 1 (coordenada antigua).
        tupla_limpia = record[:1] + record[2:]

        # 4. Convertimos la tupla limpia a string con str(), le agregamos un salto de línea "\n",
        #    y acumulamos ese renglón en nuestra variable 'reporte'.
        reporte += str(tupla_limpia) + "\n"

    # 5. Finalmente retornamos el string multilínea completo con todos los registros procesados.
    return reporte

