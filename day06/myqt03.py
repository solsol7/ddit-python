import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("./myqt03.ui")[0]

class MainClass(QMainWindow, form_class):
    
    
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        
        self.btn.clicked.connect(self.btnClick)
        
    def btnClick(self):
        arr = list(range(1,45+1))
        
        arr6 = []
        
        for i in range(1, 10000+1) :
            rnd = int(random()*45)
            temp = arr[0]
            arr[0] = arr[rnd]
            arr[rnd] = temp
        
        arr6.append(arr[0])
        arr6.append(arr[1])
        arr6.append(arr[2])
        arr6.append(arr[3])
        arr6.append(arr[4])
        arr6.append(arr[5])
        
        for i in range(0,5+1) :
            for j in range(0,5+1) :
                if arr6[i]<arr6[j] :
                    temp = arr6[i]
                    arr6[i] = arr6[j]
                    arr6[j] = temp


        self.le1.setText(str(arr6[0]))
        self.le2.setText(str(arr6[1]))
        self.le3.setText(str(arr6[2]))
        self.le4.setText(str(arr6[3]))
        self.le5.setText(str(arr6[4]))
        self.le6.setText(str(arr6[5]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainClass()
    app.exec_()
    