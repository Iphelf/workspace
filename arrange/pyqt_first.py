import sys
import random
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "Test.ui" # Enter file here.

s=list(map(lambda x:x+1,list(range(73))))
t=list(map(lambda x:[x,x,x],list(range(73))))
roll = False        
Ui_MainWindow.__init__(self)


Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        global s
        print(s[7])
        self.textEdit_1.setText(str(s[7])
        self.Start.clicked.connect(self.start)
    def start(self):
        global roll
        roll = not roll 
        self.textEdit_1.setText()

# Console fuctions:
def index(num,mode):
    n=s.index(num)
    if mode == 'G':
        if n%10==0 | 1:
            return 4
        elif n%10==2 | 3 | 4:
            return 3
        elif n%10==5 | 6 | 7:
            return 2
        else:
            return 1
    elif mode == 'p':
        if n<70:
            x=n%10 + 1
        else:
            x=n-64
        y=n/10 + 1
        return [x,y]
def printf(list,mode=73):
    if mode == 73:
        for y in range(7):
            for x in range(10):
                print("%2i" %(list[x+y*10]),end=' ')
            print()
        print("%17.2i %2i %2i"%(list[70],list[71],list[72]))

# Console main:
while(roll):
    random.shuffle(s)
printf(s)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())