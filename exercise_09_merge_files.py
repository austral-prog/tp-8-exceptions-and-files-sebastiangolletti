# Ejercicio 9 - Combinar dos archivos


def merge_files(file1, file2, output):
    """
    Lee file1 y file2 y escribe su concatenación en output.
    Si falta algún archivo de entrada, no crea output.
    """
    content1 = ""
    content2 = ""

    try:
        input_file = open(file1, "r")
        try:
            for line in input_file:
                content1 += line
        finally:
            input_file.close()

        input_file = open(file2, "r")
        try:
            for line in input_file:
                content2 += line
        finally:
            input_file.close()
    except FileNotFoundError:
        raise

    try:
        output_file = open(output, "w")
        try:
            output_file.write(content1)
            output_file.write(content2)
        finally:
            output_file.close()
    except OSError:
        raise
