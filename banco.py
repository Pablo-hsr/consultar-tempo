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

def salvar_cidade(nome, latitude, longitude, pais):
    conexao = conectar()

    conexao.execute("""
        INSERT OR IGNORE INTO cidades
        (nome, latitude, longitude, pais)
        VALUES (?, ?, ?, ?)
    """, (nome, latitude, longitude, pais))

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

def remover_cidade():
    conexao = conectar()

    cursor = conexao.execute("""
        SELECT id, nome, latitude, longitude, pais
        FROM cidades
        ORDER BY nome
    """)

    cidades = cursor.fetchall()

    if not cidades:
        print("Nenhuma cidade salva.")
        conexao.close()
        return

    print("\n--- CIDADES FAVORITAS ---")

    for cidade in cidades:
        print(f"{cidade[0]} - {cidade[1]}, {cidade[4]}")

    try:
        id_cidade = int(input("Digite o ID da cidade que deseja remover: "))
    except ValueError:
        print("Digite um número válido.")
        conexao.close()
        return

    cidade_existe = False

    for cidade in cidades:
        if cidade[0] == id_cidade:
            cidade_existe = True
            break

    if not cidade_existe:
        print("Cidade não encontrada.")
        conexao.close()
        return

    confirmacao = input(
        f"Tem certeza que deseja remover {cidade[1]}? [s/n]: "
    ).lower()

    if confirmacao != "s":
        print("Remoção cancelada.")
        conexao.close()
        return

    conexao.execute(
        "DELETE FROM cidades WHERE id = ?",
        (id_cidade,)
    )

    conexao.commit()
    conexao.close()

    print("Cidade removida com sucesso.")