import sys, random, time
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QFont
from PyQt4.QtCore import Qt

qtCreatorFile = "Test.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

roll=False
s=list(map(lambda x:x+1,list(range(73))))
t=list(map(lambda x:[x,x],list(range(73))))
f=open('List.csv','r')
r='start';n=0
while(1):
    r=f.readline()
    if len(str(r))==0:
        break
    print(r,end='')
    t[n]=r.split(',')
    n+=1
t[0][0]=1


def cr(crt):
	cr=list(map(lambda x:x+1,list(range(73))))
	return cr
saves=list(map(cr,list(range(10))))
n=0
m=0
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        global s
        count=0
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        textgroup=[self.textEdit_1,self.textEdit_2,self.textEdit_3,self.textEdit_4,self.textEdit_5,self.textEdit_6,self.textEdit_7,self.textEdit_8,self.textEdit_9,self.textEdit_10,self.textEdit_11,self.textEdit_12,self.textEdit_13,self.textEdit_14,
        self.textEdit_15,self.textEdit_16,self.textEdit_17,self.textEdit_18,self.textEdit_19,self.textEdit_20,self.textEdit_21,self.textEdit_22,self.textEdit_23,self.textEdit_24,self.textEdit_25,self.textEdit_26,self.textEdit_27,self.textEdit_28,
        self.textEdit_29,self.textEdit_30,self.textEdit_31,self.textEdit_32,self.textEdit_33,self.textEdit_34,self.textEdit_35,self.textEdit_36,self.textEdit_37,self.textEdit_38,self.textEdit_39,self.textEdit_40,self.textEdit_41,self.textEdit_42,
        self.textEdit_43,self.textEdit_44,self.textEdit_45,self.textEdit_46,self.textEdit_47,self.textEdit_48,self.textEdit_49,self.textEdit_50,self.textEdit_51,self.textEdit_52,self.textEdit_53,self.textEdit_54,self.textEdit_55,self.textEdit_56,
        self.textEdit_57,self.textEdit_58,self.textEdit_59,self.textEdit_60,self.textEdit_61,self.textEdit_62,self.textEdit_63,self.textEdit_64,self.textEdit_65,self.textEdit_66,self.textEdit_67,self.textEdit_68,self.textEdit_69,self.textEdit_70,
        self.textEdit_76,self.textEdit_77,self.textEdit_71]
        self.Start.setText("Start")
        for each in textgroup:
            each.setText(str(s[count]))
            count+=1
        count=0

        self.Start.clicked.connect(self.rdmn)
        self.Last.clicked.connect(self.last)
        self.Next.clicked.connect(self.nextl)
        # self.English.connect(self.trans)

    def showl(self):
        count=0
        global s
        textgroup=[self.textEdit_1,self.textEdit_2,self.textEdit_3,self.textEdit_4,self.textEdit_5,self.textEdit_6,self.textEdit_7,self.textEdit_8,self.textEdit_9,self.textEdit_10,self.textEdit_11,self.textEdit_12,self.textEdit_13,self.textEdit_14,
        self.textEdit_15,self.textEdit_16,self.textEdit_17,self.textEdit_18,self.textEdit_19,self.textEdit_20,self.textEdit_21,self.textEdit_22,self.textEdit_23,self.textEdit_24,self.textEdit_25,self.textEdit_26,self.textEdit_27,self.textEdit_28,
        self.textEdit_29,self.textEdit_30,self.textEdit_31,self.textEdit_32,self.textEdit_33,self.textEdit_34,self.textEdit_35,self.textEdit_36,self.textEdit_37,self.textEdit_38,self.textEdit_39,self.textEdit_40,self.textEdit_41,self.textEdit_42,
        self.textEdit_43,self.textEdit_44,self.textEdit_45,self.textEdit_46,self.textEdit_47,self.textEdit_48,self.textEdit_49,self.textEdit_50,self.textEdit_51,self.textEdit_52,self.textEdit_53,self.textEdit_54,self.textEdit_55,self.textEdit_56,
        self.textEdit_57,self.textEdit_58,self.textEdit_59,self.textEdit_60,self.textEdit_61,self.textEdit_62,self.textEdit_63,self.textEdit_64,self.textEdit_65,self.textEdit_66,self.textEdit_67,self.textEdit_68,self.textEdit_69,self.textEdit_70,
        self.textEdit_76,self.textEdit_77,self.textEdit_71]
        for each in textgroup:
            each.setText(str(s[count]))
            count+=1    
    def last(self):
        global saves,s,n,m
        s=saves[m]
        printf(s)
        self.showl()
        print(m,n)
    def nextl(self):
        global saves,s,n,m
        s=saves[m]
        printf(s)
        self.showl()
        print(m,n)
    def rdmn(self):
        global saves,s,n,m
        saves[n]=s
        random.shuffle(s)
        printf(s)
        self.showl()
        printf(saves[n-1])
        print(saves)
        n+=1
        print(m,n)
    def trans(self):
        global translate,s
        s=translate('e')
        self.showl()
        print(m,n)

        

# Console fuctions:
def translate(mode='e'):
    if mode=='e':
        return list(map(lambda x: x[1],t))
    elif mode=='c':
        return list(map(lambda x: x[2],t))
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
            print ()
        print("%2i %14.2i %2i"%(list[70],list[71],list[72]))

# Console main:

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
print(saves)