# Clima App

Projeto desenvolvido em Python para estudar consumo de APIs, organização de código, SQLite e manipulação de dados.

> Este projeto foi criado para fins de estudo e aprendizado. Não é uma aplicação pronta para produção.

## Sobre o projeto

O Clima App é uma aplicação executada no terminal que consulta a previsão do tempo para cidades favoritas.

O programa permite:

- buscar uma cidade pela API de geocodificação da Open-Meteo;
- obter latitude e longitude da cidade;
- consultar a previsão do tempo;
- mostrar as condições de hoje e amanhã;
- exibir temperatura mínima e máxima;
- mostrar chance de chuva;
- exibir índice UV e velocidade do vento;
- gerar recomendações no modo “Recomendacao ao sair?”;
- salvar cidades favoritas em um banco SQLite;
- listar cidades salvas;
- consultar a previsão de uma cidade favorita;
- remover cidades favoritas.

## Tecnologias utilizadas

- Python
- Requests
- SQLite
- Open-Meteo API
- Git
- GitHub

## Como o projeto funciona

O programa utiliza a API de geocodificação da Open-Meteo para transformar o nome de uma cidade em coordenadas geográficas.

Depois, essas coordenadas são utilizadas pela API de previsão do tempo.

```text
Nome da cidade
        ↓
API de geocodificação
        ↓
Latitude e longitude
        ↓
API de previsão do tempo
        ↓
Previsão de hoje e amanhã
        ↓
Recomendações para sair
```

As cidades favoritas são armazenadas localmente em um banco de dados SQLite.

## Modo Recomendacao ao sair?”

O modo “Recomendacao ao sair” analisa os dados da previsão e exibe recomendações para o usuário.

O programa considera informações como:

- temperatura máxima;
- temperatura mínima;
- chance de chuva;
- índice UV;
- velocidade do vento;
- código da condição climática.

Exemplos de recomendações:

```text
Leve um guarda-chuva.
Está quente. Leve água.
Use protetor solar.
Considere levar um casaco.
O clima parece tranquilo para sair.
```

Essas recomendações são baseadas nos dados retornados pela API e servem apenas como orientação.

## Estrutura do projeto

```text
consultar-tempo/
├── main.py
├── clima.py
├── lugar.py
├── banco.py
├── requirements.txt
├── .gitignore
└── README.md
```

### `main.py`

Responsável pelo menu principal e pelo fluxo da aplicação.

### `clima.py`

Responsável por consultar a previsão do tempo e gerar descrições e recomendações climáticas.

### `lugar.py`

Responsável por buscar cidades e obter suas coordenadas geográficas.

### `banco.py`

Responsável pelas operações no banco SQLite, como:

- criar a tabela;
- salvar cidades;
- listar cidades;
- remover cidades.

## Requisitos

- Python 3.10 ou superior;
- `pip`;
- acesso à internet.

## Como executar

Clone o repositório:

```bash
git clone [https://github.com/Pablo-hsr/consultar-tempo](https://github.com/Pablo-hsr/consultar-tempo)
```

Entre na pasta:

```bash
cd consultar-tempo
```

Crie um ambiente virtual:

```bash
python3 -m venv .venv
```

Ative o ambiente virtual no Linux ou macOS:

```bash
source .venv/bin/activate
```

No Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Execute o programa:

```bash
python main.py
```

## Menu atual

```text
1 - Salvar cidade favorita
2 - Listar cidades favoritas
3 - Ver previsão
4 - Remover cidade
5 - Recomendacao ao sair
0 - Sair
```

## Banco de dados

O projeto utiliza SQLite para armazenar as cidades favoritas.

O banco é criado automaticamente quando o programa é executado pela primeira vez.

As informações salvas incluem:

- ID da cidade;
- nome;
- latitude;
- longitude;
- país.

O arquivo do banco é local e está listado no `.gitignore`.

## Dependências

O arquivo `requirements.txt` contém as bibliotecas necessárias:

```text
requests
```

Para instalar manualmente:

```bash
python -m pip install requests
```

Ou para instalar todas as dependências do projeto:

```bash
python -m pip install -r requirements.txt
```

## Objetivos de estudo

Este projeto está sendo desenvolvido para praticar:

- consumo de APIs REST;
- requisições HTTP com Python;
- parâmetros de URL;
- leitura de respostas JSON;
- criação e uso de funções;
- organização de código em módulos;
- tratamento de erros;
- uso do SQLite;
- operações `INSERT`, `SELECT` e `DELETE`;
- criação de menus no terminal;
- uso de ambientes virtuais;
- versionamento com Git e GitHub;
- separação de responsabilidades;
- criação de regras de negócio;
- interpretação de dados retornados por APIs.

## Possíveis melhorias

Algumas ideias para continuar o desenvolvimento:

- impedir cidades duplicadas;
- consultar várias cidades de uma vez;
- mostrar previsão para mais dias;
- adicionar previsão por hora;
- melhorar as descrições das condições climáticas;
- adicionar alertas de chuva;
- mostrar qualidade do ar;
- salvar histórico de consultas;
- permitir editar cidades favoritas;
- criar testes automatizados;
- criar uma interface gráfica;
- transformar o projeto em uma aplicação web.

## Limitações atuais

- A previsão depende da disponibilidade das APIs externas.
- O programa funciona apenas pelo terminal.
- As recomendações do modo “Recomendacao ao sair?” são baseadas em regras simples.
- As cidades favoritas são armazenadas apenas localmente.
- O projeto ainda não possui autenticação de usuários.

## Observação

A Open-Meteo é utilizada neste projeto como fonte de dados meteorológicos.

Consulte a [documentação oficial da Open-Meteo](https://open-meteo.com/en/docs) para conhecer os endpoints e parâmetros disponíveis.
