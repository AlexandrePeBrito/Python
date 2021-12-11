from kivy.app import App
from kivy.uix.behaviors import button
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label



class teste(App):
    def build(self):                            #Interface
        box = BoxLayout( orientation='vertical')
        button=Button(text='Botao 1')
        label= Label(text='texto 1')
        box.add_widget(button)
        box.add_widget(label)

        box2 = BoxLayout( orientation='horizontal')
        button2=Button(text='Botao 2')
        label2= Label(text='texto 2')
        box2.add_widget(button2)
        box2.add_widget(label2)

        box.add_widget(box2)
        return box
        #return Button (text ='Ola Mundo')       #este retorno eh oque aparece na tela

teste().run()
