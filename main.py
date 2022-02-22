from PyQt5.QtWidgets import QApplication
from main_ui import *
import sqlite3
from sqlite3 import Error


def conexion():
    try:
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()
        cursor.execute('PRAGMA foreign_keys = ON')
        conn.commit()
        return conn
    except Error:
        print(Error)


def dbBase():
    conn = conexion()
    cursor = conn.cursor()
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS[personas] (
[id] INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
[nombre] VARCHAR (50)  NULL,
[edad] INTEGER  NULL,
[sueldo] FLOAT  NULL,
[codigo] VARCHAR(50)  NULL,
[ocupacion] VARCHAR(50)  NULL)""")
    conn.commit()
    conn.close()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        ##self.comboBox.setCurrentText("")
        self.mostrarTabla()
        # self.comboBox.currentIndexChanged.connect(self.mostrar)
        # self.comboBox.currentTextChanged.connect(self.imprimir)
        self.comboBox.currentTextChanged.connect(self.cargar_contenido)

    def cargar_contenido(self):
        ###########################################################################


        contenido = self.comboBox.currentText()

        if contenido == "":
            self.comboBox.clear()

        elif contenido!="":
            self.comboBox.clear()
            print(contenido)
            ##############a<x<axa<x#############################################################
            # id nombre edad sueldo codigo
            dato = ['%' + contenido + '%', '%' + contenido + '%', '%' + contenido + '%', '%' + contenido + '%',
                    '%' + contenido + '%']
            busqueda = "SELECT * FROM personas WHERE nombre like ? and  edad like ? and  sueldo like ? and  codigo like ? and  ocupacion like ?;"
            conn = conexion()
            cursor = conn.cursor()

            #respuesta = cursor.execute(busqueda, dato).fetchall()
            respuesta = cursor.execute(
                "SELECT * FROM personas WHERE nombre like ? OR  edad like ? OR  sueldo like ? OR  codigo like ? OR  ocupacion like ?;",dato).fetchall()
            print("respuesta")
            print(respuesta)

            dato = ""
            llave = 0


            for i in respuesta:  # [(i),(i),(i)]
                for j in i:
                    dato = dato + "     " + str(j)
                self.comboBox.insertItem(llave, dato)
                # self.fontComboBox.insertItem(llave,dato)
                dato = ""
                llave = +1

    def imprimir(self):
        print("hhh")

    def mostrar(self):
        a = self.comboBox.currentIndex()
        print("===")
        print(a)
        print("===")

    def mostrarTabla(self):
        consulta_todos_los_elementos = "select * from personas;"
        conn = conexion()
        cursor = conn.cursor()
        respuesta = cursor.execute(consulta_todos_los_elementos).fetchall()  # lista de tuplas
        print(len(respuesta))
        dato = ""
        llave = 0
        for i in respuesta:  # [(i),(i),(i)]  ()
            for j in i:
                dato = dato + "     " + str(j)
            self.comboBox.insertItem(llave, dato)
            # self.fontComboBox.insertItem(llave,dato)
            dato = ""
            llave = +1


# comboBox
# tableWidget

dbBase()
app = QApplication([])
gui = MainWindow()
gui.show()
app.exec_()
