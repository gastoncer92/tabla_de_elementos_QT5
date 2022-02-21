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
        self.mostrarTabla()

    def mostrarTabla(self):
        consulta_todos_los_elementos()


#comboBox
#tableWidget

dbBase()
app = QApplication([])
gui = MainWindow()
gui.show()
app.exec_()
