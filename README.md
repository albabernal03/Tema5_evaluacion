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
import sys 

def main():
    
    fichero= open('contador.txt','a+') #la 'a+' es para añadir y leer
    fichero.seek(0) #nos posicionamos al principio del fichero
    contenido= fichero.readline() #leemos el contenido del fichero

    if len(contenido)==0:
        contenido='0' #si el fichero esta vacio, le asignamos el valor 0
        fichero.write(contenido) #escribimos el contenido en el fichero
    fichero.close() #cerramos el fichero
    try:

        contador= int(contenido) #convertimos el contenido a entero
        if len(sys.argv)==2: 
            if sys.argv[1]=='inc':
                contador+=1
            elif sys.argv[1]=='dec':
                contador-=1
        print(contador)
        fichero= open('contador.txt','w') #la 'w' es para sobreescribir el fichero
        fichero.write(str(contador)) #escribimos el contenido en el fichero
        fichero.close() #cerramos el fichero
    except ValueError:
        print('Error: Fichero corrupto')
```
***


## Ejercicio 3:<a name="id3"></a>

En este ejercicio tendremos que hacer uso del módulo pickle. Debemos crear dos clases, la primera Personajes(donde crearemos los personajes) y otra llamada Gestor (encargada de guardarlos, eliminarlos y mostrarlos).

**Código:**

```
from io import open 
import pickle # importamos la libreria pickle que nos permite serializar objetos en ficheros es decir guardarlos en ficheros

class Personaje:

    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

    def __str__(self):
        return '{} => Vida: {} Ataque: {} Defensa: {} Alcance: {}'.format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)

class Gestor:
    personajes= []

    def __init__(self):
        self.cargar() # cargamos los personajes del fichero

    def agregar(self, p): # agregamos un personaje
        for personaje in self.personajes:  # comprobamos que no exista un personaje con el mismo nombre
            if personaje.nombre == p.nombre:
                return 
        self.personajes.append(p)
        self.guardar() # guardamos los personajes en el fichero

    def borrar(self, nombre):
        for personaje in self.personajes: 
            if personaje.nombre == nombre:
                self.personajes.remove(personaje)
                self.guardar()
                print('\nPersonaje {} borrado correctamente'.format(nombre))
                return
        print('\nNo existe el personaje {}'.format(nombre))

    def mostrar(self):
        if len(self.personajes) == 0:
            print('\nNo hay personajes, el fichero esta vacio')
            return
        for p in self.personajes:
            print(p)

    def cargar(self):
        fichero = open('personajes.pckl', 'ab+') # ab+ es para añadir y leer y lo de pickle es para que sepa que es un fichero pickle que se trata de un fichero binario, es decir que no se puede leer con un editor de texto
        fichero.seek(0) # nos posicionamos al principio del fichero
        try:
            self.personajes = pickle.load(fichero) # cargamos los personajes del fichero 
        except:
            print('El fichero esta vacio')
            pass
        finally:
            fichero.close()
            print('Se han cargado {} personajes del fichero'.format(len(self.personajes)))

    def guardar(self):
        fichero = open('personajes.pckl', 'wb')
        pickle.dump(self.personajes, fichero) # guardamos los personajes en el fichero, el .dump es para guardar 
        fichero.close()
```
***


## Ejercicio 4:<a name="id4"></a>

En este ejercicio se nos pide crear un reloj que muestre la hora minutos y segundos actuales.

**Código:**

```
import datetime
import time 
import os

def main():
    while True:
        os.system('clear') # Limpiamos la pantalla con el comando clear pues estamos en linux
        dt= datetime.datetime.now() # Obtenemos la fecha y hora actual
        print('{}:{}:{}'.format(dt.hour,dt.minute,dt.second)) # Imprimimos la hora
        time.sleep(1) # Esperamos 1 segundo
```


