# Iportando SQLite
import sqlite3 as lite

#criando conexão
try:
    con = lite.connect('cadastro_alunos.db')
    print('Conexão com o Banco de Dados realizado com Sucesso!')

except lite.Error as e:
    print("Erro ao conectar com o Banco de Dados:", e)

# Tabela de Cursos ------------------------------------

# Criar Cursos ( Create C )
def criar_curso(i):
     with con:
        cur = con.cursor()
        query = "INSERT INTO Cursos (nome, duracao, preco) VALUES (?,?,?)"
        cur.execute(query,i)

#criar_curso(['Python','Semanas', 50])

# Ver todos os cursos ( Read R )
def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Cursos')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista

#print(ver_cursos())       

# Atualizar os Cursos ( Update U )
def atualizar_curso(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Cursos SET nome=?, duracao=?, preco=?  WHERE id=?"
        cur.execute(query,i)


l = ['Python','Duas Semanas', 50.0, 1]


# Deletar os Cursos ( Delete D )
def deletar_curso(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Cursos WHERE id=?"
        cur.execute(query,i)
