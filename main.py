from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        bl = BoxLayout()
        button1 = Button(text='Hello')
        button2 = Button(text='World!')
        button3 = Button(text='Привет!')
        bl.add_widget(button1)
        bl.add_widget(button2)
        bl.add_widget(button3)
        return bl

if __name__ == '__main__':
    MyApp().run()