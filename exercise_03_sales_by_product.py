# Ejercicio 3 - Ventas por producto


def read_sales(filename):
    """
    Lee ventas en formato producto:valor;producto:valor;...
    y agrupa los valores en una lista por producto.
    """
    sales = {}

    try:
        file = open(filename, "r")
        try:
            for line in file:
                records = line.strip().split(";")
                for record in records:
                    clean_record = record.strip()
                    if clean_record != "":
                        parts = clean_record.split(":")
                        product = parts[0].strip()
                        value = float(parts[1].strip())
                        if product not in sales:
                            sales[product] = []
                        sales[product].append(value)
        finally:
            file.close()
    except FileNotFoundError:
        raise

    return sales


def process_sales(data):
    """
    Imprime total y promedio de ventas por producto.
    """
    for product in data:
        total = 0.0
        count = 0
        for value in data[product]:
            total += value
            count += 1
        average = total / count
        print(f"{product}: ventas totales ${total:.2f}, promedio ${average:.2f}")
