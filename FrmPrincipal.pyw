#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
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
        if self.validar_nombre() and self.radio_value():
            QMessageBox.information(
                self, "Formulario correcto", "Validación correcta", QMessageBox.Discard)
        else:
            QMessageBox.warning(self, "Formulario incorrecto",
                                "Validación incorrecta", QMessageBox.Discard)
                                
    def radio_value(self):
        if self.rdb1.isChecked():
           self.labelLenguaje.setText("Python ha sido seleccionado el comando 1")
        elif self.rdb2.isChecked():
             self.labelLenguaje.setText("PHP ha sido seleccionado el comando 2")
        elif self.rdb3.isChecked():
             self.labelLenguaje.setText("Perl ha sido seleccionado el comando 3")
        elif self.rdb4.isChecked():
             self.labelLenguaje.setText("Ruby ha sido seleccionado el comando 4")

        elif self.rdb5.isChecked():
                 self.labelLenguaje.setText("PHP ha sido seleccionado el comando 5")
        elif self.rdb6.isChecked():
             self.labelLenguaje.setText("Perl ha sido seleccionado el comando 6")
        elif self.rdb7.isChecked():
             self.labelLenguaje.setText("Ruby ha sido seleccionado el comando 7")

        elif self.rdb8.isChecked():
                 self.labelLenguaje.setText("PHP ha sido seleccionado el comando 8")
        elif self.rdb9.isChecked():
             self.labelLenguaje.setText("Perl ha sido seleccionado el comando 9")
        elif self.rdb10.isChecked():
             self.labelLenguaje.setText("Ruby ha sido seleccionado el comando 10")

        elif self.rdb11.isChecked():
                 self.labelLenguaje.setText("PHP ha sido seleccionado el comando 11")
        elif self.rdb12.isChecked():
             self.labelLenguaje.setText("Perl ha sido seleccionado el comando 12")
        elif self.rdb13.isChecked():
             self.labelLenguaje.setText("Ruby ha sido seleccionado el comando 13")

        elif self.rdb14.isChecked():
                 self.labelLenguaje.setText("PHP ha sido seleccionado el comando 14")
        elif self.rdb15.isChecked():
             self.labelLenguaje.setText("Perl ha sido seleccionado el comando 15")
        elif self.rdb16.isChecked():
             self.labelLenguaje.setText("Ruby ha sido seleccionado el comando 16")

        elif self.rdb17.isChecked():
                 self.labelLenguaje.setText("PHP ha sido seleccionado el comando 17")
        elif self.rdb18.isChecked():
             self.labelLenguaje.setText("Perl ha sido seleccionado el comando 18")
        elif self.rdb19.isChecked():
             self.labelLenguaje.setText("Ruby ha sido seleccionado el comando 19")

        elif self.rdb20.isChecked():
                 self.labelLenguaje.setText("PHP ha sido seleccionado el comando 20")
        else:
             self.labelLenguaje.setText("No hay seleccionado ningún lenguaje el comando")


   

app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()
