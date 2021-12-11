from kivy.app import App
from kivy.uix.boxlayout import BoxLayout




""" 
on_release -> quando soltar o botao
"""
class Incrementador(BoxLayout):
   pass

class teste(App):
    def build(self):                      
        return Incrementador()

teste().run()
