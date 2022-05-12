# 1. API com Django 3: Django Rest Framework - 8h
Boas práticas no Django: apps, pastas e paginação \
**Disponível:** [ALURA]('https://cursos.alura.com.br/course/api-django-3-rest-framework') \
**Professor:** Guilherme Lima \
**Conteúdo:**
- Desenvolva uma API do zero, utilizando a linguagem Python
- Saiba como trabalhar com modelos, serializers e views
- Crie uma boa arquitetura em seus projetos Django Rest API
- Integre o Django Admin à sua API
- Descubra como criar suas próprias APIs com Django

## 1. Instalando o Django Rest API Ver primeiro vídeo
### Introdução

[00:00] Olá. Meu nome é Guilherme Lima, e eu serei o seu instrutor neste curso de API Rest com Django.

[00:06] Nesse treinamento, o que a gente vai aprender? A gente vai aprender a criar uma API do zero, utilizando a linguagem Python e Django Rest Framework, integrando os nossos dados num banco de dados, vinculando o admin do Django com a nossa API, entendendo que são serializer, views set. Tudo isso, seguindo boas práticas de programação.

[00:27] Fazendo esse curso, você vai ser capaz de criar suas próprias APIs. Nesse treinamento, a gente vai criar essa API aqui, uma API de uma escola, onde a gente vai ser capaz de criar alunos, visualizar os dados desse aluno, atualizar tanto alunos, como curso, e vincular esses nossos dois recursos, criando, assim, as matrículas dos alunos.

[00:47] Legal? Então a gente vai entender tudo isso, e vinculando o admin do Django com a nossa API também.

[00:54] Fazendo esse curso, você vai ser capaz de criar suas próprias APIs, vinculando modelos, recursos diferentes, entendendo o funcionamento e o padrão Rest.

[01:04] Legal? Quais são os pré-requisitos deste treinamentos? É muito importante que você tenha visto os cursos anteriores de Django, porque a gente vai dar continuidade a partir deles.

[01:13] Para quem é esse curso? Esse curso é para todas as pessoas que tem vontade de entender o que é uma API, criar uma API. Pessoas que talvez nunca criaram uma API, porque a gente vai desde os fundamentos, até a nossa API funcionando.

[01:26] Talvez, se você é um expert em API, já trabalha há muito tempo no mercado, e tem muito conhecimento dessa área, talvez esse curso isso não seja recomendada para você, porque a gente vai consolidar bastante os nossos fundamentos sobre o desenvolvimento de uma API, utilizando o Phyton e o Django Rest Framework.

[01:47] Sabendo disso, vamos começar?

### Preparando o ambiente

Olá!
É muito bom receber você neste curso de Django Rest API.

Espero que seja uma experiência de aprendizado incrível e que possamos vencer todos os desafios juntos. Neste curso, vamos aprofundar nosso conhecimento utilizando o Django, criando um API junto a biblioteca do Django Rest Framework.

Este curso, apesar de ser o sexto curso de Django, não é uma continuação do projeto desenvolvido nas partes anteriores. Porém, é importante que você tenha uma base de conhecimento passado nos cursos anteriores.

Divisão das aulas
Aula	O que vamos aprender nesta aula?
Instalando o Django Rest API	Vamos aprender o que é uma API, JSON e realizar uma requisição GET
Modelos, Admin e Serializers	Vamos criar 2 modelos, vincular o Django Admin e serializar os modelos
Viewset e requisições GET e POST	Vamos entender na prática o que é o viewset e realizar requisições GET e POST
Atualizando e deletando recursos	Vamos atualizar e deletar os recursos e criar um novo modelo
ListAPIView e Autenticação	Vamos utilizar o ListAPIView e adicionar autenticação na API
Preparando ambiente
Além disso, para que tenhamos o mesmo resultado, é recomendado que você faça o download da mesma versão do Python e do Django que utilizei quando o curso foi gravado, que poderá ser encontrada aqui:

    Python 3.7.4
    Django 3.0.7

O Django pode ser instalado através do comando:

    pip install Django==3.0.7

Para otimizar o tempo do curso, criamos esta atividade descrevendo o passo a passo para criação de um projeto Django. Os passos são:

Crie uma pasta para manter seu código e acessando essa pasta em um terminal, crie um ambiente virtual com o seguinte comando:
    python3 -m venv ./venv

Ative seu ambiente virtual com o seguinte comando (MAC e Linux):
    source venv/bin/activate

Em caso de Windows, utilize o comando:

    venv\Scripts\activate.bat

Instale o Django nesse ambiente virtualizado:
    
    pip install django

Crie um projeto chamado setup utilizando o Django admin, para manter toda configuração de nossa aplicação:
django-admin startproject setup .COPIAR CÓDIGO
Para finalizar a configuração do ambiente, na pasta setup, altere no arquivo settings.py o idioma e o horário que usaremos na aplicação, incluindo as seguintes linhas de código:

    LANGUAGE_CODE = 'pt-br'
    TIME_ZONE = 'America/Sao_Paulo'

Na aula 3, vamos utilizar o Postman que é uma ferramenta que tem como objetivo testar serviços da API. Para instalar, clique neste link.
Em caso de dúvida na instalação ou durante o curso, conte sempre com o fórum da Alura!

Vamos começar?

:)

### O que é uma API?

[Pesquisa: CanalTech]('https://canaltech.com.br/software/o-que-e-api/') \
API é um **conjunto de rotinas e padrões de programação para acesso a um aplicativo de software ou plataforma** baseado na Web. A sigla API refere-se ao termo em inglês **"Application Programming Interface"** que significa em tradução para o português **"Interface de Programação de Aplicativos"**.

Uma API é criada quando uma empresa de software tem a **intenção de que outros criadores de software desenvolvam produtos associados ao seu serviço**.

---

[00:00] Para a gente botar a mão na massa e começar a criar as linhas de código para desenvolver a nossa API, vamos responder à seguinte pergunta: o que é uma API? O que uma API faz?

[00:09] Certo? E para explicar isso, vou utilizar um exemplo muito comum do nosso dia a dia. Pense num grupo de amigos que foi numa determinada pizzaria. Chegando lá, eles são atendidos por um garçom, que passa a lista de pizzas que aquela pizzaria faz. E eles decidem comer a pizza de pepperoni, por exemplo.

[00:25] O garçom pega aquele pedido, feito por aqueles clientes, entrega para a equipe que vai criar aquela pizza para os pizzaiolos, e vai falar: chegou um pedido dos clientes de uma pizza de pepperoni.

[00:37] Aquela equipe, que vai criar aquela pizza, assa aquela pizza, prepara. Quando essa pizza está feita, o garçom vai lá, pega essa pizza de pepperoni, e leva para aqueles clientes que fizeram aquele pedido.

[00:49] Certo. Você pode se perguntar: o que a pizza de pepperoni, o garçom, os clientes e o pizzaiolo tem a ver com o API Rest? Tem tudo a ver com o API.

[00:59] Observe que se a gente separar essas três entidades, nós temos os clientes que fizeram os pedidos, que podem ser representados também, no mundo da computação, por um sistema web, outra aplicação mobile que vai fazer um pedido para alguém.

[01:12] Não vai fazer um pedido para um garçom, vai fazer um pedido para uma API, trazendo aqui para o nosso contexto. Então, outro sistema vai fazer um pedido. Esse pedido, a gente vai chamar de requisição.

[01:23] Então, eu vou fazer uma requisição, por exemplo, para saber quantos alunos estão matriculados em um determinado curso. A API vai pegar essa requisição, e de alguma forma ela precisa acessar os dados criados em algum outro lugar para exibir uma resposta para aquele cliente que fez o pedido.

[01:41] Então, ele vai lá pega, esses dados, ou pega uma funcionalidade. Uma API pode disponibilizar dados e informações, ou funcionalidades, para aqueles clientes que fizeram pedido.

[01:52] E assim que ele tem aquele pedido, assim como o garçom pegou a pizza de pepperoni levou para os clientes que fizeram, a API vai pegar aqueles dados e vai devolver uma resposta para o cliente que fez o pedido.

[02:04] Se a gente for caçando esses três, a gente tem uma coisa interessante, olha só. Esse sistema web, independente da linguagem que ele foi feito, se ele foi feito em Python, em Java, em Ruby ou outra aplicação mobile, não importa. A gente vai conseguir atender todos os pedidos feitos através de requisições e respostas.

[02:25] Certo? Então, um sistema web, feito em outra linguagem, vai fazer um pedido, vai fazer uma requisição, e a gente vai exibir essa resposta. E essa resposta, geralmente é enviada de volta num formato de Json ou XML.

[02:39] Então, se a gente parar para pensar no que uma API faz, o que é uma API, a API é um núcleo comum, de funcionalidades, que pode ser usado por várias plataformas diferentes, sendo elas aplicações web, sites, aplicações móveis, ou até outras APIs.

[02:57] Sabendo disso, no próximo vídeo, vamos começar a escrever nossos códigos, e criar a nossa primeira API, entendendo todo esse fluxo de eu fazer um pedido, e depois eu tenho uma resposta, não de uma página web, mas sim de informações de dados, de funcionalidades.

### Requisição GET

#### Criação de um APP

1. No terminal: \
    _python manage.py startapp <nome_do_app>_
2. Acessar `setup.py` e adicionar o app: \
    _setup/settings.py

        INSTALLED_APPS = [
            escola,
            ...,
        ]

#### Criação de Rotas e Views
1. Acessar `urls.py`e criar uma rota:
    _escola/urls.py

---

[00:00] Vamos iniciar, então, o desenvolvimento da nossa API? Bom, nas atividades anteriores, a gente tem um passo a passo, mostrando como a gente cria um projeto com o Django, como a gente instala o Django, como a gente utiliza a VENV, o ambiente virtual do Django, e a gente chega neste momento.

[00:16] A gente tem a instalação do Diego, já com algumas configurações, com a língua em português, que a gente configurou lá no setup do nosso projeto aqui, com o português do Brasil, com o horário da América, de São Paulo.

[00:28] Legal. O que eu quero fazer agora é começar a desenvolver a minha API. Eu quero criar um APP de escola. Então, numa escola, nós temos alunos, nós temos cursos, e nós temos alunos matriculados em diferentes cursos.

[00:42] Eu quero que a minha API seja capaz de criar um aluno, atualizar um aluno, atualizar um curso, criar um curso, remover um curso, criar uma matrícula de um aluno. Ou seja, muitas funcionalidades.

[00:54] E, a primeira coisa que a gente tem que ter em mente é: uma API não renderiza uma página. Eu vou criar um APP chamado “escola”. Então eu vou apertar “Command+J” para abrir o meu terminal, e eu vou fechar aquela outra aba com o “Command+B”.

[01:08] Meu servidor está rodando para exibir a tela. Eu vou parar o meu servidor. Eu vou criar aqui com o Phyton o “manager.py”. “Start APP”, que eu vou chamar de escola. Observa que vai aparecer o ícone da escola.

[01:24] Dou um enter. Ele criou a “Escola”. Eu vou aqui em “views.py”, que faz o controle das requisições que estão vindo, e o que a gente vai fazer. Observe que o Django, quando a gente instala, ele já vem com essas palavras rápidas do Django com um import do Render. Ou seja, para a gente renderizar uma página.

[01:50] Não é o que a gente quer. A gente quer que, quando chegar uma requisição para uma determinada URL, a gente quer renderizar um Json. E como é que a gente faz isso? Primeira coisa. Eu vou colocar aqui, do Django mesmo, do pacote HTTP, eu quero importar o “json.response”.

[02:09] Legal? Aqui eu vou criar uma função. Essa função, vou chamar de “alunos”. Legal? O primeiro parâmetro que a gente vai receber, assim como a gente renderizava as nossas páginas também, vai ser o request.

[02:24] Legal? A primeira coisa que a gente vai fazer lembrar é lembrar dos nossos cursos anteriores de Django. A gente tinha alguns cenários. Observa que quando a gente queria pegar os dados de uma determinada receita, a gente utilizava o método Get, e quando a gente queria criar uma receita, a gente utilizava o método post.

[02:40] O que eu quero fazer agora? Eu vou verificar se o método que vai chegar para essa requisição de alunos é o método Get. Então, se o “request.method = = Get”, eu quero fazer alguma coisa.

[02:55] E o que eu quero fazer? Eu quero criar um Json, só para a gente mostrar de exemplo. Então, eu vou criar “aluno”, e vou passar no formato de dicionário, vou colocar entre aspas simples. Vou colocar, por exemplo, um ID.

[03:14] Eu estou criando um Json. Vou colocar “,” e vou passar outro valor. Vou colocar aqui o “nome:Guilherme”. Legal. Então, observa. Um Json, a gente vai ter um valor, um conteúdo, e esse conteúdo estará adicionado entre chaves, e cada conteúdo, a gente colocar “nome:” e o valor daquele conteúdo. Como um dicionário, mesmo.

[03:43] Está bom? Eu vou colocar um return, e observe que nos nossos cursos anteriores, a gente colocava return, render, e colocava aqui uma página para renderizar uma página. Não é o que a gente quer. A gente quer que o retorno seja o quê? Seja esse arquivo que a gente criou, o “json.response”, passando o aluno que eu criei.

[04:01] Vou salvar esse arquivo, e o que eu vou fazer? Para conseguir acessar o meu projeto, e consegui visualizar esse aluno, eu preciso cadastrar uma URL. Então, eu vou fazer assim: “localhost:8000/alunos”.

[04:17] Então, sempre que eu digitar “localhost/alunos”, e der um enter, eu quero visualizar esse meu arquivo Json. Não quero renderizar uma página. Legal? Então, o que eu vou fazer? Acessando o setup, em URL, a gente tem todas as URL cadastradas na nossa aplicação.

[04:33] A gente tem um setup da configuração, e eu vou remover essas linhas, a gente não utilizar essas linhas, agora. E o que eu quero fazer? Eu quero importar essa minha view de aluno, lá do meu código view de escola.

[04:46] Então, “from: escola.views”, eu quero importar quem? Alunos. Legal. E vou criar aqui um PATH, um novo PATH, para que quando esse meu “localhost/alunos” aparecer, então eu vou colocar “alunos/”, e quando eu tiver uma requisição para este “alunos/”, eu quero que atenda lá do meu APP de escola, na minha views, eu quero que seja esse meu método de alunos.

[05:21] Legal? Vou colocar uma “,”. Salvando. O que eu vou fazer? “Command+J” para eu subir o meu servidor, que eu tinha parado o servidor Python. “manage.py”, “runserver”.

[05:33] Executando uma vez, ele subiu, ele fala que nós temos migrações pendentes ainda para esse projeto, porque a gente não fez nenhuma migração, não cadastrou o nosso modelo. Quando eu volto para a minha aplicação e atualizo, a gente o “ID 1” e o nome Guilherme.

[05:48] E é justamente isso, essa é a ideia da API. Então, a gente quer disponibilizar, através de alguns endereços, alguns recursos, funcionalidades diferentes. Só que, o que eu quero fazer? Eu quero fazer algo muito maior. Eu quero que, baseado no endereço, e no método da requisição, eu quero criar um aluno, eu quero deletar um aluno, eu quero pegar.

[06:10] A gente tem migrações pendentes no nosso modelo. Se a gente acessar o nosso modelo de escola, nosso modo de escola, a gente não tem nenhum arquivo, a gente não tem nada nesse arquivo, está vazio.

[06:21] Ele fala quea só fez o import de modos, “from django.db”, mas a gente não tem nada. O que eu quero fazer? Eu quero criar um modelo, uma regra de negócios, quero integração com banco de dados também, mas eu quero que, no momento em que eu receber as requisições, retornar um arquivo Json.

[06:39] E, para nos auxiliar nisso, já existe uma ferramenta chamada Django Rest Framework, que nós vamos instalar no próximo vídeo, que vai nos ajudar a fazer todo esse meio de campo entre os dados que a gente quer exibir, e como a gente cadastra as URL e as rotas principais da nossa aplicação. Isso o que a gente vai fazer no próximo vídeo.

### Django Rest Framework

1. Instalação dos pacotes

        pip install djangorestframework
        pip install markdown
        pip install django-filter
2. Acessar `setup.py` e adicionar no `INSTALLED APP` o app: `rest_framework`

---

[00:00] Entendemos como funciona o fluxo de uma requisição e de uma resposta não renderizando uma página e sim um objeto Json. O que eu quero fazer agora?

[00:10] Eu quero instalar o Django Rest Framework e, baseado nos modelos, nas minhas regras de negócio, eu quero criar um aluno, eu quero remover um aluno, eu quero atualizar os alunos. E o Django Rest Framework vai nos ajudar nessas tarefas, em configurar essas URL.

[00:27] Legal? Primeira coisa que a gente vai fazer vai ser pesquisar. Vou digitar “Django Rest Framework”. Acessando aqui esse primeiro link, a gente tem a documentação do Django Rest, que está bem legal, apesar de estar em inglês.

[00:43] Está simples, está tranquilo de a gente entender. A gente pode usar um tradutor para entender legal, e ele fala que o Django Rest Framework é uma poderosa e flexível ferramenta para a gente construir web APIs. E ele dá algumas razões.

[01:00] Ele vai ter, quando a gente instalar na nossa aplicação, e depois, quando a gente for utilizando ele, uma API navegável. Ou seja, vai ser possível a gente testar as nossas requisições, alterar os verbos das nossas requisições, conteúdo que a gente vai aprender no decorrer deste curso.

[01:16] Outra coisa legal. Políticas de autenticação. A gente vai conseguir utilizar também serialização de dados, da fonte de dados ORM, não ORM, baseado nas nossas requisições. Ou seja, muita coisa legal o Django Rest Framework é capaz de fazer para a gente criar a nossa web API.

[01:38] Legal? Aqui embaixo, rolando um pouquinho a página, a gente tem os requerimentos e a instalação necessária para a gente utilizar o Django Rest para criar a nossa API.

[01:50] Legal? Então o que eu vou fazer? Ele fala que é necessário que a gente utilize sempre as versões oficiais do Python e do Django, para a gente utilizar, e sempre as versões mais atualizadas.

[02:03] Legal? Então, a gente tem aqui o Phyton e o Django, que já temos instalados na nossa aplicação. Utilizando o Pip Install, ele dá aqui outros pacotes que a gente pode utilizar também.

[02:16] E utilizando o Pip Install, a gente vai instalar esses dois pacotes, o Django Rest Framework e o Markdown. Por quê? O Django Rest Framework é o que vai fazer toda a mágica acontecer para a gente criar a nossa API, cadastrar as URL, pegar os dados que estão vindo do banco e, de uma forma, renderizar esses dados para Json, serializar esses dados para Json.

[02:40] E a gente vai fazer instalação do Markdown, que é um suporte para o browser EPI. Lembra que eu disse que a gente vai conseguir testar as nossas requisições, para saber quais são os dados que estão indo para a gente consegui testar a nossa API?

[02:55] Então, a gente vai fazer essas duas instalações e vai passar, depois, também, o Django Rest Framework como um APP instalado no nosso código, lá no nosso arquivo de setup.

[03:07] Legal? Então, vou fazer isso. Abrindo aqui o meu terminal, vou parar o meu servidor. Vou instalar o Pip Install. “install.djangorestframework”. Dou um enter, espero ele fazer a instalação.

[03:25] Ele dá aqui uma mensagem para eu atualizar o meu PIP, vou fazer isso. “pipinstall—upgradepip”. Ele está fazendo a atualização. Legal. Agora eu vou instalar o Markdown. “pipinstall.markdown”. Dou um enter.

[03:43] Legal. Ele instalou o Mark Down. Assim como a gente viu na documentação, outra coisa que a gente vai fazer vai ser ir no meu arquivo de setup, em “setings.pi”, eu vou informar aqui, dentre os meus APPs instalados, eu vou ter quem? Eu vou ter o Rest Framework.

[04:04] Eu vou ter o Rest Framework também como um APP instalado na nossa aplicação. Certo. Agora, o que eu preciso fazer? Não preciso fazer mais nada. O Django Rest está instalado na minha aplicação.

[04:16] Se a gente observar o que a gente fez na nossa aplicação, no “setup”, a gente configurou uma URL para quando for “localhost/alunos”, quem vai atender essa requisição vai ser alguém lá de “views”, que a gente importou, chamado “alunos”.

[04:37] Então, vamos em “views”. Aqui em “Escola”, a gente tem “views.pi”, e a gente tem o nosso método de alunos. E o que esse método faz? Ele verifica. Se o método for “get”, ele vai pegar esse aluno que nós criamos, via Json, e vai dar um “Json Response”.

[04:54] Só que eu quero fazer algo além. Sabe o que eu quero fazer? Eu quero que esse dado aqui não seja criado assim. Eu não quero criar os alunos assim, próximo aluno? A Ana. Eu vou a Ana com a “ID 2”.

[05:05] Não, eu não quero fazer isso. O que eu quero fazer é pegar essas informações do banco de dados, quero utilizar, assim como a gente viu nos cursos anteriores, um modelo, e através desse modelo, a gente vai fazer todo o caminho para a gente conseguir criar a nossa API.

### Exercício: Aplicação integrável

Durante os vídeos, vimos que não é interessante entregar ou renderizar sempre uma página HTML, já que existe dispositivos e finalidades que não utilizarão o HTML, mas sim os dados.

Dito isso, qual o primeiro passo para criar uma aplicação integrável?

a) Devemos transformar nossa aplicação em uma Single Page Application.

b) Devemos entregar os dados apenas no formatos JSON, já que é o único formato aceito por outras aplicações.

c) **Alternativa correta: Devemos entregar os dados em outros formatos, por exemplo JSON.**
- _Alternativa correta! Devemos entregar nossos dados em formatos mais acessíveis para agentes intermediários como outros desenvolvedores!_

### Para saber mais: Documentação oficial

O Django Rest Framework é uma biblioteca poderosa para desenvolver web APIs de forma rápida, segura e simples.

Para maiores informações sobre esta incrível biblioteca, acesse o manual ou a documentação oficial [neste link]('https://www.django-rest-framework.org/').

Quer entender melhor o que é JSON? Clique [neste link]('https://www.alura.com.br/artigos/o-que-e-json?utm_source=gnarus&utm_medium=timeline').

## 2. Modelos, Admin e Serializers
### Modelo de aluno e curso

.model”, assim como a gente fez nos cursos anteriores, eu quero que esse aluno tenha um nome, que vai ser do tipo “charfield models.charfield”, e eu vou colocar aqui uma quantidade máxima de caracteres.

[00:57] Então, “max_lenght = 30”, por exemplo. Eu quero também que o aluno tenha um RG, um CPF, a data de nascimento. Então, o RG. O RG também vai ser do tipo charfield, e eu vou colocar, por exemplo, o “max_length = 9”

[01:20] Para eu utilizar esse atalho para ele ficar copiando essa linha, eu utilizo o “Shift + Options”, ou “Shift + Control”, setinha para baixo duplica essa linha. Está bom? Então eu também quero o RG e o CPF do aluno, e eu quero também a data de nascimento.

[01:36] Vou deixar a “data_nascimento”. E aqui, a data de nascimento, vai ser do tipo “date field”. A gente não tem aqui o “max_lenght”. Legal. Temos aqui a nossa classe de alunos. Eu vou representar cada aluno pelo nome dele.

[02:05] Então vou criar um método __STR, para a gente representar esse objeto aluno do tipo string, no formato string, e eu quero que ele retorne para mim, “returnself.nome”. Legal. Além de “alunos”, o que eu quero também? Eu quero que o curso seja armazenado no banco de dados.

[02:31] Então, olha só. A gente vai ter uma URL para alunos, e vai ter uma URL também para cursos. Vou minimizar aqui, e vou criar uma classe para curso. Então, “class”, vou chamar de “curso”. Bem parecido com o de cima. Vai ser do tipo “models.model”, e eu quero que o curso tenha um código, então eu vou colocar “código_curso”, e esse código do curso vai ser o modo charfield. Vou copiar para a gente ganhar tempo.

[03:08] Modo charfield, o máximo de caracteres que eu vou deixar vão ser dez. Eu quero também que um curso tenha uma descrição. Descrição, deixa eu ganhar tempo. Vou colocar colocar com “Option + Shift”, para baixo. O curso também vai ter uma descrição.

[03:29] Eu quero que essa descrição seja do tipo charfield, e passe detalhes do curso. Então vou deixar com mais caracteres. Vou deixar com o máximo de 100 caracteres. Está bom?

[03:38] E eu quero que o curso tenha um nível. Então, eu vou colocar aqui “nível do curso”. Só que esse nível, eu quero que ele seja diferente. Eu quero que os cursos dessa escola que eu estou criando, eles são de três tipos. Ou eles são básicos, ou eles são intermediários, ou eles são avançados.

[03:53] Então eu vou fazer algo diferente. Eu vou criar uma variável de instância chamada “nível”, uma constante. Eu vou colocar aqui, dentro desse nível, que a gente tem o tipo B, representando os cursos básicos, e quero que cada um desses seja uma representação.

[04:24] Então, no banco de dados, vai estar salvo com uma letra B, só que para a gente vai ser representado com o nome básico. Está bom? Vai ser um tipo “choice field”, é o que a gente quer. A gente tem essas escolhas, quando a gente for criar esse nível do curso.

[04:40] O curso também pode ser intermediário, então eu representar pela letra “I”. Intermediário. E o curso também pode ser avançado. Então, mais um parêntese, vai representar pela letra A, avançando. Legal. E o que eu vou fazer?

[05:06] Aqui, no meu nível, eu vou colocar “model.charfield” também. Só que aqui eu vou passar uma propriedade diferente. Eu vou passar aqui o “max_lenght” dele vai ser, no máximo, de um caractere. Por quê? Porque, no banco de dados, a gente quer salvar só essas letrinhas, e na nossa aplicação, lá para o nosso cliente que estiver recebendo, vai ser representado por essas palavras: básico, intermediário ou avançado.

[05:35] Eu vou passar mais uma propriedade chamada “choice”, e vou passar o nível, que são essas nossas variáveis que a gente escolheu. Vou passar mais duas propriedades, que vai ser “blank = falso”. Por que eu vou passar o “blank = falso”? Eu não vou permitir que no banco de dados do curso não tenha um nível.

[06:00] Então, os nossos cursos, vão precisar de um nível do banco de dados. Vou passar aqui, porque eles não podem também ser nulos, que “nulo = falso”. E, para terminar, quando um curso não tiver nenhuma representação, eu vou colocar um valor default para ele. Eu vou falar que todo curso, por default, ele vai ser do tipo básico.

[06:23] Então, eu vou passar a minha propriedade default, e vou falar que vai ser do tipo B, que é do tipo básico. Legal? Então, o nosso curso tem um nível, o nosso curso tem um código, tem uma descrição, e eu quero essas informações para o nosso curso.

[06:40] Da mesma forma que a gente vai representar o objeto de uma forma de stream, representado pelo nome, eu quero que um curso seja representado por sua descrição. A gente vai ter mais informações do curso.

[06:53] Então, eu vou colocar aqui “self.descrição”. Legal? E aqui está o nosso modelo. Então, o que a gente tem? A gente tem um aluno, a gente tem um curso. Agora, eu preciso migrar esse modelo para o banco de dados. Então, para isso, o que eu vou fazer?

[07:09] Lá em “Setup > Setting.py”, observe que eu tenho os APPs instalados. Eu só tenho o Rest Framework, eu ainda não tenho a escola. Eu vou precisar colocar a escola aqui para ele entender que aqueles modelos fazem parte dessa aplicação também. Está bom? Legal.

[07:26] Coloquei a escola. Vou abrir o terminal. No meu terminal, eu vou dar um “pythonmanager.py makemigrations”. Salvar. Rodando mais uma vez o makemigrations e ele criou para a gente as migrações.

[08:25] A gente pode ver essas migrações, conteúdo que a gente já viu nos nossos outros cursos. Então ele cria para a gente essas migrações se a gente precisa fazer alguma alteração nesse arquivo de imigrações. A gente tem ele aqui também.

[08:39] O que eu quero fazer agora é iniciar o meu banco de dados. Eu quero que o banco de dados suba todas as migrações. Por quê? Olha só que coisa interessante. Quando a gente dá um “phytonmanage.py runserver”, ele fala que nós temos imigrações pendentes.

[08:56] A gente tem, agora, 18 migrações pendentes. Ele subiu o nosso servidor, mas a gente tem migrações pendentes. Só que a gente só criou o aluno, e só criou p curso. Mesmo assim, ele deixou com 18 migrações pendentes.

[09:11] Por quê? A estrutura do Django já está configurada para ser mantida no banco de dados também. Está bom? Então, eu vou subir. Agora que a gente já tem as migrações, eu vou rodar o “python manage.py migrate”. Ou seja, sobe no banco todas essas migrações que eu tenho da minha aplicação.

[09:35] Vou subir. Agora sim. Eu tenho, no meu banco de dados, uma tabela chamada “alunos” e uma tabela chamada “cursos”, para salvar esses cursos, para depois disponibilizar eles na minha API.

[09:49] Qual vai ser o próximo passo? Vamos criar alguns alunos e alguns cursos lá no nosso admin.

### Django Admin

[00:00] Vamos configurar o nosso admin para que a gente consiga criar alunos e cursos. Então, vou fechar aqui o meu “modelos.py”, vou vir aqui no meu app de escola, em “admin.py”, e vai configurar o nosso admin para a gente conseguir criar, atualizar, ter o crud completo, tanto de alunos, como de curso.

[00:21] Primeira coisa que a gente vai fazer vai ser importar lá do nosso app de escola. “from escola.models”, “import”, e a gente vai trazer um import de aluno, e um import de cursos, nossa classe de aluno e nossa classe de curso.

[00:40] Agora eu vou criar uma classe que eu vou chamar de alunos, para manter todos os nossos alunos, e ele vai ser do tipo “admin.model admin”. E aqui dentro, eu vou colocar, por exemplo, quais são os campos que eu quero exibir nesse no meu display do meu admin.

[00:59] Então eu vou colocar a propriedade “list display”, e vou passar aqui os campos que eu quero do meu aluno. Só para a gente recordar, vou deixar o meu modelo aberto. Então o aluno tem nome, RG, CPF e data de nascimento. Então eu quero o ID. Mas o ID eu não coloquei lá.

[01:22] Mas lembra que nos cursos anteriores, o ID é gerado sempre quando a gente cria um modelo. Ele já tem esse relacionamento entre as tabelas. Então, sempre é gerado. Mesmo que eu não crie um ID aqui, ele vai ser gerado e a gente vai conseguir acessar esse ID lá no nosso admin também. Legal?

[01:40] Então, ID, o nome, o RG, o CPF, data de nascimento. “data_nascimento”. Esses são as informações que eu quero disponibilizar para o meu aluno. Além disso, eu quero colocar um “list display link”. O que ele vai fazer? Sempre que eu quiser alterar algum aluno, eu quero que seja possível a gente clicar ou no ID, ou no nome do aluno. Vou deixar o nome aqui. Legal?

[02:22] Então, esses dois campos, são os campos que a gente vai conseguir alterar e editar esses nossos alunos. Eu quero também um campo de busca. Eu quero conseguir buscar os meus alunos por nome, por exemplo. Legal?

[02:36] Então, colocar aqui que a gente vai ter um campo de busca por nome. Repare que eu deixei uma vírgula depois do nome. Eu quero também conseguir uma paginação na quantidade de alunos. Vamos supor que a nossa base de dados tenha 500 alunos. A gente não quer exibir os 500 alunos de uma vez.

[02:58] Então, eu posso colocar um “list per page”, e vou passar um valor. Quero ter, por exemplo, 20 alunos por página. Criei, então, as minhas configurações dos meus alunos. O que eu vou fazer? Eu vou registrar essa minha configuração do meu admin.

[03:15] Então eu vou colocar “admin.site.register”, e vou passar duas informações. A primeira é o modelo. Qual é o modelo que eu estou usando? O modelo que a gente importou, o modelo de aluno. E segundo, qual é a configuração do “model admin” que a gente fez? É essa classe aqui. Então eu vou passar os alunos.

[03:38] Da mesma forma que a gente fez isso para os alunos, vamos fazer isso para os cursos também. Então, eu vou ter uma classe, que vai ser responsável pelos cursos no meu admin, e ela vai ser do tipo “admin.modeladmin”, e um curso, vou descer veio falar aqui um curso Ele tem um código, uma descrição e um nível.

[04:00] Então, “list display”. O curso tem uma descrição. A gente pode colocar até o ID também para ficar mais organizado. Vou colocar o ID, o código do curso, “código_curso”, e a descrição.

[04:24] E a gente também tem um nível do curso. Descrição. A gente tem o nível do curso. Só que nível do curso eu não vou colocar não. Vou deixar só esses aqui. Então, eu quero essas informações na minha lista de cursos.

[04:43] Os displays, o “list display link” que eu vou utilizar vai ser o mesmo do nosso aluno. Eu vou colocar o ID também, e vou colocar, por exemplo, o código do curso. “código_curso”. Para finalizar, a gente pode colocar um campo de busca também pelo código do curso.

[05:07] Então, vou colocar no campo de busca, vou colar, e vou passar aqui o código do curso. Legal. Fiz essas configurações, eu preciso registrar esse meu curso. As mesmas propriedades que a gente tem ali. Primeiro, qual o modelo que eu estou usando, usando um modelo de curso, qual a configuração, a classe responsável, a classe “cursos”. Legal.

[05:29] Salvei isso aqui, vou abrir o meu terminal, vou subir aqui o “pythonmanager.py”, “run server”. Dou um enter. Ele subiu. Repara que ele não deu nenhuma informação falando que você tem migrações, porque a gente já fez naquela na aula anterior. Certo?

[05:46] Então, o nosso servidor já está subindo. E repare que a gente não tem nenhuma informação falando que a gente tem migrações pendentes, porque a gente já realizou essas migrações.

[05:56] Então, aqui no meu servidor, “localhost:8000/admin”. Dou um enter. Ele está pedindo usuário e senha. Vamos criar. Vou parar o servidor com “Control+C”. vou colocar o comando Python, “manager.py”, “create super user”.

[06:19] A gente já fez isso nos vídeos anteriores. Então, ele fala aqui que se você deixar em branco, o super user vai ser Guilherme Lima. Muito grande. Vou deixar só Gui. Endereço de e-mail: gui@alura.com.

[06:31] Esse e-mail não existe, hein? Não mandem nada para esse e-mail, porque esse e-mail não existe. É um e-mail fictício. E a minha senha, eu vou colocar uma senha, repetir minha senha. Ele falou que a senha é muito comum. Quero deixar essa senha desse jeito.

[06:46] Por enquanto quero, não vou me preocupar com essa senha agora. E subir. Legal. Criei meu o meu super user. Subindo o meu servidor mais uma vez, eu vou colocar aqui o meu usuário, Gui, e vou colocar a senha que eu gerei.

[07:00] Vou colocar “acessar”, e aqui eu tenho o meu app de escola com alunos e cursos. Eu consigo criar um novo aluno. Então, vamos criar. Então eu vou criar um aluno aqui, que eu vou chamar de “teste”. O nome “teste”, não vou colocar o nome real, não vou me preocupar com isso agora.

[07:12] RG 123456789. Estou teclando e não está indo mais caracteres, porque o RG só tem dígitos. A gente tem 11 dígitos. A data de nascimento, vou colocar que nasceu hoje. Então, esse é o nosso aluno teste. Está bom?

[07:36] Vou colocar “aluno teste”, e depois a gente vai ter o “curso teste”. Não vou me preocupar com o nome de alunos e alunas, está bom? Então, “aluno teste”, criei aqui um aluno.

[07:45] Agora, o que eu quero fazer? Eu vou criar um curso. Então, voltando no nosso app de escola. “Curso > adicionar curso”. Vou criar um curso. Aqui é bem fictício. Vou usar um exemplo. Por exemplo, o código do curso vai ser curso de Django Rest Framework 01.

[08:03] Então vai ser o curso Django Rest Framework, e a descrição vai ser no nível básico, está bom? Vou salvar. Legal. Tenho um curso, e tenho também um aluno registrado. O que eu quero fazer? Lembra que quando eu digito aqui “localhost:8000/alunos”, o que está fazendo? Ele está trazendo aquele aluno, Guilherme, que eu coloquei.

[08:33] Ele está trazendo o aluno que eu gerei aqui. Tanto que se eu apagar, por exemplo, aqui, olha só que perigo que estão esses nossos dados, como eles estão sensíveis. Vai vir só um ID um. Aquela outra informação eu já perdi, eu não tenho mais.

[08:47] Só que agora a gente tem informações que a gente já cadastrou no banco de dados, que é o “aluno teste”, e o nosso curso de Django Rest Framework. Então, o que eu quero fazer? Eu quero, de alguma forma, colocar a barra “alunos”, e ele trazer para mim esses alunos já no formato Json.

[09:05] Então, quando chegar uma requisição, quero pegar os alunos do banco de dados, transformar esses dados para serem atendidos em formato no formato Json, e responder, atender essa requisição. E é o que a gente vai ver os próximos vídeos.

### Serializers
Quando criamos nossos MODELS precisamos criar um arquivo `serializers.py` para cada app. Que vai fazer a ponte entre nosso banco de dados e api.

---

[00:00] Configurei o meu admin de alunos e cursos. Eu consigo visualizar os cursos que eu crio e os alunos que eu vou criando. Esses dados estão armazenados na minha base de dados.

[00:11] O que eu gostaria de fazer agora é: da mesma forma que a gente disponibiliza esses alunos aqui, eu quero disponibilizar os alunos que estão na base de dados. Ou seja, se a gente parar para pensar, a gente tem um modelo de alunos que o Python entende, que o Django entende, que o RM do Django entende.

[00:27] E a gente precisa disponibilizar essas informações para uma forma que a nossa API vai entender. Ou seja, a gente quer que a nossa API entenda que o nome, RG, CPF e a data de nascimento estejam num formato que geralmente é usado nas APIs, que é o formato Json.

[00:44] Então, eu preciso, de alguma forma, pegar todas essas informações aqui, do aluno, transformar para uma forma que a API do Django vai entender e, depois, eu vou receber essas informações também da minha API, porque eu posso criar um aluno através da minha API, que vai vir no formato Json, e eu preciso converter para esses formatos aqui.

[01:04] Num formato que o Django entenda, e que o Django pegue essas informações que estão vindo via Json, transforme essas informações num jeito que o Python e o Django vão entender, e salva no banco de dados.

[01:16] Então, percebe que agora a gente vai ter de criar uma ponte entre as nossas informações escritas em Python, e as nossas informações escritas em Json. Então, a gente vai precisar fazer ambos: pegar a informação e Python e transformar em Json; pegar a informação em Json, transformar em Python, para salvar no banco de dados, e assim por diante.

[01:36] E quem geralmente tem essa responsabilidade? É um arquivo chamado serializer. Então, isso que eu acabei de falar, é o que o serializer vai fazer. Ele vai pegar essas informações que estão num contexto que o Django entende, escritos em Python, e vai converter essas informações para outro formato, que é o formato que a nossa API vai entender, Json.

[01:59] Então, o que eu vou fazer? Lá no nosso escopo do nosso projeto, repara que eu estou aqui no meu APP de escola, eu vou criar um novo arquivo, que vou chamar de “serializer.py”. Esse arquivo “serializer.py”, eu vou, lá do meu Rest Framework.

[02:19] Então, “from:restframework”, eu vou importar um carinha chamado serializers. Então, ele já aparece aqui para a gente, serializers. Certo? E o que eu preciso? Bom, se eu quero “serializar” informações que eu tenho lá no meu modelo, eu preciso trazer os modelos para cá.

[02:36] Então, eu vou trazer também. “from:escola.models”. Import. A gente quer o aluno, o nosso modelo de aluno, e o nosso modelo de curso. Então eu vou colocar aluno e curso. O que eu preciso fazer agora é criar uma classe para dizer qual é o modelo que a gente está utilizando e quais são os campos que eu quero utilizar em cada serializer.

[02:57] Então, por padrão, o que a gente faz? A gente queria uma classe, que vou chamar de “aluno serializer”. Esse “aluno serializer” vai ser do tipo “serializers.modelserializer”. Por quê? Porque a gente já tem o modelo, e a gente serializar, ou seja, a gente quer transformar esse nosso modelo num outro tipo.

[03:27] Então, eu tenho o meu aluno serializer. O que eu vou fazer? A gente precisa informar para ele qual é a classe meta que esse nosso serializer vai ter. Ou seja, qual é o modelo que a gente vai utilizar, e quais são os campos. Eu vou deixar “fields”. Quais são os campos e os modelos que a gente vai utilizar.

[03:48] O modelo que a gente vai utilizar no aluno serializer é o modelo de aluno. Os campos que a gente vai utilizar, a gente pode passar da seguinte forma: vou colocar uma lista, um colchete, e vou passar que eu quero visualizar o ID, que eu quero visualizar o nome do aluno, o RG, o CPF.

[04:11] Vou abrir o modelo, só para a gente não esquecer nenhuma informação. CPF e data de nascimento. Legal. “,datanascimento”. Legal. Eu preciso fazer mais alguma coisa? Não. Eu só preciso fazer isso para conseguir ter um serializador. Então, eu vou fazer a mesma coisa para o meu curso.

[04:34] Então, vou criar uma classe. Essa classe vai se chamar curso. Então eu vou criar uma classe. Essa classe vai se chamar “curso serializer”. Esse meu serializer vai ser do tipo “serializers.modelserializer”.

[04:49] Vou criar a classe para indicar, classe meta, indicando qual é o modelo que a gente vai utilizar. O modelo de curso vai ser o curso, e os campos que eu quero visualizar no meu serializer são todos os campos que eu tenho de curso.

[05:11] Em vez de a gente colocar essas informações assim, a gente pode fazer da seguinte forma. Vou tirar esses colchetes, vou deixar, entre aspas simples, vou deixar “all”. Então, “--all--”.

[05:29] Então, a gente tem aqui um serializador, tanto do aluno, como do curso. E ele vai ser responsável por fazer a ponte da nossa API. E daqui a gente já tem outra lição. Observe que se eu tiro, por exemplo, a data de nascimento, a gente tem, na nossa base de dados, um campo para a data de nascimento.

[05:50] Só que na minha API, eu não tenho esse dado disponível. Então, o serializer vai servir como um filtro dos dados que a gente quer disponibilizar para a API. Ou não. Eu posso disponibilizar todos os dados, ou eu posso colocar todos os dados que eu quero nesse serializer que eu tenho.

### Exercício: Entrega de dados

Para manter os dados armazenados no banco de dados, criamos um modelo e executamos a migração.

Sabendo disso, para entregar os dados armazenados no banco de dados no formato Json por exemplo ou receber um Json para salvar no banco de dados, o que devemos fazer?

a) **Alternativa correta:** Devemos criar uma classe com a responsabilidade de serializar os dados.
- _Alternativa correta! Certo! Os dados de saída devem ser serializados em um formato específico, e os dados de entrada serão desserializados para processamento._

b) Devemos criar uma rota em urls.py informando o tipo de dados que estamos recebendo, e outra rota informando o tipo de dado que estamos enviando.

c) Devemos renderizar uma página que transforme os dados no formato Json para instâncias conhecidas em Python.

## 3. Viewset, Urls e requisições GET e POST

### Viewset
Viewset é o responsável por processar as query no ORM do DJANGO

---

[00:00] Criamos o serializer que permite que dados sejam convertidos para forma Python, nativa, para o RM do Phyton entender, e que sejam facilmente renderizados em Json, XML, ou até outros tipos.

[00:15] No nosso caso, a gente vai manter o padrão Json. Só que, quem vai ser responsável por receber esses dados e selecionar qual é a serialização que a gente vai utilizar, se a gente está recebendo dados Json e quer transformar esses dados para Python nativo para que o nosso programa entenda.

[00:34] Bom, alguém precisa ser responsável por essa atividade. A gente tem o serializador, mas a gente não tem alguém que vai dizer que a gente vai utilizar esse aluno serializer. E quem vai fazer isso vai ser o nosso arquivo “views”.

[00:46] Então, abrindo aqui, eu venho aqui em “views.py”, e temos aqui o método que havíamos criado. A gente tem um método que a gente havia criado para a gente visualizar apenas um aluno. Vamos relembrar?

[01:00] Então, digito “localhost/alunos”. A gente tem aqui o ID 1. Lembra? Os nossos dados estavam supersensíveis. Não é isso o que eu quero. Eu quero buscar os dados que estão lá na minha base de dados, que eu já fiz, que eu já criei.

[01:17] Então, a estrutura “rest” permite que a gente inclua uma abstração para lidar com “viewsets”. O que vai ser um “viewset”? O “viewset” permite que a pessoa que está desenvolvendo a nossa API consiga pensar bem na modelagem de negócios e como a nossa aplicação está se desenvolvendo, sem se preocupar com as interações da API, deixando a construção da URL ser automaticamente criada através das convenções comuns.

[01:45] Então, o que eu vou fazer? Aqui nesse nosso arquivo, a gente vai alterar um pouquinho para utilizar os dados estão lá na nossa base de dados. Legal? Para isso, a gente vai precisar importar alguns carinhas aqui.

[01:59] Então, o primeiro que a gente vai importar vai ser o nosso arquivo “viewsets”, lá do Rest Framework. Então “from rest framework import viewset”. Legal. Tem o “view set”, e eu preciso saber quais são os modelos que eu vou utilizar. Então, “from escola.models”. “Import”. “Aluno”, “import curso”.

[02:26] E a última coisa que eu vou precisar utilizar também para esse nosso “viewset” são os nossos serializers. Então, “from serializer import”. “aluno serializer” e “curso serializer”. Maravilha.

[02:47] A gente tem tudo o que a gente precisa para criar o nosso “aluno viewset”, para que ele mantenha o controle, qual a requisição que está vindo, qual a estrutura Rest que vai ser utilizada, e ele utiliza, tanto os dados que a gente quer usar, salvar no banco de dados, ou exibir as informações do banco de dados, como serializar essas informações.

[03:09] Então, para isso, eu vou criar uma classe chamada “alunos viewset”. Esses “alunos viewset”, a gente vai ter um argumento nessa nossa classe, a gente vai dizer que ele é do tipo viewsets, e ele vai ser do tipo “model viewset”. Por quê? Porque a gente já tem um modelo integrado, já tem um modelo vinculado a essa nossa classe.

[03:50] A gente pode colocar um “docstring” para deixar essa classe um pouco mais informativa. Então, o que a gente vai querer que esse viewset faça? A gente quer exibir todos os alunos e alunas.

[04:00] Então, “exibindo todos os alunos e alunas 123”. Legal. A gente criou esse nosso docstring, e quando a gente passar o mouse, vai ter aqui “exibindo todos os alunos e alunas”.

[04:15] E a gente vai ver que esse docstring vai ser importante também para documentar A Nossa API. Agora, a gente precisa declarar duas variáveis aqui dentro dessa nossa classe, que vai ser responsável por fazer toda a mágica do nosso viewset.

[04:29] O primeiro vai ser o queryset. Então eu vou criar o queryset, e vou dizer: qual é o queryset que a gente quer utilizar? Ora, se a gente quer todos os alunos, a gente precisa trazer todos esses alunos para cá. E a gente já sabe como a gente faz isso.

[04:43] Vou colocar “alunos.objects.all”. Aí a gente traz todos os alunos do banco de dados. Vamos supor que eu queira incluir um filtro para trazer todos os alunos com uma determinada data de nascimento, eu poderia colocar aqui, alterando só o meu queryset. Está bom?

[05:04] Então aqui, no caso, a gente quer trazer todos os alunos. A segunda informação que a gente precisa passar é o nosso “serializer class”. E ele vai ser quem? Quem vai ser a classe responsável por serializar esses alunos? A classe que a gente criou anteriormente, o “aluno serializer”. Então, eu vou passar aqui, “aluno serializer”.

[05:25] Eu preciso agora verificar cada verbo do HTTP, do Rest, para ver se é um get, para ver se é um post? Não. Apenas com essas linhas de código, a gente vai conseguir manipular de forma automática todas as nossas requisições e todas as informações que a gente quer disponibilizar.

[05:44] Da mesma forma que a gente fez para o “alunos.viewset”, vamos fazer também para “cursos.viewset”. Então, “class cursos.viewset”. Vai ser do tipo “viewset.modelviewset”, e a gente vai passar, para deixar organizado, um docstring, exibindo todos os cursos.

[06:17] E eu vou passar qual é o queryset que a gente vai utilizar, vai ser “cursos.objects.all”, porque a gente quer exibir todos os cursos. E a gente vai passar o nosso serializer. E o nosso “serializer class”. O “serializer class” vai ser “cursos.serializer”. Maravilha.

[06:49] Só com isso a nossa API já vai estar funcionando? Quase. Falta apenas uma etapa. A gente criou o nosso modelo, criou o nosso serializador, e criou aqui quem vai ser responsável por serializar, qual vai ser o queryset vai responsável aqui por cada requisição.

[07:07] Só que, agora, a gente vai criar as nossas URLs. A gente vai dizer que a gente precisa registrar essas nossas URLs trabalhando tanto com “aluno viewset”, como “curso viewset”. É isso o que a gente vai fazer a seguir.

### Configurando Urls
Diferente do DJANGO TRADICIONAL as rotas são cadastradas a partir do router do URLS.PY

---

[00:00] Configuramos, agora, as nossas views. Só que, quando a gente abre o nosso terminal, a gente tem um erro, falando que a gente não tem mais alunos na “escola.view”, e isso já é esperado. Por quê? Se a gente acessar o nosso arquivo de setup URLs, a gente vai ver que a gente tem, quando chegar uma requisição para alunos, eu quero que “aluno” atenda.

[00:20] Só que lá em view a gente não tem mais esse aluno, por quê? Nós configuramos as nossas views para que sejam viewsets. Então, agora a gente vai precisar configurar as nossas rotas, para que a gente use esses viewsets que a gente criou.

[00:34] Legal? Então, o que eu vou fazer? Lá no nosso arquivo “urls.py”, no lugar de a gente tem “escola.views”, eu quero trazer os meus viewsets. Eu quero trazer o meu “aluno.viewset”, e quero trazer também o meu “curso.viewset”. Então, “curso.viewset”.

[00:53] Maravilha. Além disso, eu vou precisar de mais uma coisa. Eu vou precisar, para a gente conseguir navegar e utilizar a nossa API no nosso browser, a gente tem uma rota default que é dada pelo Django Rest.

[01:09] Então, o que eu vou fazer? Eu vou trazer essa rota para cá. Eu vou importar lá do Rest Framework, import, routers, e eu vou definir essa rota principal. Então eu vou dizer que router, no singular, ela vai ser igual a “routers.defaultrouter”, e vou criar aqui, executar a nossa função.

[01:33] Agora, o que eu preciso fazer? Eu já tenho uma rota principal default criada. Eu preciso registrar tanto o meu “aluno.viewset”, quanto o meu “curso.viewset”. Então, eu vou fazer “router.register”, e vou passar para o register qual é a rota que eu quero atender.

[01:55] Então, eu quero registrar uma rota para aluno. Eu vou deixar “alunos”, no plural, uma rota para os meus alunos. Vou dizer qual é o meu viewset, “aluno.viewset”, e vou dizer também que o basename dele vai ser “alunos”.

[02:12] Vou fazer a mesma coisa com o meu “cursos”. Então eu vou registrar uma rota para cursos, só que quem vai atender vai ser cursos.viewset, e o basename vai ser “cursos”. Legal?

[02:28] O que eu preciso fazer agora? Eu já tenho essas minhas rotas cadastradas. Eu quero que, quando a gente acessar o “localhost:8000”, eu quero visualizar a minha página de API, e conseguir navegar entre as requisições de aluno e de cursos Vamos fazer isso?

[02:48] Então, eu vou tirar. Eu não quero mais uma rota principal para alunos. Eu quero incluir as rotas desse meu router que eu acabei de criar. Então, para eu fazer isso, eu vou colocar um include. Eu não tenho um include ainda. Vamos importar. Include, agora sim.

[03:05] Então, na rota principal, eu quero incluir lá do meu arquivo router, que tem as rotas registradas “.urls”. Eu vou salvar. Se eu abrir o meu servidor, agora, observe que a gente não tem mais aquele erro acontecendo. Vou minimizar. Se eu venho aqui no “localhost:8000”, e dou um enter, a gente tem o nosso Django Rest Framework com as nossas duas rotas principais, tanto de aluno, quanto de cursos.

[03:32] Mas é aí que está. Será que se eu clicar em “alunos”, eu vou visualizar aquele aluno que eu criei aqui no meu Django Admin, que está armazenado no banco de dados esse aluno teste com o RG 123456789? Vamos ver?

[03:44] Cliquei no aluno, e apareceu ID 1, aluno teste, CPF. Vou fechar. Vamos ver, então, de cursos? Vou voltar. Então eu tenho “curso”. Eu tenho curso de Django Rest Framework certinho.

[03:59] O que eu vou fazer? Vamos fazer a prova real disso. Eu vou criar mais um aluno. Vou criar o “aluno teste 2”. O RG vai ser 000. CPF vai ser 11111111111. A data de nascimento vai ser a data de hoje. Eu vou salvar. E observe que eu tenho o aluno teste, e o aluno teste dois, armazenado no banco de dados.

[04:23] Se eu venho aqui na minha API de alunos, eu tenho aqui o aluno um e o aluno dois. Maravilha. Está funcionando. Só que isso que a gente está vendo é API? Não. Isso é uma interface do Django para que a gente possa testar esses nossos alunos.

[04:40] Observe que eu tenho “localhost:8000/alunos”. Se eu colocar um, observe o que vai acontecer, ele vai trazer informações do aluno um. E se eu colocar, por exemplo, dois, ele vai trazer informações do aluno teste dois.

[04:54] Certo? Mas, como outro programa, outra aplicação vai visualizar? Eles vão visualizar dessa forma, Json. Então, quando a gente tiver uma requisição para a nossa aplicação pedindo o aluno dois, o que a gente vai visualizar são esses dados.

[05:14] E o que outro programa, outra aplicação vai fazer? Pega para mim o aluno, pega para mim o RG e coloca nessa caixa, coloca nesse box, coloca nessa tabela. Ou seja, eles vão consumir recursos da nossa API, e a gente vai conseguir integrar a nossa API, tanto com aplicações mobile, tanto com outros sistemas, tanto com outras APIs também.

[05:36] Certo. Mas a API serve simplesmente para listar os meus alunos? Eu estou visualizando todos os alunos. Se eu colocar aluno três. Vamos ver. Coloquei aluno três. Ele falou que não é encontrado. A gente não tem o aluno três cadastrado.

[05:49] Então, o que a gente vai fazer nos próximos vídeos? A gente viu, com o admin do Django, que é possível a gente criar aluno, é possível a gente criar curso. Mas como a gente cria alunos e cursos, e como a gente visualiza esses alunos e cursos sem o Django admin? Só visualizando no formato Json para a gente ter certeza que a nossa API está funcionando.

[06:09] É isso o que a gente vai ver nos próximos vídeos.

### Método GET e POST

[00:00] Agora que a nossa API está funcionando, vamos aprender um pouquinho mais de como funciona uma API utilizando Django Rest, e simulando outra aplicação consumindo os dados dessa API.

[00:11] Primeira coisa que eu vou fazer. Eu vou em “cursos”. A gente exibe todos os cursos. A gente pode criar um curso utilizando o admin do curso, então acessando “Escola > Cursos > Adicionar Cursos”. A gente tem aqui o código do curso que a gente cria, a descrição e o nível.

[00:25] E esse curso que a gente está vendo, é um curso que a gente criou utilizando o admin. Eu quero criar um curso, agora, utilizando o Django Rest Framework. Então, a gente tem algumas opções. Descendo a página um pouquinho para baixo, a gente tem aqui o “raw data” e o “HTML Form”.

[00:38] O “HTML Form” vai criar para a gente um Formulário para a gente criar o nosso curso. Então, se você observar, o “código curso”, “descrição” e “nível”. A gente tem algo muito parecido aqui: “código curso”, “descrição” e “nível.”. Bem parecido com o admin.

[00:54] Eu vou começar criando o curso utilizando esse “raw data”. Então, aqui a gente tem um objeto do tipo Json. Então, a gente vai criar um novo curso utilizando um “Json object”.

[01:08] Então eu vou colocar um JavaScript Object. Então, o código do curso vai ser o “curso de Java avançado 03”. Por exemplo. Esse código é arbitrário, eu estou inventando. Então eu vou colocar aqui que o curso vai ser “curso de Java avançado”. E o nível. A gente tem nível básico, nível avançado e intermediário.

[01:35] Vou colocar que vai ser do nível avançado. Beleza. Vou clicar aqui no Post. O que é o Post? O Post é uma requisição para a gente criar um novo curso, para a gente gerar um novo curso na nossa API. Então eu vou clicar nesse Post, e ele criou o “curso ID 2”, código do curso, 03, descrição do curso, e o nível A.

[02:01] Legal? Se eu for aqui no admin e clicar em “cursos”, olha que legal. Vai aparecer o ID 1 de um do curso de Django que a gente criou usando o admin, e esse curso dois, agora, de Java avançado, que a gente usou utilizando o Rest Framework com o Json.

[02:17] O que eu vou fazer? Vou criar um terceiro curso. Vou criar um novo curso, “root curso”. Vou usar o HTML Form e vou colocar “curso Django Rest Framework 03”, vai ser o avançado. Então, “curso de Django Rest Framework avançado”. Legal.

[02:48] Ele vai ser um nível avançado. Reparem que ele já formatou para a gente, consegui visualizar um nível também do curso que a gente está criando. Se eu coloco o “Post”, ele mostra para a gente detalhes desse curso três. A gente consegue acessar, se eu colocar aqui “curso três”, e a gente tem “curso de Django Rest Framework avançado”.

[03:05] Se eu colocar no curso dois, a gente tem “curso de Java avançado”, e se eu coloco no curso um, a gente tem o “curso de Django Rest Framework”, que é o nível básico. Legal? Eu entendi como é que funciona a criação utilizando o Post, só que eu quero fazer agora é simular uma outra aplicação.

[03:27] Na atividade “preparando o ambiente”, lá no início do nosso curso, a gente pediu para você baixar um programa chamado Postman. Eu já tenho ele instalado, que é esse programa aqui, e esse programa vai funcionar como um simulador. A gente vai conseguir testar as nossas APIs.

[03:43] O que eu vou fazer? Primeira coisa. Se a gente observar, a gente vai precisar, ele fala qual é o endereço, a requisição URL. Vamos pegar essa requisição, vou colocar aqui na nossa lista de cursos, vou voltar e vou colocar a requisição. Essa requisição é a requisição que está mostrando todos os cursos que a gente tem cadastrados.

[04:05] Então, eu vou utilizar aqui, nessa aba, eu vou utilizar o verbo “Get”, que eu quero visualizar, e vou dar um “send”. Olha só. O que vai acontecer. Ele trouxe para a gente todas as informações no formato Json para a gente conseguir visualizar e trabalhar com esses dados.

[04:22] Então, supondo que quem fez essa requisição é uma aplicação mobile, ele teria essas informações do formato Json, e da mesma Forma que a gente faz a deserialização dos dados para a linguagem que a gente está utilizando, a gente consegue fazer em outra aplicação.

[04:42] A ideia do Postman é que a gente consiga testar as nossas aplicações. E quando a gente vem, a gente tem vários verbos. A gente vai testar dois. Então, o primeiro verbo que a gente está utilizando é o verbo “Get”, que a gente quer recuperar um determinado recurso. Então, eu vou colocar aqui “1/”, vou dar um enter, e a gente tem aqui o curso de Django.

[05:00] Se eu colocar “3/”, ele vai trazer o curso de Django avançado. Se eu tirar a barra e der um enter, ele funcionou, porém, a gente tem que ficar muito atento com os detalhes da nossa requisição.

[05:17] Por exemplo, se eu colocar duas barras e der um send, ele vai mostrar para a gente uma mensagem de erro. Ele está renderizando uma mensagem de erro, que a gente não tem essa requisição cadastrada.

[05:29] Então, um dos pontos sensíveis do Rest Framework é que as nossas URLs precisam ser muito bem definidas, e a gente precisa tomar bastante cuidado com as requisições que a gente está fazendo, se não tem nenhum erro aqui.

[05:43] Se eu colocar, por exemplo, cinco. A gente não tem nenhum curso cinco. Ele fala que não foi encontrado esse curso cinco. Então é legal que a gente já tenha algumas informações.

[05:50] Legal, Guilherme. Conseguir entender, então, que o verbo “Get” é para a gente recuperar um determinado recurso da nossa aplicação, mas o que eu quero fazer agora é criar um novo curso, ou um novo aluno, utilizando aqui o Postman. Então, a gente viu como criar um curso utilizando a interface do Django Resto.

[06:10] O que vou fazer agora? Eu vou criar um aluno. Vou voltar aqui na API Root, vou acessar “aluno”, e eu quero criar um novo aluno. Então aqui a gente tem as mesmas informações: o nome, RG, CPF, data de nascimento. Aqui no HTML Form, no raw data, a gente tem essas informações aqui.

[06:25] Eu vou copiar essas informações, e vou fazer o seguinte. Vou voltar lá no nosso código. Um detalhe. Se a gente observar, a data de nascimento está com o formato americano. Então, o que eu vou fazer? Vou copiar esse código com a ID 2. Vou voltar lá na nossa aplicação, e agora, o que eu quero fazer é um método Post para URL de alunos. “alunos/”.

[06:56] O método, então, é o Post, e eu quero fazer essa requisição. A primeira coisa que a gente vai fazer vai ser ir no “body”, eu vou remover esses dados que estão aqui e vou colar aqueles dados que eu copiei, aquele Json que eu copiei.

[07:11] O ID não precisa passar. Por quê? O ID é gerado de Forma automática assim que a gente cria o nosso modelo. Então, quando a gente identificar esse aluno, eu vou colocar “aluno do Postman”, porque aí a gente já vai saber. O RG, eu vou deixar esse mesmo, para a gente não perder tempo.

[07:31] CPF, eu vou deixar esse mesmo, e a data de nascimento, eu vou falar que nasceu no mês passado. No mês cinco. Eu vou um send, e olha só, ele deu outra informação, ele falou que não veio nenhuma mensagem de erro. Agora a gente tem o ID 3 para o aluno do Postman, que é esse programa que a gente está usando.

[07:51] Certo. Mas será que esse aluno foi gerado na nossa aplicação? Vou atualizar, e a gente tem o aluno três. Para a gente garantir, vou acessar o nosso “Admin > Escola > Alunos”, e a gente tem o aluno do Postman também gerado.

[08:04] Então, o método Get é para a gente recuperar um determinado recurso; o método Post, para a gente criar um novo recurso utilizando a nossa API.

### Um pouco mais sobre Viewsets

Como vimos na aula, os ViewSets permitem definir as interações da sua API e permitir que a estrutura REST construa os URLs dinamicamente com um objeto roteador.

Sabendo disso, analise as afirmações abaixo e marque as verdadeiras.

a) Um Viewset é a fonte única e definitiva de informações sobre seus dados.

b) **Alternativa correta:** A utilização de Viewset pode evitar repetir a lógica das views.
- _Alternativa correta! Certo! Não será necessário incluir a lógica para um CRUD, analisando as estruturas do REST para cada recurso._

c) **Alternativa correta:** Viewsets incluem ações como criar, listar, atualizar ou deletar.
- _Alternativa correta! Certo! Os Viewsets incluem essas ações ou operações por padrão._

## 4. Atualizando e deletando recursos
### Métodos PUT e PATCH

PUT: Utilizado para atualizar apenas um campo.
PATCH: Utilizado para atualizar todos os campos.

---

[00:00] Nós utilizamos o método Get para recuperar um determinado recurso. Utilizamos o método Post para criar um novo recurso na nossa API. Só que aqui temos um problema.

[00:10] Se você observar o CPF do aluno dois e o CPF do aluno três, estão iguais, então aconteceu um erro no cadastro. E a gente precisa atualizar esse nosso aluno três. O CPF dele é 22222222222. Certo?

[00:26] Então, eu vou acessar o aluno três aqui. Então, “localhost:8000/aluno3”. Trouxe esse aluno três. Temos alguns métodos em cima. Quando a gente desce um pouquinho, aparecem duas informações: o PUT e o PATCH. Vamos descobrir, então, qual a diferença entre eles e o que eles fazem.

[00:45] Para começar, o método PUT é usado também para atualizar, assim como o PATCH. Ou seja, existem dois métodos HTTP, dois verbos do HTTP, que a gente pode utilizar para fazer a atualização.

[00:59] Então, vamos lá. Vamos começar com o PUT, primeiro. O PUT substitui todos os dados atuais de um recurso de destino pelos dados passados na requisição. Ou seja, a gente escolhe o PUT quando a gente pretende fazer uma atualização completa de um determinado recurso.

[01:15] Tanto que quando a gente acessa o HTML Form, observe a gente só tem o PUT, e a gente pode fazer uma atualização completa desse recurso. Por outro lado, o PATCH permite que a gente atualize apenas um subconjunto de dados de um determinado recurso.

[01:30] Como a gente tem apenas um recurso, a gente não tem mais recurso. Vamos supor que dentro de “aluno”, eu tenho também “profissão”; e dentro dessa “profissão”, existe um outro recurso, um subconjunto de dados. Se fosse assim, eu poderia usar o método PATCH para atualizar apenas um subconjunto dos dados de um determinado recurso.

[01:51] Então, existem dois verbos. A gente pode utilizar o método PUT para fazer uma atualização completa, e a gente pode utilizar o método PATCH quando a gente quer atualizar apenas um subconjunto dos dados.

[02:03] Certo? Mas vamos ver isso na prática, acontecendo? Eu quero atualizar o CPF do aluno três. Então, vamos começar. Eu vou colocar, no lugar desses números, a gente vai ter onze números dois. Legal. Vou atualizar com o PUT, e a gente atualizou.

[02:31] Vou atualizar para o CPF para 3333 com o PATH, só para a gente ver. Então, selecionei tudo. Vou dar um PATH. E a gente também tem essa nossa atualização completa. Certo? A gente poderia atualizar também aqui no HTML Form. Vou atualizar com o quatro. Dou um PUT, atualizou com o quatro.

[02:57] Se a gente observar lá na lista dos nossos alunos, o ID 3, CPF 444. Mas será que no Postman também vai funcionar assim? Vamos testar. Vou abrir o Postman, para a gente poder visualizar. Legal.

[03:13] Então, vou trazer o aluno três., vou trazer esses recursos primeiro com o Get. Trouxe o aluno três, maravilha. Vou copiar esse nosso Json, e vou fazer, agora, um PUT desse nosso aluno. Então vou vir em body, vou colar aquele Json que eu copiei, e vou alterar para CPF cinco.

[03:38] Vou dar um send, e a gente tem aqui o CPF cinco, mas será que atualizou? Observe que ele está com quatro, vou atualizar. Agora sim, com cinco. Então, existem dois verbos utilizados para a gente atualizar, o PUT e o PATCH, e essas são as diferenças entre eles.

### Método DELETE

[00:00] O que eu quero fazer agora é remover um determinado aluno da minha API. E a gente vai ver isso, tanto na parte do admin, como na parte daqui do nosso Django Rest Framework, como utilizando o Postman, simulando outra aplicação.

[00:12] Para começar, eu vou criar o aluno que eu vou deletar. Então eu vou aqui em “Escola > Adicionar novo aluno”, e vou chamar “aluno para deletar”. O RG dele vai ser o 000, o CPF dele vai ser o 000 também. Data de nascimento, vou colocar a data de hoje, e eu vou salvar.

[00:29] Legal. A gente tem aqui um aluno para deletar. O que eu vou fazer? Eu poderia selecionar esse aluno aqui no admin, colocar “remover aluno selecionado”, vir aqui em “ir”, e ele vai falar “você quer remover um aluno”, que é o aluno para deletar. “Tem certeza que quer fazer isso?”, poderia clicar em “sim”, e eu ia remover esse meu aluno da base de dados.

[00:46] Outra coisa que eu posso fazer, se eu atualizar, eu vou ver que eu tenho o “ID 4”, agora, que é o aluno para deletar. Se o acesso aqui o “ID 4” para ter informações desse recurso, desse determinado aluno, observe que aparece aqui para a gente o método “delete”.

[01:00] Então, vou apertar o “delete”, e ele vai falar: “você tem certeza que quer deletar a instância desse aluno?”. Eu vou falar que tenho certeza, e aquele aluno não aparece mais.

[01:09] Se eu der um outro “enter” aqui, observe que ele vai falar que não tem nada, a gente não encontrou nenhum aluno, nenhum recurso para essa requisição. Então eu vou voltar. A gente tem três alunos.

[01:17] O que eu vou fazer? Eu vou deletar mais um aluno, agora. Eu vou deletar o aluno três, só que utilizando o Postman, está bom? Então, o que eu vou precisar fazer? Vou precisar acessar o meu aluno três, que é esse endereço aqui, vou lá no meu Postman, vou colocar o método que eu quero utilizar, é o método “delete”.

[01:36] E já está aqui o aluno três. Se eu der um “send”, observe que aqui embaixo a gente vai ter uma notificação. Então, a gente colocou o aluno três para ser deletado, e aqui embaixo, a gente não tem absolutamente nada.

[01:48] Eu vou voltar na nossa aplicação, no nosso Django Rest, vou atualizar, e a gente não tem nenhum detalhe aqui mais para esse aluno três. Se eu coloco aqui na nossa lista, a gente só tem dois alunos.

[02:00] Certo? Então, dessa forma, a gente conclui o crud. A gente sabe criar um determinado aluno utilizando o Post, a gente sabe deletar um aluno utilizando o método delete, recuperar um recurso com o “get”, e atualizar utilizando o PUTT ou o PATH.

[02:15] Legal? E aqui, só para a gente terminar. Se eu colocar aqui o método delete de novo para um aluno que não existe? Vamos ver. Eu vou dar aqui um “send”, e ele fala a mesma mensagem que a gente tem lá: não encontrado.

[02:26] Nos próximos cursos, a gente vai aprender melhor como trabalhar com validações, como trabalhar com essas mensagens que retornam quando acontece algo não esperado para a nossa API.

[02:35] Mas, por enquanto, é isso. Então, a gente conclui a parte do crud, e nas aulas seguintes, a gente vai aprender a fazer relacionamento. Por quê? Se a gente observar agora, a gente tem uma tabela de alunos, e uma tabela de cursos.

[02:50] O que eu quero fazer? Eu quero matricular um aluno em um determinado curso, quero falar que esse aluno está matriculado no curso de Django, e esse outro aluno está matriculado no curso de Java.

[03:00] É isso o que a gente vai começar a fazer, e aprofundar os nossos conhecimentos um pouquinho mais aqui no Django Rest Freamework.

### Modelo de matrícula

[00:00] Eu tenho aqui a lista dos meus alunos, e acessando o meu API Root, eu tenho a lista dos cursos que eu criei. Só que as listas de alunos, e as listas de cursos, não estão alinhadas. A gente não tem um relacionamento entre esses cursos e alunos.

[00:16] Por exemplo, a gente não tem uma matrícula. Eu não consigo falar que esse aluno está matriculado nesse curso. Seria legal se a gente pudesse criar isso, armazenar essas informações das matrículas também no banco de dados. E é isso o que a gente vai fazer agora.

[00:29] O que eu vou fazer? Eu vou acessar o meu “models.py”. A gente tem aqui o model, a classe aluno, a classe curso, e vou criar uma nova classe, que vai ser a classe matrícula.

[00:41] Então, classe, vou chamar de matrícula. Ele também vai ser do tipo models.model. E a minha matrícula, eu quero que tenha o aluno, o curso, e algumas informações da própria matrícula, como, por exemplo, a gente pode criar o período.

[00:58] Então eu vou colar, vou copiar esse textinho que do nível, e vou criar, no lugar de nível, uma variável de instância chamada “período”. E aqui, no período, eu vou ter três períodos: matutino vespertino e noturno. E vou colocar o matutino, vespertino e noturno.

[01:25] O que eu quero fazer agora na minha matrícula é falar que uma matrícula tem um aluno. Então, eu vou alterar, vou criar uma propriedade chamada “aluno”, que uma matrícula vai ter um aluno, e vou falar que ela vai ser da seguinte propriedade: “models.foreignkey”.

[01:41] Por que “foreignkey”? Eu já tenho esse aluno criado numa outra tabela. Eu só quero pegar o ID desse aluno e armazenar na minha matrícula. Então, a primeira informação que a gente passa quando utiliza o “models.foreignkey”, é qual a tabela que a gente vai utilizar, quem vai ser responsável por mandar essa primary key. Então, vai ser o aluno.

[02:00] Outra propriedade que a gente vai passar é o “on delete”. Vamos supor que a gente tenha um aluno matriculado em um determinado curso, e esse aluno, por algum motivo, é removido da nossa base de dados, ele foi deletado.

[02:11] O que a gente quer que aconteça com essa matrícula? Ela vai referenciar para um aluno que não existe mais? Isso não seria legal. A gente teria um erro. Então, eu vou falar que a gente vai utilizar o “models.cascade”. Ou seja, quando um aluno for deletado, a gente vai remover também as matrículas dele.

[02:28] O mesmo eu quero que aconteça para o curso. Então, o curso, ele vai ser do tipo “models”. Então eu colei, vou usar o curso, models, vou colocar o curso, “on delete cascade”. A última coisa que falta é a gente definir o período.

[02:45] Vou copiar essa nossa linha que já está feita. O que eu vou fazer? Aqui, no lugar do nível, a gente vai ter o período, e esse período vai ser propriedade sharfield, max length, o choice vai ser a nossa instância. “Blanke false”, “no false”, e o valor default dela vai ser matutino.

[03:12] Criamos a classe de matrícula. O que eu vou fazer? Para a gente conseguir visualizar essa classe de matrícula, eu vou acessar o meu “admin.py”, e vou criar uma propriedade aqui para as nossas matrículas.

[03:28] Então, eu vou trazer, primeiro, “matrículas, matrícula”. Essa classe vai ser responsável pelas configurações no admin de matrícula. A gente não vai ter um campo de busca. Eu quero só o ID, o nome do aluno, o nome do curso e o período.

[03:50] Legal. O link display vai ser o ID, e vamos registrar isso aqui. Então, a gente vai utilizar o modelo de matrícula, e quem vai ser a classe responsável pelas configurações vai ser matrículas. No plural.

[04:10] Bom, abrindo o nosso terminal, parece que está tudo certo. O que eu vou fazer? Vamos fazer a migração. A gente criou o nosso modelo, mas a gente não fez ainda a migração, a gente não passou essas informações para o banco de dados.

[04:20] Então, vou parar o meu terminal, vou colocar aqui “phythonmanager.py”, “make my graysons”. Dou um enter. Ele criou a migração de matrículas. O que eu vou fazer agora é migrar, de fato, para o banco de dados. Então, “phythonmanager.py”, “mygrade”.

[04:40] Legal. Ele aplicou essas migrações no banco de dados. O que eu vou fazer? Para a gente visualizar, vamos subir o nosso servidor com o “pythonmanager.py”, “runserver”.

[04:50] Voltando aqui no nosso admin, quando eu atualizar, apareceu aqui “matrículas”. Legal. Quando eu clico em matrícula, a gente não tem nenhuma matrícula criada. Vou clicar aqui em “adicionar matrícula”, e aqui, na lista de aluno, a gente tem não tem nada, aluno teste, aluno teste dois.

[05:04] Então eu vou matricular o aluno teste no curso de Django Rest Framework, no período matutino. Vou salvar. E a gente tem aqui a nossa primeira matrícula. Quando eu clico no “um”, a gente consegue visualizar os detalhes dessa matrícula, apagar, configurar, mudar a matrícula desse determinado aluno.

[05:22] O que eu vou fazer também? Vou criar uma segunda matrícula, só para a gente garantir. Aluno teste dois, no curso de Java avançado, no período noturno. Quando eu coloco em salvar, a gente tem o segundo aluno matriculado.

[05:37] Certo? Só que se a gente acessar a nossa interface do Django Rest, a nossa API root, a gente não tem ainda a matrícula visível, para que a gente possa fazer, gerar essas matrículas usando aqui a nossa API. É isso o que a gente vai fazer na sequência.

### Recurso de matrícula

[00:00] Configuramos nosso admin para realizar as matrículas dos alunos, e na lista de cursos que a gente tem. Isso ficou bem legal. Só que quando a gente vai na nossa API, a gente não tem esses recursos de matrículas disponíveis. Vamos tornar esses recursos disponíveis, então?

[00:15] Então, olha só. A gente já tem um modelo, vou abrir aqui o modelo, em “models.py”. A gente criou esse modelo de matrícula, ele já está na nossa base de dados. O que eu preciso fazer agora? Vamos, da mesma forma que a gente fez, para o aluno e para o curso, a gente precisa de um sinalizador.

[00:29] Depois, lá no nosso arquivo “view”, definir o nosso “viewset.modelvierset” filho para a gente conseguir exibir essas nossas matrículas, e em URLs, a gente registra essa nossa matrícula depois.

[00:42] Então, vamos fazer isso? Bom, para a gente não ficar confuso, vou fechar esses aqui. Eu vou criar uma classe para ser responsável por serializar os dados de matrícula. Então, no model, a primeira coisa que eu vou fazer vai ser trazer uma matrícula para cá.

[01:03] E eu vou chamar essa classe de “matrícula.serializer”. Ele vai ser do tipo “serializers.modelserializer”, e aqui eu vou definir a classe meta dele. E vou dizer para ele que os campos que eu quero, qual é o modelo que eu quero primeiro.

[01:30] O modelo que eu quero vai ser o modelo de matrícula, que a gente trouxe ali em cima. E os campos que eu quero, eu quero visualizar todos os campos. Se a gente olhar os outros, observe o que a gente fez. A gente tem o “fields”, o “fields.all”, para trazer todos.

[01:46] Existe uma outra forma que a gente pode visualizar os campos, que é através do “exclude”. Vamos supor que eu tenha muitos campos, e eu quero excluir, por exemplo, o ID. Eu faço dessa forma. Colchetes, e eu trago o ID.

[02:00] Dessa forma, a gente vai trazer todos os campos, exceto o ID. Só que eu quero trazer o ID também. Então, se eu deixar o “exclude” vazio, eu trago todas as informações da nossa base de dados.

[02:12] Legal? Bom, criamos uma matrícula serializer. O que eu vou fazer? Lá em “view”, eu vou trazer, primeiro, o meu modelo de matrícula. Observe que está bem passo a passo, como a gente fez nos outros.

[02:27] Trazer o modelo de matrícula, e no “escola.serializer”, eu vou trazer também o “matrícula.serializer”. E aqui eu vou criar a minha classe “viewset”. Então vai chamar “matrícula.viewset”. Vai ser do tipo “viewsets.modelviewset”. Vou colocar um “dockstring” para ficar bem bonita a nossa documentação.

[02:55] Então, listando todas as matrículas. Legal. E aqui embaixo, vou definir. O “query_set” vai ser “matrícula.objects.all”, quero trazer todas as matrículas, e o meu “serializer class” vai ser do tipo “matrícula.serializer”. Legal?

[03:25] Abrindo nosso servidor, parece que está tudo certinho. Vou adicionar, registrar essa minha matrícula no meu “urls.py”. Então, vou trazer o meu “matrícula.serializer” e vou criar uma nova rota. Vou copiar e colar isso aqui. Agora sim. Vou chamar de “matrícula.viewset”. E o basename vai ser “matrículas”.

[03:05] Abrindo nosso servidor, parece que está tudo certinho. Quando eu atualizar a página, a gente vai ter um recurso novo para visualizar todas as matrículas. Quando eu clico, aqui a gente tem a matrícula do aluno um, e a matrícula do aluno dois. Se eu acessar aqui o admin, e clicar em “matrículas”, eu tenho o ID 1, duas matrículas feitas. A gente tem a forma que esse “matrícula” está sendo executado, e tem os cursos.

[04:29] Só que aí tem algo interessante. Observe uma coisa. Na nossa API, a gente tem um recurso principal para criar um aluno, isso está bem legal. A gente tem um recurso principal para também criar cursos, editar cursos, deletar cursos, isso ficou bem legal.

[04:42] Porém, aqui nas nossas matrículas, quando a gente clica, a gente tem uma lista de todas as matrículas. E talvez isso não faz muito sentido. É legal a gente poder criar as matrículas, editar as matrículas. Por exemplo, eu quero visualizar detalhes da matrícula um. Aparece o período matutino, foi o aluno teste, e o curso, foi o curso de Django Rest Framework. Esse aluno vai mudar, ele vai para o período vespertino.

[05:06] Eu dou um PUTT, e ele alterou, foi para o período vespertino. Isso ficou legal. Só que para eu consegui identificar qual é o aluno que está matriculado em um curso, ou quais são os alunos matriculados em um determinado curso, ficou um pouco complexo.

[05:23] E o que a gente pode pensar? Se a gente observar, olha só. A nossa lista de matrículas está funcionando também em outros lugares. Se eu vier aqui no Postman e der um get em “localhost:8000/matrículas”, a gente tem todas as informações aqui.

[05:37] Ou seja, nossa matrícula está funcionando, só que a gente está listando todas. Seria legal se eu pudesse identificar quais são todos os cursos que um determinado aluno está matriculado. Ou seja, eu vou falar que o aluno dez, eu quero ver as matrículas dele.

[05:52] Então eu quero ver os cursos desse aluno. E a gente lista todos os cursos desse aluno. E se a gente precisar editar alguma informação, a gente já tem mais detalhes sobre a matrícula desse aluno. Ou o oposto também.

[06:07] Vamos supor que eu tenho o curso dois. No curso dois, eu quero listar todos os alunos. Eu coloco o “curso dois alunos”, e eu consigo visualizar todos os alunos matriculados naquele curso.

[06:19] Observe que se eu faço isso e dou um enter, a gente recebe um “page not found”. Ou seja, a gente precisa configurar a nossa API de uma forma diferente para listar algumas informações que a gente quer. Permitindo também algumas ações. por exemplo, aqui em “matrícula”, eu tenho o meu “crud” completo.

[06:36] Eu posso criar uma nova matrícula com o Raw Data, ou com o meu HTML Form e dar um post. Eu posso editar uma matrícula, se eu coloco aqui “matrícula dois”, por exemplo, eu consigo editar detalhes dessa matrícula. Eu posso deletar essa matrícula. Ou seja, eu posso fazer bastante coisa.

[06:53] Nessa minha lista de cursos, eu não quero permitir todas essas ações. Vamos supor que eu quero apenas listar, ou apenas buscar alguma informação. Não vou permitir deletar determinadas matrículas, ou determinadas turmas inteiras.

[07:09] Então, o que a gente vai aprender na sequência? Na sequência, a gente vai aprender como configurar a nossa API de forma que a gente consiga colocar mais informações na nossa URL, e a gente tenha o resultado da lista que a gente quer, dos recursos que a gente quer.

[07:24] E mais: como a gente consegue limitar quais ações a gente vai querer dentro desses recursos.

### Verbos HTTP

O protocolo HTTP define um conjunto de métodos de requisição responsáveis por indicar a ação a ser executada para um dado recurso. Embora esses métodos possam ser descritos como substantivos, eles também são comumente referenciados como HTTP Verbs (Verbos HTTP).

Em relação aos verbos, podemos dizer que:

a) **Alternativa correta:** O método DELETE remove um recurso específico.
- _Alternativa correta! Certo! Conforme vimos em aula, o localhost:8000/alunos/2 com uma solicitação DELETE por exemplo, irá remover este recurso do servidor._

b) **Alternativa correta:** Existem 2 métodos para atualizar um recurso no servidor.
- _Alternativa correta! Certo! O método PUT substitui todas as atuais representações do recurso de destino pela carga de dados da requisição Já o método PATCH é utilizado para aplicar modificações parciais em um recurso._

c) O método POST também pode ser utilizado para solicitar a representação de um recurso específico.

d) **Alternativa correta:** O método GET solicita a representação de um recurso específico.
- _Alternativa correta! Certo! Conforme vimos em aula, o localhost:8000/alunos/2 com uma solicitação GET por exemplo, nos mostra detalhes de um determinado aluno ou aluna._

### Faça como eu fiz
### O que aprendemos?
## 5. ListAPIView e Autenticação
### Projeto da aula anterior
### ListAPIView
### Matrículas de um curso
### Autenticação
### Exibindo ID
### Faça como eu fiz
### Projeto do curso
