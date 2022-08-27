# API com Django 3: Testes, segurança, e lapidações - 6h
**Professor:** Guilherme Lima

**Disponível:** [ALURA]('https://cursos.alura.com.br/course/api-django-3-testes-seguranca-lapidacoes')

**Conteúdo:**
- Aprenda na prática como trabalhar com arquivos estáticos
- Saiba na prática como armazenar o caching no Redis
- Crie testes para verificar as principais requisições e suas respostas
- Internacionalize sua API para diversos idiomas com base nas requisições
- Descubra como proteger seus projetos feitos em Django aumentando a segurança

## 01. Upload de arquivos estáticos Ver primeiro vídeo
### Apresentação

[00:00] Olá! Meu nome é Guilherme Lima e eu serei o seu instrutor nesse treinamento de API com Django 3 Testes, Segurança e Lapidações. O que nós vamos aprender nesse curso? Nesse curso vamos aprender a incluir uploads de arquivos nas requisições e na API, vamos aprender a trabalhar com Caching e vincular o Django com Redis.

[00:19] Vamos aprender a realizar a internacionalização das nossas requisições para diferentes idiomas. Vamos realizar os testes das principais requisições que temos e vamos dar uma pitada de segurança nas aplicações desenvolvidas com Django para deixarmos o nosso projeto bem legal e completo.

[00:37] Quais são os pré-requisitos para esse curso? É muito importante que você tenha feito os cursos anteriores de Django para nós mantermos uma continuidade também nos nossos estudos. Principalmente nos cursos de desenvolvimento de API.

[00:51] Qual é o público alvo desse curso? Se você quer aprender a trabalhar com Caching, Segurança, desenvolvimento de API e aprofundar os seus conhecimentos, você é muito mais do que convidado para realizar esse treinamento comigo! Sabendo de tudo isso, vamos começar?

### Preparando o ambiente

Olá!
É muito bom receber você neste curso de API com Django 3: Testes, segurança e lapidações.

Espero que seja uma experiência de aprendizado incrível, e que possamos vencer todos os desafios juntos. Neste curso, aprofundar nossos conhecimentos no Django Rest Framework e aprender como incluir arquivos estáticos em nossas requisições, caching, internacionalização, testes e segurança.

Preparando ambiente
Além disso, para que tenhamos o mesmo resultado, é recomendado que você faça o download da mesma versão do Python e do Django que utilizei quando o curso foi gravado, que poderá ser encontrada aqui:

        Python 3.7.4
        Django 3.0.7

O Django pode ser instalado através do comando:

        pip install Django==3.0.7

Este projeto é inspirado no projeto do curso API com Django 3: Versionamento, cabeçalhos e CORS, porém não é uma continuação. Usaremos o projeto do curso citado acima. Caso não tenha visto, é recomendado para um bom proveito deste treinamento.

Sendo assim, para o acompanhamento é altamente recomendado realizar o download do projeto base [neste link]('https://github.com/alura-cursos/drf_lapidacoes/archive/projeto_inicial.zip') caso não tenha feito o curso de versionamento de API com Django 3.

Após o download do projeto base, abra o projeto em seu editor de código preferido e crie uma nova venv com o comando python -m venv ./venv e ative conforme seu sistema operacional.

Para sistemas MacOS ou Linux:

        source venv/bin/activate

Já no Windows:

        venv\Scripts\activate.bat

Após ativação, faça a instalação dos módulos necessários com o seguinte comando:

        pip install -r requirements.txt

Para finalizar, vamos carregar os dados iniciais executando o comando:

        python seed.py

Para garantir que tudo deu certo, suba o servidor:

        python manage.py runserver

Na próxima atividade, vamos aprofundar ainda mais seus conhecimentos utilizando esta incrível ferramenta de desenvolvimento.

Em caso de dúvidas durante o curso ou carregamento do projeto, conte sempre com o fórum da Alura!

: )

### Incluindo campo foto
### Upload de arquivos
### Faça como eu fiz
### Upload de PDF
### O que aprendemos?
## 02. Caching
### Projeto da aula anterior
### Caching
### Para saber mais: args e kwargs
### Instalando o Redis
### Integrando Django e Redis
### Faça como eu fiz
### Definindo cache
### O que aprendemos?
## 03. Limitando ações no Viewset e Permissões
### Projeto da aula anterior
### Internacionalização - i18N
### Alterando mensagens padrões
### Content Negotiation
### Faça como eu fiz
### Negociação de conteúdo
### O que aprendemos?
## 04. Testes
### Projeto da aula anterior
### Cenário de Teste
### Testando GET e POST
### Testando PUT e DELETE
### Faça como eu fiz
### Função setUp
### O que aprendemos?
## 05. Segurança
### Projeto da aula anterior
### Pensando em segurança
### Pote de mel
### Acesso não autorizado
### Faça como eu fiz
### O que aprendemos?
### Parabéns
### Conclusão
### Logo da alura
### SOBRE A ALURA