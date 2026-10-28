# 📘 Assignment: Persistent Task Manager with SQLite

## 🎯 Objective

Crie um gerenciador de tarefas no terminal que salve os dados em um banco SQLite. Você praticará a criação de tabelas e operações CRUD em Python usando a biblioteca padrão `sqlite3`.

## 📝 Tasks

### 🛠️ Create the Database

#### Descrição
Complete `initialize_database()` no arquivo inicial para criar o banco e a tabela de tarefas. A inicialização deve poder ser executada mais de uma vez sem apagar os dados existentes.

#### Requisitos
O programa concluído deve:

- Criar o arquivo `tasks.db` ao iniciar
- Criar uma tabela `tasks` com `id`, `title` e `completed`
- Definir `id` como chave primária, `title` como campo obrigatório e `completed` como inteiro com valor padrão `0`
- Preservar a tabela e os dados quando o programa for iniciado novamente

### 🛠️ Add and List Tasks

#### Descrição
Implemente as funções para cadastrar tarefas e exibir as tarefas salvas no banco. Use consultas parametrizadas para inserir os títulos.

#### Requisitos
O programa concluído deve:

- Salvar cada tarefa em uma linha da tabela `tasks`
- Ignorar títulos vazios ou compostos apenas por espaços
- Listar o ID, o título e o estado de cada tarefa
- Mostrar uma mensagem adequada quando ainda não houver tarefas

### 🛠️ Complete and Remove Tasks

#### Descrição
Implemente as opções restantes do menu para marcar uma tarefa como concluída ou removê-la do banco de dados.

#### Requisitos
O programa concluído deve:

- Atualizar `completed` para `1` quando uma tarefa for concluída
- Remover a tarefa correspondente ao ID informado
- Manter as alterações salvas depois que o programa for encerrado
- Informar quando o ID informado não corresponder a uma tarefa

O módulo `sqlite3` já faz parte do Python, então nenhuma dependência externa é necessária. Execute a atividade com `python starter-code.py`; o arquivo `tasks.db` será criado na pasta atual.