from gestor import *

if __name__ == '__main__':
    G= Gestor()
    G.agregar(Personaje('Caballero',4,2,4,2))
    G.agregar(Personaje('Arquero',2,4,1,8))
    G.agregar(Personaje('Guerrero',2,4,2,4))
    G.mostrar()
    
