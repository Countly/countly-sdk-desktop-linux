from kivy.app import App
from kivy.core.window import Window
from kivy.metrics import sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from common.Countly import Countly


class AppWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(AppWindow, self).__init__(**kwargs)

        self.btnEventBtn = Button(text="Event Test")
        self.btnEventBtn.bind(on_press=self.handleClickEventThreadButton)
        self.add_widget(self.btnEventBtn)

        self.add_widget(Button(text='Event Thread Test'))

        self.add_widget(Button(text='Crash Test'))


    def handleClickEventThreadButton(self,instance):
        self.initCountly(0)
        countly.event("eventThreadButtonClick", "true")


    def initCountly(self, thread_size):
        global countly
        countly = Countly("API_URL", "APP_KEY", thread_size, str(sp(Window.width))+"+"+str(sp(Window.height)))



class App(App):
    def build(self):
        return AppWindow()

if __name__ == "__main__":
    App().run()




