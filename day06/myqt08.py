import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("./myqt08.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        firstNum = int(self.le_first.text())
        lastNum = int(self.le_last.text())
        star = ""
        for i in range(firstNum, lastNum+1) :
            for j in range(0,i) :
                star += "*"
            star+="\n"
            
        self.te.setText(star)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainClass()
    app.exec_()