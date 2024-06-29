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
        texte = Label(text = "gsgregfegegdgrgrrrd")
        red = Button(text = "продовшити")
        lauyte_v = BoxLayout(orientation = "vertical")
        lauyte_v.add_widget(texte)
        lauyte_v.add_widget(red)
        self.add_widget(lauyte_v)

class my_Screen2(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        text = Label(text = "щощозщ")
        redу = Button(text = "продовшити")
        lauyte_v = BoxLayout(orientation = "vertical")
        lauyte_v.add_widget(text)
        lauyte_v.add_widget(redу)
        self.add_widget(lauyte_v)

class my_Screen3(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        texteu = Label(text = "")
        redys = Button(text = "продовшити")
        lauyte_v = BoxLayout(orientation = "vertical")
        lauyte_v.add_widget(texteu)
        lauyte_v.add_widget(redys)
        self.add_widget(lauyte_v)

class my_Screen4(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        textet = Label(text = "")
        redo = Button(text = "продовшити")
        lauyte_v = BoxLayout(orientation = "vertical")
        lauyte_v.add_widget(textet)
        lauyte_v.add_widget(redo)
        self.add_widget(lauyte_v)

class my_Screen5(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        texter = Label(text = "")
        redt = Button(text = "продовшити")
        lauyte_v = BoxLayout(orientation = "vertical")
        lauyte_v.add_widget(texter)
        lauyte_v.add_widget(redt)
        self.add_widget(lauyte_v)
 
class my_app(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(my_Screen1(name = "s1"))
        sm.add_widget(my_Screen2(name = "se2"))
        sm.add_widget(my_Screen3(name = "re3"))
        sm.add_widget(my_Screen4(name = "so4"))
        sm.add_widget(my_Screen5(name = "sa5"))
        
        
        
        return sm



asd = my_app()
asd.run()