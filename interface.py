import PySimpleGUI as sg
import subprocess

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
        executar_app_py()
    elif evento == 'Atualizar Dado':
        sg.popup('Executando update()...')
        executar_app_py()
    elif evento == 'Deletar Linha':
        sg.popup('Executando deletarlinha()...')
        executar_app_py()
    elif evento == 'Mostrar Tabela':
        sg.popup('Executando MostrarTabela()...')
        executar_app_py()

# Fechando a janela ao sair do loop
janela.close()