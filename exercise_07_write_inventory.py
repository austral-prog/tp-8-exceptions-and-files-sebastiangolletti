# Ejercicio 7 - Escribir un inventario ordenado


def write_inventory(filename, inventory):
    """
    Escribe el inventario ordenado alfabéticamente por item.
    """
    try:
        file = open(filename, "w")
        try:
            keys = list(inventory.keys())
            keys.sort()
            for key in keys:
                file.write(str(key) + ":" + str(inventory[key]) + "\n")
        finally:
            file.close()
    except OSError:
        raise
