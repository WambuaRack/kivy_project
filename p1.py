from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout


class myapp(App):
    def build (self):
         layout =BoxLayout(orientation ='vertical', spacing =10, padding =20)
         
         self.label = Label(text ='WELCOME TO KIVY', font_size='24sp')
         self.btn =Button(text ='CLICK ME !!', size_hint=(1,0.2), on_press=self.on_button_click)
         
         layout.add_widget(self.label)
         layout.add_widget(self.btn)
         
         return layout
     
     #fewfwfewfwefe
    def on_button_click(self, instance):
        self.label.text= 'YOU CLICKED ME DUDE!!!'
        
myapp().run()
