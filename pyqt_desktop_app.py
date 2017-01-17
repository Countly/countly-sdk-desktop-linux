import os.path
import sys
from PyQt4 import QtGui,QtCore

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from common.Countly import Countly


class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.btnEvent = QtGui.QPushButton('Event Test', self)
        self.btnEvent.setGeometry(QtCore.QRect(40, 30, 311, 21))
        self.btnEvent.clicked.connect(self.handleClickEventButton)

        self.textEdit = QtGui.QTextEdit(self)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setGeometry(QtCore.QRect(40, 70, 51, 21))

        self.btnEventThread = QtGui.QPushButton('Event Thread Test', self)
        self.btnEventThread.setGeometry(QtCore.QRect(90, 70, 261, 21))
        self.btnEventThread.clicked.connect(self.handleClickEventThreadButton)

        self.btnCrash = QtGui.QPushButton('Crash Test', self)
        self.btnCrash.setGeometry(QtCore.QRect(40, 110, 311, 21))
        self.btnCrash.clicked.connect(self.handleClickEventButton)

    def handleClickEventButton(self):
        countly.event("eventButtonClick", "true")

    def handleClickEventThreadButton(self):
        self.initCountly(int(self.textEdit.toPlainText()))
        countly.event("eventThreadButtonClick", "true")

    def handleCrashEventButton(self):
        countly.event("crashButtonClick", "true")


    def initCountly(self, thread_size):
        global countly
        countly = Countly("API_URL", "APP_KEY", thread_size, str(screen_resolution.width()) + "x" + str(screen_resolution.height()))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    screen_resolution = app.desktop().screenGeometry()

    window = Window()

    window.initCountly(0)

    countly.event("start", "appstart")

    width = 350
    heigth = 150

    window.resize(width, heigth)
    window.move(300, 300)
    window.setWindowTitle('Countly Simple PyQt App')
    window.show()
    sys.exit(app.exec_())
