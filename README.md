# Clima App

Projeto desenvolvido em Python para estudar consumo de APIs, organização de código, SQLite e manipulação de dados.

> Este projeto foi criado para fins de estudo e aprendizado. Não é uma aplicação pronta para produção.

## Sobre o projeto

O programa permite:

- buscar uma cidade pela API de geocodificação da Open-Meteo;
- obter latitude e longitude da cidade;
- consultar a previsão do tempo;
- mostrar as condições de hoje e amanhã;
- salvar cidades favoritas em um banco SQLite;
- listar cidades salvas;
- consultar a previsão de uma cidade favorita.

## Tecnologias utilizadas

- Python
- Requests
- SQLite
- Open-Meteo API
- Git e GitHub

## Estrutura do projeto

```text
clima-app/
├── main.py
├── clima.py
├── lugar.py
├── banco.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Como o projeto funciona

O programa usa duas APIs da Open-Meteo:

```text
Nome da cidade
        ↓
API de geocodificação
        ↓
Latitude e longitude
        ↓
API de previsão do tempo
        ↓
Clima de hoje e amanhã
```

As cidades favoritas são armazenadas localmente em um banco SQLite.

## Requisitos

- Python 3.10 ou superior
- `pip`
- Acesso à internet

## Como executar

Clone o repositório:

```bash
git clone https://github.com/Pablo-hsr/consultar-tempo
```

Entre na pasta:

```bash
cd clima-app
```

Crie um ambiente virtual:

```bash
python -m venv .venv
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
pip install -r requirements.txt
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

Para instalar:

```bash
pip install -r requirements.txt
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
- operações `INSERT` e `SELECT`;
- criação de menus no terminal;
- uso de ambientes virtuais;
- versionamento com Git e GitHub.

## Possíveis melhorias

Algumas ideias para continuar o desenvolvimento:

- permitir remover cidades favoritas;
- impedir cidades duplicadas;
- consultar várias cidades de uma vez;
- mostrar previsão para mais dias;
- adicionar previsão por hora;
- criar alertas de chuva;
- mostrar umidade e velocidade do vento;
- salvar histórico de consultas;
- adicionar qualidade do ar;
- criar uma interface gráfica;
- transformar o projeto em uma aplicação web.

## Observação

A Open-Meteo é utilizada neste projeto como fonte de dados meteorológicos. Consulte a [documentação oficial da Open-Meteo](https://open-meteo.com/en/docs) para conhecer os parâmetros disponíveis.

Este projeto foi criado por Pablo Henrique como parte dos meus estudos de programação e desenvolvimento de software.
