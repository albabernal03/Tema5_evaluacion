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
        