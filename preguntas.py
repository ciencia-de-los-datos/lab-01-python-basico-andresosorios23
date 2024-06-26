"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

data = open("data.csv", "r").readlines()
lines = [row.split("\t") for row in data]


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    second_column = [int(line[1]) for line in lines]

    return sum(second_column)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    registers_per_letter = {}
    for line in lines:
        if line[0] in registers_per_letter:
            registers_per_letter[line[0]] += 1
        else:
            registers_per_letter[line[0]] = 1
    return sorted(list(registers_per_letter.items()))


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    registers_per_letter = {}
    for line in lines:
        if line[0] in registers_per_letter:
            registers_per_letter[line[0]] += int(line[1])
        else:
            registers_per_letter[line[0]] = int(line[1])
    return sorted(list(registers_per_letter.items()))


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    months = [line[2].split("-")[1] for line in lines]
    registers_per_month = {}
    for month in months:
        if month in registers_per_month:
            registers_per_month[month] += 1
        else:
            registers_per_month[month] = 1
    return sorted(list(registers_per_month.items()))


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    registers_per_letter = {}
    for line in lines:
        if line[0] in registers_per_letter:
            if int(line[1]) > registers_per_letter[line[0]][1]:
                registers_per_letter[line[0]][1] = int(line[1])
            if int(line[1]) < registers_per_letter[line[0]][2]:
                registers_per_letter[line[0]][2] = int(line[1])
        else:
            registers_per_letter[line[0]] = [line[0], int(line[1]), int(line[1])]
    return [tuple(x[1]) for x in sorted(list(registers_per_letter.items()))]


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    registers_per_key = {}
    for line in lines:
        keys = line[4].replace("\n", "").split(",")
        for key in keys:
            if key[:3] in registers_per_key:
                if int(key[4:]) > registers_per_key[key[:3]][1]:
                    registers_per_key[key[:3]][1] = int(key[4:])
                if int(key[4:]) < registers_per_key[key[:3]][0]:
                    registers_per_key[key[:3]][0] = int(key[4:])
            else:
                registers_per_key[key[:3]] = [int(key[4:]), int(key[4:])]
    return [(x[0], x[1][0], x[1][1]) for x in list(sorted(registers_per_key.items()))]


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    letters_per_number: dict[int, list[str]] = {}
    for line in lines:
        if int(line[1]) in letters_per_number:
            letters_per_number[int(line[1])].append(line[0])
        else:
            letters_per_number[int(line[1])] = [line[0]]
    return list(sorted(letters_per_number.items()))


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    letters_per_number: dict[int, list[str]] = {}
    for line in lines:
        if int(line[1]) in letters_per_number:
            letters_per_number[int(line[1])].append(line[0])
        else:
            letters_per_number[int(line[1])] = [line[0]]
    for key in letters_per_number:
        letters_per_number[key] = sorted(list(set(letters_per_number[key])))
    return list(sorted(letters_per_number.items()))


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    registers_per_key = {}
    for line in lines:
        keys = line[4].replace("\n", "").split(",")
        for key in keys:
            if key[:3] in registers_per_key:
                registers_per_key[key[:3]] += 1
            else:
                registers_per_key[key[:3]] = 1
    return dict(sorted(registers_per_key.items()))


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return [
        (line[0], len(line[3].split(",")), len(line[4].split(","))) for line in lines
    ]


def pregunta_11() -> dict[str, int]:
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    result: dict[str, int] = {
        letter: sum([int(line[1]) for line in lines if letter in line[3]])
        for letter in "abcdefg"
    }
    return result


def pregunta_12() -> dict[str, int]:
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    result: dict[str, int] = {}
    for line in lines:
        if line[0] in result:
            result[line[0]] += sum([int(x[4:]) for x in line[4].split(",")])
        else:
            result[line[0]] = sum([int(x[4:]) for x in line[4].split(",")])
    return result
