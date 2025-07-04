# Importando SQLite3

import sqlite3

#criando conexão
try:
    con = sqlite3.connect('cadastro_alunos.db')
    print('Conexão com o Banco de Dados realizado com Sucesso!')

except sqlite3.Error as e:
    print("Erro ao conectar com o Banco de Dados:", e)

# Criando tabela de cursos

    try:
        with con:
            cur = con.cursor()
            cur.execute(""" CREATE TABLE IF NOT EXISTS cursos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                duracao TEXT,
                preco REAL
            )""")

            print("Tabela Cursos criada com Sucesso!")

    except sqlite3.Error as e:
        print("Erro ao criar a tabela Cursos:", e)

# Criando tabela de turmas

    try:
        with con:
            cur = con.cursor()
            cur.execute(""" CREATE TABLE IF NOT EXISTS turmas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                curso_nome TEXT,
                data_inicio DATE,
                FOREIGN KEY (curso_nome) REFERENCES cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE
            )""")

            print("Tabela Turmas criada com Sucesso!")

    except sqlite3.Error as e:
        print("Erro ao criar a tabela Turmas:", e)
       
       
# Criando tabela de alunos

    try:
        with con:
            cur = con.cursor()
            cur.execute(""" CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                email TEXT,
                telefone TEXT,
                sexo TEXT,
                imagem TEXT,
                data_de_nascimento DATE,
                cpf TEXT,
                turma_nome TEXT,                
                FOREIGN KEY (turma_nome) REFERENCES tumas (nome) ON DELETE CASCADE 
            )""")

            print("Tabela Alunos criada com Sucesso!")

    except sqlite3.Error as e:
        print("Erro ao criar a tabela Alunos:", e)


  