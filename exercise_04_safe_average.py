# Ejercicio 4 - Promedio seguro con manejo de errores


def safe_average(filename):
    """
    Lee un archivo con un número por línea y retorna el promedio de los
    números válidos. Ignora líneas vacías o no convertibles a float.
    """
    total = 0.0
    count = 0

    try:
        file = open(filename, "r")
        try:
            for line in file:
                clean_line = line.strip()
                if clean_line != "":
                    try:
                        number = float(clean_line)
                        total += number
                        count += 1
                    except ValueError:
                        pass
        finally:
            file.close()
    except FileNotFoundError:
        raise

    if count == 0:
        raise ValueError("no valid numbers")

    return total / count
