from kivy.app import App
from instructions import *
from ruffier import *
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager


 
class my_Screen1(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
class my_Screen2(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

 
class my_Screen3(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

 
class my_Screen4(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

 
class my_Screen5(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        

class my_app(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(my_Screen1(name = "s1"))
        sm.add_widget(my_Screen2(name = "s2"))
        sm.add_widget(my_Screen3(name = "s3"))
        sm.add_widget(my_Screen4(name = "s4"))
        sm.add_widget(my_Screen5(name = "s5"))
        
        
        
        return sm
    
    

asd = my_app()
asd.run()