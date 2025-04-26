from kivy.app import App
from kivy.uix.label import Label  # Correct import


class MyFirstApp(App):
    def build(self):
        return Label(text='MY app')  # Use Label, not label


MyFirstApp().run()
