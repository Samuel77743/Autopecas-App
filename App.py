#DEPENDENCIAS E SUGESTÕES:
    # 1 - BAIXE E INSTALE O SQLITE
    # 2 - RECOMENDADO USAR SQLITESTUDIO PARA VER E MANIPULAR BD
    # 3 - BAIXAR EXTENSÕES DO VSCODE: SQLITE e SQLITE Viewer
    # 4 - TALVEZ PRECISE MUDAR O DIRETORIO DA VARIAVEL 'caminho'

import sqlite3


### Conexão
caminho = ".\\db_Autopecas.db"

def conectar(caminho):
    conexao = None
    try:
        conexao = sqlite3.connect(caminho)
        print('Conectado com sucesso!')
    except sqlite3.Error as er:
        print(er)
    return conexao


### FUNÇÕES DE PROCEDIMENTOS DO BANCO
# Criando tabela
def criarTabela(conexao, comando):
    try:
        cursor = conexao.cursor()
        cursor.execute(comando)
        
        print('Tabela criada com sucesso')
    except sqlite3.Error as er:
        print(er)

# INSERÇÃO DE DADOS
def inserirDados(conexao, comando):
    try:
        cursor = conexao.cursor()
        cursor.execute(comando)
        conexao.commit()

        print("Dados inseridos com sucesso!")
    except sqlite3.Error as er:
        print(er)

def preencher():
    print(f'\n{"PREENCHENDO":=^20}')
    campo = [
        str(input('NOME DA PEÇA -> ')).upper(),
        str(input('DESCRIÇÃO -> ')).capitalize(),
        str(input('FAMÍLIA -> ')).capitalize(),
        float(input('VALOR -> '))
    ]
    return campo

# "TRUNCATE"
comandoTruncar = """
DELETE FROM TB_PECAS;
"""
def truncar(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute(comandoTruncar)
        conexao.commit()
        print('Tabela zerada com sucesso')
    except sqlite3.Error as er:
        print(er)

# DELETAR LINHA ESPECIFICA
def deletarlinha(conexao):
    linha = int(input('Qual o ID do produto deseja excluir? '))
    cursor = conexao.cursor()
    comando = f"""
DELETE FROM TB_PECAS
WHERE CODIGO = {linha};"""
    
    try:
        cursor.execute(comando)
        conexao.commit()
        print(f'Peça de ID #{linha} deletado com sucesso!')
    except sqlite3.Error as er:
        print(er)

# Apagar tabela
def dropTable(conexao):
    comando = "DROP TABLE TB_PECAS"
    try:
        cursor = conexao.cursor()
        cursor.execute(comando)
        print('Tabela apagada com sucesso!')
    except sqlite3.Error as er:
        print(er)

# Atualizar uma célula
def update(conexao):
    print(f"\n{'UPDATE':=^25}")
    
    id = int(input('Qual o ID da linha que deseja alterar o valor -> '))

    while True:
        print(f'{"Qual a coluna":=^25}')
        print("""
        [1] NOME
        [2] DESCRICAO
        [3] FAMÍLIA
        [4] VALOR""")

        numColuna = int(input('\nSUA RESPOSTA -> '))

        if numColuna == 1:
            nomeColuna = 'nome'
            break
        elif numColuna == 2:
            nomeColuna = 'descricao'
            break
        elif numColuna == 3:
            nomeColuna = 'familia'
            break
        elif numColuna == 4:
            nomeColuna = 'valor'
            break
        else:
            print(f'{"Resposta Inválida":=^25}')
    
    if nomeColuna != 'valor':
        dado = str(input('VALOR NOVO -> '))
    else:
        while True:
            try:
                dado = float(input('VALOR NOVO -> '))
                break

            except ValueError:
                print('Digite apenas valores numéricos!')
                print(f'{"TENTE NOVAMENTE":-^25}') 

    comandoUpdate = f"""
    UPDATE TB_PECAS
    SET {nomeColuna} = '{dado}'
    WHERE rowid = {id};"""

    try:
        cursor = conexao.cursor()
        cursor.execute(comandoUpdate)
        conexao.commit()
    except sqlite3.Error as er:
        print(er)


#funcao mostrar tabela
def MostrarTabela(conexao):
    try:
        cursor = conexao.cursor()
        comandoMostrarTabela = """
        SELECT NOME, DESCRICAO
        FROM TB_PECAS;
        """
        cursor.execute(comandoMostrarTabela)
        
        #imprimindo linhas
        for linha in cursor.fetchall():
            print(linha)
    except sqlite3.Error as er:
        print(er)

### Iniciando procedimentos
comandoCriarTabela = """
CREATE TABLE TB_PECAS(
	CODIGO INTEGER PRIMARY KEY AUTOINCREMENT,
	NOME varchar(50),
	DESCRICAO TEXT,
	FAMILIA TEXT,
	VALOR DECIMAL(12,2)
    )"""

# Estabelecer conexão
vcon = conectar(caminho) 

# criarTabela(vcon, comandoCriarTabela) # Se já existe será printado "Already Exists"

# ## INSERINDO DADOS
# campos = preencher()

# comandoInserir = f"""
# INSERT INTO TB_PECAS
# (NOME, DESCRICAO, FAMILIA, VALOR) VALUES
# ('{campos[0]}', '{campos[1]}', '{campos[2]}', {campos[3]});
# """

# inserirDados(vcon, comandoInserir)

#update(vcon)

#vcon.close()



# Chamando a função MostrarTabela
MostrarTabela(vcon)