import PySimpleGUI as sg
import subprocess
from App import *

# Função para executar o App.py
def executar_app_py():
    subprocess.Popen(["python", "App.py"], shell=True)

# Layout da interface gráfica
layout = [
    [sg.Text('Selecione uma opção para executar:')],
    [sg.Button('Inserir Dados'), sg.Button('Atualizar Dado'), sg.Button('Deletar Linha'), sg.Button('Mostrar Tabela')],
    [sg.Button('Sair')]
]

# Criando a janela
janela = sg.Window('Interface para App.py', layout)

# Loop de eventos para capturar interações do usuário
while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED or evento == 'Sair':
        break
    elif evento == 'Inserir Dados':
        sg.popup('Executando inserirDados()...')
        inserirDados()
    elif evento == 'Atualizar Dado':
        sg.popup('Executando update()...')
        update()
    elif evento == 'Deletar Linha':
        sg.popup('Executando deletarlinha()...')
        deletarlinha()
    elif evento == 'Mostrar Tabela':
        sg.popup('Executando MostrarTabela()...')
        MostrarTabela()

# Fechando a janela ao sair do loop
janela.close()