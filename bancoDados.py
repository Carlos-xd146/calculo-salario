import sqlite3
import os

caminho_bancodados = 'regstro.db'


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
