import sqlite3
import PySimpleGUI as sg

# Conexão com o banco de dados
def conectar(caminho):
    # Função para estabelecer a conexão com o banco de dados
    conexao = None
    try:
        conexao = sqlite3.connect(caminho)
        print('Conectado com sucesso!')
    except sqlite3.Error as er:
        print(er)
    return conexao

# Mostrar tabela de filmes
def mostrar_filmes(conexao):
    # Função para buscar e exibir todos os filmes no banco de dados
    cursor = conexao.cursor()
    comando_mostrar_tabela = "SELECT * FROM tb_Filmes"
    cursor.execute(comando_mostrar_tabela)
    filmes = cursor.fetchall()
    return filmes

# Inserir filme
def inserir_filme(conexao, titulo, genero, ano, bilheteria):
    # Função para inserir um novo filme no banco de dados
    comando = f"INSERT INTO tb_Filmes (TITULO, GENERO, ANO, BILHETERIA) VALUES (?, ?, ?, ?)"
    try:
        cursor = conexao.cursor()
        cursor.execute(comando, (titulo, genero, ano, bilheteria))
        conexao.commit()
        return True
    except sqlite3.Error as er:
        print(er)
        return False

# Deletar filme
def deletar_filme(conexao, id_filme):
    # Função para deletar um filme do banco de dados pelo seu ID
    comando = f"DELETE FROM tb_Filmes WHERE CODIGO = ?"
    try:
        cursor = conexao.cursor()
        cursor.execute(comando, (id_filme,))
        conexao.commit()
        return True
    except sqlite3.Error as er:
        print(er)
        return False

# Atualizar filme
def atualizar_filme(conexao, id_filme, campo, novo_valor):
    # Função para atualizar um atributo específico de um filme no banco de dados
    comando = f"UPDATE tb_Filmes SET {campo} = ? WHERE CODIGO = ?"
    try:
        cursor = conexao.cursor()
        cursor.execute(comando, (novo_valor, id_filme))
        conexao.commit()
        return True
    except sqlite3.Error as er:
        print(er)
        return False

# Função principal da interface
def main():
    # Configurações iniciais
    caminho_banco = "db_Filmes.db"
    conexao = conectar(caminho_banco)

    # Layout da interface
    layout = [
        [sg.Text("Menu", font=("Helvetica", 20), justification="center")],
        [sg.Button("Ver Filmes", size=(20, 1))],
        [sg.Button("Inserir Filme", size=(20, 1))],
        [sg.Button("Deletar Filme", size=(20, 1))],
        [sg.Button("Atualizar Filme", size=(20, 1))],
        [sg.Button("Sair", size=(20, 1))]
    ]

    # Criando a janela principal
    janela = sg.Window("Menu", layout, size=(400, 300), element_justification='c')

    while True:
        # Loop principal da interface
        evento, valores = janela.read()

        if evento == sg.WINDOW_CLOSED or evento == "Sair":
            # Fechar a janela e sair do programa se clicar em "Sair" ou fechar a janela
            break
        elif evento == "Ver Filmes":
            # Exibir filmes se clicar no botão "Ver Filmes"
            filmes = mostrar_filmes(conexao)
            sg.popup_scrolled('\n'.join(map(str, filmes)), title='Filmes', button_color=('white', 'blue'))
        elif evento == "Inserir Filme":
            # Abrir janela para inserir um novo filme
            layout_inserir = [
                [sg.Text("Título:", size=(10, 1)), sg.InputText(size=(20, 1))],
                [sg.Text("Gênero:", size=(10, 1)), sg.InputText(size=(20, 1))],
                [sg.Text("Ano:", size=(10, 1)), sg.InputText(size=(20, 1))],
                [sg.Text("Bilheteria:", size=(10, 1)), sg.InputText(size=(20, 1))],
                [sg.Button("Inserir", size=(10, 1)), sg.Button("Cancelar", size=(10, 1))]
            ]
            janela_inserir = sg.Window("Inserir Filme", layout_inserir)
            evento_inserir, valores_inserir = janela_inserir.read()

            if evento_inserir == sg.WINDOW_CLOSED or evento_inserir == "Cancelar":
                # Fechar janela de inserção se clicar em "Cancelar" ou fechar a janela
                janela_inserir.close()
            else:
                # Inserir novo filme no banco de dados
                titulo = valores_inserir[0]
                genero = valores_inserir[1]
                ano = int(valores_inserir[2])
                bilheteria = int(valores_inserir[3])
                inserido = inserir_filme(conexao, titulo, genero, ano, bilheteria)
                if inserido:
                    sg.popup("Filme inserido com sucesso!")
                    janela_inserir.close()
                else:
                    sg.popup("Erro ao inserir filme. Por favor, tente novamente.")
        elif evento == "Deletar Filme":
            # Deletar filme se clicar no botão "Deletar Filme"
            id_filme = sg.popup_get_text("Informe o ID do filme a ser deletado:")
            if id_filme:
                deletado = deletar_filme(conexao, id_filme)
                if deletado:
                    sg.popup("Filme deletado com sucesso!")
                else:
                    sg.popup("Erro ao deletar filme. Por favor, tente novamente.")
        elif evento == "Atualizar Filme":
            # Atualizar filme se clicar no botão "Atualizar Filme"
            id_filme = sg.popup_get_text("Informe o ID do filme a ser atualizado:")
            if id_filme:
                while True:
                    campo = sg.popup_get_text("Informe o campo a ser atualizado (TITULO, GENERO, ANO, BILHETERIA):")
                    if campo is None:
                        break  # Se clicar em cancelar, voltar ao menu
                    novo_valor = sg.popup_get_text("Informe o novo valor:")
                    if novo_valor is None:
                        break  # Se clicar em cancelar, voltar ao menu
                    atualizado = atualizar_filme(conexao, id_filme, campo.upper(), novo_valor)
                    if atualizado:
                        sg.popup("Filme atualizado com sucesso!")
                    else:
                        sg.popup("Erro ao atualizar filme. Por favor, tente novamente.")
                    break  # Sair do loop de atualização

    # Fechar janela e conexão com o banco de dados ao sair do programa
    janela.close()
    conexao.close()

if __name__ == "__main__":
    main()
