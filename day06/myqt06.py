import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("./myqt06.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()

        self.pb1.clicked.connect(self.btnClick)
        self.pb2.clicked.connect(self.btnClick)
        self.pb3.clicked.connect(self.btnClick)
        self.pb4.clicked.connect(self.btnClick)
        self.pb5.clicked.connect(self.btnClick)
        self.pb6.clicked.connect(self.btnClick)
        self.pb7.clicked.connect(self.btnClick)
        self.pb8.clicked.connect(self.btnClick)
        self.pb9.clicked.connect(self.btnClick)
        self.pb0.clicked.connect(self.btnClick)
        self.pbCall.clicked.connect(self.btnCallClick)
        
        
    def btnClick(self):
        global num
        str_new = self.sender().text()
        str_old = self.le.text()
        self.le.setText(str_old+str_new)
        
        
    def btnCallClick(self):
        str_tel = self.le.text()
        QMessageBox.about(self,'calling',str_tel)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainClass()
    app.exec_()