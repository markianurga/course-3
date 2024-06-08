from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager



class mainscreen (Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        red = Button(text = "так",color = "red")
        redy = Button(text = "ні",color = "red")
        red.on_press = self.text
        redy.on_press = self.textes
        txt = Label(text = "чи 2 + 2 = 5",color = "red")
        matu = Image(source = "m2/u1/m.jpg")
        lauyt_v = BoxLayout(orientation = "vertical")
        lauyte_h  = BoxLayout()
        lauyt_v.add_widget(txt)
        lauyt_v.add_widget(matu)
        lauyt_v.add_widget(lauyte_h)
        lauyte_h.add_widget(red)
        lauyte_h.add_widget(redy)
        self.add_widget(lauyt_v)
    def text(self):
        self.manager.current = "no"

    def textes(self):
        self.manager.current = "yes"

        
class screen_yes(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        red = Button(text = "наступне питання",color = "green")
        texte = Label(text = "правильно")
        matus = Image(source = "m2/u1/yese.jpg",size_hint = (0.9,0.9), allow_stretch= True, keep_ratio= True)
        lauyte_v = BoxLayout(orientation = "vertical")
        lauyte_h = BoxLayout()
        lauyte_v.add_widget(matus)
        lauyte_h.add_widget(texte)
        lauyte_h.add_widget(red)
        lauyte_v.add_widget(lauyte_h)
        self.add_widget(lauyte_v)
        
class screen_no(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        texte = Label(text = "не правильно")
        matus = Image(source = "m2/u1/no.jpg",size_hint = (1,1), allow_stretch= True, keep_ratio= True)
#        lauyte_v = BoxLayout(orientation = "vertical")
#        lauyte_h = BoxLayout()
        matus.add_widget(texte)
        self.add_widget(matus)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(mainscreen(name = "ms"))
        sm.add_widget(screen_yes(name = "yes"))
        sm.add_widget(screen_no(name = "no"))
        
        
        
        return sm
    
    

asd = MyApp()
asd.run()