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

            

    

    




