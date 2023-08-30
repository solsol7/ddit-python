import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("./myqt04.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        
        # self.pb.clicked.connect(self.btnClick)
        self.leMine.returnPressed.connect(self.btnClick)
        
    def btnClick(self):
        com = ""
        mine = self.leMine.text()
        result = ""
        rnd = int(random()*3)
        if rnd==0 :
            com = "가위"
        elif rnd==1 :
            com = "바위"
        elif rnd==2 :
            com = "보"
        
        if mine=="가위" and com=="보" or mine=="바위" and com=="가위" or mine=="보" and com=="바위" :
            result = "이김"
        elif mine=="가위" and com=="가위" or mine=="바위" and com=="바위" or mine=="보" and com=="보" :
            result = "비김"
        else :
            result = "짐"
        
        self.leCom.setText(com)
        self.leResult.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainClass()
    app.exec_()