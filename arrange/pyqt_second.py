import sys, random, time
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "Test.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

roll=False
s=list(map(lambda x:x+1,list(range(73))))
t=list(map(lambda x:[x,x,x],list(range(73))))


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Start.setCheckable(True)
        self.Start.pressed.connect(self.Change)

    def Change(self):
        global roll
        roll = not roll
        if roll:
            self.Start.setText("Pause")
        else: self.Start.setText("Start")
        # rndm()
        while(roll):
            random.shuffle(s)
            printf(s)
        

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
                print "%2i" %(list[x+y*10]),
            print
        print("%17.2i %2i %2i"%(list[70],list[71],list[72]))

# Console main:
"""def rndm():
    begin = int(10000*time.clock)
    while(roll):
        now = int(10000*time.clock)
        if int(now - begin) / 2 == 0:
            random.shuffle(s)
            print(s)"""

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    while(roll):
        random.shuffle(s)
        printf(s)
    sys.exit(app.exec_())
