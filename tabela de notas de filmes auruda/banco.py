import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bita2020",
    database="biblioteca_filmes"
)

cursor = conexao.cursor()

def inserir(nome, genero, nota, assistido):
    sql = """
    INSERT INTO filmes (nome, genero, nota, assistido)
    VALUES (%s, %s, %s, %s)
    """

    valores = (nome, genero, nota, assistido)

    cursor.execute(sql, valores)
    conexao.commit()