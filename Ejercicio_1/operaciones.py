def suma(a, b):
    try:
        a = int(a) or float(a)
        b = int(b) or float(b)
        return a + b
    except ValueError: 
        print("Error: Solo se permiten numeros")


def resta(a, b):
    try:
        a = int(a) or float(a)
        b = int(b) or float(b)
        return a - b
    except ValueError:
        print("Error: Solo se permiten numeros")

def producto(a, b):
    try:
        a = int(a) or float(a)
        b = int(b) or float(b)
        return a * b
    except ValueError:
        print("Error: Solo se permiten numeros")


def division(a, b):
    try:
        a = int(a) or float(a)
        b = int(b) or float(b) and b != 0
        return a / b
    except ValueError:
        print("Error: Solo se permiten numeros")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero")

        

