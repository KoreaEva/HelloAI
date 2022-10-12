import sys 
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


ui_path = r"34. 그림판 만들기(PYQT)\그림판.ui"
form_class = uic.loadUiType(ui_path)[0] 


class WindowClass(QMainWindow, form_class) : 
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.brushColor = Qt.black  

        self.canvas = QtGui.QPixmap(self.lb_canvas.width(), self.lb_canvas.height()) 
        self.canvas.fill(QtGui.QColor("white"))  
        self.lb_canvas.setPixmap(self.canvas)

        self.btn_black.clicked.connect(self.btn_clicked) 
        self.btn_black.setStyleSheet('background:black')

        self.btn_red.clicked.connect(self.btn_clicked)
        self.btn_red.setStyleSheet('background:red')

        self.btn_blue.clicked.connect(self.btn_clicked)
        self.btn_blue.setStyleSheet('background:blue')

        self.btn_clear.clicked.connect(self.btn_clear_clicked) 
    
    def btn_clicked(self):
        btn_value = self.sender().objectName()
        print(btn_value)
    
    def btn_clear_clicked(self):
        print("모두지움")

    def mouseMoveEvent(self, e):
        print(e.x(),e.y())

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()