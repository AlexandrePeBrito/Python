from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

class Tarefas(ScrollView):
    def __init__(self,tarefas,**kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Tarefa(text=tarefa))
    
    def addWidget(self):
        texto= self.ids.texto.text
        self.ids.box.add_widget(Tarefa(text=texto))

class Tarefa(BoxLayout):
    def __init__(self,text='',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text= text

class AuxAula7(App):
    def build(self):
        return Tarefas(['Fazer compras','Buscar filho','Molhar a calçada','Lavar pratos','Fazer comida','Varrer a casa'])

AuxAula7().run()