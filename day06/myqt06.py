import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("./myqt06.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self):
        global num
        num = ""

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
        sending_button = self.sender()
        num += sending_button.text()
        self.le.setText(num)

        
        
    def btnCallClick(self):
        global num
        QMessageBox.about(self,'calling',num)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainClass()
    app.exec_()