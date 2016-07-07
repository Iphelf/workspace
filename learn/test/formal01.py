#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we create a simple
window in PyQt4.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui


def window():
    
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    b=QtGui.QLabel(w)
    b.setText("Hello World!")
    b.move(50,20)
    w.setGeometry(100,100,200,50)
    w.setWindowTitle('PyQt')
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
