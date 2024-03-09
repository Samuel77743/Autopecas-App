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

### Criando tabela

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

### "TRUNCATE"
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

### DELETAR LINHA ESPECIFICA
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

### Apagar tabela
def dropTable(conexao):
    comando = """
DROP TABLE TB_PECAS"""
    try:
        cursor = conexao.cursor()
        cursor.execute(comando)
        print('Tabela apagada com sucesso!')
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

vcon = conectar(caminho) # Estabelecer conexão

criarTabela(vcon, comandoCriarTabela)
# Se já existe será printado "Already Exists"

### INSERINDO DADOS
campos = preencher()

comandoInserir = f"""
INSERT INTO TB_PECAS
(NOME, DESCRICAO, FAMILIA, VALOR) VALUES
('{campos[0]}', '{campos[1]}', '{campos[2]}', {campos[3]});
"""

inserirDados(vcon, comandoInserir)

vcon.close()