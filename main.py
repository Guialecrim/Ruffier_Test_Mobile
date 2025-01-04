from kivy.app import App # Importa a classe App responsavel por definir como aplicação móvel
from kivy.uix.screenmanager import Screen # Screen permite a criação de Ecras
from kivy.uix.label import Label # Label permite renderizar texto
from kivy.uix.button import Button # Button permite renderizar botões
from kivy.uix.textinput import TextInput # permite renderizar um objeto que recebe texto do utilizador
from kivy.uix.boxlayout import BoxLayout # Layout em caixas permite organizar os objetos no ecra

from instructions import txt_instruction, txt_test1

class InstrScr(Screen): # primeiro ecra
    def __init__(self, **kwargs): # construtor da classe InstrScr, Kwargs é um dicionario.
        super().__init__(*kwargs)
        
        instr = Label(text = txt_instruction)
        
        lbl1 = Label(text = 'Enter your name', halign = 'right')
        self.in_name = TextInput(multiline = False)
        
        lbl2 = Label(text = 'Enter your age:', halign = 'right')
        self.in_age = TextInput(multiline = False)
        
        self.btn = Button(text = 'Start', size_hint = (0.3, 0.2), pos_hint = {'center_x':0.5})# certer_x representa a posição 
        #horizontal central do widget de 0 borda a esquerda a 1 borda a direita
        
        line1 = BoxLayout(size_hint = (0.8, None), height = '30sp') # sp = scalated-individual pixels
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2 = BoxLayout(size_hint = (0.8, None), height = '30sp') 
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)
        
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8) # |
        outer.add_widget(instr)                                               # |
        outer.add_widget(line1)                                               # |adiciona todos os widget na Box principal 
        outer.add_widget(line2)                                               # |
        outer.add_widget(self.btn)                                            # |
        
        self.add_widget(outer)


class PulseScr(Screen): # segundo ecra
    def __init__(self, **kwargs): 
        super().__init__(*kwargs)    
        
        instr = Label(text = txt_test1)
        lbl_result = Label(text = 'Enter the result', halign = 'right')
        self.in_result = TextInput(text = '0', multiline = False) # multiline false significa uma linha única na input
        self.btn = Button(text = 'Next', size_hint = (0.3, 0.2), pos_hint = {'center_x': 0.5})
        
        line = BoxLayout(size_hint = (0.8, None), height = '30sp') 
        line.add_widget(lbl_result)
        line.add_widget(self.in_result)
        
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(line)
        outer.add_widget(self.btn)
        
        self.add_widget(outer)

class CheckScr(Screen): # terceiro ecra
    def __init__(self, **kwargs): 
        super().__init__(*kwargs)   
  
class PulseScr2(Screen): # quarto ecra
    def __init__(self, **kwargs): 
        super().__init__(*kwargs)    
  
class Result(Screen): # quinto ecra
    def __init__(self, **kwargs): 
        super().__init__(*kwargs)    
        
class HeartCheck(App):
    def build(self): # build é o método para renderizaçáo gráfica em kivy
        return PulseScr()
    
    
    
HeartCheck().run() # run é o loop onde acontece a aplicação