# CRUD Flask - Gerenciamento de Tarefas

## Índice de Conteúdo

- [Introdução](#introdução)
- [Tecnologias](#tecnologias)
- [Instalação](#instalação)
- [Como Rodar o Projeto](#como-rodar-o-projeto)
- [Escopo de Funcionalidades](#escopo-de-funcionalidades)
- [Exemplo de Uso](#exemplo-de-uso)
- [Status do Projeto](#status-do-projeto)
- [Contribuindo](#contribuindo)
- [Referências](#referências)

## Introdução

Este projeto é um sistema CRUD (Create, Read, Update, Delete) para gerenciamento de tarefas. Ele permite que os usuários criem, listem, atualizem e excluam tarefas de uma lista. O projeto foi desenvolvido utilizando Flask e SQLite, com uma interface simples em HTML/CSS. É uma aplicação prática para aprender a desenvolver um sistema CRUD com Flask e SQLite.

## Tecnologias

O projeto utiliza as seguintes tecnologias:

- **Python**: Linguagem principal utilizada no desenvolvimento.
- **Flask**: Framework para desenvolvimento de aplicações web.
- **SQLite**: Banco de dados relacional embutido utilizado para o armazenamento local de dados.
- **HTML/CSS**: Para a criação da interface de usuário simples.

## Instalação

Para instalar o projeto em seu ambiente local, siga as instruções abaixo:

1. Clone este repositório:

```bash
git clone https://github.com/SeuUsuario/task_simples.git
```
2. Acesse a pasta do projeto:
```bash
cd task_simples
```
## Siga os passos abaixo para rodar o projeto em seu ambiente local:

Crie e ative um ambiente virtual (opcional, mas recomendado):

No Linux/Mac:
python3 -m venv venv
source venv/bin/activate

No Windows:
python -m venv venv
venv\Scripts\activate

Instale as dependências:
pip install -r requirements.txt

Execute a aplicação:
python app.py

O servidor iniciará na porta 8080. Acesse a aplicação em http://127.0.0.1:8080.
Caso queira rodar em uma porta diferente, utilize:
flask run --port=5001

## Escopo de Funcionalidades
A aplicação oferece as seguintes funcionalidades:

Listar Tarefas: Visualização de todas as tarefas cadastradas.

Criar Tarefa: Adicionar uma nova tarefa ao banco de dados.

Ler Informações de Tarefa: Visualizar os detalhes de uma tarefa específica.

Atualizar Tarefa: Modificar as informações de uma tarefa existente.

Excluir Tarefa: Remover uma tarefa do sistema.

Cada tarefa possui os seguintes atributos:

id: Identificador único da tarefa.

title: Título da tarefa.

description: Descrição detalhada da tarefa.

created_at: Data de criação da tarefa.

## Exemplo de Uso
Para cadastrar uma nova tarefa, navegue até a página de criação de tarefas, preencha o 
formulário com os dados necessários (título e descrição), e envie o formulário. A nova tarefa aparecerá na lista de tarefas.

Exemplo de URL para Cadastro:
http://127.0.0.1:8080/add

## Status do Projeto
O status do projeto é ativo e funcional. Todos os endpoints CRUD estão implementados. O projeto está pronto para ser utilizado, e melhorias adicionais, como autenticação e otimizações de desempenho, podem ser consideradas em versões futuras.

## Referências
Consulte a documentação oficial do Flask e SQLite para mais informações sobre as tecnologias utilizadas:

- [Documentação oficial do Flask](https://flask.palletsprojects.com/)
- [Documentação oficial do SQLite](https://www.sqlite.org/docs.html)

O projeto segue uma estrutura padrão de aplicações Flask e é open-source, permitindo modificações e distribuição livre.
