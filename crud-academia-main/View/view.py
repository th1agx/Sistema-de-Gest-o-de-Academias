class AcademiaView:
    @staticmethod
    def mostrar_menu():
        print("\n=== Sistema de Gestão de Academias ===")
        print("1. Criar Cliente")
        print("2. Criar Treinador")
        print("3. Listar Clientes")
        print("4. Listar Treinadores")
        print("5. Atualizar Cliente")
        print("6. Atualizar Treinador")
        print("7. Excluir Cliente")
        print("8. Excluir Treinador")
        print("9. Sair")

    @staticmethod
    def obter_dados_cliente():
        while True:
            try:
                nome = input("Nome do cliente: ")
                if any(char.isdigit() for char in nome):
                    raise ValueError("Digite apenas texto para o nome.")

                idade = input("Idade do cliente: ")
                if not idade.isdigit():
                    raise ValueError("Digite um valor numérico para a idade.")
                idade = int(idade)

                sexo = input("Sexo do cliente (Masculino/Feminino): ").lower()
                if sexo in ['m', 'masculino', 'MASCULINO']:
                    sexo = 'Masculino'
                elif sexo in ['f', 'feminino', 'FEMININO']:
                    sexo = 'Feminino'
                else:
                    raise ValueError("Digite 'Masculino' ou 'Feminino' para o sexo.")

                endereco = input("Endereço do cliente (Rua, Nº, Bairro, Cidade, CEP): ")
                telefone = input("Telefone do cliente (DDD + número com 9 dígitos): ")

                if len(telefone) != 11 or not telefone.isdigit():
                    raise ValueError("Telefone deve conter DDD e 9 dígitos numéricos.")

                return nome, idade, sexo, endereco, telefone
            except ValueError as e:
                print(f"Erro: {e}. Por favor, preencha corretamente.\n")

    @staticmethod
    def obter_dados_treinador():
        while True:
            try:
                nome = input("Nome do treinador: ")
                if any(char.isdigit() for char in nome):
                    raise ValueError("Digite apenas texto para o nome.")

                especializacao = input("Especialização do treinador: ")
                experiencia = input("Experiência do treinador (ex: 12 meses, 04 anos): ")
                numero_registro = input("Número de registro do treinador: ")

                return nome, especializacao, experiencia, numero_registro
            except ValueError as e:
                print(f"Erro: {e}. Por favor, preencha corretamente.\n")

    @staticmethod
    def listar_pessoas(pessoas):
        for pessoa in pessoas:
            print(pessoa)
