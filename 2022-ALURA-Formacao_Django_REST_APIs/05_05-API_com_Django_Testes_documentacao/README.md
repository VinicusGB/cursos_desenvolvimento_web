# API com Django 3: Aprofundando em testes e documentação - 8h
**Professor:** Guilherme Lima

**Disponível:** [ALURA]('https://cursos.alura.com.br/course/api-django-3-testes-documentacao')

**Conteúdo:**
- Aprenda a escrever testes automatizados nos modelos, serializers e outras partes de sua aplicação
- Entenda a importância dos testes no desenvolvimento de software
- Saiba como integrar o Swagger para gerar a documentação de sua API
- Conheça uma forma de carregar dados JSON no banco de dados, integrando os modelos
- Descubra como realizar diferentes testes no Postman

## 01. Tipos de testes
### Apresentação

[00:00] Olá! Meu nome é Guilherme Lima e eu serei o seu instrutor nesse treinamento de Django Rest, aprofundando em testes e documentação. O que vamos aprender nesse curso?

[00:109] Nesse curso vamos escrever uma série de testes automatizados para verificarmos os nossos modelos, nossos serializers, para verificarmos a autenticação de um determinado recurso, se é permitido ou não. Veremos como conseguimos escrever esses testes.

[00:23] Vamos aprender também como documentarmos a nossa API para que outras pessoas consigam utilizar. Para quem é esse curso? Esse curso é super indicado para as pessoas que fizeram o curso anterior, de pré-requisito, de Django Rest; já vimos uma pincelada de teste. Nesse curso vamos nos aprofundar nesse conceito de testes.

[00:43] Fazendo esse curso, vamos trabalhar e escrever uma série de testes: testes de autenticação, testes nos nossos modelos, testes no serializer e como executamos e escrevemos esses testes da melhor forma.

[00:56] Falando da parte da documentação da nossa API que vamos desenvolver, vamos ter um recurso de programas e vamos ver como documentar esses programas utilizando o “Swagger”.

[01:09] Então, fazendo esse curso nós vamos aprender uma série de coisas bacanas relacionadas a testes e documentação utilizando o Django Rest. Sabendo de tudo isso, vamos começar?

### Preparando o ambiente

Olá!
É muito bom receber você neste curso de API com Django 3: Aprofundando em testes e documentação.

Espero que seja uma experiência de aprendizado incrível e que possamos vencer todos os desafios juntos. Neste curso, vamos aprofundar nossos conhecimentos no Django Rest Framework e aprender como criar diferentes tipos de testes, sejam eles nos modelos, serializers e muitos outros. Vamos entender a importância dos testes e documentar nossa API com Swagger.

Carregando o projeto base do curso
Para que tenhamos o mesmo resultado, é recomendado que você faça o download da mesma versão do Python e do Django que utilizei quando o curso foi gravado, que poderá ser encontrada aqui:

        Python 3.7.4
        Django 3.1.5

O Django pode ser instalado através do comando:

        pip install Django==3.1.5

Além disso, usaremos um projeto base no qual você pode realizar o download [neste link]('https://github.com/alura-cursos/drf_teste_documentacao/archive/projeto_inicial.zip').

Após o download, abra o projeto em seu editor de código preferido e crie uma nova venv com o comando python -m venv ./venv e ative conforme seu sistema operacional.

Para sistemas MacOS ou Linux:
source venv/bin/activateCOPIAR CÓDIGO
Já no Windows:

        venv\Scripts\activate.bat

Após ativação, faça a instalação dos módulos necessários com o seguinte comando:

        pip install -r requirements.txt

Agora, execute as migrações dos modelos:

        python manage.py migrate

Para garantir que tudo deu certo, suba o servidor:

        python manage.py runserver

Na próxima atividade, vamos aprofundar ainda mais nossos conhecimentos utilizando esta incrível ferramenta de desenvolvimento.

Em caso de dúvidas durante o curso ou carregamento do projeto, conte sempre com o fórum da Alura!

:)

### Conhecendo o projeto

1. No terminal podemos carregar nossos dados com um comando:

        python manage.py loaddata programa_iniciais.json

---

[00:00] Vamos iniciar os nossos estudos, então? Para começarmos, na atividade anterior a esse vídeo temos um passo a passo de como você vai baixar o projeto base que vamos utilizar para criarmos a nossa documentação, criarmos os testes da nossa API e aprofundarmos os nossos conhecimentos com o Django Rest.

[00:17] Já segui todos os passos descritos nessa atividade e o que vou fazer agora vai ser subir o meu servidor, para nós entendemos melhor como está funcionando a nossa API. Então digito python manage.py runserver no aplicativo, com minha venv já ativada. Aperto a tecla “Enter” e vou abrir o localhost:8000.

[00:36] Temos uma API de programas. Quando eu clico, ele pede que eu tenha um usuário de acesso. Na atividade também está descrito para criar um usuário, então vou colocar meu usuário gui e minha senha que ninguém imagina que é, 123. Vou apertar a tecla “Enter” e conseguir acesso à minha API.

[00:54] Nesse projeto vamos trabalhar com uma API inspirada nos sistemas de streamers que temos, como Netflix, Amazon Prime, entre outros. Então na nossa API vamos ter um título, vamos ter um tipo, uma data de lançamento e a quantidade de likes. Essa vai ser a ideia da nossa API.

[01:14] O que vou precisar fazer? Temos nossa API e queremos testar a nossa API, além disso, se clicamos em “Filtros”, observe que temos filtros para filtrarmos só o filme ou filtrarmos apenas as séries, e tem um campo de busca em que eu consigo pesquisar pelo título.

[01:32] Todas essas informações, conseguimos observar no app “aluraflix > views.py”. Se observarmos esse teste, temos o nosso queryset de objetos, temos nossa classe de serializer e temos o filtro que eu mostrei para vocês.

[01:49] Então vamos conseguir pesquisar pelo título do programa, seja ele um filme ou uma série. Temos um campo de busca no lugar do título, um filtro para identificarmos se vai ser um filme ou uma série e temos a nossa classe de autenticação, o BasicAuthentication. Isso ficou bem bacana, só que eu tenho 0 filmes.

[02:09] Sempre quando vamos iniciar um projeto, seria legal se tivéssemos uma forma de carregarmos os dados iniciais - no nosso caso, os programas iniciais, sejam eles séries ou filmes. Existe uma forma de fazermos isso!

[02:21] Vamos imaginar que estamos desenvolvendo nossa API e que o time que cuida do banco de dados já nos passou alguns programas iniciais. Então dentro do nosso app da “aluraflix”, temos uma pasta chamada “fixtures”. Quando eu clico nela, temos o objeto JSON, que se chama “programas_iniciais.json” e dentro temos um array com vários programas.

[02:49] O primeiro programa então é aluraflix.programa- sempre identificamos o modelo que estamos trabalhando. Temos a chave primária, qual vai ser o id desse programa, os campos e seus respectivos atributos.

[03:05] Então eu tenho: ”título”: “Coisas bizarras” - é uma série, tem a data de lançamento, quantidade de likes e quantidade de dislikes. Eu tenho essa informação para todos os outros filmes e séries.

[03:17] Então tem: “Coisas bizarras”, “O Bruxo”, “Emília em São Francisco”, “Corações de lata”, “Le Le Lend”, “Saltadores Ultimato” e grandes sucessos da “aluraflix”. Qualquer semelhança com um filme real é coincidência mesmo.

[03:29] Então tenho esses programas, tenho esse arquivo JSON. Como que eu faço para carregar esses arquivos JSON na minha base de dados? Abrindo o meu terminal, vou pará-lo e, o que vou fazer? Existe um comando para eu carregar os dados, o nome é muito parecido com o que falamos mesmo: loaddata, ou seja, “carrega os dados”. Agora vou passar qual é o arquivo que eu quero carregar os dados.

[03:53] Poxa, está em JSON e vamos fazer nosso projeto utilizando o Python, o Django! Como ele vai entender do JSON para o Django, como ele nos faz essa ponte? Esse método tem essa responsabilidade. Na próxima atividade eu vou deixar um link para nós entendermos melhor como essa função funciona.

[04:14] Então, loaddata. Vou passar que eu quero carregar programas_iniciais.json. Quando eu aperto a tecla “Enter”, olhe o que vai acontecer: ele fala que foi instalado novos objetos de uma fixture(s). Então tem algo importante para eu passar para vocês.

[04:30] Observe que dentro da pasta do meu app, eu tenho uma pasta chamada “fixtures”, dentro dessa pasta eu tenho um arquivo JSON com os dados que eu quero carregar, os iniciais. Para eu conseguir carregar esses dados, eu só executo o comando loaddata do manage.py e passo o nome do arquivo JSON.

[04:50] Vamos supor que no meu modelo da “aluraflix” eu tenha, além de programas, diretores, roteiristas e várias outras classes de modelo. O que eu poderia fazer? Poderia criar um outro arquivo JSON para preencher esses modelos.

[05:08] E aqui eu faço a referência, que nesse caso é o programa - mas se fosse os diretores eu escreveria aluraflix.diretores e passaria qual é id e quais são os campos com seus dados. Para eu carregar, só passo o nome dele depois do loaddata.

[05:27] Carreguei, mas será que carregou mesmo? Vamos ver! Vou subir o meu servidor mais uma vez. Quando eu venho no programa e atualizo, temos “Coisas bizarras”, “O bruxo”, “Corações de lata”, “Resgate do soldado Carlinhos” e vários outros filmes bem legais também, “Capitão Bahia”. Filmes de sucesso da “aluraflix”.

[05:45] Qual é o nosso desafio agora? Podemos conferir, por exemplo, se eu colocar o filtro de “Série” no campo “Tipo” e enviar que eu quero ver só as séries, eu tenho: “Coisas bizarras”, “O bruxo” e “Emília em São Francisco”. Se eu coloco, por exemplo, “Filme” no campo “Tipo” e enviar, temos só os filmes: “Corações de lata”, “Le Le Lend” e “Saltadores ultimato”. Isso ficou bem bacana!

[06:08] Se eu pesquisar também, por exemplo, por “Saltadores” e dar uma busca, verei só aquele filme “Saltadores ultimato”. Isso ficou bem legal! Aparentemente a nossa API está funcionando, porém é importante que garantamos que partes diferentes da nossa API estejam funcionando. Vamos entregar o comportamento que esperamos. Por isso a importância dos testes.

[06:33] Nas próximas aulas vamos aprofundar mais ainda nesse conhecimento dos testes, a importância dele e como testamos diferentes partes da nossa API.

### Tipos de testes

"O código sem testes será quebrado conforme projetado." Jacob Moss

 #### Tipos de testes
- **Teste manual _[Uma pessoa]_**
- **Teste automatizado _[Máquina]_**
  - **Teste de unidade:** Testar métodos e funções individuais
  - **Teste de integração:** Testar diferentes módulos ou serviços usados para um aplicativo
  - **Teste funcional:** Testar os requisitos do negócio

Outros para pesquisar:
- **Testes funcionais:**
  - _unidade / integração / aceitação_
- **Testes não funcionais:**
  - _performance / carga / estresse_

---

[02:26] Lembra, no nosso curso anterior em que realizamos o teste para verificarmos a requisição get, a requisição post e a requisição init? Aquele teste poderia ser feito por uma pessoa. Eu poderia contratar uma pessoa, um amigo meu e falar: “teste, faça uma requisição get e me fale o que acontece. Anote o que acontece” e a pessoa iria anotando.

[02:45] Nos testes automatizados, o que garantimos? Garantimos que a máquina vai cumprir as etapas do script que passamos e garantimos os determinados resultados esperados. Caso um resultado não dê certo, aquele teste falhe e podemos identificar o porquê da falha.

[03:01] Então dentro deste mundo de testes automatizados, existe um teste chamado “teste de unidade”. Qual o objetivo dele? É testar métodos e funções individuais.

[03:11] Se observarmos na nossa aplicação, nós temos um modelo, um serializer, nossa view; então eu quero testar o modelo. Por exemplo: no nosso modelo, observe que temos os campos titulo e tipo, porém entre esses campos existem alguns valores default. Então caso eu não passe nenhum valor de like ou dislike, o valor default deles será 0.

[03:33] Então eu poderia criar um teste para verificar se de fato esse valor default está sendo executado. Isso seria um teste de unidade, em que eu queira testar apenas o modelo – ou que eu queira testar agora se o serializer está serializando os campos corretos. Então eu poderia realizar um teste só no meu serializer.

[03:55] Não estou pegando a minha API e fazendo uma requisição get para testar todos os campos, estou testando uma parte única da minha aplicação. Quando falamos em parte única, eu vou testar funções e métodos individuais. Chamamos esse teste de “teste de unidade”.

[04:12] Existe um segundo teste, que é o “teste de integração”. O que é o teste de integração? Ele visa testar diferentes módulos ou serviços usados em uma aplicação. Então se pararmos para pensar, em nossa aplicação Django Rest, nossa API, nós temos a API e o banco de dados. Esse banco de dados pode ser SQLite, MySQL ou PostgreSQL, não importa, ele é uma outra aplicação que interage com a aplicação do Django Rest.

[04:39] Então se eu quero testar, por exemplo, se eu consigo ter acesso ao banco de dados ou se eu consigo salvar no banco de dados alguma coisa, ou recuperar uma determinada informação do banco de dados - nós chamamos esse teste de “teste de integração”.

[04:54] Eu tenho a minha aplicação, o módulo principal, só que esse módulo interage com outros módulos - como, por exemplo, o banco de dados. Então se eu faço um acesso a um banco de dados, se eu quero fazer uma verificação de alguma informação no meu projeto e, para isso, eu vou precisar acessar o banco de dados, nós vamos chamar esse teste de “teste de integração”.

[05:17] Existe um outro teste também, chamado de “teste funcional”. Qual é o objetivo do teste funcional? É testar o requisito do negócio, então ele vai se concentrar em verificar a saída de uma ação, verificar se eu consigo ter acesso a algumas informações ou ao fluxo que um cliente vai ter dentro da nossa aplicação.

[05:42] Esse teste funcional pode gerar uma certa confusão com o teste de integração, então vou exemplificar de uma forma bem simples. Podemos pensar que o teste de integração, que vimos anteriormente, visa consultar o banco de dados. Então eu tenho a minha aplicação e quero consultar o banco de dados.

[06:01] Já o teste funcional, eu quero fazer um teste para verificar se eu consigo obter um valor especifico do banco de dados, conforme definido no nosso teste. Então esse seria um teste funcional, diferente de um teste de integração.

[06:17] Dentre esses testes, eu deixo um desafio para você pesquisar outros tipos de testes. Além do teste de unidade que falamos, existe o teste de integração, teste de aceitação - e todos esses são conhecidos como testes funcionais.

[06:31] Existem outros tipos de testes também, chamados de “testes não funcionais”. Qual é o objetivo desses outros testes? É realizar outros tipos de testes não relacionados a como o nosso sistema foi feito, mas a ambientes diferentes para o nosso sistema - cenários diferentes e externos à nossa aplicação. Como por exemplo, um teste de estresse - qual o objetivo? É submeter o nosso software às situações extremas.

[07:03] Então eu vou testar os limites da minha aplicação e avaliar como ela se comporta, ou vou um teste de carga. Eu quero verificar o limite de dados processados pela minha aplicação e tentar enxergar até quando a minha aplicação suporta.

[07:22] Ou um teste de desempenho/performance, onde eu quero verificar, por exemplo, como o sistema se comporta em diferentes cargas. Ou qual é o comportamento do nosso software em diferentes cenários externos a ele. Então esses são conhecidos como testes não funcionais.

[07:42] O que eu vou fazer? Nas próximas atividades eu vou deixar um link com algumas leituras extras em relação a esse mundo de testes e nas próximas aulas nós vamos começar a botar a mão na massa e vamos aprender como testamos a nossa API, para garantirmos o controle e o funcionamento da nossa aplicação da forma desejada.

### Faça como eu fiz: Fixtures

Opinião do instrutor

Para carregar dados iniciais utilizando as Fixtures, é necessário criar uma pasta chamada fixtures dentro do app onde os dados são carregados.

Depois podemos criar um arquivo chamado programas_iniciais.json, com uma lista indicando o nome do app, a classe do modelo com os dados, o ID e os campos com seus respectivos atributos, como ilustra o código abaixo:

        [
            {
              "model": "aluraflix.programa",
              "pk": 1,
              "fields": {
                "titulo": "Coisas bizarras",
                "tipo": "S",
                "data_lancamento": "2016-07-15",
                "likes": 7864,
                "dislikes": 465
              }
            },
            {
                "model": "aluraflix.programa",
                "pk": 2,
                "fields": {
                  "titulo": "O bruxo",
                  "tipo": "S",
                  "data_lancamento": "2019-12-20",
                  "likes": 845,
                  "dislikes": 32
              }
            },
            {
                "model": "aluraflix.programa",
                "pk": 3,
                "fields": {
                  "titulo": "Emília em São Francisco",
                  "tipo": "S",
                  "data_lancamento": "2020-10-02",
                  "likes": 441,
                  "dislikes": 12
              }
            },
            {
                "model": "aluraflix.programa",
                "pk": 4,
                "fields": {
                  "titulo": "Corações de lata",
                  "tipo": "F",
                  "data_lancamento": "2015-02-05",
                  "likes": 2873,
                  "dislikes": 132
              }
            },
            {
                "model": "aluraflix.programa",
                "pk": 5,
                "fields": {
                  "titulo": "Le Le Lend",
                  "tipo": "F",
                  "data_lancamento": "2017-01-13",
                  "likes": 1230,
                  "dislikes": 19
              }
            },
            {
                "model": "aluraflix.programa",
                "pk": 6,
                "fields": {
                  "titulo": "Saltadores Utimato",
                  "tipo": "F",
                  "data_lancamento": "2019-04-25",
                  "likes": 31771,
                  "dislikes": 87
              }
            },
            {
                "model": "aluraflix.programa",
                "pk": 7,
                "fields": {
                  "titulo": "Capitão Bahia",
                  "tipo": "F",
                  "data_lancamento": "2011-07-29",
                  "likes": 10340,
                  "dislikes": 127
              }
            },
            {
                "model": "aluraflix.programa",
                "pk": 8,
                "fields": {
                  "titulo": "Caderno da vida",
                  "tipo": "S",
                  "data_lancamento": "2017-07-20",
                  "likes": 51,
                  "dislikes": 89
              }
            },
            {
              "model": "aluraflix.programa",
              "pk": 9,
              "fields": {
                "titulo": "O resgate do soldado Carlinhos",
                "tipo": "F",
                "data_lancamento": "1999-09-05",
                "likes": 51,
                "dislikes": 89
            }
          }
          ]
        
Para migrar esses dados para o banco de dados, basta executar o seguinte comando:

        python manage.py loaddata programas_iniciais.json

Sucesso! Sua base de dados agora possui 9 programas cadastrados!

Você pode ler mais sobre [Fixtures na documentação]('https://docs.djangoproject.com/en/3.1/howto/initial-data/').

Ficou com alguma dúvida, lembre-se do fórum da Alura. Não tem dúvidas? Que tal ajudar alguém no fórum?

:)

### Carregando dados iniciais

Marcos está desenvolvendo uma API e gostaria de fornecer alguns dados iniciais para seus modelos. Esses dados iniciais correspondem a aplicativos e modelos diferentes.

Sabendo disso, analise as afirmações abaixo e marque a verdadeira.

a) O Django fornece uma forma de carregar dados iniciais desde que o formato dos dados seja JSON. Não há suporte para outros tipos de dados.

b) Tanto o Django como o Django Rest Framework não possuem suporte para carregamento de dados iniciais.

c) **Alternativa correta:** O Django fornece uma forma de carregar dados iniciais para diferentes modelos através das Fixtures.
- _Alternativa correta! Certo! Podemos utilizar fixtures dentro de cada APP com arquivos JSON ou YAML, por exemplo, referenciando cada modelo, a chave primária, os campos e seus respectivos valores._

### Para saber mais: Testes automatizados

A ideia é fazer com que a pessoa desenvolvedora escreva testes automatizados de maneira constante ao longo do desenvolvimento de um software. Um ponto que é sempre levantado em qualquer discussão sobre testes manuais versus testes automatizados é produtividade.

O argumento mais comum é o de que agora a equipe de desenvolvimento gastará tempo escrevendo código de teste; antes ela só gastava tempo escrevendo código de produção. Portanto, essa equipe será menos produtiva.

A pergunta que devemos fazer é: o que é produtividade? Se produtividade for medida através do número de linhas de código de produção escritas por dia, talvez a pessoa desenvolvedora seja sim menos produtiva.

Agora, se a produtividade for a quantidade de linhas de código de produção sem defeitos escritos por dia, provavelmente o desenvolvedor ou desenvolvedora será mais produtivo ao usar testes automatizados.

[..] Aniche, Maurício. Test Driven Development: Teste e Design no Mundo Real. [Casa do código]('https://www.casadocodigo.com.br/products/livro-tdd')

### Para saber mais: Teste funcional e de unidade

Existem muitas maneiras de descrever tipos de testes. Para nossos propósitos, vamos diferenciar entre testes de unidade e testes funcionais. A distinção é semântica, mas informará nossa estratégia de teste.

Testes de unidade
Concentram-se nas preocupações da pessoa que desenvolve e geralmente são pequenos. São executados em microssegundos e testam uma única parte do projeto.

Teste funcional
O teste funcional é focado na experiência do usuário, pode ser grande e levar mais tempo quando comparado aos testes de unidade. Geralmente, simula aquilo que um usuário faria.

Para saber mas sobre o assunto, leia [este artigo e descubra outros tipos de testes (texto em inglês)]('https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing').

### O que aprendemos?

**Nesta aula:**
- Aprendemos que é possível carregar dados iniciais para os modelos através das fixtures. Para isso, dentro de cada APP, podemos criar uma pasta chamada fixtures com dados no formato JSON, por exemplo, e carregá-los executando o comando manage.py loaddata seguido do nome do arquivo que contém os dados.
- Aprendemos que existem diferentes formas de testar uma aplicação, como testes manuais, automatizados, testes de unidade, integração, entre outros.

**Na próxima aula:**
- Vamos aprender como testar nossos modelos e serializers na prática, escrevendo testes de unidade!

## 02. Testes de unidade
### Projeto da aula anterior
### Testando modelo
### Testando serializer
### Conteúdo do serializer
### Faça como eu fiz
### Uso do Set
### O que aprendemos?
## 03. Teste de integração
### Projeto da aula anterior
### Testando a autenticação
### Credenciais incorretas
### Requisições de user autenticado
### Faça como eu fiz
### Unidade ou Integração?
### O que aprendemos?
## 04. Testando a API
### Projeto da aula anterior
### Fixtures nos testes
### Preparando o ambiente: Postman
### Testando API no Postman
### Faça como eu fiz
### Função setUP
### O que aprendemos?
## 05. Documentando a API com Swagger
### Projeto da aula anterior
### Swagger
### DRF e Swagger
### Faça como eu fiz
### Detalhes do Swagger
### Projeto final do curso
### O que aprendemos?
 