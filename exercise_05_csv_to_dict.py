# Ejercicio 5 - CSV a lista de diccionarios


def csv_to_dict(filename):
    """
    Lee un CSV simple con header name,age,city y retorna una lista de
    diccionarios. No usa el módulo csv.
    """
    result = []
    header = None

    try:
        file = open(filename, "r")
        try:
            for line in file:
                clean_line = line.strip()
                if header is None:
                    if clean_line != "":
                        header = clean_line.split(",")
                        i = 0
                        while i < len(header):
                            header[i] = header[i].strip()
                            i += 1
                else:
                    if clean_line != "":
                        values = clean_line.split(",")
                        i = 0
                        while i < len(values):
                            values[i] = values[i].strip()
                            i += 1

                        row = {}
                        i = 0
                        while i < len(header):
                            key = header[i]
                            value = values[i]
                            if key == "age":
                                row[key] = int(value)
                            else:
                                row[key] = value
                            i += 1
                        result.append(row)
        finally:
            file.close()
    except FileNotFoundError:
        raise

    return result
