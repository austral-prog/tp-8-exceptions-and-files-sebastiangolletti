# Ejercicio 2 - Contar palabras en un archivo


def count_words(filename):
    """
    Lee un archivo y retorna un diccionario palabra -> cantidad.
    El conteo no distingue mayúsculas/minúsculas.
    """
    words_count = {}

    try:
        file = open(filename, "r")
        try:
            for line in file:
                words = line.split()
                for word in words:
                    clean_word = word.lower()
                    if clean_word in words_count:
                        words_count[clean_word] += 1
                    else:
                        words_count[clean_word] = 1
        finally:
            file.close()
    except FileNotFoundError:
        raise

    return words_count
