from Model.model import AcademiaModel
from View.view import AcademiaView

class AcademiaController:
    def __init__(self):
        self.model = AcademiaModel()
        self.view = AcademiaView()

    def executar(self):
        while True:
            self.view.mostrar_menu()
            escolha = input("Escolha uma opção: ")

            try:
                escolha_int = int(escolha)

                if escolha == '1':
                    nome, idade, sexo, endereco, telefone = self.view.obter_dados_cliente()
                    self.model.criar_cliente(nome, idade, sexo, endereco, telefone)
                elif escolha == '2':
                    nome, especializacao, experiencia, numero_registro = self.view.obter_dados_treinador()
                    self.model.criar_treinador(nome, especializacao, experiencia, numero_registro)
                elif escolha == '3':
                    clientes = self.model.listar_clientes()
                    self.view.listar_pessoas(clientes)
                elif escolha == '4':
                    treinadores = self.model.listar_treinadores()
                    self.view.listar_pessoas(treinadores)
                elif escolha == '5':
                    id = int(input("ID do cliente a ser atualizado: "))
                    nome, idade, sexo, endereco, telefone = self.view.obter_dados_cliente()
                    self.model.atualizar_cliente(id, nome, idade, sexo, endereco, telefone)
                elif escolha == '6':
                    id = int(input("ID do treinador a ser atualizado: "))
                    nome, especializacao, experiencia, numero_registro = self.view.obter_dados_treinador()
                    self.model.atualizar_treinador(id, nome, especializacao, experiencia, numero_registro)
                elif escolha == '7':
                    id = int(input("ID do cliente a ser excluído: "))
                    self.model.excluir_cliente(id)
                elif escolha == '8':
                    id = int(input("ID do treinador a ser excluído: "))
                    self.model.excluir_treinador(id)
                elif escolha == '9':
                    break
                else:
                    print("Digite uma das opções de 1 a 9!")
            except ValueError:
                print("Digite uma das opções de 1 a 9!")

    def encerrar(self):
        self.model.close_connection()
