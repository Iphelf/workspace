import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "Test.ui" # Enter file here.

s=list(map(lambda x:x+1,list(range(73))))
t=list(map(lambda x:[x,x,x],list(range(73))))
roll = False 

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Start.connect(self.shows)
    def shows(self):
        global roll
        roll=not roll
        self.Start.setText("Pause")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.Show()
    sys.exit(app.exec_())