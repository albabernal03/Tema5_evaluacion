<h1 align="center">Evaluación Tema 5</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/Tema5_evaluacion)

***
<h2>¿De qué trata esta tarea?</h2>
En esta tarea se nos pide realizar 4 ejercicios distintos.

***
## Indice

1. [Ejercicio 1](#id1)
2. [Ejercicio 2](#id2)
3. [Ejercico 3](#id3)
4. [Ejercicio 4](#id4)

***

## Ejercicio 1:<a name="id1"></a>

En este ejercicio se nos pide crear un módulo llamado operaciones.py; donde encontamos 4 funciones (sumar,restar,producto y división). Si estas fallan mostrar un error por pantalla.

**Código:**
```

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
```
***

## Ejercicio 2:<a name="id2"></a>

En este ejercicio nos piden crear un script llamado contador.py que realice varias tareas sobre un fichero llamado contador.txt que almacenará un contador de visitas.

- Si el fichero no existe o está vacío lo crearemos con el número 0
-    Luego a partir de un argumento:

·        Si se envía el argumento inc, se incrementará el contador en uno y se mostrará por pantalla.

·        Si se envía el argumento dec, se decrementará el contador en uno y se mostrará por pantalla.

·        Si no se envía ningún argumento (o algo que no sea inc o dec), se mostrará el valor del contador por pantalla.

·        Finalmente guardará de nuevo el valor del contador de nuevo en el fichero.

·        Utiliza excepciones si crees que es necesario, puedes mostrar el mensaje: Error: Fichero corrupto.

**Código:**
```
```
