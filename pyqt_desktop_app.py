import os.path
import sys
from PyQt4 import QtGui

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from common.Countly import Countly


def main():
    app = QtGui.QApplication(sys.argv)

    screen_resolution = app.desktop().screenGeometry()

    countly = Countly("API_URL", "APP_KEY", 0,
                      str(screen_resolution.width()) + "x" + str(screen_resolution.height()))

    countly.event("start", "appstart")

    width = 250
    heigth = 150

    w = QtGui.QWidget()
    w.resize(width, heigth)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
