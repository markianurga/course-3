from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image


def text():
    print("ні")

def textes():
    print("так")


class MyApp(App):
    def build(self):
        red = Button(text = "так",color = "red")
        redy = Button(text = "ні",color = "red")
        red.on_press = text
        redy.on_press = textes
        txt = Label(text = "чи 2 + 2 = 5",color = "red")
        matu = Image(source = "m2/u1/m.jpg")
        lauyt_v = BoxLayout(orientation = "vertical")
        lauyte_h  = BoxLayout()
        lauyt_v.add_widget(txt)
        lauyt_v.add_widget(matu)
        lauyt_v.add_widget(lauyte_h)
        lauyte_h.add_widget(red)
        lauyte_h.add_widget(redy)
        
        
        
        
        return lauyt_v
    
    

asd = MyApp()
asd.run()