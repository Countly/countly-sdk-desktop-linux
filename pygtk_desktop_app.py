import gtk

from common.Countly import Countly
class AppWindow:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.box1 = gtk.VBox(False, 0)
        self.window.add(self.box1)

        self.btnEvent = gtk.Button("Event Test")
        self.btnEvent.connect("clicked", self.handleClickEventButton, None)
        self.btnEvent.connect_object("clicked", gtk.Widget.destroy, self.window)
        self.box1.pack_start(self.btnEvent, True, True, 0)
        self.btnEvent.show()

        self.btnEventThread = gtk.Button("Event Thread Test")
        self.btnEventThread.connect("clicked", self.handleClickEventThreadButton, None)
        self.btnEventThread.connect_object("clicked", gtk.Widget.destroy, self.window)
        self.box1.pack_start(self.btnEventThread, True, True, 0)
        self.btnEventThread.show()

        self.btnCrash = gtk.Button("Crash Test")
        self.btnCrash.connect("clicked", self.handleCrashEventButton, None)
        self.btnCrash.connect_object("clicked", gtk.Widget.destroy, self.window)
        self.box1.pack_start(self.btnCrash, True, True, 0)
        self.btnCrash.show()

        self.box1.show()
        self.window.show()


    def main(self):
        gtk.main()


    def handleClickEventButton(self, widget, data=None):
        countly.event("eventButtonClick", "true")

    def handleClickEventThreadButton(self, widget, data=None):
        self.initCountly(int(self.textEdit.toPlainText()))
        countly.event("eventThreadButtonClick", "true")

    def handleCrashEventButton(self, widget, data=None):
        countly.event("crashButtonClick", "true")


    def initCountly(self, thread_size):
        global countly
        countly = Countly("API_URL", "APP_KEY", thread_size, str(gtk.gdk.screen_width()) + "x" + str(gtk.gdk.screen_height()))


print __name__
if __name__ == "__main__":
    base = AppWindow()
    base.initCountly(0)
    base.main()