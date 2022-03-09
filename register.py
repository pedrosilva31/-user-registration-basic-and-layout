import PySimpleGUI as sg 

class TelaPython:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Nome:',size=(11,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade:',size=(11,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Telefone(DDD):',size=(11,0)),sg.Input(size=(15,0),key='contato')],
            [sg.Text('Qual seu genero?')],
            [sg.Radio('Masculino','sexo',key='sexo_M'),sg.Radio('Feminino','sexo',key='sexo_F')],
            [sg.Text('Quais e-mail você usa?')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Button('Enviar Dados')]
        ]
        #janela
        self.janela = sg.Window("Dados do usuário").layout(layout)
        #exibir na tela
        self.Button, self.values = self.janela.Read()

    def Iniciar(self):
        while True:
            #exibir na tela
            self.Button, self.values = self.janela.Read()
            nome= self.values['nome']
            idade= self.values['idade']
            v_gmail= self.values['gmail']
            v_outlook= self.values['outlook']
            v_yahoo = self.values['yahoo']
            sexom = self.values['sexo_M']
            sexof = self.values['sexo_F']
            contato_ =self.values['contato']
            print(f'nome:{nome}')
            print(f'idade:{idade}')
            print(f'sexo masculino:{sexom}')
            print(f'sexo feminino:{sexof}')
            print(f'usa gmail:{v_gmail}')
            print(f'usa outlook:{v_outlook}')
            print(f'usa yahoo:{v_yahoo}')
            print(f'contato:{contato_}')
tela = TelaPython()
tela.Iniciar()



