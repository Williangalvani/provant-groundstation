import sys
import os
from PyQt4 import QtGui, uic, Qt
from windows.mainwindow import MainWindow

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
