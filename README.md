<h1  align="center">

COW - Chatbot para Whatsapp

</h1>

<p  align="center">

<img  alt="progress"  src="https://img.shields.io/badge/status-in_progress-blue">

</p>

<h4  align="center">

<a  href="#pencil-sobre-o-projeto">Sobre o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;

<a  href="#rocket-stack">Stack</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;

<a  href="#blue_book-configurando-ambiente">Configurando ambiente</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;

</h4>

  

## :pencil: Sobre o projeto

**Resumo**: O presidente de uma empresa júnior local pediu para você, que projetasse um chatbot para automatizar seus atendimentos no whatsapp. Ele precisa que você mostre as principais informações e serviços de sua EJ. Além de atrair mais clientes, ele deseja automatizar algumas funções. O seu trabalho é desenvolver um assistente virtual capaz de atender os pedidos e encaminha-los para produção. Espera-se que o chatbot envie todas as requisições já feitas para um banco de dados afim de serem armazenadas e usadas posteriormente.

  

**Objetivo**:

Integrar tecnologias de automação ao whatsapp

  

## :rocket: Stack

<p  align="center">

  
  

<img  alt="Rasa"  src="https://img.shields.io/badge/Rasa-chatbot-blueviolet?style=for-the-badge">

  

<img  alt="Scrapy"  src="https://img.shields.io/badge/Scrapy-Backend-orange?style=for-the-badge">

  

<img  alt="Selenium"  src="https://img.shields.io/badge/Selenium-backend-blue?style=for-the-badge">

  

</p>

  

## :blue_book: Configurando ambiente

### Usando máquina virtual  

Antes de começar, é preciso ter duas ferramentas instaladas:

- **Pyenv** : Permite que você instale outras versões do python em sua máquina

- **Virtualenv**: Permite criar ambientes virtuais em sua máquina


```bash

# clone o projeto

git https://github.com/grvela/chatterbox.git

# instale a versão 

pyenv install 3.7.0
```
 Com virtualenv:
```bash
# crie uma máquina virtual a partir dela

virtualenv -p ~/.pyenv/versions/3.7.0/bin/python nome_da_máquina_virtual

# ative sua máquina virtual

source nome_da_máquina_virtual/bin/activate
```
Com pyenv:
```bash

# crie uma máquina virtual a partir dela

pyenv virtualenv 3.7.0 nome_da_máquina_virtual

# ative sua máquina virtual

pyenv activate nome_da_máquina_virtual

  

# Por fim, instale as tecnologias utilizadas

pip install -r requirements.txt

```
### Usando Docker

Antes de começar, é preciso ter duas ferramentas instaladas:

- **Docker** : Permite criar e usar containeres

- **Docker Compose**: Permite rodar multiplos containeres 

```bash
 //TO DO 
 docker-compose up
```
    

## Bom code! ##