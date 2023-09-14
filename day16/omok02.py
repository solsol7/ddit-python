import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton, QSize
from typing_extensions import Self

form_class = uic.loadUiType("./omok01.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.arr2D = [
            [0,1,0,0,0, 0,0,0,0,0],
            [1,2,2,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
        ]
        
        self.arr = []
        
        for i in range(10) :
            for j in range(10) :
                lego = QPushButton('', self)
                lego.setIcon(QtGui.QIcon('0.png'))
                lego.setGeometry(40*j, 40*i, 40, 40)
                lego.setIconSize(QSize(40,40))
                self.arr.append(lego)
                
        
        self.show()
        self.myrender()
        
        
    def myrender(self):
        print("myrender")
        
    def myclick(self):
        print("myclick")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainClass()
    app.exec_()