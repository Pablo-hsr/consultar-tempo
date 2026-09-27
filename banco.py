import sqlite3

NOME_BANCO = "clima.db"

def conectar():
    return sqlite3.connect(NOME_BANCO)

def criar_tabela():
    conexao = conectar()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS cidades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            pais TEXT,
            UNIQUE(nome, latitude, longitude)
        )
    """)
    conexao.commit()
    conexao.close()

def listar_cidades():
    conexao = conectar()

    cursor = conexao.execute("""
        SELECT id, nome, latitude, longitude, pais
        FROM cidades
        ORDER BY nome
    """)

    cidades = cursor.fetchall()

    conexao.close()

    return cidades