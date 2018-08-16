import sys
import os
import datetime
#ruta="./"
#caar=os.listdir(ruta) #saber cuantos archivos ahi en la ruta
#print(caar)

# esto se  usa  para crear  una  nueva carpeta  se  podria pasar una ruta predeterminada 
#casar=os.mkdir("carpeta1") #con  una  variable
#print(casar)
#Eliminar Carpeta
#cason=os.rmdir("carpeta1")
#Cambiar nombre de carpeta
#cambio=os.rename("carpeta1","carpeta2")

#esto  para eliminar archivos
#kamir=os.remove("leer.txt")
#print(kamir)

#casys=os.symlink("./","Enlace")
#print(casys)
#kamir=os.getcwd()
#print(kamir)

#print (time.strftime("%d/%m/%y"))
#os.openpty()





#tamano= os.stat("Villan"+".txt").st_size
#print(tamano+ "bytes") 

#fechamod= os.getgroups() #("casan.txt")
#print(fechamod)




print os.getloadavg()#retorna la cantidad de  procesos en cola de los  ultimos  1,5 a  los ultimos 15 minutos
print os.getuid()
print os.pathsep
print os.getppid()
print os.urandom(50)#Devuelve una cadena de n bytes aleatorios para uso criptograficos 







