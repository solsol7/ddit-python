import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("./myqt02.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
       leInt = int(self.le.text())
       self.le.setText(str(leInt*2))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainClass()
    app.exec_()