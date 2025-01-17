"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada word de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    max_min_per_word = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")
            word = columns[0]
            valor = int(columns[1])
            if word in max_min_per_word:
                max_min_per_word[word][0] = max(max_min_per_word[word][0], valor)
                max_min_per_word[word][1] = min(max_min_per_word[word][1], valor)
            else:
                max_min_per_word[word] = [valor, valor]
    resultado = [
    (word, valores[0], valores[1])
    for word, valores in sorted(max_min_per_word.items())
]
    return resultado

print(pregunta_05())