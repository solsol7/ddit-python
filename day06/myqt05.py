import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("./myqt05.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        num = int(self.le.text())
        result = ""
        for i in range(1,9+1) :
            result += "{}*{}={}\n".format(num, i, num*i)
        self.te.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainClass()
    app.exec_()