import datetime
import time 
import os

def main():
    while True:
        os.system('clear') # Limpiamos la pantalla con el comando clear pues estamos en linux
        dt= datetime.datetime.now() # Obtenemos la fecha y hora actual
        print('{}:{}:{}'.format(dt.hour,dt.minute,dt.second)) # Imprimimos la hora
        time.sleep(1) # Esperamos 1 segundo


