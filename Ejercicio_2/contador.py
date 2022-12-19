import sys 

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


