# Ejercicio 8 - Palabra más larga de un archivo


def find_longest_word(filename):
    """
    Lee un archivo y retorna la primera palabra de mayor longitud.
    """
    longest = None

    try:
        file = open(filename, "r")
        try:
            for line in file:
                words = line.split()
                for word in words:
                    if longest is None or len(word) > len(longest):
                        longest = word
        finally:
            file.close()
    except FileNotFoundError:
        raise

    if longest is None:
        raise ValueError("file has no words")

    return longest
