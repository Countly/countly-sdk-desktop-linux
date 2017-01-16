import os.path
import sys
from PyQt4 import QtGui

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from common.Countly import Countly


class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.btnEvent = QtGui.QPushButton('Click Event Test', self)
        self.btnEvent.clicked.connect(self.handleClickEventButton)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.btnEvent)

        self.btnCrash = QtGui.QPushButton('Click Crash Test', self)
        self.btnCrash.clicked.connect(self.handleClickEventButton)
        layout.addWidget(self.btnCrash)

    def handleClickEventButton(self):
        countly.event("eventButtonClick", "true")

    def handleCrashEventButton(self):
        countly.event("crashButtonClick", "true")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    screen_resolution = app.desktop().screenGeometry()

    countly = Countly("API_URL", "APP_KEY", 0,
                      str(screen_resolution.width()) + "x" + str(screen_resolution.height()))

    countly.event("start", "appstart")

    width = 350
    heigth = 150

    window = Window()
    window.resize(width, heigth)
    window.move(300, 300)
    window.setWindowTitle('Countly Simple PyQt App')
    window.show()
    sys.exit(app.exec_())
