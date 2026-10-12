House Database é um projeto desenvolvido com Django que tem como objetivo centralizar e organizar informações sobre os objetos e bens presentes em uma residência.

A proposta é criar um sistema que funcione como um banco de dados doméstico, permitindo registrar objetos, armazenar suas características e facilitar o gerenciamento dos bens compartilhados ou pertencentes aos moradores de uma casa.
O projeto tem como principal objetivo aplicar e demonstrar conhecimentos em desenvolvimento web e bancos de dados relacionais, utilizando uma situação prática: a organização dos bens de uma residência.

Além de facilitar o gerenciamento doméstico, o House Database serve como projeto de estudo para aprofundar conhecimentos em Django, modelagem de dados, relacionamentos entre entidades e operações CRUD.

A proposta do sistema inclui:

- Gerenciamento de objetos: cadastro e organização dos bens de uma residência.
- Cadastro de livros: armazenamento de informações como título, autor e outras características.
- Gerenciamento de veículos: registro de motos, carros e suas respectivas características.
- Organização por moradores: associação dos objetos aos seus respectivos proprietários ou responsáveis.
- Armazenamento centralizado: informações organizadas em um banco de dados.
- Consulta e manutenção de registros: possibilidade de visualizar, atualizar e excluir informações cadastradas.

As funcionalidades serão desenvolvidas e ampliadas conforme a evolução do projeto.

Tecnologias utilizadas

- Python — linguagem de programação.
- Django — framework para desenvolvimento web.
- Banco de dados relacional — armazenamento e organização das informações.
- HTML e CSS — estrutura e estilização das páginas.
- Docker e Docker Compose — execução e gerenciamento do ambiente de desenvolvimento, quando configurados.

Modelagem de dados

Um dos principais focos do House Database é a estruturação do banco de dados.

O sistema pode ser organizado em entidades relacionadas, como:

- Moradores: informações sobre as pessoas que fazem parte da residência.
- Objetos: informações gerais sobre os bens cadastrados.
- Livros: características específicas dos livros.
- Veículos: informações sobre carros e motos.
- Categorias: classificação dos objetos por tipo.

A modelagem busca evitar redundância, manter a integridade dos dados e permitir que diferentes tipos de objetos possuam características específicas sem perder a organização geral do sistema.

 Conceitos aplicados

Durante o desenvolvimento, o projeto permite praticar conceitos importantes, como:

- Modelagem de bancos de dados relacionais.
- Relacionamentos entre tabelas e entidades.
- Chaves primárias e estrangeiras.
- Operações CRUD (*Create, Read, Update e Delete*).
- Desenvolvimento de modelos, views, URLs e templates no Django.
- Validação e organização de dados.
- Separação de responsabilidades na aplicação.
- Organização de um projeto utilizando boas práticas de desenvolvimento.

Como executar o projeto

### Pré-requisitos

- Python instalado, caso a execução seja local.
- Git.
- Docker e Docker Compose, caso utilize o ambiente conteinerizado.

### Instalação

Clone o repositório:

```bash
git clone https://github.com/GabrielsOliveiira/houseDatabase.git
```

Entre na pasta do projeto:

```bash
cd houseDatabase
```

Se o projeto estiver configurado com Docker Compose, execute:

```bash
docker compose up --build
```

Caso prefira executar localmente, crie e ative um ambiente virtual, instale as dependências do projeto e aplique as migrações:

```bash
python -m venv venv
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 👨‍💻 Sobre o projeto

O House Database é um projeto pessoal desenvolvido com o objetivo de consolidar conhecimentos em programação e bancos de dados por meio de uma aplicação prática.

Mais do que um simples cadastro de objetos, a proposta é construir uma estrutura organizada de dados que possa crescer conforme novas necessidades de gerenciamento doméstico surgirem.

**Desenvolvido por Gabriel Oliveira.**
