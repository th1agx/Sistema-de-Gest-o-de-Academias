import tkinter as tk
from tkinter import ttk
from Controller.controller import AcademiaController

class AcademiaGUI:
    def __init__(self, root):
        self.controller = AcademiaController()
        self.root = root
        self.root.title("Sistema de Gestão de Academias")

        # Quadro para operações de cliente
        self.frame_cliente = ttk.Frame(self.root)
        self.frame_cliente.pack(side=tk.LEFT, padx=20, pady=20)
        self.create_cliente_interface()

        # Quadro para operações de treinador
        self.frame_treinador = ttk.Frame(self.root)
        self.frame_treinador.pack(side=tk.RIGHT, padx=20, pady=20)
        self.create_treinador_interface()

    def create_cliente_interface(self):
        label_cliente = ttk.Label(self.frame_cliente, text="Cadastro de Cliente")
        label_cliente.grid(column=0, row=0, columnspan=2, pady=5)

        # Rótulos e Entradas para os campos de entrada do cliente
        ttk.Label(self.frame_cliente, text="Nome:").grid(column=0, row=1, sticky='w', padx=5)
        self.nome_entry = ttk.Entry(self.frame_cliente)
        self.nome_entry.grid(column=1, row=1, padx=5)

        ttk.Label(self.frame_cliente, text="Idade:").grid(column=0, row=2, sticky='w', padx=5)
        self.idade_entry = ttk.Entry(self.frame_cliente)
        self.idade_entry.grid(column=1, row=2, padx=5)

        ttk.Label(self.frame_cliente, text="Sexo:").grid(column=0, row=3, sticky='w', padx=5)
        self.sexo_entry = ttk.Entry(self.frame_cliente)
        self.sexo_entry.grid(column=1, row=3, padx=5)

        ttk.Label(self.frame_cliente, text="Endereço:").grid(column=0, row=4, sticky='w', padx=5)
        self.endereco_entry = ttk.Entry(self.frame_cliente)
        self.endereco_entry.grid(column=1, row=4, padx=5)

        ttk.Label(self.frame_cliente, text="Telefone:").grid(column=0, row=5, sticky='w', padx=5)
        self.telefone_entry = ttk.Entry(self.frame_cliente)
        self.telefone_entry.grid(column=1, row=5, padx=5)

        # Botões para operações de cliente
        button_criar_cliente = ttk.Button(self.frame_cliente, text="Criar Cliente", command=self.criar_cliente)
        button_criar_cliente.grid(column=0, row=6, columnspan=2, pady=10)

        button_listar_clientes = ttk.Button(self.frame_cliente, text="Listar Clientes", command=self.listar_clientes)
        button_listar_clientes.grid(column=0, row=7, columnspan=2, pady=10)

        # Seção para mostrar dados de clientes
        self.clientes_text = tk.Text(self.frame_cliente, height=10, width=40)
        self.clientes_text.grid(column=0, row=8, columnspan=2, pady=10)
        
    def create_treinador_interface(self):
        label_treinador = ttk.Label(self.frame_treinador, text="Cadastro de Treinador")
        label_treinador.grid(column=0, row=0, columnspan=2, pady=5)

        # Rótulos e Entradas para os campos de entrada do treinador
        ttk.Label(self.frame_treinador, text="Nome:").grid(column=0, row=1, sticky='w', padx=5)
        self.nome_treinador_entry = ttk.Entry(self.frame_treinador)
        self.nome_treinador_entry.grid(column=1, row=1, padx=5)

        ttk.Label(self.frame_treinador, text="Especialização:").grid(column=0, row=2, sticky='w', padx=5)
        self.especializacao_entry = ttk.Entry(self.frame_treinador)
        self.especializacao_entry.grid(column=1, row=2, padx=5)

        ttk.Label(self.frame_treinador, text="Experiência:").grid(column=0, row=3, sticky='w', padx=5)
        self.experiencia_entry = ttk.Entry(self.frame_treinador)
        self.experiencia_entry.grid(column=1, row=3, padx=5)

        ttk.Label(self.frame_treinador, text="Número de Registro:").grid(column=0, row=4, sticky='w', padx=5)
        self.numero_registro_entry = ttk.Entry(self.frame_treinador)
        self.numero_registro_entry.grid(column=1, row=4, padx=5)

        # Botões para operações de treinador
        button_criar_treinador = ttk.Button(self.frame_treinador, text="Criar Treinador", command=self.criar_treinador)
        button_criar_treinador.grid(column=0, row=5, columnspan=2, pady=10)

        button_listar_treinadores = ttk.Button(self.frame_treinador, text="Listar Treinadores", command=self.listar_treinadores)
        button_listar_treinadores.grid(column=0, row=6, columnspan=2, pady=10)

        # Seção para mostrar dados de treinadores
        self.treinadores_text = tk.Text(self.frame_treinador, height=10, width=40)
        self.treinadores_text.grid(column=0, row=7, columnspan=2, pady=10)

    def criar_cliente(self):
        nome = self.nome_entry.get()
        idade = self.idade_entry.get()
        sexo = self.sexo_entry.get()
        endereco = self.endereco_entry.get()
        telefone = self.telefone_entry.get()

        self.controller.model.criar_cliente(nome, idade, sexo, endereco, telefone)
        self.listar_clientes()

    def listar_clientes(self):
        clientes = self.controller.model.listar_clientes()
        self.clientes_text.delete(1.0, tk.END)
        for cliente in clientes:
            self.clientes_text.insert(tk.END, f"{cliente}\n")

    def criar_treinador(self):
        nome = self.nome_treinador_entry.get()
        especializacao = self.especializacao_entry.get()
        experiencia = self.experiencia_entry.get()
        numero_registro = self.numero_registro_entry.get()

        self.controller.model.criar_treinador(nome, especializacao, experiencia, numero_registro)
        self.listar_treinadores()

    def listar_treinadores(self):
        treinadores = self.controller.model.listar_treinadores()
        self.treinadores_text


if __name__ == "__main__":
    root = tk.Tk()
    app = AcademiaGUI(root)
    root.mainloop()
