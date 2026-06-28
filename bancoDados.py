import sqlite3
import os

caminho_bancodados = 'ponto.db'


def criar_banco():
    if os.path.exists(caminho_bancodados):
        return
    with open("bancoDados.sql", 'r', encoding="utf=8") as arquivo:
        sql = arquivo.read()
    conexao = sqlite3.connect(caminho_bancodados)
    conexao.executescript(sql)
    conexao.commit()
    conexao.close()


def pegar_todos_pontos():
    conexao = sqlite3.connect(caminho_bancodados)
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM ponto ORDER BY _data")
    dados = cursor.fetchall()

    conexao.close()
    return dados
    
