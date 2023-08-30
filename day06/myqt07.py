import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("./myqt07.ui")[0]

class MainClass(QMainWindow, form_class):
    
    
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        
        global numArr
        
        numArr = []

        while len(numArr)!=3 :
            flag = True
            num = int(random()*10)
            
            for i in numArr :
                if(i==num) : flag=False
            if(flag==True) :
                numArr.append(num)
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        
        
        print(numArr)
        
        sCnt = 0;


        sCnt = 0;
        bCnt = 0;
        userNum = self.le.text()
        userArr = userNum.split(" ")
        result = self.pt.toPlainText()
        
        for i in range(0,2+1) :
            userArr[i] = int(userArr[i])
    
        for i in numArr :
            for j in userArr :
                if i==j and numArr.index(i)==userArr.index(j) :
                    sCnt += 1
                elif i==j and numArr.index(i)!=userArr.index(j) :
                    bCnt += 1
            
        result += "{}\t{}S{}B\n".format(userArr,sCnt,bCnt)
        if sCnt==3 : result += "정답입니다."
        self.le.setText("")
        
        self.pt.setPlainText(result)

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainClass()
    app.exec_()