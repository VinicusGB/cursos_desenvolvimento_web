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
### Testando modelo

1. Criar um arquivo test_models.py:

        from django.test import TestCase
        from aluraflix.models import Programa

        class ProgramaModelTestCase(TestCase):
                def setUp(self):
                        self.programa = Programa(
                                titulo = 'Procurando ninguem em latim',
                                data_lancamento = '2003-07=04',
                        )
                def test_verfica_aribuots_do_programa(self):
                        """Teste que verifica os atribuots de um programa"""
                        self.assertEqual(self.programa.titulo,'Procurando ninguem em latim' ),
                        self.assertEqual(self.programa.data_lancamento,'2003-07-04')
                def test_falha(self):
                        self.fail('Teste falhou')

---

[00:00] No treinamento passado nós criamos testes automatizados para verificarmos as principais requisições da nossa API: get, post, put e init. Isso ficou bem legal, porém não testamos nenhuma outra parte da nossa API. Então vamos começar a testar algumas partes da nossa API.

[00:17] Se você acessar o “aluraflix”, vai observar que não temos aquele “teste.py” que vem por padrão quando criamos um app. Por quê? Nós vamos criar uma série de testes e vamos testar partes diferentes da nossa aplicação. Vimos que existe uma série de testes diferentes.

[00:32] Então eu vou clicar para criar uma nova pasta dentro do “aluraflix”, que eu vou chamar de “testes”. Então ele está dentro do “aluraflix”. Dentro do “aluraflix” eu vou criar um arquivo para que os testes sejam executados, um arquivo init. Então, “init.py”, para os nossos testes serem executados. Vou criar mais um arquivo, que vou chamar de “test”, no singular, com underline e o nome do teste que vamos criar.

[01:05] Então para começarmos, vamos testar os nossos modelos. Então vou colocar “test_models.py”. Criei o “test” e tenho o teste do meu modelo. Eu vou deixar meu modelo aberto, ao lado, só para visualizarmos. Tenho o meu arquivo de teste. Vamos focar, então!

[01:24] Quando eu vou criar um programa novo, seja ele um filme ou uma série, observe que tenho alguns valores default. Então um programa da “aluraflix” vai ter um título, um tipo - se ele é um filme ou uma série - e o valor default para filme. Ele tem uma data de lançamento, quantidade de like e quantidade de dislike. Caso eu não passe nenhum valor, ele atribui o valor default=0.

[01:51] Mas será que, de fato, isso está acontecendo? Podemos criar um teste para verificarmos isso. Então a primeira coisa que vamos fazer vai ser importar from django.test import TestCase.

[02:09] Como queremos testar se nosso modelo vai atribuir esses valores default, eu vou trazer também o nosso modelo, então: from aluraflix.models import Programa. Vamos criar nossa classe de teste, que eu vou chamar de class ProgramaModelTestCase(TestCase):.

[02:34] O que isso significa? Quando eu crio uma classe e utilizo o argumento TestCase vai significar que todos os métodos que tem o prefixo “Test” serão executados quando eu rodar o python manage.py test - e é isso o que queremos fazer! Só para garantir, vou criar uma função, chamá-la de test_falha(self):, dentro self.fail(‘Teste falhou’) e vou executar isso no nosso terminal.

[03:18] Parei meu servidor e vou executar python manage.py test. Quando aperto a tecla “Enter”, observe o que acontece: nós temos um “F”, nosso teste falhou. Temos self.fail(‘Teste falhou’).

[03:32] Então tomando cuidado só com algumas coisas: nome das pastas, no plural, tests; o arquivo init e test no singular, underline e o nome do que vamos testar. Fazendo tudo isso, o nosso teste está sendo executado.

[03:45] Não quero criar um teste para falhar, eu quero criar um cenário de teste onde eu não vou passar os valores que são atribuídos por default, no meu modelo. Primeira coisa: vou criar uma função setUp, que vai ser executada antes dos nossos testes, para criar o nosso cenário de teste.

[04:07] Então vou colocar self.programa, vou falar que self.programa vai ser um programa que vem do nosso modelo, só que nesse caso eu não vou utilizar Programa.objects.create. Por que eu não vou fazer isso?

[04:22] Não vou fazer isso porque se eu faço isso, eu estou usando o meu teste mais o banco de dados dele, estou de fato criando esse programa no banco de dados de teste - e não é isso que eu quero fazer, eu quero utilizar apenas uma instância de programa.

[04:39] Então, o que eu vou fazer? Vou tirar esse objects.create. Eu quero um teste de unidade, não de integração. Eu vou passar as propriedades que contém esse programa. Então, o programa tem um título, que vou chamar de Procurando ninguém em latim e vou passar para ele uma data, por exemplo: 4 de julho de 2003, então vou passar data_lancamento = '2003-07-04'.

[05:25] Passei esses 2 valores, tenho a instância de um programa e não estou vinculando no banco de dados. Eu quero fazer agora uma verificação dos atributos desse programa, um teste para verificar os atributos, então digito def test_verifica_atributos_do_programa(self):.

[05:52] Para manter nossos testes bem organizados, vou passar uma docstring, para deixar nossos testes bem claros. Então “““Teste que verifica os atributos de um programa com valores default”””. Esse é o objetivo do nosso teste.

[06:15] Então vou começar minhas acertações: self.assertEqual. Eu quero pegar esse programa que criamos (self.progama.titulo,) e quero verificar se o título desse programa é igual a “Procurando ninguém em latim”, então vou passar uma string “Procurando ninguém em latim”.

[06:37] Porém, eu quero fazer o mesmo com os outros campos. Vou segurar a tecla “Shift + Ctrl” para baixo para fazer uma cópia dessa linha. Então temos um programa o título o tipo, que eu não lembro, vou precisar ver... Título, tipo, data de lançamento, likes e dislikes.

[06:53] Então título, self.programa.data_lancamento, self.programa.likes e self.programa.dislikes. O que vamos fazer agora? Vamos verificar. Quando não atribuímos nenhum valor, qual é o tipo que esperamos?

[07:10] Segundo nosso modelo, quando não temos nenhum valor, o valor default dele é um filme. Então vou passar que o tipo vai ser F. Além do tipo, nós temos a data de lançamento, que precisa ser igual à data de lançamento que colocamos em cima. Então: 2003-07-04. Quantidade de likes, quando não passamos nenhum valor, qual é o valor de like default? É 0 para likes e 0 para dislikes. Então vou passar o valor 0 para os dois.

[07:48] Um ponto importante: se eu passo esse valor 0 como string, vou ter um erro, porque o 0 inteiro não é igual ao 0 string, então precisamos deixar o 0 sem ser no formato de string. Subindo, vamos testar... Vou ligar meu teste e digitar python manage.py test. Está executando. Executou o nosso teste e ele foi aprovado!

[08:11] Só para garantir, vou colocar entre strings para você ver esse 0. Então vamos supor que você errou e passou um 0 string. Quando executar o teste, ele vai falar que essa acertação está errada; no teste que verifica os atributos de um programa com valor default, o 0 string não é igual a um 0 inteiro. Então vou tirar as aspas simples para nosso teste ser aprovado.

[08:35] Dessa forma nós conseguimos garantir no nosso teste de modelo, os atributos e os valores default desse nosso programa.

### Testando serializer

1. Criar um arquivo test_serializar.py:

        from django.test import TestCase
        from aluraflix.models import Programa
        from aluraflix.serializers import ProgramaSerializar

        class ProgramaSerializerTestCase(TestCase):
                def setUp(self):
                        self.programa = Programa(
                                ...
                        )
                        self.serializar = ProgramaSerializer(instance=self.programa)
                
                def test_verifcar_campos_serializados(self):
                        """Teste que verifica os campos que estão sendo serializados"""
                        data = self.serializer.data
                        self.asserEqual(set(data.keys()), set['titulo','data_lancamento','likes','tipo'])

---

[00:00] Dentro de um API, os serializers possuem um papel muito importante. É importante que consigamos testar para garantirmos o seu funcionamento. Então vamos escrever um teste para verificarmos o serializer e como podemos escrever os testes automatizados para garantirmos o seu funcionamento.

[00:17] Vou fechar nossos testes de modelo e vou abrir nossa pasta de testes dentro do “aluraflix” e vou criar mais um teste, “test_serializers.py”. O que vamos precisar para realizarmos nossos testes do serializer?

[00:35] Em primeiro lugar o Django, então digito from Django.test import TestCase. Vamos precisar do nosso modelo de programa, então digito from aluraflix.models import Programa. Vamos precisar também do nosso serializer, então digito from aluraflix.serializers import ProgramaSerializer.

[00:58] Trouxemos os imports necessários para realizarmos os testes do serializer e vamos criar nossa classe de teste, então digitamos class ProgramaSerializerTestCase(TestCase):. Vamos preparar nosso cenário de teste, nossa função setup, vou falar passando o nosso self e vou começar criando o programa – def setUp(self):.

[01:30] Esse programa eu vou criar assim: vou passar a instância, self.programa= e vou criar um novo programa, vou fazer da mesma forma. Quero garantir os testes de unidade, então não vou dar o objects.create, vou passar apenas as propriedades do programa.

[01:48] Vou roubar um pouco, vou no nosso teste de modelo, copiar o título e a data de lançamento e vou passar os outros valores também. Então, Procurando ninguém em latim. Vou colocar que o tipo dele vai ser um filme. Vou passar também uma quantidade de likes, por exemplo: likes=2340. Esqueci a virgula nas linhas 12 e 13. Para finalizar, os dislikes, que vão ser igual a 40, dislikes=40, só um pouquinho.

[02:28] Criei um programa, então tenho título, tipo, data de lançamento, likes e dislikes. Eu preciso passar agora o serializer que vamos utilizar, uma instância do serializer. Como fazemos isso?

[02:40] Vou utilizar a palavra self.serializer = ProgramaSerializer, porém eu preciso de uma instância dele e informar que essa instância é vinculada com esse programa que estamos utilizando. Como fazemos isso?

[03:00] Vou utilizar a palavra (instance=self.programa), dessa forma já temos o serializer apontando para esse programa que acabamos de criar. Esse é o nosso cenário de teste, ele está feito. Agora vamos para as verificações.

[03:18] O que eu preciso fazer/testar em um serializer? Então, a primeira coisa que podemos pensar em testarmos no serializer é verificarmos se os campos que estão sendo serializados são os mesmos campos que queremos que sejam serializados. Então podemos verificar os campos serializados.

[03:39] Vou colocar uma função def. Vou jogar para cima para visualizarmos melhor. Então, def test_verifica_campos_serializados(self) e vou colocar a docstring para ficar legal. Nessa docstring eu posso escrever algo, por exemplo, como um teste que verifica os campos que estão sendo serializados, então digito “““Teste que verifica os campos que estão sendo serializados”””.

[04:19] Para começarmos, do que precisamos? É importante que antes de já verificarmos nosso serializer e criarmos nossa acertação, que já tenhamos alguma data ou algum campo específico, para falarmos: “os campos do serializer são esses”.

[04:37] Então vou armazenar essa informação aqui data = self.serializer.data. O que isso significa? Que eu estou pegando todos os campos do serializer e armazenando nessa variável data, só para manter nosso código mais organizado. Agora vou criar nossa assertação: self.assertEqual() e nela vou passar alguma propriedades para o assertEqual.

[05:06] Em primeiro lugar, eu preciso garantir que os campos/atributos desse serializer de fato vão ser serializados, então vou colocar data.keys - que é a função que vai pega o serializer. Porém, é importante passarmos uma outra coisa antes de pegarmos de fato os dados do serializer que vou passar, ele se chama set.

[05:30] O que o set vai fazer? Usando o set vamos garantir que a saída do serializer tenha as chaves extas que estamos esperando. Então sempre que utilizamos o set para fazermos essa verificação, na verdade, o que estamos fazendo? Qualquer alteração que tivermos no serializer vai refletir no nosso teste.

[05:49] Então tenho o nosso set do serializer. Vou voltar porque faltou alguns parênteses. Eu peguei todos os dados do meu reializer, então qualquer alteração que fizer no serializer vai ser refletida no nosso teste. Preciso verificar agora se esse set contém os campos que eu quero, então vou colocar set e vou passar o nome dos campos. Eu tenho titulo? Tenho a data_lancamento?

[06:28] O que podemos fazer também para o nosso teste ficar mais claro é darmos uma olhada no nosso serializer, igual eu tinha feito no modelo. Então, o que temos? Vou copiar titulo, tipo, data_lancamento e likes.

[06:41] Observe que os dislikes não aparecem aqui, então vou colocar só esses valores set[titulo,tipo,data_lancamento,likes] )). Eu achei que abri um parêntese errado e fechei um parêntese a mais no nosso set.

[07:01] Então começou nossa acertação, então temos o set do data, esses dois fecham corretamente. No nosso set tem mais um parêntese, eu me esqueci, me desculpe. Tem mais um. Agora sim, tinha me esquecido desse parêntese. Vou colocar para visualizarmos a linha toda, mas é só para entendermos que está na mesma linha e para conseguirmos visualizar na nossa tela.

[07:25] Criamos o nosso teste, vamos ver se isso está de fato acontecendo e realizar algumas alterações. Vou reexecutar o teste. Ele executou e passou, até aí tudo bem. O que fizemos? Falamos “olhe, o serializer possui esses campos: titulo, tipo, data_lancamento e likes?” Possui, então nosso teste foi aprovado!

[07:44] O que vou fazer agora? Vou alterar! Vamos supor que mudou, os dislikes que não estavam sendo exibidos no nosso serializer entraram, então eu tenho likes e dislikes. Vou rodar meu teste mais uma vez. Olhe só que interessante, nosso teste foi aprovado porque o dislike eu escrevi errado.

[08:07] Agora eu acho que vai sim, vamos ver. Salvei o serializer e está executando o teste. Agora sim, nós recebemos a mensagem de erro. Naquela hora eu tinha escrito errado.

[08:17] No que nosso teste falhou? Um teste foi aprovado (nosso teste de modelo) e esse teste falhou (o teste que verifica os campos que estão sendo serializados). Ele fala assim: “você tem um item que está no primeiro set, mas não está no segundo set, que é o dislike”.

[08:34] O que isso significa? Significa que no nosso primeiro set temos um item que não está no segundo. Qual item é esse? É o dislike. Então observe que qualquer alteração que eu faço no meu serializer, vou conseguir pegar essas alterações quando eu executar os meus testes. Isso vai garantir que consigamos o comportamento esperado nos nossos campos que estão sendo serializados.

### Conteúdo do serializer

1. Em test_serializers.py:

        ...
                def test_verfica_conteudo_dos_campos_serializados(self):
                        """Verifica se o conteudo dos campos serializados"""
                        data = self.serializar.data
                        self.assertEqual(data['titulo'], self.programa.titulo)
                        ...

---

[00:00] Conseguimos testar os campos serializados do programa serializer, só que esse não é o único teste que podemos executar no nosso serializer. Podemos verificar se o conteúdo que está sendo serializado é igual ao conteúdo que criamos, para vermos se o serializer está fazendo sua função certa.

[00:18] Então, o que eu vou fazer? Antes de tudo, vou tirar o dislike, não temos o dislike no serializer, temos apenas esses 4 campos sendo serializados. Eu vou criar um novo teste, porque eu quero verificar o conteúdo.

[00:32] Então vou comparar o conteúdo do serializer com o conteúdo da instância do programa que temos, então digito def test_. Posso chamar esse teste de verifica_conteudo_dos_campos_serializdos(self). Nós vamos começar colocando nossa docstring para mantermos nossos códigos bem documentados.

[00:56] Então o objetivo desse teste é verificar o conteúdo dos campos serializados, então digito “““Teste que verifica o conteudo dos campos serializados”””. A primeira coisa que vou fazer vai ser pegar todos os dados do serializer, então digito self.serializer.data e guardo isso em uma variável que vou chamar de data, bem semelhante com o que fizemos em cima.

[01:28] Agora eu vou criar uma acertação para verificar, por exemplo, se o data que está vindo do serializer, o titulo, é igual à instância que criamos em cima, de programa; se é igual a esse título do programa.

[01:42] Então, self.assertEqual() e vou passar a nossa primeira acertação. Vou pegar o data, que é o nosso serializer, mas eu quero o campo titulo. Vou verificar se o campo titulo é igual ao self.programa.titulo. Ficou self.assertEqual(data[titulo], self.programa.titulo).

[02:10] Vou fazer o mesmo com os outros campos, então vou colar com as teclas “Ctrl + C” e colar com “Ctrl + V”. Acho até que coloquei um a mais. Eu tenho o título e data de lançamento, então vou passar também data_lancamento.

[02:26] Esse data_lancamento vai vir para o nosso data do serializer. Temos o tipo e, para finalizarmos, temos os likes. Temos os dislikes sendo serializados, então não faz sentido eu colocar esse teste, ele iria falhar.

[02:51] Então, o que acontece? Temos 4 campos sendo serializados: título, tipo, data de lançamento e os likes. Então eu quero verificar se o conteúdo desses campos, do serializer, é o mesmo conteúdo que temos da instância do nosso programa.

[03:05] Abrindo o nosso terminal, vou executar manage.py test. Quando eu aperto a tecla “enter”, o nosso teste é aprovado. Vou colocar o campo dislikes, por exemplo. Coloquei um campo a mais que não está sendo serializado, dislikes. Vou perguntar se ele é igual a dislikes.

[03:25] Quando eu salvo isso no nosso teste serializer e executo, olhe só que interessante. Executei. Vamos ver... Ele está pensando se vai executar ou não. Executou e deu um erro, temos alguns erros.

[03:43] O primeiro erro que temos foi dos campos serializados, então vamos verificar qual é o problema. Ele fala que temos o KeyError nesse dislikes, na linha 29; porquê? Porque esse dado não tem no serializer, esse conteúdo dislikes não está disponível no nosso serializer, então não tem como compararmos.

[04:07] Então o nosso teste foi reprovado e garantimos o comportamento que esperamos. Se eu executar o teste de novo, sem o dislikes, terei o teste certo. Criando o banco de dados de teste... E agora sim foi aprovado!

[04:21] Então essa é uma outra forma que nós temos para testarmos os nossos serializers.

### Faça como eu fiz

Nesta aula, vimos como criar testes de unidades para verificar partes isoladas da aplicação. Testamos se os valores default atribuídos nos modelos estavam sendo setados quando nenhum valor era passado na instância de um programa.

Como criar testes de unidades para verificar o comportamento dos modelos no Django?

#### Opinião do instrutor

Nosso modelo de produtos possuem as seguintes características:

        class Programa(models.Model):
            TIPO = (('F', 'Filme'),('S', 'Serie'),)

            titulo = models.CharField(max_length=50)
            tipo = models.CharField(max_length=1,choices=TIPO, blank=False, null=False,default='F')
            data_lancamento = models.DateField()
            likes = models.PositiveIntegerField(default=0)
            dislikes= models.PositiveIntegerField(default=0)

Observe que os campos tipo, likes e dislikes possuem os seguintes valores default: F, 0 e 0. Isso significa que, na ausência de atribuição de valores nestes campos, esses valores são incluídos.

Para testar este comportamento, vamos realizar um teste, onde criamos uma instância de programa atribuindo valores nos campos que não possuem a tag default, nesse caso, título e data de lançamento, como ilustra o código abaixo:

        class ProgramaModelTestCase(TestCase):

            def setUp(self):
                self.programa = Programa(
                    titulo = 'Procurando ninguém em latim',
                    data_lancamento = '2003-07-04'
                )

            def test_verifica_atributos_do_programa(self):
                """Teste que verifica os atributos de um programa com valores default"""
                self.assertEqual(self.programa.titulo, 'Procurando ninguém em latim')
                self.assertEqual(self.programa.tipo, 'F')
                self.assertEqual(self.programa.data_lancamento, '2003-07-04')
                self.assertEqual(self.programa.likes, 0)
                self.assertEqual(self.programa.dislikes, 0)
        
Vamos executar este teste?

        python manage.py test

Tudo certo! Nosso teste foi aprovado e os valores default foram atribuídos com sucesso.

Ficou com alguma dúvida, lembre-se do fórum da Alura. Não tem dúvidas? Que tal ajudar alguém no fórum?

:)

### Uso do Set

Nesta aula, criamos um teste para verificar quais campos estavam sendo serializados pelo ProgramaSerializer com o seguinte código:

        class ProgramaSerializerTestCase(TestCase):

            def setUp(self):
                self.programa = Programa(
                    titulo = 'Procurando ninguém em latim',
                    data_lancamento = '2003-07-04',
                    tipo='F',
                    likes=2340,
                    dislikes=40
                )
                self.serializer = ProgramaSerializer(instance=self.programa)

            def test_verifica_campos_serializados(self):
                """Teste que verifica os campos que estão sendo serializados"""
                data = self.serializer.data
                self.assertEqual(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes'] ))

Analisando o código acima, podemos afirmar que o uso do set no método que verifica os campos serializados tem a função de:

a) Adicionar campos não serializados presentes ou disponíveis no modelo.
b) Remover os dados serializados do banco de dados.
c) **Alternativa correta:** Garantir que a saída do serializador tenha as chaves exatas.
- _Alternativa correta! Certo! Usar um set para fazer essa verificação é na verdade muito importante porque vai garantir que a adição ou remoção de qualquer campo do serializador seja percebida pelo teste._

### O que aprendemos?

**Nesta aula:**
- Aprendemos que o teste de unidade é um método de teste de software no qual os componentes individuais do programa, chamados de unidades, são testados a despeito das dependências necessárias;
- Criamos os testes de unidade para verificar os campos serializados e se o modelo atribuía os valores default quando eram omitidos.

**Na próxima aula:**
- Vamos criar testes de integração para verificar a requisição de um usuário autenticado com as credenciais corretas!

## 03. Teste de integração
### Testando a autenticação

1. Criar um arquivo test_authentication.py:

        from django.contrib.auth.models import User
        from rest_framework.test import APITestCAse
        from django.contrib.auth import authenticate

        class AuthenticationTestCase(APITestCase):
                def setUp(self):
                        self.user = User.objects.create_user('c3po',password='123456')
                def test_autenticacao_user_com_credenciais_corretas(self):
                        """Teste que verifica a autenticacao de um user com dados correto"""
                        user = authenticate(username='c3po',password='123456')
                        self.assertTrue(user is not None) and user.is_authenticated)

---

[00:00] A nossa API possui um sistema de autenticação, isso significa que se eu tentar visualizar os recursos e programa, ele vai me pedir o username e a password. Então eu coloco o meu nome, coloco a minha senha supersegura e quando eu aperto a tecla “Enter”, aparece os recursos. Eu posso criar um novo programa ou atualizar um determinado programa.

[00:22] Se eu coloco, por exemplo, ID 2, aparece “O bruxo” e eu consigo visualizar, dar um PUT, atualizar ou deletar algum recurso. Ou seja, para de fato consumir a minha API, é necessário que eu esteja autenticado.

[00:33] Mas minha pergunta é: como será que podemos testar esse comportamento, esse fluxo de um usuário que faz uma autenticação e tenta consumir os dados da API? Vamos ver isso, então!

[00:44] Para começar, eu vou abrir do lado a nossa pasta do “aluraflix > tests” e criar um novo arquivo, chamado “test_authentication.py”, porque eu quero testar as nossas autenticações. Para começar, nos outros testes sempre tínhamos um modelo como referência, então tenho um modelo de programa no “aluraflix”.

[01:07] Nesse nosso caso da autenticação, qual é o modelo que vamos utilizar como referência? É o modelo de usuário do próprio Django. Então lá do “django.contrib.auth.models” (esse nome é grande) tem o modelo do usuário do Django que conseguimos verificar se ele está autenticado ou não.

[01:24] Então vamos trazê-lo - ‘from Django.contrib.auth.models import User’. Além disso, nesse nosso teste vamos utilizar uma propriedade, que é a ‘APITestCase’ porque posteriormente vamos tentar realizar uma requisição, de fato, para essa nossa rota dos programas que temos da nossa API.

[01:56] O que eu vou fazer? Primeira coisa: vou importar do ‘from rest_framework.test import APITestCase’. Vamos criar a nossa classe de teste, vou chamar de ‘class AuthenticationUserTestCase(APITestCase):’ e nós vamos começar!

[02:29] Em primeiro lugar vamos criar o nosso cenário de teste - ‘def setUp(self)’. De quem eu preciso? Eu preciso de um usuário, então vou colocar ‘self.user = User’. Eu preciso agora, de fato, criar um usuário. Porém temos uma reflexão interessante: vamos observar nosso teste de modelo e o nosso teste do serializer, vou abrir os 3.

[03:00] No teste do modelo temos uma instância do programa, não temos o programa de fato no banco de dados. O mesmo acontece no nosso teste do serializer.

[03:09] Não temos esse programa que usamos no teste do serializer ou no teste do modelo criado no banco de dados. Isso define que os nossos testes são testes de unidade. Pegamos toda a nossa API em pedaços, depois pegamos todo o contexto da API, pegamos um pedacinho de código que se trata do modelo e testamos os modelos.

[03:31] Nesse nosso caso da autenticação, o que vamos fazer? Queremos verificar se o usuário respeita todas as regras de negócio impostas pelo Django. Então é importante que nesse teste não façamos um teste de unidade, e sim um teste de integração - porque vamos integrar o banco de dados com a nossa API.

[03:55] Lembrando que o banco de dados não é o banco de dados real que está em produção, onde estão os nossos filmes. Lembre-se que o Django já tem uma estrutura para criar sempre os bancos de dados de teste.

[04:07] Então para eu criar um programa, nesse caso vou usar o ‘objects,create_user()’ e vou criar um usuário que será criado quando eu executar esse teste no banco de dados de teste. Vou chamar esse usuário de “c3po” e vou criar uma senha para ele, então ficou ‘(‘c3po’, password=’123456’)’.

[04:34] Criei meu usuário e agora quero criar um teste para verificar se de fato esse usuário consegue ser autenticado. Então para conseguir de fato testar se esse usuário consegue se autenticar, eu vou importar mais um módulo - ‘from Django.contrib.auth import authenticate’ - porque eu quero autenticar esse usuário.

[05:04] Vou criar um novo teste ‘def test_’. Esse teste eu posso chamar como, por exemplo, autenticação de um user com credenciais corretas – acho que fica bem legal - ‘def test_autenticacao_user_com_credenciais_corretas(self):’. Nós vamos começar a escrever o nosso teste. Colocando a nossa docstring, então esse é um teste que verifica a autenticação de um user com as credenciais corretas.

[05:59] Colocamos a nossa docstring e agora vamos começar a escrever o nosso teste. Então em primeiro lugar, eu tenho um usuário já criado através do setup, esse usuário ‘c3po’ que criamos. Vamos autenticar o ‘c3po’.

[06:12] Então vou chamar ‘authenticate(username=’c3po’, password=’123456’)’. Vou guardar isso dentro de uma variável chamada ‘user = ’ e vou fazer uma acertação para verificar se esse usuário de fato está autenticado.

[06:35] Então vou verificar duas coisas. Primeiro: se o usuário não é vazio e se temos um usuário de fato criado. Então para isso vou colocar um ‘self.assertTrue()’. Eu quero que isso seja verdadeiro.

[06:49] Então em primeiro lugar eu vou verificar assim: ‘(use is not None)’ - isso significa que eu tenho um usuário criado. Além disso, vou colocar ‘and user is_authenticated’, dizendo que esse usuário está de fato autenticado.

[07:07] Abrindo nosso terminal e parando nosso servidor, eu vou executar ‘manage.py test’. Quando apertar a tecla “enter” vai rodar o nosso teste... O nosso teste passou!

[07:21] Como o nosso teste passou e deu tudo certo, o que podemos fazer na sequência? Podemos verificar outras coisas. Se eu tento, de fato, uma requisição sem realizar a autenticação desse usuário, o que será que acontece? Vamos ver como criar esses outros testes, na sequência!

### Credenciais incorretas

1. Em test_authentication.py:

        ...
        from django.urls import reverse
        from rest_framework import status

        ...
                def setUp(self):
                        self.list_url = reverse('programas-list')
                        self.user = ...
                        ...
                ...
                def test_requisicao_get_nao_autorizada(self):
                        """Teste que verifica uma requisição GET sem autenticar"""
                        response = self.client.get(self.list_url)
                        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
                def test_autenticacao_de_user_com_usernaem_incorreto(self):
                        """Teste que verifica a autenticacao de um user com dados incorreto"""
                        user = authenticate(username='c3pp',password='123456')
                        self.assertFalse(user is not None) and user.is_authenticated)
                ...

---

[00:00] Nós realizamos o nosso teste para verificarmos se o usuário c3po conseguia se autenticar - e ele conseguiu. Esse foi um teste. Eu quero criar um outro teste, agora um pouco mais além. Nem vou falar de autenticação, eu quero realizar uma requisição get para programas, para ver o que acontece.

[00:19] Para nós conseguirmos realizar essa requisição get é importante passarmos a URL que ele vai passar a requisição. Existe um módulo do Django, o from django.urls, chamado de reverse. Através desse módulo reverse ele vai expandir para nós todas as possíveis URLs.

[00:42] Por que vamos utilizar o reverse para passarmos o localhost8000/? Porque queremos garantir que esse código continue funcionando e que nossos testes continuem funcionando depois que subirmos nosso projeto em produção também.

[00:57] Então não vamos utilizar passando o localhost, não quero fazer uma requisição do localhost. Eu quero fazer uma requisição na lista dos meus endpoints relacionados ao programa. Então, para isso eu vou criar uma instância chamada self.list_url = reverse(`)` e entre parênteses eu vou precisar passar qual vai ser o endpoint/recurso que eu quero utilizar.

[01:26] O recurso que vamos utilizar, podemos visualizar exatamente o nome dele em “aluraflix > setup > urls.py”. Existe um base name chamado programas, então no meu teste de autenticação, eu posso passar programas. Só que eu não quero realizar apenas uma requisição get ou apenas uma requisição post ou delit, eu quero realizar diferentes requisições.

[01:48] Então eu quero passar uma lista dos endpoints relacionados aos programas. Então eu coloco um traço e escrevo “list”. Desta forma, quando eu falo “uma requisição get” para essa lista URL”, ela já sabe que é uma requisição get para programas.

[02:05] Temos a nossa requisição, o que eu preciso fazer agora é criar o nosso teste. Para criar o nosso teste - def test_requisicao_get_nao_autorizada() - vou colocar em cima para vermos melhor - (self): e vou começar a escrever o nosso teste: “““Teste que verifica uma requisição GET sem autetnicar”””.

[02:56] Primeira coisa: vou precisar realizar um get. Então vou utilizar o cliente que é disponível no APITestCase, então: self.client. Quando eu colocar o ponto final já vai aparecer o get - self.client.get(self.list_url).

[03:21] Essa requisição, estou a fazendo e vou guardar a resposta dela. Então vou criar uma nova variante chamada response e vou guardar essa requisição dentro desta variável response.

[03:35] Vou fazer agora uma acertação self.assertEqual e vou colocar a nossa acertação. Se o status code dessa resposta, (response.status_code,), for igual a um status não autorizado - para deixarmos bem legal, o nosso código, vamos importar também um status. Então do rest frame, nós temos o status: from rest_framework import status.

[04:13] Então para colocar o status e ficar bem bonito, vou chamar de status.HTTP_401_UNAUTHORIZED. Significa “sem autenticar” ou “não autorizado”, acho que os dois nomes ficariam bem.

[04:30] O que fizemos aqui? Fizemos uma requisição com o cliente que vem do APITestCase, uma requisição get para nossa lista de URLs que estamos utilizando em cima, através do reverse do programa. Então, o endpoint do programa.

[04:45] Vou guardar essa resposta e verificar se o status code dessa resposta é igual ao status 401, de não autorizado. Vou executar meu teste... Nosso teste foi aprovado! Então quando temos uma requisição get, sem autenticarmos e recebemos um 401. Será mesmo que isso está acontecendo? Vamos verificar!

[05:08] Vou na minha view e vou comentar essa linha da autenticação. O que vai acontecer agora? Eu não tenho mais a autenticação na minha view e quando eu fizer uma requisição get, ele vai aceitar a requisição get - e vai devolver o quê? Um 200, esse teste vai falhar.

[05:27] Fiz o teste e ele falhou! Ele devolveu 200 != 401. O assert fala que é o teste que verifica a requisição get sem autenticar. “Requisição GET não autorizada”, vai ficar bem chique. Vou mudar para “““Teste que verifica uma requisição GET não autorizada”””.

[05:47] Não é isso o que eu quero, no nosso projeto nós queremos a autenticação. Então quando eu volto e tiro o comentário da nossa view, deixo a autenticação e rodo o nosso teste mais uma vez. Observe que o nosso código é aprovado.

[06:04] Outro teste em que podemos verificar em relação às credenciais, em relação ao autorizado ou não é: quando um usuário erra o seu nome, será que de fato ele está autenticado? Será que nós queremos que ele esteja autenticado se ele errar o nome ou errar a senha? Vou criar um teste para garantir esses dois cenários.

[06:23] Então vou criar um teste aqui, vou chamá-lo de def test_autenticacao_de_user_com_username_incorreto(self):. Esperamos que ele não consiga se autenticar. O que vamos fazer?

[06:49] Vamos fazer a mesma autenticação que fizemos em cima. Eu vou até copiar as linhas 15 e 16, exatamente isso que queremos fazer nesse teste. Copiei o “aluraflix” também, não é isso que queremos.

[07:04] Vou autenticar, só que com o username incorreto. Então ao invés de c3po, vai ser c3pp, digitou errado. Então ele vai verificar se o usuário não é nulo e se ele está autenticado. Só que eu não quero uma acertação verdadeira, eu espero que isso seja falso, então digito assertFalse. Vamos verificar isso. Subindo o nosso teste... Aprovado!

[07:31] Então se erramos o nome ou erramos a senha, o nosso usuário não consegue ser autenticado. Podemos fazer o mesmo com a senha, então no lugar de username eu posso colocar password. Só para deixar nosso código bem legal, vou deixar o username correto e a senha vou colocar como 123455.

[07:58] Na linha 23, o que eu vou fazer? Só para manter o nosso código organizado eu vou colocar “““Teste que verifica autenticação de um user com username incorreto”””. Queremos essa mesma docstring, só que no lugar de username nós vamos mudar para senha – password.

[08:33] Dessa forma manteremos o nosso código sempre organizado e com as informações que queremos.

### Requisições de user autenticado

[FORCE AUTHENTICATION]('https://www.django-rest-framework.org/api-guide/testing/#forcing-authentication')

1. Em test_authentication.py:

        ...
        def test_requisicao_get_com_user_autenticado(self):
                """Teste que verifica um requisição get de um user autenticado"""
                self.client.force_authenticate(self.user)
                response = self.client.get(self.list_url)
                self.assertEqual(response.status_code, status.HTTP_200_OK)

...

[00:00] Realizamos diferentes testes para autenticarmos o usuário, para verificarmos se esse comportamento está correto. Vimos se com as credenciais do usuário ele consegue estar autenticado, se ele consegue realizar uma requisição não estando autenticado - e obtivemos sucesso nesses nossos testes.

[00:19] Porém, o que eu quero fazer agora é o oposto, eu quero fazer agora uma requisição get com o usuário autorizado. Então vou criar um novo teste - def test_requisicao_get_com_user_autenticado(self):.

[00:46] Vamos começar a escrever a nossa docstring para mantermos o nosso teste bem documentado. Então, “““Teste que verifica uma requisição GET de um user autenticado”””.

[01:13] A primeira coisa que vamos ter em mente é que nós não podemos usar, nesse caso, o authenticate. Por quê? O authenticate é uma ação que verifica se o usuário passa nessas regras de autenticação do Django durante uma solicitação.

[01:34] Então ele vai verificar o username, o password. O objetivo de quando utilizamos esse método authentication é de fato a eficiência. Então ele vai verificar se as credenciais estão certas. Se estiverem certas, esse usuário estará autenticado.

[01:51] Então, nesse caso, o que eu preciso fazer? Para que eu consiga de fato visualizar os dados da requisição é importante que eu esteja autenticado. Então eu preciso, de alguma maneira, forçar a requisição. Nós vamos utilizar esse método chamado force authentication.

[02:10] Qual é a diferença dele? O objetivo de forçar a autenticação é assim: mesmo que o usuário faça a autenticação com uma negação de algum username ou password, nós vamos garantir que ele seja autenticado, vamos forçar a autenticação através dele. Mas como fazemos isso?

[02:32] Para começar, eu vou criar self.client.force. Aqui está escrito force_login, mas o nome que vamos utilizar é force_authenticate. O que precisamos passar para esse force_authenticate? Vamos passar o usuário que criamos, então digitamos (self.user). Então estamos forçando, estamos falando que queremos que o cliente da requisição seja autenticado. Ficou self.client.focr_authenticate(self.user).

[03:11] Podemos encontrar mais detalhes disso na própria documentação do Django Rest sobre o force authentication. Temos a assinatura do método, request, o user - que criamos na nossa função de setup - e temos todos esses detalhes bem explicados.

[03:32] Então forçamos que o cliente da requisição esteja autenticado com esse usuário que acabamos de criar. Até aí está tudo bem. O que eu quero fazer agora é criar uma requisição get. Podemos usar o mesmo código que usamos na linha 20. Vou copiar esse linha response = self.client.get(self.list_url).

[03:56] Então nós temos um usuário que foi forçado à uma autenticação e que fez uma requisição get. O que vou fazer agora? Vou verificar se esse status é 200, se o status code da resposta desse response que eu tenho é de 200. Então vou digitar self.assertEqual(reponse.status_code, status HTTP¬_200_OK).

[04:30] Abrindo nosso console, vou rodar o “manage.py test” e vou deixar em cima para nós visualizarmos. Ele vai começar a rodar os nossos testes... Nosso teste foi aprovado! Então quando queremos de fato testar se o usuário está autenticado, esse cliente da requisição precisa de outros passos e nós precisamos da autenticação.

[04:55] Então, utilizamos o force authenticate e não apenas o authenticate.[00:00] Realizamos diferentes testes para autenticarmos o usuário, para verificarmos se esse comportamento está correto. Vimos se com as credenciais do usuário ele consegue estar autenticado, se ele consegue realizar uma requisição não estando autenticado - e obtivemos sucesso nesses nossos testes.

[00:19] Porém, o que eu quero fazer agora é o oposto, eu quero fazer agora uma requisição get com o usuário autorizado. Então vou criar um novo teste - def test_requisicao_get_com_user_autenticado(self):.

[00:46] Vamos começar a escrever a nossa docstring para mantermos o nosso teste bem documentado. Então, “““Teste que verifica uma requisição GET de um user autenticado”””.

[01:13] A primeira coisa que vamos ter em mente é que nós não podemos usar, nesse caso, o authenticate. Por quê? O authenticate é uma ação que verifica se o usuário passa nessas regras de autenticação do Django durante uma solicitação.

[01:34] Então ele vai verificar o username, o password. O objetivo de quando utilizamos esse método authentication é de fato a eficiência. Então ele vai verificar se as credenciais estão certas. Se estiverem certas, esse usuário estará autenticado.

[01:51] Então, nesse caso, o que eu preciso fazer? Para que eu consiga de fato visualizar os dados da requisição é importante que eu esteja autenticado. Então eu preciso, de alguma maneira, forçar a requisição. Nós vamos utilizar esse método chamado force authentication.

[02:10] Qual é a diferença dele? O objetivo de forçar a autenticação é assim: mesmo que o usuário faça a autenticação com uma negação de algum username ou password, nós vamos garantir que ele seja autenticado, vamos forçar a autenticação através dele. Mas como fazemos isso?

[02:32] Para começar, eu vou criar self.client.force. Aqui está escrito force_login, mas o nome que vamos utilizar é force_authenticate. O que precisamos passar para esse force_authenticate? Vamos passar o usuário que criamos, então digitamos (self.user). Então estamos forçando, estamos falando que queremos que o cliente da requisição seja autenticado. Ficou self.client.focr_authenticate(self.user).

[03:11] Podemos encontrar mais detalhes disso na própria documentação do Django Rest sobre o force authentication. Temos a assinatura do método, request, o user - que criamos na nossa função de setup - e temos todos esses detalhes bem explicados.

[03:32] Então forçamos que o cliente da requisição esteja autenticado com esse usuário que acabamos de criar. Até aí está tudo bem. O que eu quero fazer agora é criar uma requisição get. Podemos usar o mesmo código que usamos na linha 20. Vou copiar esse linha response = self.client.get(self.list_url).

[03:56] Então nós temos um usuário que foi forçado à uma autenticação e que fez uma requisição get. O que vou fazer agora? Vou verificar se esse status é 200, se o status code da resposta desse response que eu tenho é de 200. Então vou digitar self.assertEqual(reponse.status_code, status HTTP¬_200_OK).

[04:30] Abrindo nosso console, vou rodar o “manage.py test” e vou deixar em cima para nós visualizarmos. Ele vai começar a rodar os nossos testes... Nosso teste foi aprovado! Então quando queremos de fato testar se o usuário está autenticado, esse cliente da requisição precisa de outros passos e nós precisamos da autenticação.

[04:55] Então, utilizamos o force authenticate e não apenas o authenticate.

### Faça como eu fiz

Nos testes de modelo e serializer, não utilizamos o banco de dados para a criar um objeto no banco de dados de teste, usamos apenas uma instância de programa. Porém, nesta aula, vinculamos o banco de dados de teste, criamos um usuário e realizamos uma série de testes para garantir que os dados da API serão mostrados apenas para usuários cadastrados.

Que magia é essa aí?

#### Opinião do instrutor

Para começar, vamos criar a lista das URLs do recurso de programa e criar um usuário no banco de dados de teste:

        class AuthenticationUserTestCase(APITestCase):

            def setUp(self):
                self.list_url = reverse('programas-list')
                self.user = User.objects.create_user('c3po', password='123456')

Agora, vamos escrever um teste para verificar se o usuário c3po consegue se autenticar:

        def test_autenticacao_user_com_credenciais_corretas(self):
                """Teste que verifica a autenticação de um user com as credenciais corretas"""
                user = authenticate(username='c3po', password='123456')
                self.assertTrue((user is not None) and user.is_authenticated)

Em seguida, vamos tentar realizar uma requisição sem autenticar nenhum usuário:

        def test_requisicao_get_nao_autorizada(self):
                """Teste que verifica uma requisição GET não autorizada"""
                response = self.client.get(self.list_url)
                self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
Para fechar com chave de ouro, vamos autenticar o usuário criado na função setUp e realizar uma requisição GET:

        def test_requisicao_get_com_user_autenticado(self):
                """Teste que verifica uma requisição GET de um user autenticado"""
                self.client.force_authenticate(self.user)
                response = self.client.get(self.list_url)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
        
Ao executar o `manage.py` test, nossos testes serão aprovados!

Ficou com alguma dúvida, lembre-se do fórum da Alura. Não tem dúvidas? Que tal ajudar alguém no fórum?

:)

### Unidade ou Integração?

O método de teste setUp permite criar dados de teste comuns com facilidade e eficiência. Uma vez que você configura os registros para a classe, você não precisa recriar os registros para cada método de teste, como ilustram os códigos abaixo:

Código 1

        def setUp(self):
                self.programa = Programa(
                    titulo = 'Procurando ninguém em latim',
                    data_lancamento = '2003-07-04'
                )

Código 2

        def setUp(self):
                self.programa = Programa.objects.create(
                    titulo = 'Procurando ninguém em latim',
                    data_lancamento = '2003-07-04'
                )

Analisando os trechos de código acima, podemos afirmar que:

a) Os testes que usam a função setUp do Código 1 podem ser chamados de testes de integração e do Código 2, podem ser chamados de testes de unidade.
b) **Alternativa correta:** Os testes que usam a função setUp do Código 1 podem ser chamados de testes de unidade e do Código 2, podem ser chamados de testes de integração.
- _Alternativa correta! Certo! Os testes de unidade são focados nos componentes individuais do programa. Já os testes de integração, testam componentes e suas dependências._
c) Ambos são testes de integração, tanto oCódigo 1 como o Código 2.

### O que aprendemos?

**Nesta aula:**
- Criamos os testes que verificam a autenticação de um usuário com base nas políticas de acesso do Django, criando um usuário na base de dados de testes;
- Verificamos as tentativas de acesso de um usuário com as credenciais corretas e incorretas e realizamos uma requisição GET de um usuário autenticado.

**Na próxima aula:**
- Vamos aprender como carregar os dados das fixtures em nossos testes e descobrir como podemos escrever testes no Postman!

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
 