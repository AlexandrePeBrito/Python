from kivy.app import App
from kivy.uix.behaviors import button
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

""" 
on_release -> quando soltar o botao
"""


class teste(App):
    def build(self):                            #Interface
        box = BoxLayout( orientation='vertical')
        button=Button(text='Botao 1',font_size=30, on_release=self.incrementar)
        self.label= Label(text='1',font_size=30, )
        box.add_widget(button)
        box.add_widget(self.label)

        return box
        #return Button (text ='Ola Mundo')       #este retorno eh oque aparece na tela
    def incrementar(self, button,):
        button.text='Soltei'
        self.label.text=f"{int(self.label.text)+1}"

teste().run()
