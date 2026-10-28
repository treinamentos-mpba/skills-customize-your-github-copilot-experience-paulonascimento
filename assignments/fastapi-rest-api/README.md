# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar um catálogo de livros usando FastAPI. Você praticará rotas HTTP, validação de dados com modelos, códigos de status e operações CRUD.

## 📝 Tasks

### 🛠️ Consultar Livros

#### Descrição
Complete os endpoints de consulta no arquivo inicial. A API deve permitir listar os livros cadastrados e buscar um livro pelo seu ID.

#### Requisitos
O programa concluído deve:

- Responder a `GET /books` com a lista de livros, começando com uma lista vazia
- Responder a `GET /books/{book_id}` com o livro correspondente
- Retornar o status HTTP `404` quando o ID solicitado não existir
- Exibir a documentação interativa em `/docs`

### 🛠️ Cadastrar Livros

#### Descrição
Adicione um endpoint para cadastrar livros. Use os modelos Pydantic fornecidos para validar os dados recebidos pela API.

#### Requisitos
O programa concluído deve:

- Aceitar `POST /books` com `title`, `author` e `published_year`
- Gerar um ID único e armazenar o novo livro durante a execução do servidor
- Retornar o livro criado com status HTTP `201`
- Rejeitar dados inválidos com a resposta de validação padrão do FastAPI

Exemplo de corpo da requisição:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien",
  "published_year": 1937
}
```

### 🛠️ Atualizar e Remover Livros

#### Descrição
Complete as operações restantes para que clientes possam substituir os dados de um livro e removê-lo do catálogo.

#### Requisitos
O programa concluído deve:

- Aceitar `PUT /books/{book_id}` com os campos `title`, `author` e `published_year`
- Atualizar o livro existente e retornar seus dados atualizados
- Aceitar `DELETE /books/{book_id}` e responder com status HTTP `204` quando a remoção for concluída
- Retornar status HTTP `404` ao tentar atualizar ou remover um livro inexistente

Para executar o starter, instale as dependências com `python -m pip install fastapi uvicorn` e inicie o servidor com `python starter-code.py`. Acesse `http://127.0.0.1:8000/docs` para testar os endpoints.