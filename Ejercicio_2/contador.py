import sys 

fichero= open('contador.txt','a') #la 'a' es para añadir al final del fichero
fichero.seek(0) #nos posicionamos al principio del fichero
contenido= fichero.read() #leemos el contenido del fichero

if len(contenido)==0:
    contenido='0' #si el fichero esta vacio, le asignamos el valor 0
    fichero.write(contenido) #escribimos el contenido en el fichero