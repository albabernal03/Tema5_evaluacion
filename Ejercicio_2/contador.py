import sys 

fichero= open('contador.txt','a') #la 'a' es para añadir al final del fichero
fichero.seek(0) #nos posicionamos al principio del fichero
contenido= fichero.read() #leemos el contenido del fichero