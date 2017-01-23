from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from common.Countly import Countly


class AppWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(AppWindow, self).__init__(**kwargs)

        self.btnEvent = Button(text="Event Test")
        self.add_widget(self.btnEvent)
        self.btnEvent.bind(on_press=self.handleClickEventButton)

        self.btnEventThread = Button(text='Event Thread Test')
        self.add_widget(self.btnEventThread)
        self.btnEventThread.bind(on_press=self.handleClickEventThreadButton)

        self.btnCrash = Button(text='Crash Test')
        self.add_widget(self.btnCrash)
        self.btnCrash.bind(on_press=self.handleCrashEventButton)

    def handleClickEventButton(self,instance):
        self.initCountly(0)
        countly.event("eventButtonClick", "true")

    def handleClickEventThreadButton(self,instance):
        self.initCountly(10)
        countly.event("eventThreadButtonClick", "true")

    def handleCrashEventButton(self,instance):
        self.initCountly(0)
        countly.event("crashButtonClick", "true")

    def initCountly(self, thread_size):
        global countly
        countly = Countly("API_URL", "APP_KEY", thread_size, str(sp(Window.width)) + "+" + str(sp(Window.height)))


class App(App):
    def build(self):
        appWindow = AppWindow()
        appWindow.initCountly(0)
        return appWindow


if __name__ == "__main__":
    App().run()