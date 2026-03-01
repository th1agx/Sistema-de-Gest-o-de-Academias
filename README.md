# Sistema de Gestão de Academias

Este repositório contém um pequeno sistema em Python para cadastro e gerenciamento de clientes e treinadores de uma academia. O projeto segue o padrão MVC (Model-View-Controller) e oferece duas interfaces:

- Interface de linha de comando (CLI) para interação básica
- Interface gráfica (GUI) utilizando `tkinter` para operações de cadastro e listagem

---

## 🧩 Funcionalidades

- Criar, listar, atualizar e excluir clientes
- Criar, listar, atualizar e excluir treinadores
- Armazenamento persistente usando banco de dados SQLite (`academia.db`)
- Validação simples de entradas na camada de visualização

---

## 🗂 Estrutura do Projeto

```
crud-academia-main/
├── Controller/
│   └── controller.py        # Lógica de controle do fluxo de aplicação
├── Model/
│   └── model.py             # Acesso ao banco de dados e operações CRUD
├── View/
│   └── view.py              # Funções de entrada/saída e validação
├── academia_interface.py    # Interface gráfica com tkinter
├── main.py                  # Ponto de entrada para a versão CLI
└── README.md                # Documentação do projeto
```

---

## ✅ Requisitos

- Python 3.7 ou superior (testado em 3.14)
- Biblioteca padrão `sqlite3` (já vem com Python)
- `tkinter` para a GUI (normalmente incluído nas instalações padrão do Python)

---

## ⚙️ Instalação

1. Clone este repositório ou copie os arquivos para seu ambiente de trabalho.
2. (Opcional) crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```
3. Instale dependências se houver (não são necessárias para este projeto simples). Apenas certifique-se de ter o Python e o tkinter configurados.

---

## 🚀 Uso

### Interface de linha de comando (CLI)

Execute o módulo principal para iniciar o menu interativo:

```bash
python main.py
```

Siga as instruções exibidas e digite o número da opção desejada.

### Interface gráfica (GUI)

Execute o script `academia_interface.py` para abrir a janela gráfica:

```bash
python academia_interface.py
```

Use os campos e botões para cadastrar ou listar clientes e treinadores.

> Observação: a GUI atual apenas exibe clientes e treinadores cadastrados; a atualização e exclusão ainda não foram implementadas nessa interface.

---

## 📘 Banco de Dados

O arquivo `academia.db` é criado automaticamente no diretório de trabalho ao iniciar o sistema. Contém duas tabelas:

- `clientes` (id, nome, idade, sexo, endereco, telefone)
- `treinadores` (id, nome, especializacao, experiencia, numero_registro)

---

## 🛠️ Contribuições

Este projeto é um exercício acadêmico. Você pode adaptá-lo, estender as funcionalidades (por exemplo, adicionando atualização/exclusão na GUI) ou usá-lo como base para projetos maiores.

---

## 📄 Licença

Sinta-se à vontade para usar e modificar o código conforme necessário. Não há uma licença explícita no repositório.

---

Qualquer dúvida ou sugestão, entre em contato. 💡
