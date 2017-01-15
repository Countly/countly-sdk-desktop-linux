import os.path
import sys
from PyQt4 import QtGui

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from common.Countly import Countly


class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.button = QtGui.QPushButton('Test',self)
        self.button.clicked.connect(self.handleButton)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)


    def handleButton(self):
        countly.event("buttonClick", "true")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    screen_resolution = app.desktop().screenGeometry()

    countly = Countly("API_URL", "APP_KEY", 0,
                      str(screen_resolution.width()) + "x" + str(screen_resolution.height()))

    countly.event("start", "appstart")

    width = 250
    heigth = 150

    window = Window()
    window.resize(width, heigth)
    window.move(300, 300)
    window.setWindowTitle('Countly Simple PyQT App')
    window.show()
    sys.exit(app.exec_())
