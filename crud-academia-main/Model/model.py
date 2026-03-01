import sqlite3

class AcademiaModel:
    def __init__(self):
        self.conn = sqlite3.connect("academia.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER,
            sexo TEXT,
            endereco TEXT,
            telefone TEXT
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS treinadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            especializacao TEXT,
            experiencia INTEGER,
            numero_registro TEXT
        )
        """)
        self.conn.commit()

    def criar_cliente(self, nome, idade, sexo, endereco, telefone):
        self.cursor.execute("INSERT INTO clientes (nome, idade, sexo, endereco, telefone) VALUES (?, ?, ?, ?, ?)",
                            (nome, idade, sexo, endereco, telefone))
        self.conn.commit()

    def criar_treinador(self, nome, especializacao, experiencia, numero_registro):
        self.cursor.execute("INSERT INTO treinadores (nome, especializacao, experiencia, numero_registro) VALUES (?, ?, ?, ?)",
                            (nome, especializacao, experiencia, numero_registro))
        self.conn.commit()

    def listar_clientes(self):
        self.cursor.execute("SELECT * FROM clientes")
        return self.cursor.fetchall()

    def listar_treinadores(self):
        self.cursor.execute("SELECT * FROM treinadores")
        return self.cursor.fetchall()

    def atualizar_cliente(self, id, nome, idade, sexo, endereco, telefone):
        self.cursor.execute("UPDATE clientes SET nome=?, idade=?, sexo=?, endereco=?, telefone=? WHERE id=?",
                            (nome, idade, sexo, endereco, telefone, id))
        self.conn.commit()

    def atualizar_treinador(self, id, nome, especializacao, experiencia, numero_registro):
        self.cursor.execute("UPDATE treinadores SET nome=?, especializacao=?, experiencia=?, numero_registro=? WHERE id=?",
                            (nome, especializacao, experiencia, numero_registro, id))
        self.conn.commit()

    def excluir_cliente(self, id):
        self.cursor.execute("DELETE FROM clientes WHERE id=?", (id,))
        self.conn.commit()

    def excluir_treinador(self, id):
        self.cursor.execute("DELETE FROM treinadores WHERE id=?", (id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
