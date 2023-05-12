
<div  align="center">

  
  

# README - Telegram Bot para compartilhar Livros

  

Este código é um bot para Telegram que permite que os usuários escolham um livro de uma lista de opções e recebam o arquivo PDF correspondente. O bot é baseado na biblioteca Python `telebot`.

  

## Configuração do Bot

  

Antes de executar o código, é necessário criar um bot no Telegram e obter o token de acesso. O token deve ser adicionado à linha de código que inicia o bot:

  
  

`bot = telebot.TeleBot(token='<seu_token_aqui>', parse_mode='HTML')`

  

## Funcionalidades do Bot

  

### Início do Bot

  

Quando o usuário envia o comando `/start`, o bot envia uma mensagem de boas-vindas com algumas opções de escolha, usando um botão inline keyboard.

  

### Escolha de Livro

  

Quando o usuário escolhe a opção "livros", o bot envia uma lista de livros disponíveis para download, usando outro botão inline keyboard.

  

### Envio de Documento

  

Quando o usuário escolhe um livro, o bot envia o arquivo PDF correspondente, usando o método `send_document`. O bot também inclui uma opção "voltar" para retornar à lista de livros.

  

## Como Executar o Bot

  

Para executar o bot, é necessário ter o Python instalado e as seguintes bibliotecas:

  

-  `telebot`

-  `types`

  

O bot pode ser executado em um ambiente de desenvolvimento, ou a partir do prompt de comando:



`python <nome_do_arquivo>.py`

  

Certifique-se de que o token do bot esteja correto. O bot ficará em execução e responderá às mensagens dos usuários.

</div>