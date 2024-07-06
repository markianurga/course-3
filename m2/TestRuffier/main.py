from kivy.app import App
from instructions import *
from ruffier import *
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager

name = ""
age = 0
p1 = 0
p2 = 0
p3 = 0
 
class my_Screen1(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.neme = TextInput(text = "",multiline=False, size_hint = (0.9,0.9))           
        self.vik = TextInput(text = "",multiline=False, size_hint = (0.9,0.9))
        texte = Label(text = txt_instruction)
        textp = Label(text = "ведіть імя")
        textpy = Label(text = "ведіть вік")
        red = Button(text = "продовшити")
        
        lauyte_v = BoxLayout(orientation = "vertical")
        lauyte_h = BoxLayout()
        lauyte_h2 = BoxLayout()
        
        lauyte_v.add_widget(texte)
        lauyte_h.add_widget(textp)
        lauyte_h.add_widget(self.neme)
        lauyte_h2.add_widget(textpy)

        lauyte_h2.add_widget(self.vik)

                
        lauyte_v.add_widget(lauyte_h)
        lauyte_v.add_widget(lauyte_h2)
        lauyte_v.add_widget(red)
        self.add_widget(lauyte_v)
        
        red.on_press = self.next
        
    def next(self):
        global name, age
        self.manager.current = "s2"
        
        name = self.neme.text
        
        age = int(self.vik.text)


class my_Screen2(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        text = Label(text = txt_test1)
        red = Button(text = "продовшити")
        self.texerw = TextInput(text = "")
        tevkdf = Label(text = "ведіть результат",)
        lauyte_v = BoxLayout(orientation = "vertical")
        lauyte_h_2 = BoxLayout()
        lauyte_v.add_widget(text)
        lauyte_v.add_widget(lauyte_h_2)
        lauyte_h_2.add_widget(tevkdf)
        lauyte_h_2.add_widget(self.texerw)
        lauyte_v.add_widget(red)
        self.add_widget(lauyte_v)
        red.on_press = self.next
        
    def next(self):
        global p1
        self.manager.current = "s3"
        
        p1 = int(self.texerw.text)

 
class my_Screen3(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        texteu = Label(text = txt_test2)
        red = Button(text = "продовшити")
        lauyte_v = BoxLayout(orientation = "vertical")
        lauyte_v.add_widget(texteu)
        lauyte_v.add_widget(red)
        self.add_widget(lauyte_v)
        red.on_press = self.next
        
    def next(self):
        self.manager.current = "s4"


class my_Screen4(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        textet = Label(text = txt_test3)
        red = Button(text = "продовшити")
        self.neme = TextInput(text = "",multiline=False, size_hint = (0.9,0.9))
        self.vik = TextInput(text = "",multiline=False, size_hint = (0.9,0.9))
        textp = Label(text = "результат")
        textpy = Label(text = "результат після відпочинку")
        lauyte_v = BoxLayout(orientation = "vertical")
        lauyte_h_4 = BoxLayout()
        lauyte_h_23 = BoxLayout()
        lauyte_v.add_widget(textet)
        lauyte_h_4.add_widget(textp)
        lauyte_h_4.add_widget(self.neme)
        lauyte_h_23.add_widget(textpy)
        lauyte_h_23.add_widget(self.vik)
        lauyte_v.add_widget(lauyte_h_4)
        lauyte_v.add_widget(lauyte_h_23)
        lauyte_v.add_widget(red)
        self.add_widget(lauyte_v)
        red.on_press = self.next
        
    def next(self):
        global p2, p3
        self.manager.current = "s5"

        
        p2 = int(self.neme.text)
        p3 = int(self.vik.text)
 


class my_Screen5(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.texter = Label(text = "")

        
        self.texte = Label(text = "")
        
        self.textero = Label(text = "")
        
        lauyte_v = BoxLayout(orientation = "vertical")
        lauyte_v.add_widget(self.texter)
        lauyte_v.add_widget(self.texte)
        lauyte_v.add_widget(self.textero)
        self.add_widget(lauyte_v)
    def on_enter(self) :
        self.texter.text = name
        
        self.texte.text = test(p1,p2, p3, age)

        
        
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