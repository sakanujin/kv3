from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

from kivy.uix.togglebutton import ToggleButton # for toggle

class TextWidget(Widget):
    text = StringProperty()
    text2 = StringProperty()
    text3 = StringProperty()

    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = 'オフ'
        self.text2 = 'UP'
        self.text3 = 'DOWN'

    def buttonClicked(self):  
        self.text = "オン"

    def btc2(self):  
        self.text2 = "温度UP"

    def btc3(self):  
        self.text3 = "温度DOWN"

class TestApp(App):

    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'freezer UI/UX'

    def build(self):
        return TextWidget()

if __name__ == "__main__":
    TestApp().run()
