import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QFont
from PyQt4.QtCore import Qt

qtCreatorFile = "Example.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        
        self.setupUi(self)
        self.PT1.setFont(QFont("Ubuntu Mono",36))
        self.PT1.setAlignment(Qt.AlignVCenter)
        self.PT1.setAlignment(Qt.AlignHCenter)
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())