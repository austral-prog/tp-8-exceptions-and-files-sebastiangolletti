# Ejercicio 10 - Parser de archivos de log


def parse_log(filename):
    """
    Lee un log con líneas NIVEL: mensaje y agrupa los mensajes por nivel.
    """
    logs = {}

    try:
        file = open(filename, "r")
        try:
            for line in file:
                clean_line = line.strip()
                if clean_line != "":
                    if ":" not in clean_line:
                        raise ValueError("invalid log line")

                    parts = clean_line.split(":", 1)
                    level = parts[0].strip()
                    message = parts[1].strip()

                    if level not in logs:
                        logs[level] = []
                    logs[level].append(message)
        finally:
            file.close()
    except FileNotFoundError:
        raise

    return logs
