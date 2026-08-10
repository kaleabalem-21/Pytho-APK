from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='Hello ጀግናው! My First App', font_size=50)

if __name__ == '__main__':
    MyApp().run()
