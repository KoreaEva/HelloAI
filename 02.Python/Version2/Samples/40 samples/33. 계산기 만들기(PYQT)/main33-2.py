import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic


ui_path = r"33. 계산기 만들기(PYQT)\계산기.ui"
form_class = uic.loadUiType(ui_path)[0] 


class WindowClass(QMainWindow, form_class) : 
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.btn_C.clicked.connect(self.btn_clicked)
        self.btn_number0.clicked.connect(self.btn_clicked)
        self.btn_number1.clicked.connect(self.btn_clicked)
        self.btn_number2.clicked.connect(self.btn_clicked)
        self.btn_number3.clicked.connect(self.btn_clicked)
        self.btn_number4.clicked.connect(self.btn_clicked)
        self.btn_number5.clicked.connect(self.btn_clicked)
        self.btn_number6.clicked.connect(self.btn_clicked)
        self.btn_number7.clicked.connect(self.btn_clicked)
        self.btn_number8.clicked.connect(self.btn_clicked)
        self.btn_number9.clicked.connect(self.btn_clicked)
        self.btn_result.clicked.connect(self.btn_clicked)
        self.btn_minus.clicked.connect(self.btn_clicked)
        self.btn_add.clicked.connect(self.btn_clicked)
        self.btn_multipy.clicked.connect(self.btn_clicked)
        self.btn_divide.clicked.connect(self.btn_clicked)

        self.le_view.setEnabled(False)
        
    def btn_clicked(self):
        btn_value = self.sender().text()
        print(btn_value)

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()