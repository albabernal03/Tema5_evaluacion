import datetime
import time 
import os

while True:
    os.system('clear') # Limpia la pantalla en este caso al ser mac utilizo el comando clear
    dt= datetime.datetime.now() # Obtenemos la fecha y hora actual
    print('{}:{}:{}'.format(dt.hour,dt.minute,dt.second)) # Imprimimos la hora