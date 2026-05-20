# Ejercicio 6 - Estadísticas de notas por estudiante


def grades_stats(filename):
    """
    Lee líneas estudiante:nota1,nota2,... y retorna promedio, máximo y mínimo
    por estudiante en una tupla de floats.
    """
    stats = {}

    try:
        file = open(filename, "r")
        try:
            for line in file:
                clean_line = line.strip()
                if clean_line != "":
                    parts = clean_line.split(":")
                    student = parts[0].strip()
                    grades_text = parts[1].split(",")

                    total = 0.0
                    count = 0
                    maximum = None
                    minimum = None

                    for grade_text in grades_text:
                        grade = float(grade_text.strip())
                        total += grade
                        count += 1
                        if maximum is None or grade > maximum:
                            maximum = grade
                        if minimum is None or grade < minimum:
                            minimum = grade

                    average = total / count
                    stats[student] = (average, maximum, minimum)
        finally:
            file.close()
    except FileNotFoundError:
        raise

    return stats
