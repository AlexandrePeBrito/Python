from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
t=[]
def usuario():
    opcao=int(input('Deseja inserir tarefa? 1- Sim 0- Não '))
    if(opcao==1):
        tarefa=input("Informe o nome da tarefa: ")
        t.append(tarefa)
    pass
class Tarefas(BoxLayout):
    def __init__(self,tarefas,**kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text=tarefa))

class teste(App):
    def build(self):
        return Tarefas(['Fazer compras','Buscar filho','Molhar a calçada'],orientation="horizontal")

teste().run()