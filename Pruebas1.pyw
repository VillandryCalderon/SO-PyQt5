#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
import os
import time
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import uic


class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("Ventana.ui", self)
       
        self.nombre.textChanged.connect(self.validar_nombre)
        self.radio_value()
        self.boton.clicked.connect(self.validar_formulario)
   

    def validar_nombre(self):
        nombre = self.nombre.text()
        validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', nombre, re.I)
        if nombre == "":
            self.nombre.setStyleSheet("border: 1px solid yellow;")
            return False
        elif not validar:
            self.nombre.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.nombre.setStyleSheet("border: 1px solid green;")
            return True

    def validar_formulario(self):
        if self.validar_nombre() and self.radio_value() ==True:
            QMessageBox.information(
                self, "Formulario correcto", "Validación correcta", QMessageBox.Discard)
        else:
            QMessageBox.information(self, "Formulario correcto",
                                "Validación correcta", QMessageBox.Discard)
                                
    def radio_value(self):
        if self.rdb1.isChecked():
           self.labelLenguaje.setText("Comando 1  listdir + Ruta , Cuantos archivos existen en la ruta")
           self.comando1()
                 

        elif self.rdb2.isChecked():
             self.labelLenguaje.setText("Comando 2 mkdir , Crear Carpetas")
             self.comando2()
        
        elif self.rdb3.isChecked():
             self.labelLenguaje.setText("Comando 3  rename + Nombre de Carpeta, Renombrar Carpeta")
             self.comando3()
        
        elif self.rdb4.isChecked():                
             self.labelLenguaje.setText("Comando 4 mkdir + nombre del archivo, Crear un nuevo Archivo")
             self.comando4()

        elif self.rdb5.isChecked():
             self.labelLenguaje.setText("Comando 5 rmdir + nombre del archivo, Borrar Carpeta")
             self.comando5()

        elif self.rdb6.isChecked():
             self.labelLenguaje.setText("Comando 6 less + nombre del archivo, Leer un Archivo revisar en windows")
             self.comando6()

        elif self.rdb7.isChecked():
             self.labelLenguaje.setText("Comando 7 rm-f + nombre del archivo, Borrar Archivo")
             self.comando7()


        elif self.rdb8.isChecked():
             self.labelLenguaje.setText("Comando 8 Write + Escribir en Archivo")
             self.comando8()
        
        elif self.rdb9.isChecked():
             self.labelLenguaje.setText("Comando 9 date, Obtener la Fecha")
             self.comando9()
        
        elif self.rdb10.isChecked():
             self.labelLenguaje.setText("Comando 10 , Obtener el nombre del Sistema Operativo sobre el que se ejecuta")
             self.comando10()

        elif self.rdb11.isChecked():
             self.labelLenguaje.setText("Comando 11 , Saber que version de python corre y fecha de emision")
             self.comando11()
        
        elif self.rdb12.isChecked():
             self.labelLenguaje.setText("Comando 12, Conocer el directorio")
             self.comando12() 
        elif self.rdb13.isChecked():
             self.labelLenguaje.setText("Comando 13,Saber si un directorio existe")
             self.comando13() 
        
        elif self.rdb14.isChecked():
             self.labelLenguaje.setText("Comando 14,Obtener tamano de archivo sin abrirlo")
             self.comando14()
             
        elif self.rdb15.isChecked():
             self.labelLenguaje.setText("Comando 15, Obtener ultima fecha de modificacion de un archivo")
             self.comando15() 

        elif self.rdb16.isChecked():
             self.labelLenguaje.setText("Comando 16, Identificacion de grupo segun el proceso Actual")
             self.comando16() 

        elif self.rdb17.isChecked():
             self.labelLenguaje.setText("Comando 17, Cadena que da la ruta absoluta del binario ejecutable para el  interprete de Python")
             self.comando17() 

        elif self.rdb18.isChecked():
             self.labelLenguaje.setText("Comando 18, Retorna la cantidad de procesos en cola de los ultimos 1,5 a los ultimos 15 minutos")
             self.comando18() 

        elif self.rdb19.isChecked():
             self.labelLenguaje.setText("Comando 19, Devuelve una cadena de n bytes aleatorios para uso Criptograficos")
             self.comando19() 

        elif self.rdb20.isChecked():
             self.labelLenguaje.setText("Comando 20, para salir del Programa")
             self.comando20() 

        else:
             self.labelLenguaje.setText("No hay seleccionado ningún lenguaje el comando")


    def comando1(self):
        ruta="./"
        caar=os.listdir(ruta) #saber cuantos archivos ahi en la ruta
        print(caar)
        
    def comando2(self):
        #Crear Carpeta
        casar=os.mkdir(self.nombre.text())
            
    def comando3(self):
        #Cambiar nombre de carpeta
        cambio=os.rename(self.nombre.text(),self.nombre2.text())

    def comando4(self):
        #Crear archivo
        archivos=open(self.nombre.text()+".txt",'w')

    def comando5(self):
        #Eliminar Carpeta
        carperta=os.rmdir(self.nombre.text())
        QMessageBox.information(self, "Se ha Eliminado la carpeta",self.nombre.text(), QMessageBox.Discard)
    
    def comando6(self):
        archivo3=open(self.nombre.text()+".txt","r")
        linea1=archivo3.readline()
        while linea1!="":
            #print(linea1)
            linea1=archivo3.readline()
            self.labelLenguaje2.setText(linea1)
            #archivo3.close()
   

    def comando7(self):
        #Eliminar Archivo
        kamir=os.remove(self.nombre.text()+".txt")
        #print(kamir)    
        QMessageBox.information(self, "Se ha Eliminado el Archivo","Nombre de Archivo", QMessageBox.Discard)
    
    def comando8(self):
        archivo2=open(self.nombre.text()+".txt","a")
        archivo2.write(self.nombre2.text()+"\n")
    
    def comando9(self):
        print (self.nombre.text()+time.strftime("%d/%m/%y"))  

    def comando10(self):
        #Saber en cual Sistema Operativo me encuentro
        casys=sys.platform
        print(casys)

    
    def comando11(self):
        #Saber  la version de mi python y su emision 
        casys=sys.version
        print("Python "+ casys)

    
    def comando12(self):
       #Conocer el directorio
       kamir=os.getcwd()
       print(kamir)
       
    def comando13(self):
        #saber si  un directorio existe
       directorio= os.path.exists(self.nombre.text()) 
       print(directorio)

    
    def comando14(self):
        tamano= os.stat(self.nombre.text()+".txt").st_size
        print(tamano) 

    def comando15(self): 
     fechamod= os.getmtime(self.nombre.texr()+".txt")
     print(fechamod)
     
    def comando16(self):
     print os.getgid()

    def comando17(self):
     print sys.executable
     
    def comando18(self): 
     print os.getloadavg()#Retorna la cantidad de procesos en cola de los ultimos 1,5 a los ultimos 15 minutos
    
    def comando19(self):
     print os.urandom(50)#Devuelve una cadena de n bytes aleatorios para uso Criptograficos 
        
    def comando20(self):
     directorio= os.exit() 
     print("Gracias por usar el interpreter "  +directorio)    
   



app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()
