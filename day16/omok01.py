import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton, QSize

form_class = uic.loadUiType("./omok01.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.arr = []
        self.flag_wb = True;
        for i in range(10) :
            for j in range(10) :
                btn1 = QPushButton('', self)
                btn1.setIcon(QtGui.QIcon('0.png'))
                btn1.setGeometry(40*j, 40*i, 40, 40)
                btn1.setIconSize(QSize(40,40))
                self.arr.append(btn1)
                btn1.clicked.connect(self.myclick)
                
        
        self.show()

        
    def myclick(self):
        if self.flag_wb :
            self.sender().setIcon(QtGui.QIcon('1.png'))
            self.flag_wb = not self.flag_wb
        else :
            self.sender().setIcon(QtGui.QIcon('2.png'))
            self.flag_wb = not self.flag_wb
            

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainClass()
    app.exec_()