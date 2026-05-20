# Ejercicio 1 - Leer líneas de un archivo


def read_lines(filename):
    """
    Lee un archivo de texto y retorna una lista con sus líneas no vacías,
    sin saltos de línea ni espacios al principio/final.
    """
    lines = []

    try:
        file = open(filename, "r")
        try:
            for line in file:
                clean_line = line.strip()
                if clean_line != "":
                    lines.append(clean_line)
        finally:
            file.close()
    except FileNotFoundError:
        raise

    return lines
