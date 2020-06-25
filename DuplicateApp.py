from PyQt5 import QtWidgets, QtGui, QtMultimedia, QtCore, QtNetwork
from mainView import Ui_MainWindow

import re
import sys
import os
import json


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.scriptDir = os.path.dirname(os.path.realpath(__file__))
        url = QtCore.QUrl.fromLocalFile(self.scriptDir + os.path.sep + 'Resources/Alarm.mp3')
        content = QtMultimedia.QMediaContent(url)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.setWindowIcon(QtGui.QIcon(self.scriptDir + os.path.sep + 'Resources/Logo2.ico'))
        self.setWindowTitle('TRG-Duplicate Tracker')
        self.currentLocation = ''


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())
